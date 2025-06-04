@echo off
chcp 65001 >nul
echo ============================================
echo 🚀 Nesne Tespit Uygulaması - GitHub Yükleme
echo ============================================
echo.

echo 📋 Git kurulumu kontrol ediliyor...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git yüklü değil!
    echo 📥 Git'i indirmek için browser açılıyor...
    start https://git-scm.com/download/win
    echo.
    echo ⏰ Git'i kurun ve bu scripti tekrar çalıştırın.
    pause
    exit /b 1
) else (
    echo ✅ Git zaten yüklü!
)

echo.
echo 📁 Proje klasörü kontrol ediliyor...
if not exist "ana_uygulama.py" (
    echo ❌ Ana uygulama dosyası bulunamadı!
    echo 📍 Bu scripti proje klasörünün içinde çalıştırın.
    pause
    exit /b 1
)

echo ✅ Proje dosyaları mevcut!
echo.

echo 🔧 Git yapılandırması...
set /p kullanici_adi="👤 GitHub kullanıcı adınızı girin: "
set /p email="📧 Email adresinizi girin: "

git config --global user.name "%kullanici_adi%"
git config --global user.email "%email%"

echo.
echo 🏗️ Git deposu başlatılıyor...
git init

echo.
echo 📦 Dosyalar hazırlanıyor...
git add .

echo.
echo 💾 İlk commit yapılıyor...
git commit -m "İlk commit: Nesne tespit uygulaması eklendi"

echo.
echo 🌐 GitHub repository URL'i girin:
echo Örnek: https://github.com/kullaniciadi/proje-adi.git
set /p repo_url="🔗 Repository URL: "

echo.
echo 🔗 Uzak depo ekleniyor...
git remote add origin %repo_url%

echo.
echo 📤 GitHub'a yükleniyor...
git branch -M main
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Başarılı! Projeniz GitHub'a yüklendi!
    echo 🎉 Repository: %repo_url%
    echo.
    echo 📊 Sonraki adımlar:
    echo - Repository'nizi GitHub'da kontrol edin
    echo - README.md dosyasını güncelleyin
    echo - Issues ve pull request'leri izleyin
) else (
    echo.
    echo ❌ Yükleme sırasında hata oluştu!
    echo 🔧 Muhtemel çözümler:
    echo - GitHub hesabınızı kontrol edin
    echo - Repository URL'ini doğrulayın
    echo - Authentication token gerekebilir
)

echo.
echo 📱 GitHub Desktop'ı tercih ederseniz:
echo https://desktop.github.com adresinden indirebilirsiniz.

echo.
pause 