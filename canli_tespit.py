import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
import threading
import time
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import json
import os
from datetime import datetime
import sqlite3

class CanliTespit(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Veritabanı bağlantısını oluştur
        self.veritabani_olustur()
        
        # YOLO ve DeepSORT modellerini yükle
        self.model = YOLO("yolov8n.pt")
        self.tracker = DeepSort(max_age=30)
        
        # Nesne sınıflarının Türkçe karşılıkları
        self.sinif_isimleri = {
            "person": "Insan",
            "bed": "Yatak",
            "chair": "Sandalye",
            "table": "Masa",
            "tv": "Televizyon",
            "laptop": "Dizustu Bilgisayar",
            "mouse": "Fare",
            "keyboard": "Klavye",
            "phone": "Telefon",
            "book": "Kitap",
            "bottle": "Sise",
            "cup": "Fincan",
            "bowl": "Kase",
            "wine glass": "Sarap Bardagi",
            "donut": "Corek",
            "cake": "Pasta",
            "pizza": "Pizza",
            "sandwich": "Sandvic",
            "orange": "Portakal",
            "apple": "Elma",
            "banana": "Muz",
            "carrot": "Havuc",
            "broccoli": "Brokoli",
            "hot dog": "Sosisli",
            "hamburger": "Hamburger",
            "potted plant": "Saksi Bitkisi",
            "vase": "Vazo",
            "scissors": "Makas",
            "toothbrush": "Dis Fircasi",
            "hair brush": "Sac Fircasi",
            "toilet": "Tuvalet",
            "sink": "Lavabo",
            "refrigerator": "Buzdolabi",
            "microwave": "Mikrodalga",
            "oven": "Firin",
            "toaster": "Tost Makinesi",
            "clock": "Saat",
            "backpack": "Sirt Cantasi",
            "umbrella": "Semsiye",
            "handbag": "El Cantasi",
            "tie": "Kravat",
            "suitcase": "Bavul",
            "frisbee": "Frizbi",
            "skis": "Kayak",
            "snowboard": "Snowboard",
            "sports ball": "Spor Topu",
            "kite": "Ucurtma",
            "baseball bat": "Beyzbol Sopasi",
            "baseball glove": "Beyzbol Eldiveni",
            "skateboard": "Kaykay",
            "surfboard": "Sorf Tahtasi",
            "tennis racket": "Tenis Raketi",
            "bottle": "Sise",
            "wine glass": "Sarap Bardagi",
            "cup": "Fincan",
            "fork": "Catal",
            "knife": "Bicak",
            "spoon": "Kasik",
            "bowl": "Kase",
            "banana": "Muz",
            "apple": "Elma",
            "sandwich": "Sandvic",
            "orange": "Portakal",
            "broccoli": "Brokoli",
            "carrot": "Havuc",
            "hot dog": "Sosisli",
            "pizza": "Pizza",
            "donut": "Corek",
            "cake": "Pasta",
            "chair": "Sandalye",
            "couch": "Kanepe",
            "potted plant": "Saksi Bitkisi",
            "bed": "Yatak",
            "dining table": "Yemek Masasi",
            "toilet": "Tuvalet",
            "tv": "Televizyon",
            "laptop": "Dizustu Bilgisayar",
            "mouse": "Fare",
            "remote": "Kumanda",
            "keyboard": "Klavye",
            "cell phone": "Cep Telefonu",
            "microwave": "Mikrodalga",
            "oven": "Firin",
            "toaster": "Tost Makinesi",
            "sink": "Lavabo",
            "refrigerator": "Buzdolabi",
            "book": "Kitap",
            "clock": "Saat",
            "vase": "Vazo",
            "scissors": "Makas",
            "teddy bear": "Oyuncak Ayi",
            "hair drier": "Sac Kurutma Makinesi",
            "toothbrush": "Dis Fircasi"
        }
        
        # Kamera ve görüntü işleme değişkenleri
        self.cap = None
        self.is_running = False
        self.current_frame = None
        self.tespit_edilen_nesneler = {}  # Tespit edilen nesnelerin bilgilerini tut
        self.tespit_gecmisi = []  # Tespit geçmişini tut
        self.insan_sayisi = 0  # Tespit edilen insan sayısı
        self.diger_nesne_sayisi = 0  # Tespit edilen diğer nesnelerin sayısı
        self.son_guncelleme = 0  # Son liste güncelleme zamanı
        self.aktif_track_idler = set()  # Aktif takip ID'lerini tut
        
        # Tespit raporları klasörünü oluştur
        self.rapor_klasoru = "tespit_raporlari"
        if not os.path.exists(self.rapor_klasoru):
            os.makedirs(self.rapor_klasoru)
        
        # Ana container
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Kamera görüntüsü üstte
        self.kamera_frame = ctk.CTkFrame(self.container)
        self.kamera_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        
        self.canvas = tk.Canvas(self.kamera_frame, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Sayaçlar ve butonlar kameranın hemen altında
        self.ust_kontrol_frame = ctk.CTkFrame(self.container)
        self.ust_kontrol_frame.pack(fill=tk.X, padx=10, pady=(0, 5))
        
        # Güven eşiği ayarı - kontrol alanının sol tarafında
        self.guven_label = ctk.CTkLabel(self.ust_kontrol_frame, text="Güven Eşiği:")
        self.guven_label.pack(side=tk.LEFT, padx=5)
        
        self.guven_slider = ctk.CTkSlider(self.ust_kontrol_frame, from_=0.1, to=0.9, 
                                         number_of_steps=80, width=120)
        self.guven_slider.set(0.5)  # Varsayılan değer
        self.guven_slider.pack(side=tk.LEFT, padx=5)
        
        self.guven_deger_label = ctk.CTkLabel(self.ust_kontrol_frame, text="0.50")
        self.guven_deger_label.pack(side=tk.LEFT, padx=5)
        
        # Slider değeri güncelleme fonksiyonu
        self.guven_slider.configure(command=self.guven_guncelle)
        
        self.insan_sayisi_label = ctk.CTkLabel(self.ust_kontrol_frame, 
                                             text="Tespit Edilen İnsan: 0",
                                             font=("Arial", 12, "bold"))
        self.insan_sayisi_label.pack(side=tk.LEFT, padx=5)
        
        self.diger_nesne_sayisi_label = ctk.CTkLabel(self.ust_kontrol_frame,
                                                   text="Diğer Nesneler: 0",
                                                   font=("Arial", 12, "bold"))
        self.diger_nesne_sayisi_label.pack(side=tk.LEFT, padx=5)
        
        self.baslat_buton = ctk.CTkButton(self.ust_kontrol_frame, text="Kamerayı Başlat",
                                        command=self.kamerayi_baslat,
                                        fg_color="#1E88E5", hover_color="#1565C0",
                                        height=35, font=("Arial", 12))
        self.baslat_buton.pack(side=tk.RIGHT, padx=5)
        
        self.durdur_buton = ctk.CTkButton(self.ust_kontrol_frame, text="Durdur",
                                        command=self.kamerayi_durdur,
                                        fg_color="#E53935", hover_color="#C62828",
                                        height=35, font=("Arial", 12))
        self.durdur_buton.pack(side=tk.RIGHT, padx=5)
        
        self.kaydet_buton = ctk.CTkButton(self.ust_kontrol_frame, text="Tespitleri Kaydet",
                                        command=self.tespitleri_kaydet,
                                        fg_color="#43A047", hover_color="#2E7D32",
                                        height=35, font=("Arial", 12))
        self.kaydet_buton.pack(side=tk.RIGHT, padx=5)
        
        # Alt frame - Tespit listeleri yan yana
        self.alt_liste_frame = ctk.CTkFrame(self.container)
        self.alt_liste_frame.pack(fill=tk.X, padx=10, pady=(5, 10))
        
        # İnsan tespitleri listesi
        self.insan_liste_frame = ctk.CTkFrame(self.alt_liste_frame)
        self.insan_liste_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.insan_liste_baslik = ctk.CTkLabel(self.insan_liste_frame, 
                                             text="Tespit Edilen İnsanlar",
                                             font=("Arial", 14, "bold"))
        self.insan_liste_baslik.pack(pady=5)
        
        self.insan_liste_container = ctk.CTkScrollableFrame(self.insan_liste_frame)
        self.insan_liste_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Diğer nesneler listesi
        self.nesne_liste_frame = ctk.CTkFrame(self.alt_liste_frame)
        self.nesne_liste_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.nesne_liste_baslik = ctk.CTkLabel(self.nesne_liste_frame,
                                             text="Tespit Edilen Diğer Nesneler",
                                             font=("Arial", 14, "bold"))
        self.nesne_liste_baslik.pack(pady=5)
        
        self.nesne_liste_container = ctk.CTkScrollableFrame(self.nesne_liste_frame)
        self.nesne_liste_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tespit listesi için etiketler
        self.insan_tespit_etiketleri = []
        self.nesne_tespit_etiketleri = []
        
        # Durdur butonunu başlangıçta devre dışı bırak
        self.durdur_buton.configure(state="disabled")
    
    def veritabani_olustur(self):
        """Veritabanı ve tabloları oluşturur"""
        try:
            # Veritabanı klasörünü oluştur
            if not os.path.exists("veritabani"):
                os.makedirs("veritabani")
            
            # Veritabanı bağlantısı
            self.conn = sqlite3.connect("veritabani/canli_tespit.db")
            self.cursor = self.conn.cursor()
            
            # Tespitler tablosunu oluştur
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tespitler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nesne_id INTEGER,
                    sinif TEXT,
                    tarih DATETIME,
                    rapor_id INTEGER
                )
            ''')
            
            # Raporlar tablosunu oluştur
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS raporlar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    baslik TEXT,
                    tarih DATETIME,
                    insan_sayisi INTEGER
                )
            ''')
            
            self.conn.commit()
        except Exception as e:
            print(f"Veritabanı oluşturma hatası: {e}")
    
    def kamerayi_baslat(self):
        """Kamerayı başlatır ve tespit işlemini başlatır"""
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Hata", "Kamera açılamadı!")
                return
            
            # Kamera çözünürlüğünü ayarla
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            
            self.is_running = True
            self.tespit_thread = threading.Thread(target=self.tespit_dongusu)
            self.tespit_thread.daemon = True
            self.tespit_thread.start()
            
            self.baslat_buton.configure(state="disabled")
            self.durdur_buton.configure(state="normal")
    
    def kamerayi_durdur(self):
        """Kamerayı durdurur ve tespit işlemini sonlandırır"""
        self.is_running = False
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        
        self.baslat_buton.configure(state="normal")
        self.durdur_buton.configure(state="disabled")
    
    def tespit_dongusu(self):
        """Sürekli olarak kameradan görüntü alır ve nesne tespiti yapar"""
        while self.is_running:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                # YOLO ile nesne tespiti
                results = self.model(frame, conf=self.guven_slider.get())
                
                # Tespit edilen nesneleri işle
                detections = []
                current_insan_sayisi = 0
                current_diger_nesne_sayisi = 0
                current_time = time.time()
                
                for r in results:
                    boxes = r.boxes
                    for box in boxes:
                        x1, y1, x2, y2 = box.xyxy[0]
                        conf = box.conf[0]
                        cls = int(box.cls[0])
                        cls_name = self.model.names[cls]
                        
                        if cls_name == "person":
                            current_insan_sayisi += 1
                        else:
                            current_diger_nesne_sayisi += 1
                        
                        detections.append(([x1, y1, x2, y2], conf, cls))
                
                # DeepSORT ile nesne takibi
                tracks = self.tracker.update_tracks(detections, frame=frame)
                
                # Görüntüyü PIL Image'e dönüştür
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(frame_rgb)
                draw = ImageDraw.Draw(pil_image)
                
                # Aktif track ID'lerini güncelle
                current_track_ids = set()
                
                # Tespit edilen nesneleri çiz ve listele
                for track in tracks:
                    if not track.is_confirmed():
                        continue
                    
                    track_id = track.track_id
                    current_track_ids.add(track_id)
                    ltrb = track.to_ltrb()
                    
                    # Tespit edilen nesnenin sınıfını bul
                    cls_name = "Bilinmeyen"
                    for det in detections:
                        if (abs(det[0][0] - ltrb[0]) < 10 and 
                            abs(det[0][1] - ltrb[1]) < 10):
                            cls_name = self.model.names[det[2]]
                            break
                    
                    # Türkçe sınıf adını al
                    turkce_sinif = self.sinif_isimleri.get(cls_name, cls_name)
                    
                    # Nesneyi çerçeve içine al
                    draw.rectangle([(int(ltrb[0]), int(ltrb[1])), 
                                  (int(ltrb[2]), int(ltrb[3]))], 
                                 outline=(0, 255, 0), width=2)
                    
                    # Nesne bilgilerini yaz
                    etiket = f"{turkce_sinif} (ID: {track_id})"
                    draw.text((int(ltrb[0]), int(ltrb[1]-20)), etiket, 
                             fill=(0, 255, 0))
                    
                    # Yeni tespit edilen nesneyi listeye ekle
                    if track_id not in self.tespit_edilen_nesneler:
                        self.tespit_edilen_nesneler[track_id] = {
                            "id": track_id,
                            "sinif": turkce_sinif,
                            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                            "tip": "insan" if cls_name == "person" else "nesne"
                        }
                        self.tespit_gecmisi.append(self.tespit_edilen_nesneler[track_id])
                        
                        # Liste güncellemesini sınırla (en fazla her 0.5 saniyede bir)
                        if current_time - self.son_guncelleme > 0.5:
                            self.liste_guncelle()
                            self.son_guncelleme = current_time
                
                # Aktif olmayan track ID'lerini temizle
                self.aktif_track_idler = current_track_ids
                
                # Sayıları güncelle
                if (self.insan_sayisi != current_insan_sayisi or 
                    self.diger_nesne_sayisi != current_diger_nesne_sayisi):
                    self.insan_sayisi = current_insan_sayisi
                    self.diger_nesne_sayisi = current_diger_nesne_sayisi
                    self.insan_sayisi_label.configure(
                        text=f"Tespit Edilen İnsan: {self.insan_sayisi}")
                    self.diger_nesne_sayisi_label.configure(
                        text=f"Diğer Nesneler: {self.diger_nesne_sayisi}")
                
                # Görüntüyü göster
                self.goruntu_guncelle(pil_image)
                time.sleep(0.03)  # FPS sınırlaması
                
            except Exception as e:
                print(f"Tespit döngüsü hatası: {e}")
                continue
    
    def goruntu_guncelle(self, pil_image):
        """Kamera görüntüsünü günceller"""
        try:
            # Görüntüyü canvas boyutuna ölçekle
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            if canvas_width > 1 and canvas_height > 1:  # Canvas boyutu geçerli mi?
                pil_image = pil_image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            
            # PIL Image'i PhotoImage'e dönüştür
            photo = ImageTk.PhotoImage(image=pil_image)
            
            # Canvas'ı güncelle
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.photo = photo  # Referansı tut
        except Exception as e:
            print(f"Görüntü güncelleme hatası: {e}")
    
    def liste_guncelle(self):
        """Tespit listelerini günceller"""
        try:
            # Eski etiketleri temizle
            for etiket in self.insan_tespit_etiketleri:
                etiket.destroy()
            self.insan_tespit_etiketleri.clear()
            
            for etiket in self.nesne_tespit_etiketleri:
                etiket.destroy()
            self.nesne_tespit_etiketleri.clear()
            
            # Yeni etiketleri oluştur
            for tespit in self.tespit_gecmisi:
                etiket = ctk.CTkLabel(
                    self.insan_liste_container if tespit['tip'] == 'insan' else self.nesne_liste_container,
                    text=f"{tespit['sinif']} (ID: {tespit['id']}) - {tespit['tarih']}"
                )
                etiket.pack(pady=2)
                
                if tespit['tip'] == 'insan':
                    self.insan_tespit_etiketleri.append(etiket)
                else:
                    self.nesne_tespit_etiketleri.append(etiket)
                    
        except Exception as e:
            print(f"Liste güncelleme hatası: {e}")
    
    def tespitleri_kaydet(self):
        """Tespit edilen nesneleri veritabanına kaydeder"""
        if not self.tespit_gecmisi:
            messagebox.showwarning("Uyarı", "Kaydedilecek tespit bulunamadı!")
            return
        
        try:
            # Yeni rapor oluştur
            self.cursor.execute('''
                INSERT INTO raporlar (baslik, tarih, insan_sayisi)
                VALUES (?, ?, ?)
            ''', ("Canlı Tespit Raporu", datetime.now(), self.insan_sayisi))
            
            rapor_id = self.cursor.lastrowid
            
            # Tespitleri kaydet
            for tespit in self.tespit_gecmisi:
                self.cursor.execute('''
                    INSERT INTO tespitler (nesne_id, sinif, tarih, rapor_id)
                    VALUES (?, ?, ?, ?)
                ''', (tespit['id'], tespit['sinif'], 
                      datetime.strptime(tespit['tarih'], "%d.%m.%Y %H:%M:%S"),
                      rapor_id))
            
            self.conn.commit()
            messagebox.showinfo("Bilgi", f"Tespitler başarıyla veritabanına kaydedildi!")
            
            # Listeyi temizle
            self.tespit_edilen_nesneler.clear()
            self.tespit_gecmisi.clear()
            self.liste_guncelle()
            
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Hata", f"Tespitler kaydedilirken hata oluştu: {e}")
    
    def guven_guncelle(self, deger):
        """Güven eşiği değerini günceller"""
        self.guven_deger_label.configure(text=f"{deger:.2f}")
    
    def destroy(self):
        """Frame kapatıldığında kamerayı durdur ve veritabanı bağlantısını kapat"""
        self.kamerayi_durdur()
        if hasattr(self, 'conn'):
            self.conn.close()
        super().destroy() 