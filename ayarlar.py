import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
import os
from giris import kullanici_bilgilerini_yukle, kullanici_bilgilerini_kaydet

# Ayarlar dosyası yolu
AYARLAR_DOSYASI = "ayarlar.json"

def ayarlari_yukle():
    """
    Kaydedilmiş ayarları yükler.
    """
    if os.path.exists(AYARLAR_DOSYASI):
        with open(AYARLAR_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "dil": "Türkçe",
        "varsayilan_kamera": "Kamera 0",
        "cozunurluk": "1280x720",
        "guven_esigi": 0.5
    }

def ayarlari_kaydet(ayarlar):
    """
    Ayarları kaydeder.
    """
    with open(AYARLAR_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(ayarlar, f, ensure_ascii=False, indent=4)

def icerik_goster(parent_frame):
    """
    Ayarlar modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Başlık
    baslik = ctk.CTkLabel(container, text="Ayarlar", font=("Arial", 24, "bold"))
    baslik.pack(pady=20)
    
    # Ayarlar için frame
    ayarlar_frame = ctk.CTkFrame(container)
    ayarlar_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Genel Ayarlar
    genel_frame = ctk.CTkFrame(ayarlar_frame)
    genel_frame.pack(fill=tk.X, padx=20, pady=10)
    
    genel_baslik = ctk.CTkLabel(genel_frame, text="Genel Ayarlar", font=("Arial", 16, "bold"))
    genel_baslik.pack(anchor=tk.W, padx=10, pady=5)
    
    # Dil seçimi
    dil_frame = ctk.CTkFrame(genel_frame)
    dil_frame.pack(fill=tk.X, padx=10, pady=5)
    
    dil_label = ctk.CTkLabel(dil_frame, text="Dil:")
    dil_label.pack(side=tk.LEFT, padx=10)
    
    dil_secim = ctk.CTkComboBox(dil_frame, values=["Türkçe", "English"])
    dil_secim.pack(side=tk.LEFT, padx=10)
    dil_secim.set("Türkçe")
    
    # Kamera Ayarları
    kamera_frame = ctk.CTkFrame(ayarlar_frame)
    kamera_frame.pack(fill=tk.X, padx=20, pady=10)
    
    kamera_baslik = ctk.CTkLabel(kamera_frame, text="Kamera Ayarları", font=("Arial", 16, "bold"))
    kamera_baslik.pack(anchor=tk.W, padx=10, pady=5)
    
    # Varsayılan kamera
    varsayilan_frame = ctk.CTkFrame(kamera_frame)
    varsayilan_frame.pack(fill=tk.X, padx=10, pady=5)
    
    varsayilan_label = ctk.CTkLabel(varsayilan_frame, text="Varsayılan Kamera:")
    varsayilan_label.pack(side=tk.LEFT, padx=10)
    
    kamera_secim = ctk.CTkComboBox(varsayilan_frame, values=["Kamera 0", "Kamera 1", "Kamera 2"])
    kamera_secim.pack(side=tk.LEFT, padx=10)
    kamera_secim.set("Kamera 0")
    
    # Çözünürlük
    cozunurluk_frame = ctk.CTkFrame(kamera_frame)
    cozunurluk_frame.pack(fill=tk.X, padx=10, pady=5)
    
    cozunurluk_label = ctk.CTkLabel(cozunurluk_frame, text="Çözünürlük:")
    cozunurluk_label.pack(side=tk.LEFT, padx=10)
    
    cozunurluk_secim = ctk.CTkComboBox(cozunurluk_frame, 
                                     values=["640x480", "1280x720", "1920x1080"])
    cozunurluk_secim.pack(side=tk.LEFT, padx=10)
    cozunurluk_secim.set("1280x720")
    
    # Tespit Ayarları
    tespit_frame = ctk.CTkFrame(ayarlar_frame)
    tespit_frame.pack(fill=tk.X, padx=20, pady=10)
    
    tespit_baslik = ctk.CTkLabel(tespit_frame, text="Tespit Ayarları", font=("Arial", 16, "bold"))
    tespit_baslik.pack(anchor=tk.W, padx=10, pady=5)
    
    # Güven eşiği
    guven_frame = ctk.CTkFrame(tespit_frame)
    guven_frame.pack(fill=tk.X, padx=10, pady=5)
    
    guven_label = ctk.CTkLabel(guven_frame, text="Güven Eşiği:")
    guven_label.pack(side=tk.LEFT, padx=10)
    
    guven_slider = ctk.CTkSlider(guven_frame, from_=0, to=1, number_of_steps=100)
    guven_slider.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
    guven_slider.set(0.5)
    
    guven_deger = ctk.CTkLabel(guven_frame, text="0.5")
    guven_deger.pack(side=tk.LEFT, padx=10)
    
    def guven_guncelle(value):
        """Güven eşiği değerini günceller"""
        guven_deger.configure(text=f"{value:.2f}")
    
    guven_slider.configure(command=guven_guncelle)
    
    # Şifre Değiştirme
    sifre_frame = ctk.CTkFrame(ayarlar_frame)
    sifre_frame.pack(fill=tk.X, padx=20, pady=10)
    
    sifre_baslik = ctk.CTkLabel(sifre_frame, text="Şifre Değiştirme", font=("Arial", 16, "bold"))
    sifre_baslik.pack(anchor=tk.W, padx=10, pady=5)
    
    # Mevcut şifre
    mevcut_frame = ctk.CTkFrame(sifre_frame)
    mevcut_frame.pack(fill=tk.X, padx=10, pady=5)
    
    mevcut_label = ctk.CTkLabel(mevcut_frame, text="Mevcut Şifre:")
    mevcut_label.pack(side=tk.LEFT, padx=10)
    
    mevcut_sifre = ctk.CTkEntry(mevcut_frame, show="•", width=300)
    mevcut_sifre.pack(side=tk.LEFT, padx=10)
    
    # Yeni şifre
    yeni_frame = ctk.CTkFrame(sifre_frame)
    yeni_frame.pack(fill=tk.X, padx=10, pady=5)
    
    yeni_label = ctk.CTkLabel(yeni_frame, text="Yeni Şifre:")
    yeni_label.pack(side=tk.LEFT, padx=10)
    
    yeni_sifre = ctk.CTkEntry(yeni_frame, show="•", width=300)
    yeni_sifre.pack(side=tk.LEFT, padx=10)
    
    # Yeni şifre tekrar
    tekrar_frame = ctk.CTkFrame(sifre_frame)
    tekrar_frame.pack(fill=tk.X, padx=10, pady=5)
    
    tekrar_label = ctk.CTkLabel(tekrar_frame, text="Yeni Şifre (Tekrar):")
    tekrar_label.pack(side=tk.LEFT, padx=10)
    
    tekrar_sifre = ctk.CTkEntry(tekrar_frame, show="•", width=300)
    tekrar_sifre.pack(side=tk.LEFT, padx=10)
    
    def sifre_degistir():
        """Şifre değiştirme işlemini gerçekleştirir"""
        if not mevcut_sifre.get():
            messagebox.showwarning("Uyarı", "Lütfen mevcut şifrenizi girin!")
            return
        
        if not yeni_sifre.get():
            messagebox.showwarning("Uyarı", "Lütfen yeni şifrenizi girin!")
            return
        
        if yeni_sifre.get() != tekrar_sifre.get():
            messagebox.showwarning("Uyarı", "Yeni şifreler eşleşmiyor!")
            return
        
        kullanici_bilgileri = kullanici_bilgilerini_yukle()
        
        if mevcut_sifre.get() != kullanici_bilgileri["sifre"]:
            messagebox.showerror("Hata", "Mevcut şifre hatalı!")
            return
        
        # Şifre gereksinimlerini kontrol et
        if len(yeni_sifre.get()) < 8:
            messagebox.showwarning("Uyarı", "Şifre en az 8 karakter uzunluğunda olmalı!")
            return
        
        if not any(c.isupper() for c in yeni_sifre.get()):
            messagebox.showwarning("Uyarı", "Şifre en az bir büyük harf içermeli!")
            return
        
        if not any(c.islower() for c in yeni_sifre.get()):
            messagebox.showwarning("Uyarı", "Şifre en az bir küçük harf içermeli!")
            return
        
        if not any(c.isdigit() for c in yeni_sifre.get()):
            messagebox.showwarning("Uyarı", "Şifre en az bir rakam içermeli!")
            return
        
        if not any(c in "!@#$%^&*" for c in yeni_sifre.get()):
            messagebox.showwarning("Uyarı", "Şifre en az bir özel karakter içermeli!")
            return
        
        # Şifreyi güncelle ve kaydet
        kullanici_bilgileri["sifre"] = yeni_sifre.get()
        kullanici_bilgilerini_kaydet(kullanici_bilgileri)
        
        messagebox.showinfo("Bilgi", "Şifreniz başarıyla değiştirildi!")
        mevcut_sifre.delete(0, tk.END)
        yeni_sifre.delete(0, tk.END)
        tekrar_sifre.delete(0, tk.END)
    
    # Şifre değiştirme butonu
    sifre_buton = ctk.CTkButton(sifre_frame, text="Şifreyi Değiştir", 
                               command=sifre_degistir,
                               fg_color="#34A853", hover_color="#2E7D32")
    sifre_buton.pack(pady=10)
    
    # Kaydet butonu
    kaydet_buton = ctk.CTkButton(container, text="Ayarları Kaydet", 
                                command=lambda: ayarlari_kaydet_ve_kapat(),
                                fg_color="#1E88E5", hover_color="#1565C0")
    kaydet_buton.pack(pady=20)
    
    def ayarlari_kaydet_ve_kapat():
        """Ayarları kaydeder ve bilgi mesajı gösterir"""
        ayarlar = {
            "dil": dil_secim.get(),
            "varsayilan_kamera": kamera_secim.get(),
            "cozunurluk": cozunurluk_secim.get(),
            "guven_esigi": guven_slider.get()
        }
        ayarlari_kaydet(ayarlar)
        messagebox.showinfo("Bilgi", "Ayarlar başarıyla kaydedildi!") 