# 🔍 Nesne Tespit Uygulaması (Object Detection Application)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green.svg)](https://opencv.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-8.3.145-orange.svg)](https://ultralytics.com)
[![Lisans](https://img.shields.io/badge/Lisans-MIT-red.svg)](LICENSE)

## 📋 Genel Bakış

Bu, Python ile geliştirilmiş kapsamlı bir **Nesne Tespit Uygulaması**dır. Gerçek zamanlı kamera tespiti, video analizi ve görüntü işleme yetenekleri içerir. Uygulama, nesne tespiti için YOLOv8 ve nesne takibi için DeepSORT kullanarak doğru ve verimli tespit sonuçları sağlar.

### 🎯 Ana Özellikler

- **🎥 Gerçek Zamanlı Kamera Tespiti**: Kamera akışından canlı nesne tespiti
- **📹 Video Analizi**: Video dosyalarını yükleyip nesne tespiti analizi
- **🖼️ Görüntü İşleme**: Toplu görüntü işleme ile nesne tespiti
- **📊 Tespit Raporları**: İstatistikler ve görselleştirmeler içeren kapsamlı raporlar
- **🗄️ Veritabanı Depolama**: Tespit sonuçlarını saklamak için SQLite veritabanı
- **🌍 İki Dilli Arayüz**: Türkçe ve İngilizce dil desteği
- **🎨 Modern Arayüz**: CustomTkinter ile modern, duyarlı arayüz
- **👤 Kullanıcı Kimlik Doğrulaması**: Kullanıcı yönetimi ile güvenli giriş sistemi
- **⚙️ Özelleştirilebilir Ayarlar**: Ayarlanabilir güven eşikleri ve tespit parametreleri

## 🚀 Kurulum

### Ön Gereksinimler

- Python 3.11 veya üzeri
- Web kamerası (gerçek zamanlı tespit için)
- GPU desteği (isteğe bağlı, daha iyi performans için)

### Kurulum Adımları

1. **Repoyu klonlayın**
```bash
git clone https://github.com/adembayhoca/nesne-tespit-uygulamasi.git
cd nesne-tespit-uygulamasi
```

2. **Sanal ortam oluşturun**
```bash
python -m venv venv
source venv/bin/activate  # Windows'ta: venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **YOLO modellerini indirin** (isteğe bağlı - ilk çalıştırmada otomatik indirilir)
```bash
# YOLOv8 modelleri otomatik olarak indirilecek
# Veya manuel olarak şuradan indirin: https://github.com/ultralytics/ultralytics
```

5. **Uygulamayı çalıştırın**
```bash
python ana_uygulama.py
```

## 📖 Kullanım

### 🔐 Giriş
- Varsayılan kullanıcı adı: `admin`
- Varsayılan şifre: `1234`
- Ayarlar menüsünden kimlik bilgilerini değiştirebilirsiniz

### 🎥 Gerçek Zamanlı Tespit
1. Menüden "Canlı Tespit" seçeneğine tıklayın
2. Kaydırıcıyı kullanarak güven eşiğini ayarlayın
3. Tespiti başlatmak için "Kamerayı Başlat"a tıklayın
4. Sınırlayıcı kutular ve etiketlerle gerçek zamanlı nesne tespitini görüntüleyin
5. "Tespitleri Kaydet" kullanarak tespit sonuçlarını kaydedin

### 📹 Video Analizi
1. "Video Tespit" seçeneğini seçin
2. "Video Seç" kullanarak bir video dosyası yükleyin
3. İşlenmiş video için çıktı dizinini seçin
4. İşlemi başlatın ve sonuçları ek açıklamalarla görüntüleyin

### 🖼️ Görüntü İşleme
1. "Resim Tespit" bölümüne gidin
2. Tek görüntü seçin veya birden fazla görüntüyü toplu işleyin
3. Güven skorları ile tespit sonuçlarını görüntüleyin
4. Sonuçları çeşitli formatlarda dışa aktarın

### 📊 Raporlar ve Analitik
- Detaylı tespit istatistiklerini görüntüleyin
- Raporları PDF veya JSON olarak dışa aktarın
- Zaman içindeki tespit trendlerini analiz edin
- Sonuçları nesne türü ve tarihe göre filtreleyin

## 🛠️ Teknik Detaylar

### 🧠 Kullanılan AI Modelleri
- **YOLOv8**: Birincil nesne tespit modeli
- **DeepSORT**: Nesne takip algoritması
- **OpenCV**: Bilgisayarlı görü işlemleri

### 🗃️ Veritabanı Şeması
Uygulama aşağıdakileri saklamak için SQLite veritabanları kullanır:
- Kullanıcı kimlik doğrulama verileri
- Tespit sonuçları ve meta veriler
- Uygulama ayarları ve tercihleri
- Tespit geçmişi ve raporları

### 📁 Proje Yapısı
```
nesne-tespit-uygulamasi/
├── ana_uygulama.py         # Ana uygulama giriş noktası
├── giris.py                # Giriş sistemi
├── canli_tespit.py         # Gerçek zamanlı tespit modülü
├── video_tespit.py         # Video analizi modülü
├── resim_tespit.py         # Görüntü işleme modülü
├── tespit_raporlari.py     # Raporlar ve analitik
├── ayarlar.py              # Ayarlar yönetimi
├── yardim.py               # Yardım dokümantasyonu
├── hakkinda.py             # Hakkında sayfası
├── iletisim.py             # İletişim bilgileri
├── sifre_degistir.py       # Şifre yönetimi
├── requirements.txt        # Python bağımlılıkları
├── README.md               # İngilizce dokümantasyon
├── README_TR.md            # Türkçe dokümantasyon
├── veritabani/             # Veritabanı dosyaları
├── tespit_raporlari/       # Tespit raporları
├── loglar/                 # Uygulama günlükleri
└── assets/                 # UI varlıkları ve görseller
```

## 🎯 Kullanım Alanları ve Uygulamalar

### 🏢 İş Uygulamaları
- **Güvenlik İzleme**: Gerçek zamanlı gözetleme ve tehdit tespiti
- **Perakende Analizi**: Müşteri davranış analizi ve envanter yönetimi
- **Kalite Kontrolü**: Üretim hata tespiti
- **Trafik Yönetimi**: Araç ve yaya sayımı

### 🎓 Eğitim ve Araştırma
- **Bilgisayarlı Görü Öğrenimi**: Nesne tespiti ile uygulamalı deneyim
- **Veri Toplama**: Otomatik etiketleme ve veri seti oluşturma
- **Algoritma Karşılaştırması**: Farklı tespit modellerini test etme
- **Araştırma Projeleri**: Özel nesne tespit deneyleri

### 🏠 Kişisel Kullanım
- **Ev Güvenliği**: Mülkünüzü uzaktan izleme
- **Evcil Hayvan İzleme**: Evcil hayvan aktivitelerini ve davranışlarını takip etme
- **Bahçe Yönetimi**: Bitki ve vahşi yaşam gözlemi
- **Spor Analizi**: Performans takibi ve teknik analizi

## ⚙️ Yapılandırma

### 🎛️ Ayar Seçenekleri
- **Dil**: Türkçe/İngilizce arayüz
- **Kamera Seçimi**: Varsayılan kamera cihazını seçin
- **Çözünürlük Ayarları**: Video kalitesini ayarlayın
- **Tespit Eşiği**: Güven seviyelerini belirleyin
- **Veritabanı Seçenekleri**: Depolama tercihlerini yapılandırın

### 📊 Performans Optimizasyonu
- **GPU Hızlandırması**: Daha hızlı işleme için CUDA'yı etkinleştirin
- **Toplu İşleme**: Çoklu dosya işleme için optimize edin
- **Bellek Yönetimi**: Verimli kaynak kullanımı
- **Threading**: Daha iyi performans için paralel işleme

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları takip edin:

1. Repoyu fork edin
2. Özellik dalı oluşturun (`git checkout -b feature/harika-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika özellik ekle'`)
4. Dalı push edin (`git push origin feature/harika-ozellik`)
5. Pull Request açın

### 📋 Geliştirme Yönergeleri
- PEP 8 kodlama standartlarını takip edin
- Tutarlılık için Türkçe yorumlar ekleyin
- Yeni özellikler için testler dahil edin
- Gerektiğinde dokümantasyonu güncelleyin

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

**Adem Bayhoca**
- GitHub: [@adembayhoca](https://github.com/adembayhoca)
- Email: [GitHub üzerinden iletişim](https://github.com/adembayhoca)

## 🙏 Teşekkürler

- YOLOv8 için [Ultralytics](https://ultralytics.com)
- Bilgisayarlı görü araçları için [OpenCV](https://opencv.org)
- Modern UI bileşenleri için [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Nesne takibi için [DeepSORT](https://github.com/nwojke/deep_sort)

## 📞 Destek

Destek ve sorular için:
- GitHub'da issue oluşturun
- [Yardım Dokümantasyonu](yardim.py)nu inceleyin
- [SSS bölümü](#sss)nü gözden geçirin

## 🔧 SSS

**S: Uygulama başlamıyor, ne yapmalıyım?**
A: Önce tüm bağımlılıkların yüklendiğinden emin olun. `pip install -r requirements.txt` komutunu çalıştırın.

**S: Kamera açılmıyor?**
A: Kameranızın başka bir uygulama tarafından kullanılmadığından emin olun. Ayarlardan farklı bir kamera seçmeyi deneyin.

**S: Tespit doğruluğu düşük?**
A: Güven eşiğini ayarlayın ve daha iyi aydınlatma koşulları sağlayın. GPU kullanıyorsanız daha büyük YOLO modeli deneyebilirsiniz.

**S: Şifremi unuttum?**
A: Giriş ekranında kullanıcı adınızı girip "Şifremi Unuttum" butonuna tıklayın. Şifreniz varsayılan değere (1234) sıfırlanacak.

**S: Toplu resim işleme nasıl yapılır?**
A: Resim Tespit modülünde "Toplu İşleme" seçeneğini seçin ve işlemek istediğiniz klasörü belirleyin.

---

⭐ **Bu repoyu yararlı bulduysanız yıldızlamayı unutmayın!** 