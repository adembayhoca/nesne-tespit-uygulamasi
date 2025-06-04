import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import threading
import time
from datetime import datetime
import os
from PIL import Image, ImageTk
import video_tespit
import resim_tespit
import tespit_raporlari
import ayarlar
import yardim
import hakkinda
import iletisim
import sifre_degistir
import json
import webbrowser
from giris import GirisEkrani
from canli_tespit import CanliTespit
from video_tespit import VideoTespit

class AnaUygulama(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Pencere ayarları
        self.title("Nesne Tespit")
        self.geometry("1280x800")
        self.minsize(1024, 800)
        
        # Tema ayarları
        self.mevcut_tema = "light"
        ctk.set_appearance_mode(self.mevcut_tema)
        ctk.set_default_color_theme("blue")
        
        # Ana container
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # Sol menü
        self.sol_menu = ctk.CTkFrame(self.container, width=250)
        self.sol_menu.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Logo ve geliştirici bilgileri bölümü
        self.logo_container = ctk.CTkFrame(self.sol_menu)
        self.logo_container.pack(fill=tk.X, padx=10, pady=10)
        
        # Geliştirici ikonu ve isim
        self.gelistirici_label = ctk.CTkLabel(self.logo_container, text="🧑‍💻 Geliştirici", 
                                            font=("Arial", 12, "bold"))
        self.gelistirici_label.pack(pady=5)
        
        self.gelistirici_ad = ctk.CTkLabel(self.logo_container, text="Adem Bayhoca", 
                                         font=("Arial", 16, "bold"),
                                         text_color="#1f77b4")
        self.gelistirici_ad.pack(pady=5)
        
        # GitHub butonu
        def github_ac():
            webbrowser.open("https://github.com/adembayhoca?tab=repositories")
        
        self.github_buton = ctk.CTkButton(self.logo_container, 
                                        text="🔗 GitHub",
                                        command=github_ac,
                                        font=("Arial", 10, "bold"),
                                        fg_color="#24292e",
                                        hover_color="#0366d6",
                                        width=150,
                                        height=30)
        self.github_buton.pack(pady=8)
        
        # Saat
        self.saat_label = ctk.CTkLabel(self.sol_menu, text="", font=("Arial", 16))
        self.saat_label.pack(pady=10)
        self.saati_guncelle()
        
        # Ayırıcı çizgi
        self.ayirici1 = ctk.CTkFrame(self.sol_menu, height=2)
        self.ayirici1.pack(fill=tk.X, padx=15, pady=15)
        
        # Menü butonları
        self.menu_butonlari = []
        
        menu_items = [
            ("Canlı Tespit", self.canli_tespit_goster),
            ("Video Tespit", self.video_tespit_goster),
            ("Resim Tespit", resim_tespit.icerik_goster),
            ("Tespit Raporları", tespit_raporlari.icerik_goster),
            ("Yardım", yardim.icerik_goster),
            ("Hakkında", hakkinda.icerik_goster),
            ("İletişim", iletisim.icerik_goster),
            ("Şifre Değiştir", sifre_degistir.icerik_goster),
            ("Ayarlar", ayarlar.icerik_goster)
        ]
        
        # Buton boyutları için sabit değerler
        buton_yukseklik = 40
        buton_yazi_boyutu = 14
        
        for text, command in menu_items:
            btn = ctk.CTkButton(self.sol_menu, text=text, command=lambda cmd=command: self.icerik_goster(cmd),
                              height=buton_yukseklik, font=("Arial", buton_yazi_boyutu, "bold"),
                              fg_color="#1E88E5", hover_color="#1565C0")
            btn.pack(fill=tk.X, padx=20, pady=8)
            self.menu_butonlari.append(btn)
        
        # Alt ayırıcı çizgi
        self.ayirici2 = ctk.CTkFrame(self.sol_menu, height=2)
        self.ayirici2.pack(fill=tk.X, padx=15, pady=15)
        
        # Tema değiştirme butonu
        self.tema_buton = ctk.CTkButton(self.sol_menu, text="Tema Değiştir", 
                                      command=self.tema_degistir,
                                      height=buton_yukseklik, font=("Arial", buton_yazi_boyutu, "bold"),
                                      fg_color="#E91E63", hover_color="#C2185B")
        self.tema_buton.pack(fill=tk.X, padx=20, pady=8)
        
        # Çıkış butonu
        self.cikis_buton = ctk.CTkButton(self.sol_menu, text="Çıkış", 
                                        command=self.quit,
                                        fg_color="#EA4335", hover_color="#C62828",
                                        height=buton_yukseklik, font=("Arial", buton_yazi_boyutu, "bold"))
        self.cikis_buton.pack(fill=tk.X, padx=20, pady=8)
        
        # İçerik alanı
        self.icerik_alani = ctk.CTkFrame(self.container)
        self.icerik_alani.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Canlı tespit modülü
        self.canli_tespit = CanliTespit(self.icerik_alani)
        self.canli_tespit.pack(fill=tk.BOTH, expand=True)
        
        # Video tespit modülü
        self.video_tespit = VideoTespit(self.icerik_alani)
        self.video_tespit.pack(fill=tk.BOTH, expand=True)
        self.video_tespit.pack_forget()  # Başlangıçta gizle
        
        # Varsayılan içeriği göster
        self.canli_tespit_goster()
    
    def canli_tespit_goster(self, parent=None):
        """Canlı tespit modülünü gösterir"""
        # Mevcut içeriği temizle
        for widget in self.icerik_alani.winfo_children():
            widget.destroy()
        
        # Canlı tespit modülünü göster
        self.canli_tespit = CanliTespit(self.icerik_alani)
        self.canli_tespit.pack(fill=tk.BOTH, expand=True)
        
        # Son içeriği kaydet
        self.son_icerik = self.canli_tespit_goster
    
    def video_tespit_goster(self, parent=None):
        """Video tespit modülünü gösterir"""
        # Mevcut içeriği temizle
        for widget in self.icerik_alani.winfo_children():
            widget.destroy()
        
        # Video tespit modülünü göster
        self.video_tespit = VideoTespit(self.icerik_alani)
        self.video_tespit.pack(fill=tk.BOTH, expand=True)
        
        # Son içeriği kaydet
        self.son_icerik = self.video_tespit_goster
    
    def tema_degistir(self):
        """Tema değiştirme fonksiyonu"""
        # Mevcut temayı değiştir
        self.mevcut_tema = "dark" if self.mevcut_tema == "light" else "light"
        
        # Tüm uygulamaya yeni temayı uygula
        ctk.set_appearance_mode(self.mevcut_tema)
        
        # Menü butonlarının renklerini güncelle
        for btn in self.menu_butonlari:
            if self.mevcut_tema == "dark":
                btn.configure(fg_color="#34A853", hover_color="#2E7D32")
            else:
                btn.configure(fg_color="#1E88E5", hover_color="#1565C0")
        
        # Tüm widget'ları yeniden oluştur
        self.update()
        
        # İçerik alanını yeniden yükle
        if hasattr(self, 'son_icerik'):
            self.icerik_goster(self.son_icerik)
    
    def saati_guncelle(self):
        """Saat ve tarihi günceller"""
        simdi = datetime.now()
        self.saat_label.configure(text=simdi.strftime("%d.%m.%Y %H:%M:%S"))
        self.after(1000, self.saati_guncelle)
    
    def icerik_goster(self, icerik_fonksiyonu):
        """İçerik alanını günceller"""
        # Mevcut içeriği temizle
        for widget in self.icerik_alani.winfo_children():
            widget.destroy()
        
        # Son içeriği kaydet
        self.son_icerik = icerik_fonksiyonu
        
        # Yeni içeriği göster
        if icerik_fonksiyonu == self.canli_tespit_goster:
            self.canli_tespit_goster()
        elif icerik_fonksiyonu == self.video_tespit_goster:
            self.video_tespit_goster()
        else:
            icerik_fonksiyonu(self.icerik_alani)

def main():
    """
    Uygulamanın ana başlangıç fonksiyonu.
    Bu fonksiyon setup.py entry point'i için kullanılır.
    """
    try:
        # Giriş ekranını başlat
        app = GirisEkrani()
        app.mainloop()
    except Exception as e:
        print(f"Uygulama başlatılırken hata oluştu: {e}")
        return 1
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main()) 