import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def icerik_goster(parent_frame):
    """
    Yardım modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Başlık
    baslik = ctk.CTkLabel(container, text="Yardım ve Destek", font=("Arial", 24, "bold"))
    baslik.pack(pady=20)
    
    # SSS için frame
    sss_frame = ctk.CTkFrame(container)
    sss_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    sss_baslik = ctk.CTkLabel(sss_frame, text="Sıkça Sorulan Sorular", font=("Arial", 16, "bold"))
    sss_baslik.pack(anchor=tk.W, padx=10, pady=5)
    
    # SSS içeriği
    sss_icerik = [
        {
            "soru": "Kameramı nasıl bağlayabilirim?",
            "cevap": "Kameranızı USB portuna bağladıktan sonra, 'Canlı Tespit' sayfasından kamera seçimini yapabilirsiniz. Eğer kamera görünmüyorsa, lütfen sürücülerin yüklü olduğundan emin olun."
        },
        {
            "soru": "Hangi video formatları destekleniyor?",
            "cevap": "Sistem MP4, AVI, MOV ve MKV formatlarını desteklemektedir. En iyi performans için MP4 formatını kullanmanızı öneririz."
        },
        {
            "soru": "Tespit sonuçlarını nasıl kaydedebilirim?",
            "cevap": "Tespit sonuçları otomatik olarak kaydedilir. Ayrıca 'Tespit Raporları' sayfasından sonuçları Excel veya PDF olarak dışa aktarabilirsiniz."
        },
        {
            "soru": "Tema nasıl değiştirilir?",
            "cevap": "Sağ üst köşedeki tema butonuna tıklayarak açık/koyu tema arasında geçiş yapabilirsiniz."
        }
    ]
    
    for i, item in enumerate(sss_icerik):
        soru_frame = ctk.CTkFrame(sss_frame)
        soru_frame.pack(fill=tk.X, padx=10, pady=5)
        
        soru_label = ctk.CTkLabel(soru_frame, text=f"Soru {i+1}: {item['soru']}", 
                                font=("Arial", 12, "bold"))
        soru_label.pack(anchor=tk.W, padx=10, pady=5)
        
        cevap_label = ctk.CTkLabel(soru_frame, text=item['cevap'], 
                                 wraplength=800, justify=tk.LEFT)
        cevap_label.pack(anchor=tk.W, padx=20, pady=5)
    
    # İletişim bilgileri
    iletisim_frame = ctk.CTkFrame(container)
    iletisim_frame.pack(fill=tk.X, padx=20, pady=10)
    
    iletisim_baslik = ctk.CTkLabel(iletisim_frame, text="İletişim Bilgileri", 
                                  font=("Arial", 16, "bold"))
    iletisim_baslik.pack(anchor=tk.W, padx=10, pady=5)
    
    iletisim_bilgileri = [
        "E-posta: destek@nesnetespit.com",
        "Telefon: +90 (212) 123 45 67",
        "Adres: Teknoloji Caddesi No:1, İstanbul"
    ]
    
    for bilgi in iletisim_bilgileri:
        bilgi_label = ctk.CTkLabel(iletisim_frame, text=bilgi)
        bilgi_label.pack(anchor=tk.W, padx=20, pady=2)
    
    # Destek talebi butonu
    destek_buton = ctk.CTkButton(container, text="Destek Talebi Oluştur", 
                                command=lambda: destek_talebi_olustur(),
                                fg_color="#4285F4", hover_color="#1A73E8")
    destek_buton.pack(pady=20)
    
    def destek_talebi_olustur():
        """Destek talebi oluşturma işlemini başlatır"""
        messagebox.showinfo("Bilgi", "Destek talebi oluşturma sayfasına yönlendiriliyorsunuz...") 