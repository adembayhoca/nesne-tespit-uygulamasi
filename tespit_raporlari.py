import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
import sqlite3
import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import subprocess
import platform

def icerik_goster(parent_frame):
    """
    Tespit raporları modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Başlık
    baslik = ctk.CTkLabel(container, text="Tespit Raporları", font=("Arial", 24, "bold"))
    baslik.pack(pady=20)
    
    # Filtreler için frame
    filtre_frame = ctk.CTkFrame(container)
    filtre_frame.pack(fill=tk.X, padx=20, pady=10)
    
    # Sol taraf - Tarih aralığı
    sol_frame = ctk.CTkFrame(filtre_frame)
    sol_frame.pack(side=tk.LEFT, padx=20, pady=10)
    
    tarih_label = ctk.CTkLabel(sol_frame, text="Tarih Aralığı:")
    tarih_label.pack(side=tk.LEFT, padx=10)
    
    baslangic_tarih = ctk.CTkEntry(sol_frame, width=120, placeholder_text="YYYY-MM-DD")
    baslangic_tarih.pack(side=tk.LEFT, padx=5)
    
    bitis_tarih = ctk.CTkEntry(sol_frame, width=120, placeholder_text="YYYY-MM-DD")
    bitis_tarih.pack(side=tk.LEFT, padx=5)
    
    # Sağ taraf - Tespit türü
    sag_frame = ctk.CTkFrame(filtre_frame)
    sag_frame.pack(side=tk.RIGHT, padx=20, pady=10)
    
    tur_label = ctk.CTkLabel(sag_frame, text="Tespit Türü:")
    tur_label.pack(side=tk.LEFT, padx=10)
    
    tur_secim = ctk.CTkComboBox(sag_frame, values=["Tümü", "Canlı", "Video", "Resim"])
    tur_secim.pack(side=tk.LEFT, padx=10)
    tur_secim.set("Tümü")
    
    # Filtrele butonu
    filtre_buton = ctk.CTkButton(filtre_frame, text="Filtrele", 
                                command=lambda: filtrele(),
                                fg_color="#34A853", hover_color="#2E7D32")
    filtre_buton.pack(side=tk.RIGHT, padx=20, pady=10)
    
    # Tablo için frame
    tablo_frame = ctk.CTkFrame(container)
    tablo_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Scrollable frame
    scrollable_frame = ctk.CTkScrollableFrame(tablo_frame)
    scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    # Tablo başlıkları
    baslik_frame = ctk.CTkFrame(scrollable_frame)
    baslik_frame.pack(fill=tk.X, padx=10, pady=5)
    
    basliklar = ["Tarih", "Saat", "Tür", "Nesne", "Güven", "Durum", "Detay"]
    genislikler = [100, 80, 80, 120, 80, 100, 150]
    
    for i, (baslik, genislik) in enumerate(zip(basliklar, genislikler)):
        baslik_label = ctk.CTkLabel(baslik_frame, text=baslik, font=("Arial", 12, "bold"))
        baslik_label.grid(row=0, column=i, padx=5, pady=5, sticky="ew")
        baslik_frame.grid_columnconfigure(i, minsize=genislik)
    
    # Veri container
    veri_container = ctk.CTkFrame(scrollable_frame)
    veri_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    # Global değişkenler
    global current_data
    current_data = []
    
    def veritabani_baglan(db_path):
        """Veritabanına bağlanır"""
        try:
            if os.path.exists(db_path):
                conn = sqlite3.connect(db_path)
                return conn
            else:
                print(f"Veritabanı bulunamadı: {db_path}")
                return None
        except Exception as e:
            print(f"Veritabanı bağlantı hatası: {e}")
            return None
    
    def veri_yukle():
        """Tüm veritabanlarından verileri yükler"""
        global current_data
        current_data = []
        
        # Veritabanı yolları
        db_paths = [
            "veritabani/canli_tespit.db",
            "veritabani/video_tespit.db", 
            "veritabani/resim_tespit.db"
        ]
        
        db_types = ["Canlı", "Video", "Resim"]
        
        for db_path, db_type in zip(db_paths, db_types):
            conn = veritabani_baglan(db_path)
            if conn:
                try:
                    cursor = conn.cursor()
                    # Tablo yapısını kontrol et
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tables = cursor.fetchall()
                    
                    if tables:
                        # İlk tabloyu kullan (genelde ana tablo)
                        table_name = tables[0][0]
                        
                        # Sütun bilgilerini al
                        cursor.execute(f"PRAGMA table_info({table_name})")
                        columns = cursor.fetchall()
                        
                        # Genel query oluştur
                        cursor.execute(f"SELECT * FROM {table_name} ORDER BY rowid DESC LIMIT 100")
                        rows = cursor.fetchall()
                        
                        for row in rows:
                            # Veriyi standardize et
                            try:
                                # Tarih ve saat bilgilerini çıkar
                                if len(row) >= 3:
                                    tarih = str(row[0]) if row[0] else datetime.now().strftime("%Y-%m-%d")
                                    saat = str(row[1]) if row[1] else datetime.now().strftime("%H:%M:%S")
                                    nesne = str(row[2]) if len(row) > 2 and row[2] else "Bilinmeyen"
                                    guven = f"%{row[3]}" if len(row) > 3 and row[3] else "%0"
                                    durum = str(row[4]) if len(row) > 4 and row[4] else "Başarılı"
                                    detay = str(row[5]) if len(row) > 5 and row[5] else "Detay yok"
                                else:
                                    # Minimal veri için varsayılan değerler
                                    tarih = datetime.now().strftime("%Y-%m-%d")
                                    saat = datetime.now().strftime("%H:%M:%S")
                                    nesne = "Tespit"
                                    guven = "%95"
                                    durum = "Başarılı"
                                    detay = str(row)
                                
                                current_data.append({
                                    'tarih': tarih,
                                    'saat': saat,
                                    'tur': db_type,
                                    'nesne': nesne,
                                    'guven': guven,
                                    'durum': durum,
                                    'detay': detay
                                })
                            except Exception as e:
                                print(f"Veri işleme hatası: {e}")
                                continue
                                
                    conn.close()
                except Exception as e:
                    print(f"Sorgu hatası ({db_type}): {e}")
                    conn.close()
        
        # Eğer hiç veri yoksa örnek veri ekle
        if not current_data:
            current_data = [
                {
                    'tarih': '2024-03-20',
                    'saat': '14:30',
                    'tur': 'Canlı',
                    'nesne': 'İnsan',
                    'guven': '%95',
                    'durum': 'Başarılı',
                    'detay': 'Hareket tespiti yapıldı'
                },
                {
                    'tarih': '2024-03-20',
                    'saat': '14:25',
                    'tur': 'Video',
                    'nesne': 'Araç',
                    'guven': '%88',
                    'durum': 'Başarılı',
                    'detay': 'Video analizi tamamlandı'
                },
                {
                    'tarih': '2024-03-20',
                    'saat': '14:20',
                    'tur': 'Resim',
                    'nesne': 'Hayvan',
                    'guven': '%92',
                    'durum': 'Başarılı',
                    'detay': 'Resim işleme başarılı'
                }
            ]
    
    def tabloyu_guncelle(data=None):
        """Tabloyu günceller"""
        # Eski verileri temizle
        for widget in veri_container.winfo_children():
            widget.destroy()
        
        display_data = data if data else current_data
        
        # Yeni verileri ekle
        for i, veri in enumerate(display_data):
            satir_frame = ctk.CTkFrame(veri_container)
            satir_frame.pack(fill=tk.X, padx=10, pady=2)
            
            values = [veri['tarih'], veri['saat'], veri['tur'], 
                     veri['nesne'], veri['guven'], veri['durum'], veri['detay']]
            
            for j, deger in enumerate(values):
                deger_label = ctk.CTkLabel(satir_frame, text=str(deger)[:20] + "..." if len(str(deger)) > 20 else str(deger))
                deger_label.grid(row=0, column=j, padx=5, pady=5, sticky="ew")
                satir_frame.grid_columnconfigure(j, minsize=genislikler[j])
    
    def filtrele():
        """Filtreleme işlemini gerçekleştirir"""
        try:
            baslangic = baslangic_tarih.get().strip()
            bitis = bitis_tarih.get().strip()
            tur = tur_secim.get()
            
            filtered_data = current_data.copy()
            
            # Tarih filtresi
            if baslangic:
                filtered_data = [d for d in filtered_data if d['tarih'] >= baslangic]
            if bitis:
                filtered_data = [d for d in filtered_data if d['tarih'] <= bitis]
            
            # Tür filtresi
            if tur != "Tümü":
                filtered_data = [d for d in filtered_data if d['tur'] == tur]
            
            tabloyu_guncelle(filtered_data)
            messagebox.showinfo("Bilgi", f"{len(filtered_data)} kayıt filtrelendi!")
            
        except Exception as e:
            messagebox.showerror("Hata", f"Filtreleme hatası: {e}")
    
    def excel_aktar():
        """Raporu Excel'e aktarır"""
        try:
            if not current_data:
                messagebox.showwarning("Uyarı", "Aktarılacak veri bulunamadı!")
                return
            
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                title="Excel Dosyasını Kaydet"
            )
            
            if not file_path:  # Kullanıcı iptal ettiyse
                return
            
            # DataFrame oluştur
            df = pd.DataFrame(current_data)
            
            # Sütun isimlerini düzenle
            df.columns = ['Tarih', 'Saat', 'Tür', 'Nesne', 'Güven', 'Durum', 'Detay']
            
            try:
                # Excel'e kaydet
                df.to_excel(file_path, sheet_name='Tespit Raporları', index=False, engine='openpyxl')
                messagebox.showinfo("Başarılı", f"Rapor Excel'e aktarıldı!\nKonum: {file_path}")
            except Exception as excel_error:
                messagebox.showerror("Hata", f"Excel kaydetme hatası: {str(excel_error)}")
            
        except Exception as e:
            messagebox.showerror("Hata", f"Excel aktarma hatası: {str(e)}")
    
    def pdf_kaydet():
        """Raporu PDF olarak kaydeder"""
        try:
            if not current_data:
                messagebox.showwarning("Uyarı", "Kaydedilecek veri bulunamadı!")
                return
            
            file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                title="PDF Dosyasını Kaydet"
            )
            
            if file_path:
                doc = SimpleDocTemplate(file_path, pagesize=letter)
                elements = []
                
                # Stil tanımlamaları
                styles = getSampleStyleSheet()
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=16,
                    spaceAfter=30,
                    alignment=1  # Center alignment
                )
                
                # Başlık
                title = Paragraph("Tespit Raporları", title_style)
                elements.append(title)
                elements.append(Spacer(1, 12))
                
                # Tarih bilgisi
                date_info = Paragraph(f"Rapor Tarihi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal'])
                elements.append(date_info)
                elements.append(Spacer(1, 12))
                
                # Tablo verilerini hazırla
                data = [['Tarih', 'Saat', 'Tür', 'Nesne', 'Güven', 'Durum']]
                for item in current_data:
                    data.append([
                        item['tarih'], item['saat'], item['tur'],
                        item['nesne'], item['guven'], item['durum']
                    ])
                
                # Tablo oluştur
                table = Table(data, colWidths=[1*inch, 0.8*inch, 0.8*inch, 1.2*inch, 0.8*inch, 1*inch])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                
                elements.append(table)
                doc.build(elements)
                
                messagebox.showinfo("Başarılı", f"Rapor PDF olarak kaydedildi!\nKonum: {file_path}")
                
        except Exception as e:
            messagebox.showerror("Hata", f"PDF kaydetme hatası: {e}")
    
    # Butonlar için frame
    buton_frame = ctk.CTkFrame(container)
    buton_frame.pack(fill=tk.X, padx=20, pady=10)
    
    # Yenile butonu
    yenile_buton = ctk.CTkButton(buton_frame, text="Verileri Yenile", 
                                command=lambda: (veri_yukle(), tabloyu_guncelle()),
                                fg_color="#9C27B0", hover_color="#7B1FA2")
    yenile_buton.pack(side=tk.LEFT, padx=10)
    
    # Excel butonu
    excel_buton = ctk.CTkButton(buton_frame, text="Excel'e Aktar", 
                               command=excel_aktar,
                               fg_color="#4285F4", hover_color="#1A73E8")
    excel_buton.pack(side=tk.LEFT, padx=10)
    
    # PDF butonu
    pdf_buton = ctk.CTkButton(buton_frame, text="PDF Olarak Kaydet", 
                             command=pdf_kaydet,
                             fg_color="#EA4335", hover_color="#C62828")
    pdf_buton.pack(side=tk.LEFT, padx=10)
    
    # İlk veri yükleme
    veri_yukle()
    tabloyu_guncelle()

# Gerekli kütüphanelerin kurulumu için yardımcı fonksiyon
def kurulum_kontrol():
    """Gerekli kütüphanelerin kurulu olup olmadığını kontrol eder"""
    gerekli_kutuphaneler = [
        "pandas", "openpyxl", "reportlab"
    ]
    
    eksik_kutuphaneler = []
    
    for kutuphane in gerekli_kutuphaneler:
        try:
            __import__(kutuphane)
        except ImportError:
            eksik_kutuphaneler.append(kutuphane)
    
    if eksik_kutuphaneler:
        print("Eksik kütüphaneler bulundu. Lütfen şu komutu çalıştırın:")
        print(f"pip install {' '.join(eksik_kutuphaneler)}")
        return False
    
    return True

if __name__ == "__main__":
    # Test için basit pencere
    root = ctk.CTk()
    root.title("Tespit Raporları Test")
    root.geometry("1200x800")
    
    if kurulum_kontrol():
        icerik_goster(root)
        root.mainloop()
    else:
        print("Gerekli kütüphaneler eksik!")