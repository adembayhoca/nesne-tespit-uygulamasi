# Python 3.11 base image kullan
FROM python:3.11-slim

# Metadata
LABEL maintainer="Adem Bayhoca <https://github.com/adembayhoca>"
LABEL description="Nesne Tespit Uygulaması - YOLOv8 ve DeepSORT ile"
LABEL version="1.0.0"

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgthread-2.0-0 \
    libgtk-3-0 \
    python3-tk \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Python bağımlılıklarını kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Gerekli dizinleri oluştur
RUN mkdir -p veritabani tespit_raporlari loglar

# Kullanıcı hesabı oluştur (güvenlik için)
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Port ayarları (gelecekte web interface için)
EXPOSE 8080

# Ortam değişkenleri
ENV PYTHONPATH=/app
ENV DISPLAY=:0

# Başlangıç komutu
CMD ["python", "ana_uygulama.py"]

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import ana_uygulama; print('OK')" || exit 1

# Volume tanımları
VOLUME ["/app/veritabani", "/app/tespit_raporlari", "/app/loglar"] 