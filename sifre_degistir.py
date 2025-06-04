import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def icerik_goster(parent_frame):
    """
    Şifre değiştirme modülünün içeriğini gösterir.
    
    Args:
        parent_frame: İçeriğin gösterileceği frame
    """
    # Ana container
    container = ctk.CTkFrame(parent_frame)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Başlık
    baslik = ctk.CTkLabel(container, text="Şifre Değiştir", font=("Arial", 24, "bold"))
    baslik.pack(pady=20)
    
    # Form için frame
    form_frame = ctk.CTkFrame(container)
    form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Mevcut şifre
    mevcut_frame = ctk.CTkFrame(form_frame)
    mevcut_frame.pack(fill=tk.X, padx=20, pady=10)
    
    mevcut_label = ctk.CTkLabel(mevcut_frame, text="Mevcut Şifre:")
    mevcut_label.pack(side=tk.LEFT, padx=10)
    
    mevcut_sifre = ctk.CTkEntry(mevcut_frame, show="•", width=300)
    mevcut_sifre.pack(side=tk.LEFT, padx=10)
    
    # Yeni şifre
    yeni_frame = ctk.CTkFrame(form_frame)
    yeni_frame.pack(fill=tk.X, padx=20, pady=10)
    
    yeni_label = ctk.CTkLabel(yeni_frame, text="Yeni Şifre:")
    yeni_label.pack(side=tk.LEFT, padx=10)
    
    yeni_sifre = ctk.CTkEntry(yeni_frame, show="•", width=300)
    yeni_sifre.pack(side=tk.LEFT, padx=10)
    
    # Yeni şifre tekrar
    tekrar_frame = ctk.CTkFrame(form_frame)
    tekrar_frame.pack(fill=tk.X, padx=20, pady=10)
    
    tekrar_label = ctk.CTkLabel(tekrar_frame, text="Yeni Şifre (Tekrar):")
    tekrar_label.pack(side=tk.LEFT, padx=10)
    
    tekrar_sifre = ctk.CTkEntry(tekrar_frame, show="•", width=300)
    tekrar_sifre.pack(side=tk.LEFT, padx=10)
    
    # Şifre gereksinimleri
    gereksinimler_frame = ctk.CTkFrame(form_frame)
    gereksinimler_frame.pack(fill=tk.X, padx=20, pady=10)
    
    gereksinimler_label = ctk.CTkLabel(gereksinimler_frame, 
                                     text="Şifre Gereksinimleri:",
                                     font=("Arial", 12, "bold"))
    gereksinimler_label.pack(anchor=tk.W, padx=10, pady=5)
    
    gereksinimler = [
        "• En az 8 karakter uzunluğunda olmalı",
        "• En az bir büyük harf içermeli",
        "• En az bir küçük harf içermeli",
        "• En az bir rakam içermeli",
        "• En az bir özel karakter içermeli (!@#$%^&*)"
    ]
    
    for gereksinim in gereksinimler:
        label = ctk.CTkLabel(gereksinimler_frame, text=gereksinim)
        label.pack(anchor=tk.W, padx=20, pady=2)
    
    # Butonlar için frame
    buton_frame = ctk.CTkFrame(form_frame)
    buton_frame.pack(fill=tk.X, padx=20, pady=20)
    
    kaydet_buton = ctk.CTkButton(buton_frame, text="Şifreyi Değiştir", 
                                command=lambda: sifre_degistir(),
                                fg_color="#34A853", hover_color="#2E7D32")
    kaydet_buton.pack(side=tk.LEFT, padx=10)
    
    iptal_buton = ctk.CTkButton(buton_frame, text="İptal", 
                               command=lambda: iptal(),
                               fg_color="#EA4335", hover_color="#C62828")
    iptal_buton.pack(side=tk.LEFT, padx=10)
    
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
        
        messagebox.showinfo("Bilgi", "Şifreniz başarıyla değiştirildi!")
        mevcut_sifre.delete(0, tk.END)
        yeni_sifre.delete(0, tk.END)
        tekrar_sifre.delete(0, tk.END)
    
    def iptal():
        """İşlemi iptal eder"""
        mevcut_sifre.delete(0, tk.END)
        yeni_sifre.delete(0, tk.END)
        tekrar_sifre.delete(0, tk.END) 