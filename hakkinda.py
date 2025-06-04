import customtkinter as ctk
import tkinter as tk
import webbrowser

def icerik_goster(parent_frame):
    """
    Hakkında modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Başlık
    baslik = ctk.CTkLabel(container, text="Nesne Tespit Sistemi", font=("Arial", 28, "bold"))
    baslik.pack(pady=20)
    
    # Versiyon
    versiyon = ctk.CTkLabel(container, text="Versiyon 1.0.0", font=("Arial", 14))
    versiyon.pack(pady=5)
    
    # Geliştirici Bilgileri
    gelistirici_frame = ctk.CTkFrame(container)
    gelistirici_frame.pack(fill=tk.X, padx=20, pady=15)
    
    gelistirici_baslik = ctk.CTkLabel(gelistirici_frame, text="🧑‍💻 Geliştirici", 
                                    font=("Arial", 18, "bold"))
    gelistirici_baslik.pack(pady=10)
    
    gelistirici_ad = ctk.CTkLabel(gelistirici_frame, text="Adem Bayhoca", 
                                 font=("Arial", 16, "bold"),
                                 text_color="#1f77b4")
    gelistirici_ad.pack(pady=5)
    
    # GitHub Link Butonu
    def github_ac():
        webbrowser.open("https://github.com/adembayhoca?tab=repositories")
    
    github_buton = ctk.CTkButton(gelistirici_frame, 
                                text="🔗 GitHub Profili",
                                command=github_ac,
                                font=("Arial", 12, "bold"),
                                fg_color="#24292e",
                                hover_color="#0366d6",
                                width=200)
    github_buton.pack(pady=10)
    
    # Açıklama
    aciklama_frame = ctk.CTkFrame(container)
    aciklama_frame.pack(fill=tk.X, padx=20, pady=10)
    
    aciklama_baslik = ctk.CTkLabel(aciklama_frame, text="📋 Uygulama Hakkında", 
                                  font=("Arial", 16, "bold"))
    aciklama_baslik.pack(pady=10)
    
    aciklama = """
    Nesne Tespit Sistemi, yapay zeka ve derin öğrenme teknolojileri kullanarak geliştirilmiş 
    modern bir nesne tespit ve tanıma uygulamasıdır. YOLO (You Only Look Once) algoritması 
    ile desteklenen bu sistem, gerçek zamanlı nesne tespiti, video analizi ve resim işleme 
    yetenekleri sunar.
    
    Bu uygulama, güvenlik sistemleri, akıllı şehir projeleri, endüstriyel kalite kontrol 
    ve araştırma projelerinde kullanılmak üzere tasarlanmıştır.
    """
    
    aciklama_label = ctk.CTkLabel(aciklama_frame, text=aciklama, 
                                 wraplength=800, justify=tk.LEFT)
    aciklama_label.pack(padx=20, pady=10)
    
    # Teknolojiler
    teknoloji_frame = ctk.CTkFrame(container)
    teknoloji_frame.pack(fill=tk.X, padx=20, pady=10)
    
    teknoloji_baslik = ctk.CTkLabel(teknoloji_frame, text="🛠️ Kullanılan Teknolojiler", 
                                   font=("Arial", 16, "bold"))
    teknoloji_baslik.pack(pady=10)
    
    teknolojiler = [
        "• Python 3.11+ - Ana programlama dili",
        "• YOLOv8 (Ultralytics) - Yapay zeka nesne tespit modeli",
        "• OpenCV - Görüntü işleme kütüphanesi",
        "• CustomTkinter - Modern kullanıcı arayüzü",
        "• DeepSORT - Nesne takip algoritması",
        "• SQLite - Veritabanı yönetimi",
        "• PIL/Pillow - Resim işleme kütüphanesi"
    ]
    
    for teknoloji in teknolojiler:
        teknoloji_label = ctk.CTkLabel(teknoloji_frame, text=teknoloji)
        teknoloji_label.pack(anchor=tk.W, padx=20, pady=2)
    
    # Özellikler
    ozellikler_frame = ctk.CTkFrame(container)
    ozellikler_frame.pack(fill=tk.X, padx=20, pady=10)
    
    ozellikler_baslik = ctk.CTkLabel(ozellikler_frame, text="⭐ Temel Özellikler", 
                                    font=("Arial", 16, "bold"))
    ozellikler_baslik.pack(pady=10)
    
    ozellikler = [
        "• Gerçek zamanlı canlı nesne tespiti",
        "• Video dosyalarından nesne analizi",
        "• Resim dosyalarından nesne tespiti", 
        "• Güven eşiği ayarlama seçenekleri",
        "• Detaylı raporlama ve istatistikler",
        "• Türkçe nesne sınıf adları",
        "• Veritabanı tabanlı kayıt sistemi",
        "• Modern ve kullanıcı dostu arayüz"
    ]
    
    for ozellik in ozellikler:
        ozellik_label = ctk.CTkLabel(ozellikler_frame, text=ozellik)
        ozellik_label.pack(anchor=tk.W, padx=20, pady=2)
    
    # Telif hakkı ve Lisans - Daha görünür hale getirme
    alt_frame = ctk.CTkFrame(container)
    alt_frame.pack(fill=tk.X, padx=20, pady=20)
    
    # Copyright vurgusu
    telif_text = "© 2024 Adem Bayhoca - Nesne Tespit Sistemi"
    telif_label = ctk.CTkLabel(alt_frame, text=telif_text, 
                              font=("Arial", 14, "bold"),
                              text_color="#1565c0")
    telif_label.pack(pady=10)
    
    # Haklar vurgusu
    haklar_text = "Tüm hakları saklıdır."
    haklar_label = ctk.CTkLabel(alt_frame, text=haklar_text, 
                               font=("Arial", 12, "bold"),
                               text_color="#d32f2f")
    haklar_label.pack(pady=5)
    
    # Lisans bilgisi
    lisans_text = "Bu yazılım MIT lisansı altında lisanslanmıştır."
    lisans_label = ctk.CTkLabel(alt_frame, text=lisans_text, 
                               font=("Arial", 11))
    lisans_label.pack(pady=5)
    
    # Türkiye vurgusu - daha büyük ve görünür
    gelistirme_text = "🇹🇷 Türkiye'de geliştirilmiştir 🇹🇷"
    gelistirme_label = ctk.CTkLabel(alt_frame, text=gelistirme_text, 
                                   font=("Arial", 16, "bold"), 
                                   text_color="#e74c3c")
    gelistirme_label.pack(pady=15) 