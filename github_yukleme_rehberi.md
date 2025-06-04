# 🚀 GitHub'a Proje Yükleme Rehberi

## 📋 Gereksinimler

### 1. Git Kurulumu
1. **Git İndir**: https://git-scm.com/download/win adresinden Git'i indirin
2. **Kurulum**: İndirilen dosyayı çalıştırın ve varsayılan ayarlarla kurun
3. **Kontrol**: PowerShell'de `git --version` komutuyla kontrol edin

### 2. GitHub Hesabı
- GitHub.com'da hesabınız olmalı
- Hesabınızın kullanıcı adını ve şifresini bilin

## 🛠️ Adım Adım Yükleme

### Adım 1: Git Deposunu Başlatma
```bash
git init
```

### Adım 2: Uzak Depo Ekleme
GitHub'da yeni bir repository oluşturduktan sonra:
```bash
git remote add origin https://github.com/KULLANICI_ADINIZ/nesne-tespit-uygulamasi.git
```

### Adım 3: Dosyaları Hazırlama
```bash
# Tüm dosyaları staging area'ya ekle
git add .

# Commit mesajı ile kaydet
git commit -m "İlk commit: Nesne tespit uygulaması eklendi"
```

### Adım 4: GitHub'a Yükleme
```bash
# Ana branch'i main olarak ayarla
git branch -M main

# GitHub'a push et
git push -u origin main
```

## 🎯 Hızlı Komutlar

### Tek Komutta Tüm İşlem:
```bash
git init
git add .
git commit -m "İlk commit: Nesne tespit uygulaması"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/REPO_ADI.git
git push -u origin main
```

## 🔧 Sorun Giderme

### Git Yüklü Değil Hatası:
1. Git'i yukarıdaki linkten indirin
2. PowerShell'i yeniden başlatın
3. `git --version` ile kontrol edin

### Push Hatası:
```bash
# Uzak depodan önce pull yapın
git pull origin main --allow-unrelated-histories
git push origin main
```

### Kimlik Doğrulama:
```bash
git config --global user.name "Adınız Soyadınız"
git config --global user.email "email@adresiniz.com"
```

## 📱 GitHub Desktop ile Alternatif

1. **GitHub Desktop İndir**: https://desktop.github.com/
2. **Kurulum**: Programa giriş yapın
3. **Add Existing Repository**: Proje klasörünüzü seçin
4. **Publish**: Repository'yi GitHub'a yükleyin

## ✅ Son Kontroller

- [ ] README.md dosyası mevcut
- [ ] .gitignore dosyası mevcut
- [ ] LICENSE dosyası mevcut
- [ ] requirements.txt dosyası mevcut
- [ ] Docker dosyaları mevcut
- [ ] GitHub workflows mevcut
- [ ] Proje çalışır durumda

## 🎉 Başarı!

Projeniz GitHub'da yayında! Artık:
- ⭐ Star alabilir
- 🍴 Fork edilebilir
- 🐛 Issue açılabilir
- 🔀 Pull request alabilir
- 📊 Analytics görüntüleyebilir

### Kullanışlı GitHub Komutları:
```bash
# Güncellemeleri çekme
git pull origin main

# Yeni değişiklikleri gönderme
git add .
git commit -m "Güncelleme: açıklama"
git push origin main

# Branch oluşturma
git checkout -b yeni-ozellik
git push -u origin yeni-ozellik
``` 