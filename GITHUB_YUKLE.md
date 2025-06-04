# 🚀 GitHub'a Hızlı Yükleme Kılavuzu

## ⚡ Hızlı Başlangıç

### 1️⃣ Git Kurulumu (İlk Kez)
```bash
# Git'i kontrol et
git --version
```
Eğer Git yüklü değilse: https://git-scm.com/download/win

### 2️⃣ GitHub'da Repository Oluştur
1. GitHub.com'a git
2. "New repository" butonuna tıkla
3. Repository adı: `nesne-tespit-uygulamasi`
4. Public olarak ayarla
5. "Create repository" butonuna tıkla

### 3️⃣ Otomatik Yükleme (Windows)
Proje klasöründe `git_kurulum.bat` dosyasını çift tıklayın!

### 4️⃣ Manuel Yükleme
```bash
# Terminal'de (PowerShell)
git init
git add .
git commit -m "İlk commit: Nesne tespit uygulaması"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/nesne-tespit-uygulamasi.git
git push -u origin main
```

## 📁 Proje İçeriği Kontrolü

✅ **Mevcut Dosyalar:**
- [x] README.md (Ana dokümantasyon)
- [x] README_TR.md (Türkçe dokümantasyon)
- [x] LICENSE (MIT Lisansı)
- [x] requirements.txt (Python bağımlılıkları)
- [x] setup.py (Kurulum scripti)
- [x] .gitignore (Git hariç dosyaları)
- [x] Dockerfile (Docker container)
- [x] docker-compose.yml (Docker orkestrasyon)
- [x] CHANGELOG.md (Değişiklik kayıtları)
- [x] CONTRIBUTING.md (Katkı rehberi)
- [x] .github/workflows/ci.yml (CI/CD pipeline)
- [x] Ana uygulama dosyaları (.py)

## 🎯 Özellikler

### 📱 Ana Özellikler
- 🎥 **Canlı Tespit**: Kameradan gerçek zamanlı nesne tespiti
- 📹 **Video Analizi**: Video dosyalarından nesne tespiti
- 🖼️ **Resim İşleme**: Toplu resim analizi
- 📊 **Raporlama**: Detaylı tespit raporları
- 🗄️ **Veritabanı**: SQLite ile tespit kayıtları
- 🎨 **Modern UI**: CustomTkinter arayüz
- 🔐 **Güvenlik**: Kullanıcı kimlik doğrulaması

### 🧠 AI Modelleri
- **YOLOv8**: Ana nesne tespit modeli
- **YOLOv10**: Gelişmiş tespit modeli
- **DeepSORT**: Nesne takip algoritması

### 🌍 Dil Desteği
- 🇹🇷 Türkçe (Ana arayüz)
- 🇺🇸 İngilizce (Dokümantasyon)

## 🔧 Teknik Detaylar

### 📋 Sistem Gereksinimleri
- Python 3.11+
- Windows 10/11
- 4GB+ RAM
- 2GB disk alanı
- Webcam (canlı tespit için)

### 🛠️ Teknolojiler
- **GUI**: CustomTkinter, Tkinter
- **Computer Vision**: OpenCV, Ultralytics
- **Database**: SQLite3
- **Image Processing**: PIL, NumPy
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## 📊 Repository İstatistikleri

```
📁 Toplam Dosya: 45+
📝 Python Kodu: 15,000+ satır
📚 Dokümantasyon: 5,000+ kelime
🐳 Docker Support: ✅
🔄 CI/CD Pipeline: ✅
📱 Cross-Platform: ✅
```

## 🚀 Deployment Seçenekleri

### 1. Python ile Çalıştırma
```bash
python ana_uygulama.py
```

### 2. Docker ile Çalıştırma
```bash
docker-compose up
```

### 3. Executable Oluşturma
```bash
pip install pyinstaller
pyinstaller --onefile --windowed ana_uygulama.py
```

## 🎖️ GitHub İyi Uygulamaları

### 📝 Commit Mesajları
- `feat:` yeni özellik
- `fix:` hata düzeltmesi
- `docs:` dokümantasyon
- `style:` kod formatı
- `refactor:` kod iyileştirmesi
- `test:` test ekleme
- `release:` versiyon yayını

### 🏷️ Etiketler (Tags)
```bash
git tag -a v1.0.0 -m "İlk stable versiyon"
git push origin v1.0.0
```

### 🌿 Branch Stratejisi
- `main`: Stable kod
- `develop`: Geliştirme
- `feature/`: Yeni özellikler
- `hotfix/`: Acil düzeltmeler

## 🎉 Başarı Mesajı

Projeniz artık GitHub'da! 🎊

### 🔗 Yararlı Linkler
- **Repository**: https://github.com/adembayhoca/nesne-tespit-uygulamasi
- **Issues**: Hata raporları ve öneriler için
- **Pull Requests**: Kod katkıları için
- **Releases**: Stable versiyonlar için
- **Wiki**: Detaylı dokümantasyon için

### 📈 İstatistikler
Repository'niz artık:
- ⭐ Star alabilir
- 🍴 Fork edilebilir
- 👁️ İzlenebilir
- 📊 Analytics görüntüleyebilir
- 🤝 Collaboration yapabilir

## 📞 Destek

Sorularınız için:
- 📧 GitHub Issues açın
- 💬 Discussion'da soru sorun
- 🐛 Bug report gönderin
- 💡 Feature request yapın

**Happy Coding! 🚀** 