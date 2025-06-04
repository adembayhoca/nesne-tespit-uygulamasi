import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os
from datetime import datetime
from PIL import Image, ImageTk

# Kullanıcı bilgileri dosyası
KULLANICI_DOSYASI = "kullanici.json"
GIRIS_GECMISI_DOSYASI = "giris_gecmisi.json"

def kullanici_bilgilerini_yukle():
    """
    Kaydedilmiş kullanıcı bilgilerini yükler.
    """
    if os.path.exists(KULLANICI_DOSYASI):
        with open(KULLANICI_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "kullanici_adi": "admin",
        "sifre": "1234",
        "profil_resmi": "",
        "son_giris": "",
        "giris_gecmisi": []
    }

def kullanici_bilgilerini_kaydet(bilgiler):
    """
    Kullanıcı bilgilerini kaydeder.
    """
    with open(KULLANICI_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(bilgiler, f, ensure_ascii=False, indent=4)

def giris_gecmisi_kaydet(kullanici_adi, basarili=True):
    """
    Giriş geçmişini kaydeder.
    """
    gecmis = []
    if os.path.exists(GIRIS_GECMISI_DOSYASI):
        with open(GIRIS_GECMISI_DOSYASI, "r", encoding="utf-8") as f:
            gecmis = json.load(f)
    
    gecmis.append({
        "kullanici_adi": kullanici_adi,
        "tarih": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "basarili": basarili
    })
    
    # Son 10 girişi tut
    gecmis = gecmis[-10:]
    
    with open(GIRIS_GECMISI_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(gecmis, f, ensure_ascii=False, indent=4)

class GirisEkrani(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Pencere ayarları
        self.title("Nesne Tespit - Giriş")
        self.geometry("500x700")
        self.resizable(False, False)
        
        # Tema ayarları
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Ana container
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Logo
        self.logo = ctk.CTkLabel(self.container, text="Nesne Tespit", 
                                font=("Arial", 28, "bold"))
        self.logo.pack(pady=20)
        
        # Giriş formu
        self.form_frame = ctk.CTkFrame(self.container)
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Profil resmi
        self.profil_frame = ctk.CTkFrame(self.form_frame)
        self.profil_frame.pack(pady=20)
        
        self.profil_resmi = ctk.CTkLabel(self.profil_frame, text="", 
                                       font=("Arial", 64))
        self.profil_resmi.pack()
        
        self.profil_buton = ctk.CTkButton(self.profil_frame, text="Profil Resmi Ekle", 
                                        command=self.profil_resmi_sec,
                                        fg_color="#34A853", hover_color="#2E7D32",
                                        height=35, font=("Arial", 12))
        self.profil_buton.pack(pady=5)
        
        # Kullanıcı adı
        self.kullanici_label = ctk.CTkLabel(self.form_frame, text="Kullanıcı Adı:",
                                          font=("Arial", 14))
        self.kullanici_label.pack(anchor=tk.W, padx=10, pady=5)
        
        self.kullanici_entry = ctk.CTkEntry(self.form_frame, width=400, height=35,
                                          font=("Arial", 14))
        self.kullanici_entry.pack(padx=10, pady=5)
        
        # Şifre
        self.sifre_label = ctk.CTkLabel(self.form_frame, text="Şifre:",
                                      font=("Arial", 14))
        self.sifre_label.pack(anchor=tk.W, padx=10, pady=5)
        
        self.sifre_entry = ctk.CTkEntry(self.form_frame, show="•", width=400, height=35,
                                      font=("Arial", 14))
        self.sifre_entry.pack(padx=10, pady=5)
        
        # Giriş butonu
        self.giris_buton = ctk.CTkButton(self.form_frame, text="Giriş Yap", 
                                        command=self.giris_yap,
                                        fg_color="#1E88E5", hover_color="#1565C0",
                                        height=40, font=("Arial", 14, "bold"))
        self.giris_buton.pack(pady=15)
        
        # Şifremi unuttum butonu
        self.sifremi_unuttum_buton = ctk.CTkButton(self.form_frame, text="Şifremi Unuttum", 
                                                  command=self.sifremi_unuttum,
                                                  fg_color="#FBBC05", hover_color="#F9A825",
                                                  height=35, font=("Arial", 12))
        self.sifremi_unuttum_buton.pack(pady=5)
        
        # Bilgi etiketi
        self.bilgi_label = ctk.CTkLabel(self.form_frame, 
                                      text="Varsayılan kullanıcı adı: admin\nVarsayılan şifre: 1234",
                                      justify=tk.CENTER, font=("Arial", 12))
        self.bilgi_label.pack(pady=10)
        
        # Enter tuşu ile giriş
        self.bind('<Return>', lambda event: self.giris_yap())
        
        # Profil resmini yükle
        self.profil_resmi_yukle()
    
    def profil_resmi_yukle(self):
        """Kaydedilmiş profil resmini yükler"""
        kullanici_bilgileri = kullanici_bilgilerini_yukle()
        if kullanici_bilgileri.get("profil_resmi"):
            try:
                image = Image.open(kullanici_bilgileri["profil_resmi"])
                image = image.resize((150, 150))  # Profil resmi boyutu büyütüldü
                photo = ImageTk.PhotoImage(image)
                self.profil_resmi.configure(image=photo)
                self.profil_resmi.image = photo
            except:
                pass
    
    def profil_resmi_sec(self):
        """Profil resmi seçme işlemini gerçekleştirir"""
        dosya_yolu = filedialog.askopenfilename(
            title="Profil Resmi Seç",
            filetypes=[("Resim Dosyaları", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        
        if dosya_yolu:
            try:
                # Resmi yükle ve göster
                image = Image.open(dosya_yolu)
                image = image.resize((150, 150))  # Profil resmi boyutu büyütüldü
                photo = ImageTk.PhotoImage(image)
                self.profil_resmi.configure(image=photo)
                self.profil_resmi.image = photo
                
                # Resmi kaydet
                kullanici_bilgileri = kullanici_bilgilerini_yukle()
                kullanici_bilgileri["profil_resmi"] = dosya_yolu
                kullanici_bilgilerini_kaydet(kullanici_bilgileri)
                
            except Exception as e:
                messagebox.showerror("Hata", f"Resim yüklenirken hata oluştu: {str(e)}")
    
    def sifremi_unuttum(self):
        """Şifremi unuttum işlemini gerçekleştirir"""
        kullanici_adi = self.kullanici_entry.get()
        
        if not kullanici_adi:
            messagebox.showwarning("Uyarı", "Lütfen kullanıcı adınızı girin!")
            return
        
        kullanici_bilgileri = kullanici_bilgilerini_yukle()
        
        if kullanici_adi == kullanici_bilgileri["kullanici_adi"]:
            # Varsayılan şifreye sıfırla
            kullanici_bilgileri["sifre"] = "1234"
            kullanici_bilgilerini_kaydet(kullanici_bilgileri)
            messagebox.showinfo("Bilgi", "Şifreniz varsayılan şifreye (1234) sıfırlandı!")
        else:
            messagebox.showerror("Hata", "Kullanıcı adı bulunamadı!")
    
    def giris_yap(self):
        """
        Giriş işlemini gerçekleştirir.
        """
        kullanici_adi = self.kullanici_entry.get()
        sifre = self.sifre_entry.get()
        
        if not kullanici_adi or not sifre:
            messagebox.showwarning("Uyarı", "Lütfen kullanıcı adı ve şifre girin!")
            return
        
        kullanici_bilgileri = kullanici_bilgilerini_yukle()
        
        if kullanici_adi == kullanici_bilgileri["kullanici_adi"] and \
           sifre == kullanici_bilgileri["sifre"]:
            # Giriş başarılı
            giris_gecmisi_kaydet(kullanici_adi, True)
            
            # Son giriş tarihini güncelle
            kullanici_bilgileri["son_giris"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            kullanici_bilgilerini_kaydet(kullanici_bilgileri)
            
            self.destroy()  # Giriş ekranını kapat
            from ana_uygulama import AnaUygulama
            app = AnaUygulama()
            app.mainloop()
        else:
            # Giriş başarısız
            giris_gecmisi_kaydet(kullanici_adi, False)
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")
            self.sifre_entry.delete(0, tk.END)  # Şifre alanını temizle

if __name__ == "__main__":
    app = GirisEkrani()
    app.mainloop() 