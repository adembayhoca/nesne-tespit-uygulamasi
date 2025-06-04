# 🔍 Object Detection Application (Nesne Tespit Uygulaması)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green.svg)](https://opencv.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-8.3.145-orange.svg)](https://ultralytics.com)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

## 📋 Overview

This is a comprehensive **Object Detection Application** built with Python, featuring real-time camera detection, video analysis, and image processing capabilities. The application uses YOLOv8 for object detection and DeepSORT for object tracking, providing accurate and efficient detection results.

### 🎯 Key Features

- **🎥 Real-time Camera Detection**: Live object detection from camera feed
- **📹 Video Analysis**: Upload and analyze video files for object detection
- **🖼️ Image Processing**: Batch processing of images for object detection
- **📊 Detection Reports**: Comprehensive reports with statistics and visualizations
- **🗄️ Database Storage**: SQLite database for storing detection results
- **🌍 Bilingual Interface**: Turkish and English language support
- **🎨 Modern UI**: Built with CustomTkinter for a modern, responsive interface
- **👤 User Authentication**: Secure login system with user management
- **⚙️ Customizable Settings**: Adjustable confidence thresholds and detection parameters

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- Webcam (for real-time detection)
- GPU support (optional, for better performance)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/adembayhoca/nesne-tespit-uygulamasi.git
cd nesne-tespit-uygulamasi
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download YOLO models** (optional - models will be downloaded automatically on first run)
```bash
# YOLOv8 models will be downloaded automatically
# Or manually download from: https://github.com/ultralytics/ultralytics
```

5. **Run the application**
```bash
python ana_uygulama.py
```

## 📖 Usage

### 🔐 Login
- Default username: `admin`
- Default password: `1234`
- You can change credentials from the settings menu

### 🎥 Real-time Detection
1. Click "Canlı Tespit" (Live Detection) from the menu
2. Adjust confidence threshold using the slider
3. Click "Kamerayı Başlat" (Start Camera) to begin detection
4. View real-time object detection with bounding boxes and labels
5. Save detection results using "Tespitleri Kaydet" (Save Detections)

### 📹 Video Analysis
1. Select "Video Tespit" (Video Detection)
2. Upload a video file using "Video Seç" (Select Video)
3. Choose output directory for processed video
4. Start processing and view results with annotations

### 🖼️ Image Processing
1. Go to "Resim Tespit" (Image Detection)
2. Select single image or batch process multiple images
3. View detection results with confidence scores
4. Export results in various formats

### 📊 Reports and Analytics
- View detailed detection statistics
- Export reports as PDF or JSON
- Analyze detection trends over time
- Filter results by object type and date

## 🛠️ Technical Details

### 🧠 AI Models Used
- **YOLOv8**: Primary object detection model
- **DeepSORT**: Object tracking algorithm
- **OpenCV**: Computer vision operations

### 🗃️ Database Schema
The application uses SQLite databases to store:
- User authentication data
- Detection results and metadata
- Application settings and preferences
- Detection history and reports

### 📁 Project Structure
```
nesne-tespit-uygulamasi/
├── ana_uygulama.py         # Main application entry point
├── giris.py                # Login system
├── canli_tespit.py         # Real-time detection module
├── video_tespit.py         # Video analysis module
├── resim_tespit.py         # Image processing module
├── tespit_raporlari.py     # Reports and analytics
├── ayarlar.py              # Settings management
├── yardim.py               # Help documentation
├── hakkinda.py             # About page
├── iletisim.py             # Contact information
├── sifre_degistir.py       # Password management
├── requirements.txt        # Python dependencies
├── README.md               # English documentation
├── README_TR.md            # Turkish documentation
├── veritabani/             # Database files
├── tespit_raporlari/       # Detection reports
├── loglar/                 # Application logs
└── assets/                 # UI assets and images
```

## 🎯 Use Cases and Applications

### 🏢 Business Applications
- **Security Monitoring**: Real-time surveillance and threat detection
- **Retail Analytics**: Customer behavior analysis and inventory management
- **Quality Control**: Manufacturing defect detection
- **Traffic Management**: Vehicle and pedestrian counting

### 🎓 Educational and Research
- **Computer Vision Learning**: Hands-on experience with object detection
- **Data Collection**: Automated annotation and dataset creation
- **Algorithm Comparison**: Testing different detection models
- **Research Projects**: Custom object detection experiments

### 🏠 Personal Use
- **Home Security**: Monitor your property remotely
- **Pet Monitoring**: Track pet activities and behavior
- **Garden Management**: Plant and wildlife observation
- **Sports Analysis**: Performance tracking and technique analysis

## ⚙️ Configuration

### 🎛️ Settings Options
- **Language**: Turkish/English interface
- **Camera Selection**: Choose default camera device
- **Resolution Settings**: Adjust video quality
- **Detection Threshold**: Set confidence levels
- **Database Options**: Configure storage preferences

### 📊 Performance Optimization
- **GPU Acceleration**: Enable CUDA for faster processing
- **Batch Processing**: Optimize for multiple file processing
- **Memory Management**: Efficient resource utilization
- **Threading**: Parallel processing for better performance

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📋 Development Guidelines
- Follow PEP 8 coding standards
- Add comments in Turkish for consistency
- Include tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Adem Bayhoca**
- GitHub: [@adembayhoca](https://github.com/adembayhoca)
- Email: [Contact through GitHub](https://github.com/adembayhoca)

## 🙏 Acknowledgments

- [Ultralytics](https://ultralytics.com) for YOLOv8
- [OpenCV](https://opencv.org) for computer vision tools
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for modern UI components
- [DeepSORT](https://github.com/nwojke/deep_sort) for object tracking

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the [Help Documentation](yardim.py)
- Review the [FAQ section](README_TR.md#sss)

---

⭐ **Star this repository if you find it helpful!** 