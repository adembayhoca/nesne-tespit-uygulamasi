import customtkinter as ctk
import tkinter as tk
import webbrowser
from tkinter import messagebox
import subprocess
import sys

def icerik_goster(parent_frame):
    """
    İletişim modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Başlık
    baslik = ctk.CTkLabel(container, text="📞 İletişim", font=("Arial", 28, "bold"))
    baslik.pack(pady=20)
    
    # Geliştirici Bilgileri
    gelistirici_frame = ctk.CTkFrame(container)
    gelistirici_frame.pack(fill=tk.X, padx=20, pady=15)
    
    gelistirici_baslik = ctk.CTkLabel(gelistirici_frame, text="🧑‍💻 Geliştirici", 
                                    font=("Arial", 18, "bold"))
    gelistirici_baslik.pack(pady=15)
    
    # Geliştirici adı
    gelistirici_ad = ctk.CTkLabel(gelistirici_frame, text="Adem Bayhoca", 
                                 font=("Arial", 20, "bold"),
                                 text_color="#1f77b4")
    gelistirici_ad.pack(pady=10)
    
    # E-mail Bilgisi
    email_frame = ctk.CTkFrame(gelistirici_frame)
    email_frame.pack(fill=tk.X, padx=20, pady=10)
    
    email_baslik = ctk.CTkLabel(email_frame, text="📧 E-mail", 
                               font=("Arial", 16, "bold"))
    email_baslik.pack(pady=10)
    
    email_adres = ctk.CTkLabel(email_frame, text="bayhoca77@gmail.com", 
                              font=("Arial", 14, "bold"),
                              text_color="#d32f2f")
    email_adres.pack(pady=5)
    
    def email_gonder():
        """E-mail gönderme fonksiyonu"""
        try:
            email_komutu = f"mailto:bayhoca77@gmail.com?subject=Nesne Tespit Sistemi Hakkında"
            webbrowser.open(email_komutu)
        except Exception as e:
            messagebox.showinfo("Bilgi", "E-mail adresi panoya kopyalandı: bayhoca77@gmail.com")
    
    email_buton = ctk.CTkButton(email_frame, 
                               text="📧 E-mail Gönder",
                               command=email_gonder,
                               font=("Arial", 12, "bold"),
                               fg_color="#d32f2f",
                               hover_color="#b71c1c",
                               width=200)
    email_buton.pack(pady=10)
    
    # GitHub Bilgisi
    github_frame = ctk.CTkFrame(gelistirici_frame)
    github_frame.pack(fill=tk.X, padx=20, pady=10)
    
    github_baslik = ctk.CTkLabel(github_frame, text="🔗 GitHub", 
                                font=("Arial", 16, "bold"))
    github_baslik.pack(pady=10)
    
    github_adres = ctk.CTkLabel(github_frame, text="github.com/adembayhoca", 
                               font=("Arial", 14, "bold"),
                               text_color="#24292e")
    github_adres.pack(pady=5)
    
    def github_ac():
        """GitHub profilini açma fonksiyonu"""
        webbrowser.open("https://github.com/adembayhoca?tab=repositories")
    
    github_buton = ctk.CTkButton(github_frame, 
                                text="🔗 GitHub Profili",
                                command=github_ac,
                                font=("Arial", 12, "bold"),
                                fg_color="#24292e",
                                hover_color="#0366d6",
                                width=200)
    github_buton.pack(pady=10)
    
    # Proje Bilgileri
    proje_frame = ctk.CTkFrame(container)
    proje_frame.pack(fill=tk.X, padx=20, pady=15)
    
    proje_baslik = ctk.CTkLabel(proje_frame, text="💼 Proje Hakkında", 
                               font=("Arial", 16, "bold"))
    proje_baslik.pack(pady=15)
    
    proje_aciklama = """
    Bu nesne tespit sistemi, modern yapay zeka teknolojileri kullanılarak 
    geliştirilmiş açık kaynak kodlu bir projedir. YOLO algoritması ile 
    desteklenen sistem, gerçek zamanlı tespit yetenekleri sunar.
    
    Proje hakkında sorularınız, önerileriniz veya işbirliği teklifleriniz 
    için lütfen iletişime geçiniz.
    """
    
    proje_label = ctk.CTkLabel(proje_frame, text=proje_aciklama, 
                              wraplength=700, justify=tk.LEFT,
                              font=("Arial", 12))
    proje_label.pack(padx=20, pady=10)
    
    # Sosyal Medya ve Bağlantılar
    sosyal_frame = ctk.CTkFrame(container)
    sosyal_frame.pack(fill=tk.X, padx=20, pady=15)
    
    sosyal_baslik = ctk.CTkLabel(sosyal_frame, text="🌐 Bağlantılar", 
                                font=("Arial", 16, "bold"))
    sosyal_baslik.pack(pady=15)
    
    # Butonlar frame'i
    butonlar_frame = ctk.CTkFrame(sosyal_frame)
    butonlar_frame.pack(pady=10)
    
    # LinkedIn butonu (varsayılan)
    def linkedin_ac():
        messagebox.showinfo("Bilgi", "LinkedIn profili henüz mevcut değil.")
    
    linkedin_buton = ctk.CTkButton(butonlar_frame, 
                                  text="💼 LinkedIn",
                                  command=linkedin_ac,
                                  font=("Arial", 12, "bold"),
                                  fg_color="#0077b5",
                                  hover_color="#005885",
                                  width=150)
    linkedin_buton.pack(side=tk.LEFT, padx=10)
    
    # Twitter butonu (varsayılan)
    def twitter_ac():
        messagebox.showinfo("Bilgi", "Twitter profili henüz mevcut değil.")
    
    twitter_buton = ctk.CTkButton(butonlar_frame, 
                                 text="🐦 Twitter",
                                 command=twitter_ac,
                                 font=("Arial", 12, "bold"),
                                 fg_color="#1da1f2",
                                 hover_color="#0d8bd9",
                                 width=150)
    twitter_buton.pack(side=tk.LEFT, padx=10)
    
    # İletişim Formu
    form_frame = ctk.CTkFrame(container)
    form_frame.pack(fill=tk.X, padx=20, pady=15)
    
    form_baslik = ctk.CTkLabel(form_frame, text="📝 Hızlı İletişim", 
                              font=("Arial", 16, "bold"))
    form_baslik.pack(pady=15)
    
    # Konu girişi
    konu_label = ctk.CTkLabel(form_frame, text="Konu:", font=("Arial", 12, "bold"))
    konu_label.pack(anchor=tk.W, padx=20)
    
    konu_entry = ctk.CTkEntry(form_frame, width=400, placeholder_text="Mesajınızın konusu...")
    konu_entry.pack(padx=20, pady=(5, 10))
    
    # Mesaj girişi
    mesaj_label = ctk.CTkLabel(form_frame, text="Mesaj:", font=("Arial", 12, "bold"))
    mesaj_label.pack(anchor=tk.W, padx=20)
    
    mesaj_text = ctk.CTkTextbox(form_frame, width=400, height=100)
    mesaj_text.pack(padx=20, pady=(5, 15))
    
    def mesaj_gonder():
        """Mesaj gönderme fonksiyonu (e-mail yönlendirme)"""
        konu = konu_entry.get()
        mesaj = mesaj_text.get("1.0", tk.END)
        
        if not konu.strip() or not mesaj.strip():
            messagebox.showwarning("Uyarı", "Lütfen konu ve mesaj alanlarını doldurunuz.")
            return
        
        try:
            email_komutu = f"mailto:bayhoca77@gmail.com?subject={konu}&body={mesaj}"
            webbrowser.open(email_komutu)
            messagebox.showinfo("Başarılı", "E-mail programınız açıldı. Mesajınızı gönderebilirsiniz.")
            konu_entry.delete(0, tk.END)
            mesaj_text.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("Hata", f"E-mail programı açılırken hata oluştu: {e}")
    
    gonder_buton = ctk.CTkButton(form_frame, 
                                text="📧 Mesaj Gönder",
                                command=mesaj_gonder,
                                font=("Arial", 12, "bold"),
                                fg_color="#4caf50",
                                hover_color="#388e3c",
                                width=200)
    gonder_buton.pack(pady=10)
    
    # Alt bilgi
    alt_frame = ctk.CTkFrame(container)
    alt_frame.pack(fill=tk.X, padx=20, pady=15)
    
    tesekkur_text = "İletişim için teşekkür ederiz! En kısa sürede dönüş yapılacaktır. 🇹🇷"
    tesekkur_label = ctk.CTkLabel(alt_frame, text=tesekkur_text, 
                                 font=("Arial", 12, "bold"),
                                 text_color="#2e7d32")
    tesekkur_label.pack(pady=15) 