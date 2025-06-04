import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
from datetime import datetime
import sqlite3
from ultralytics import YOLO
import numpy as np

class ResimTespit:
    def __init__(self):
        """
        Resim tespit sınıfını başlatır.
        YOLO modelini yükler ve veritabanı bağlantısını oluşturur.
        """
        # YOLO modelini yükle - daha iyi performans için yolov8s kullan
        try:
            self.model = YOLO("yolov8s.pt")  # Daha büyük model, daha iyi tespit
            print("YOLO modeli başarıyla yüklendi.")
        except Exception as e:
            print(f"Model yükleme hatası: {e}")
            # Yedek olarak nano modeli dene
            self.model = YOLO("yolov8n.pt")
        
        # Nesne sınıflarının Türkçe karşılıkları (genişletilmiş)
        self.sinif_isimleri = {
            "person": "İnsan",
            "bicycle": "Bisiklet",
            "car": "Araba",
            "motorcycle": "Motosiklet",
            "airplane": "Uçak",
            "bus": "Otobüs",
            "train": "Tren",
            "truck": "Kamyon",
            "boat": "Tekne",
            "traffic light": "Trafik Işığı",
            "fire hydrant": "Yangın Musluğu",
            "stop sign": "Dur Tabelası",
            "parking meter": "Park Saati",
            "bench": "Bank",
            "bird": "Kuş",
            "cat": "Kedi",
            "dog": "Köpek",
            "horse": "At",
            "sheep": "Koyun",
            "cow": "İnek",
            "elephant": "Fil",
            "bear": "Ayı",
            "zebra": "Zebra",
            "giraffe": "Zürafa",
            "backpack": "Sırt Çantası",
            "umbrella": "Şemsiye",
            "handbag": "El Çantası",
            "tie": "Kravat",
            "suitcase": "Bavul",
            "frisbee": "Frizbi",
            "skis": "Kayak",
            "snowboard": "Snowboard",
            "sports ball": "Spor Topu",
            "kite": "Uçurtma",
            "baseball bat": "Beyzbol Sopası",
            "baseball glove": "Beyzbol Eldiveni",
            "skateboard": "Kaykay",
            "surfboard": "Sörf Tahtası",
            "tennis racket": "Tenis Raketi",
            "bottle": "Şişe",
            "wine glass": "Şarap Bardağı",
            "cup": "Fincan",
            "fork": "Çatal",
            "knife": "Bıçak",
            "spoon": "Kaşık",
            "bowl": "Kase",
            "banana": "Muz",
            "apple": "Elma",
            "sandwich": "Sandviç",
            "orange": "Portakal",
            "broccoli": "Brokoli",
            "carrot": "Havuç",
            "hot dog": "Sosisli",
            "pizza": "Pizza",
            "donut": "Çörek",
            "cake": "Pasta",
            "chair": "Sandalye",
            "couch": "Kanepe",
            "potted plant": "Saksı Bitkisi",
            "bed": "Yatak",
            "dining table": "Yemek Masası",
            "toilet": "Tuvalet",
            "tv": "Televizyon",
            "laptop": "Dizüstü Bilgisayar",
            "mouse": "Fare",
            "remote": "Uzaktan Kumanda",
            "keyboard": "Klavye",
            "cell phone": "Cep Telefonu",
            "microwave": "Mikrodalga",
            "oven": "Fırın",
            "toaster": "Tost Makinesi",
            "sink": "Lavabo",
            "refrigerator": "Buzdolabı",
            "book": "Kitap",
            "clock": "Saat",
            "vase": "Vazo",
            "scissors": "Makas",
            "teddy bear": "Oyuncak Ayı",
            "hair drier": "Saç Kurutma Makinesi",
            "toothbrush": "Diş Fırçası"
        }
        
        # Tespit renkleri
        self.insan_rengi = (255, 0, 0)  # Kırmızı
        self.nesne_rengi = (0, 255, 0)  # Yeşil
        
        # Tespit değişkenleri
        self.tespit_edilen_nesneler = {}
        self.tespit_gecmisi = []
        self.insan_sayisi = 0
        self.diger_nesne_sayisi = 0
        self.insan_tespit_etiketleri = []
        self.nesne_tespit_etiketleri = []
        
        # Veritabanı bağlantısını oluştur
        self.veritabani_olustur()
    
    def veritabani_olustur(self):
        """Veritabanı ve tabloları oluşturur"""
        try:
            if not os.path.exists("veritabani"):
                os.makedirs("veritabani")
            
            self.conn = sqlite3.connect("veritabani/resim_tespit.db")
            self.cursor = self.conn.cursor()
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tespitler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nesne_id INTEGER,
                    sinif TEXT,
                    konum_x1 INTEGER,
                    konum_y1 INTEGER,
                    konum_x2 INTEGER,
                    konum_y2 INTEGER,
                    guven REAL,
                    tarih DATETIME,
                    rapor_id INTEGER
                )
            ''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS raporlar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    baslik TEXT,
                    tarih DATETIME,
                    insan_sayisi INTEGER,
                    diger_nesne_sayisi INTEGER,
                    toplam_tespit INTEGER
                )
            ''')
            
            self.conn.commit()
            print("Veritabanı başarıyla oluşturuldu.")
        except Exception as e:
            print(f"Veritabanı oluşturma hatası: {e}")

    def gelismis_tespit(self, resim_yolu, guven_esigi=0.25):
        """
        Gelişmiş nesne tespiti yapar
        """
        try:
            # Resmi oku
            resim = cv2.imread(resim_yolu)
            if resim is None:
                raise ValueError("Resim okunamadı!")
            
            # Resim boyutunu kontrol et ve gerekirse yeniden boyutlandır
            yukseklik, genislik = resim.shape[:2]
            max_boyut = 1280
            
            if max(yukseklik, genislik) > max_boyut:
                olcek = max_boyut / max(yukseklik, genislik)
                yeni_genislik = int(genislik * olcek)
                yeni_yukseklik = int(yukseklik * olcek)
                resim = cv2.resize(resim, (yeni_genislik, yeni_yukseklik))
            
            # YOLO tespiti - daha düşük güven eşiği ve farklı parametreler
            sonuclar = self.model(
                resim, 
                conf=guven_esigi,      # Daha düşük güven eşiği
                iou=0.45,              # Non-Maximum Suppression eşiği
                max_det=100,           # Maksimum tespit sayısı
                verbose=False          # Detaylı çıktıyı kapat
            )
            
            print(f"Tespit sonucu: {len(sonuclar[0].boxes) if len(sonuclar) > 0 and sonuclar[0].boxes is not None else 0} nesne tespit edildi")
            
            return resim, sonuclar
            
        except Exception as e:
            print(f"Tespit hatası: {e}")
            raise

def icerik_goster(parent_frame):
    """
    Resim tespit modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # ResimTespit sınıfını oluştur
    resim_tespit = ResimTespit()
    
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Görüntü alanı - En üstte ve büyük
    goruntu_frame = ctk.CTkFrame(container)
    goruntu_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    canvas = tk.Canvas(goruntu_frame, bg="black", height=500)
    canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # Kontrol alanı - Resmin altında
    kontrol_frame = ctk.CTkFrame(container)
    kontrol_frame.pack(fill=tk.X, padx=20, pady=10)
    
    # Resim seçimi ve butonlar
    resim_sec_frame = ctk.CTkFrame(kontrol_frame)
    resim_sec_frame.pack(fill=tk.X, padx=10, pady=5)
    
    resim_label = ctk.CTkLabel(resim_sec_frame, text="Resim Seçin:")
    resim_label.pack(side=tk.LEFT, padx=10)
    
    resim_path = ctk.CTkEntry(resim_sec_frame, width=300)
    resim_path.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
    
    # Güven eşiği ayarı
    guven_frame = ctk.CTkFrame(kontrol_frame)
    guven_frame.pack(fill=tk.X, padx=10, pady=5)
    
    guven_label = ctk.CTkLabel(guven_frame, text="Güven Eşiği:")
    guven_label.pack(side=tk.LEFT, padx=10)
    
    guven_slider = ctk.CTkSlider(guven_frame, from_=0.1, to=0.9, number_of_steps=80)
    guven_slider.set(0.25)  # Varsayılan değer
    guven_slider.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
    
    guven_deger_label = ctk.CTkLabel(guven_frame, text="0.25")
    guven_deger_label.pack(side=tk.LEFT, padx=10)
    
    # Slider değeri güncelleme
    def guven_guncelle(deger):
        guven_deger_label.configure(text=f"{deger:.2f}")
    
    guven_slider.configure(command=guven_guncelle)
    
    # Butonlar için frame
    buton_frame = ctk.CTkFrame(resim_sec_frame)
    buton_frame.pack(side=tk.LEFT, padx=10)
    
    resim_sec_buton = ctk.CTkButton(buton_frame, text="Resim Seç", 
                                   command=lambda: resim_sec(resim_path),
                                   width=120)
    resim_sec_buton.pack(side=tk.LEFT, padx=5)
    
    tespit_buton = ctk.CTkButton(buton_frame, text="Tespit Et", 
                                command=lambda: tespit_et(resim_tespit, resim_path, canvas, 
                                                        guven_slider.get(),
                                                        insan_liste_container, nesne_liste_container,
                                                        istatistik_label),
                                fg_color="#34A853", hover_color="#2E7D32",
                                width=120)
    tespit_buton.pack(side=tk.LEFT, padx=5)
    
    kaydet_buton = ctk.CTkButton(buton_frame, text="Tespitleri Kaydet", 
                                command=lambda: tespitleri_kaydet(resim_tespit, istatistik_label),
                                fg_color="#4285F4", hover_color="#1A73E8",
                                width=120)
    kaydet_buton.pack(side=tk.LEFT, padx=5)
    
    # İstatistik bilgisi
    istatistik_frame = ctk.CTkFrame(kontrol_frame)
    istatistik_frame.pack(fill=tk.X, padx=10, pady=5)
    
    istatistik_label = ctk.CTkLabel(istatistik_frame, 
                                   text="İstatistik: Henüz tespit yapılmadı",
                                   font=("Arial", 12, "bold"))
    istatistik_label.pack(pady=5)
    
    # Tespit listeleri
    liste_frame = ctk.CTkFrame(container)
    liste_frame.pack(fill=tk.X, padx=20, pady=10)
    
    # İnsan tespitleri listesi
    insan_liste_frame = ctk.CTkFrame(liste_frame)
    insan_liste_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    insan_liste_baslik = ctk.CTkLabel(insan_liste_frame, 
                                     text="🚶 Tespit Edilen İnsanlar",
                                     font=("Arial", 14, "bold"))
    insan_liste_baslik.pack(pady=5)
    
    insan_liste_container = ctk.CTkScrollableFrame(insan_liste_frame, height=200)
    insan_liste_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # Diğer nesneler listesi
    nesne_liste_frame = ctk.CTkFrame(liste_frame)
    nesne_liste_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    nesne_liste_baslik = ctk.CTkLabel(nesne_liste_frame,
                                     text="📦 Tespit Edilen Diğer Nesneler",
                                     font=("Arial", 14, "bold"))
    nesne_liste_baslik.pack(pady=5)
    
    nesne_liste_container = ctk.CTkScrollableFrame(nesne_liste_frame, height=200)
    nesne_liste_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

def resim_sec(resim_path):
    """Resim dosyası seçme dialogunu açar"""
    dosya_yolu = filedialog.askopenfilename(
        title="Resim Seçin",
        filetypes=[
            ("Resim Dosyaları", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp"),
            ("JPEG Dosyaları", "*.jpg *.jpeg"),
            ("PNG Dosyaları", "*.png"),
            ("Tüm Dosyalar", "*.*")
        ]
    )
    if dosya_yolu:
        resim_path.delete(0, tk.END)
        resim_path.insert(0, dosya_yolu)

def tespit_et(resim_tespit, resim_path, canvas, guven_esigi, 
              insan_liste_container, nesne_liste_container, istatistik_label):
    """Seçilen resimde tespit işlemini başlatır"""
    if not resim_path.get():
        messagebox.showwarning("Uyarı", "Lütfen önce bir resim seçin!")
        return
    
    if not os.path.exists(resim_path.get()):
        messagebox.showerror("Hata", "Seçilen dosya bulunamadı!")
        return
    
    try:
        # İstatistiği güncelle
        istatistik_label.configure(text="İstatistik: Tespit işlemi devam ediyor...")
        
        # Gelişmiş tespit yap
        resim, sonuclar = resim_tespit.gelismis_tespit(resim_path.get(), guven_esigi)
        
        # Tespit değişkenlerini sıfırla
        resim_tespit.tespit_edilen_nesneler.clear()
        resim_tespit.tespit_gecmisi.clear()
        resim_tespit.insan_sayisi = 0
        resim_tespit.diger_nesne_sayisi = 0
        
        # Görüntüyü PIL Image'e dönüştür
        resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(resim_rgb)
        draw = ImageDraw.Draw(pil_image)
        
        # Font ayarları (varsa)
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()
        
        # Tespit edilen nesneleri işle
        if len(sonuclar) > 0 and sonuclar[0].boxes is not None:
            kutular = sonuclar[0].boxes
            print(f"İşlenecek kutu sayısı: {len(kutular)}")
            
            for i, kutu in enumerate(kutular):
                try:
                    # Koordinatları al
                    x1, y1, x2, y2 = map(int, kutu.xyxy[0])
                    guven = float(kutu.conf[0])
                    sinif_id = int(kutu.cls[0])
                    sinif_adi = resim_tespit.model.names[sinif_id]
                    
                    print(f"Tespit {i+1}: {sinif_adi} - Güven: {guven:.2f}")
                    
                    # Türkçe sınıf adını al
                    turkce_sinif = resim_tespit.sinif_isimleri.get(sinif_adi, sinif_adi.title())
                    
                    # Renk seçimi
                    if sinif_adi == "person":
                        renk = resim_tespit.insan_rengi
                        kalinlik = 3
                    else:
                        renk = resim_tespit.nesne_rengi
                        kalinlik = 2
                    
                    # Nesneyi çerçeve içine al
                    draw.rectangle([(x1, y1), (x2, y2)], outline=renk, width=kalinlik)
                    
                    # Arka plan için dikdörtgen çiz
                    etiket = f"{turkce_sinif} %{guven*100:.0f}"
                    text_bbox = draw.textbbox((x1, y1-25), etiket, font=font)
                    draw.rectangle([text_bbox[0]-2, text_bbox[1]-2, text_bbox[2]+2, text_bbox[3]+2], 
                                 fill=(0, 0, 0, 180))
                    
                    # Nesne bilgilerini yaz
                    draw.text((x1, y1-25), etiket, fill=(255, 255, 255), font=font)
                    
                    # Tespit sonuçlarını kaydet
                    nesne_id = len(resim_tespit.tespit_edilen_nesneler) + 1
                    tespit_bilgisi = {
                        "id": nesne_id,
                        "sinif": turkce_sinif,
                        "orijinal_sinif": sinif_adi,
                        "konum": (x1, y1, x2, y2),
                        "guven": guven,
                        "tarih": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                        "tip": "insan" if sinif_adi == "person" else "nesne"
                    }
                    
                    resim_tespit.tespit_edilen_nesneler[nesne_id] = tespit_bilgisi
                    resim_tespit.tespit_gecmisi.append(tespit_bilgisi)
                    
                    # Sayıları güncelle
                    if sinif_adi == "person":
                        resim_tespit.insan_sayisi += 1
                    else:
                        resim_tespit.diger_nesne_sayisi += 1
                        
                except Exception as e:
                    print(f"Kutu işleme hatası {i}: {e}")
                    continue
        
        # Görüntüyü göster
        goruntu_guncelle(pil_image, canvas)
        
        # Listeleri güncelle
        liste_guncelle(resim_tespit, insan_liste_container, nesne_liste_container)
        
        # İstatistikleri güncelle
        toplam_tespit = resim_tespit.insan_sayisi + resim_tespit.diger_nesne_sayisi
        istatistik_label.configure(
            text=f"İstatistik: {resim_tespit.insan_sayisi} İnsan, {resim_tespit.diger_nesne_sayisi} Nesne (Toplam: {toplam_tespit})"
        )
        
        if toplam_tespit > 0:
            messagebox.showinfo("Başarılı", f"Tespit tamamlandı!\n{toplam_tespit} nesne tespit edildi.")
        else:
            messagebox.showwarning("Uyarı", "Hiçbir nesne tespit edilemedi.\nGüven eşiğini düşürmeyi deneyin.")
        
    except Exception as e:
        print(f"Tespit hatası: {e}")
        messagebox.showerror("Hata", f"Tespit sırasında hata oluştu:\n{str(e)}")
        istatistik_label.configure(text="İstatistik: Tespit işlemi başarısız")

def goruntu_guncelle(pil_image, canvas):
    """Resim görüntüsünü günceller"""
    try:
        # Canvas'ın gerçek boyutlarını al
        canvas.update()
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        if canvas_width > 50 and canvas_height > 50:  # Minimum boyut kontrolü
            # Oranı koru
            img_width, img_height = pil_image.size
            scale = min(canvas_width/img_width, canvas_height/img_height)
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            
            pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # PIL Image'i PhotoImage'e dönüştür
        photo = ImageTk.PhotoImage(image=pil_image)
        
        # Canvas'ı temizle ve yeni resmi yerleştir
        canvas.delete("all")
        canvas.create_image(canvas_width//2, canvas_height//2, image=photo, anchor=tk.CENTER)
        canvas.photo = photo  # Referansı sakla
        
    except Exception as e:
        print(f"Görüntü güncelleme hatası: {e}")

def liste_guncelle(resim_tespit, insan_liste_container, nesne_liste_container):
    """Tespit listelerini günceller"""
    try:
        # Eski etiketleri temizle
        for etiket in resim_tespit.insan_tespit_etiketleri:
            etiket.destroy()
        resim_tespit.insan_tespit_etiketleri.clear()
        
        for etiket in resim_tespit.nesne_tespit_etiketleri:
            etiket.destroy()
        resim_tespit.nesne_tespit_etiketleri.clear()
        
        # Yeni etiketleri oluştur
        for tespit in resim_tespit.tespit_gecmisi:
            etiket_metni = f"🔍 {tespit['sinif']} (ID: {tespit['id']})\n📊 Güven: %{tespit['guven']*100:.1f}\n🕒 {tespit['tarih']}"
            
            container = insan_liste_container if tespit['tip'] == 'insan' else nesne_liste_container
            
            etiket = ctk.CTkLabel(
                container,
                text=etiket_metni,
                justify="left"
            )
            etiket.pack(pady=3, padx=5, anchor="w")
            
            if tespit['tip'] == 'insan':
                resim_tespit.insan_tespit_etiketleri.append(etiket)
            else:
                resim_tespit.nesne_tespit_etiketleri.append(etiket)
        
        # Boş liste mesajları
        if resim_tespit.insan_sayisi == 0:
            bos_etiket = ctk.CTkLabel(insan_liste_container, text="Henüz insan tespit edilmedi", 
                                     text_color="gray")
            bos_etiket.pack(pady=10)
            resim_tespit.insan_tespit_etiketleri.append(bos_etiket)
            
        if resim_tespit.diger_nesne_sayisi == 0:
            bos_etiket = ctk.CTkLabel(nesne_liste_container, text="Henüz nesne tespit edilmedi", 
                                     text_color="gray")
            bos_etiket.pack(pady=10)
            resim_tespit.nesne_tespit_etiketleri.append(bos_etiket)
                
    except Exception as e:
        print(f"Liste güncelleme hatası: {e}")

def tespitleri_kaydet(resim_tespit, istatistik_label):
    """Tespit edilen nesneleri veritabanına kaydeder"""
    if not resim_tespit.tespit_gecmisi:
        messagebox.showwarning("Uyarı", "Kaydedilecek tespit bulunamadı!")
        return
    
    try:
        # Yeni rapor oluştur
        toplam_tespit = resim_tespit.insan_sayisi + resim_tespit.diger_nesne_sayisi
        
        resim_tespit.cursor.execute('''
            INSERT INTO raporlar (baslik, tarih, insan_sayisi, diger_nesne_sayisi, toplam_tespit)
            VALUES (?, ?, ?, ?, ?)
        ''', ("Resim Tespit Raporu", datetime.now(), 
              resim_tespit.insan_sayisi, resim_tespit.diger_nesne_sayisi, toplam_tespit))
        
        rapor_id = resim_tespit.cursor.lastrowid
        
        # Tespitleri kaydet
        for tespit in resim_tespit.tespit_gecmisi:
            x1, y1, x2, y2 = tespit['konum']
            resim_tespit.cursor.execute('''
                INSERT INTO tespitler 
                (nesne_id, sinif, konum_x1, konum_y1, konum_x2, konum_y2, guven, tarih, rapor_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (tespit['id'], tespit['sinif'], x1, y1, x2, y2, tespit['guven'],
                  datetime.strptime(tespit['tarih'], "%d.%m.%Y %H:%M:%S"), rapor_id))
        
        resim_tespit.conn.commit()
        
        messagebox.showinfo("Başarılı", 
                          f"Tespitler başarıyla kaydedildi!\n"
                          f"Rapor ID: {rapor_id}\n"
                          f"Toplam tespit: {toplam_tespit}")
        
        # İstatistik güncelle
        istatistik_label.configure(text=f"İstatistik: Son veriler kaydedildi (Rapor ID: {rapor_id})")
        
    except Exception as e:
        resim_tespit.conn.rollback()
        print(f"Kaydetme hatası: {e}")
        messagebox.showerror("Hata", f"Tespitler kaydedilirken hata oluştu:\n{str(e)}")