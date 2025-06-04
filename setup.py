from setuptools import setup, find_packages
import os

# README dosyasını oku
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Requirements dosyasını oku
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="nesne-tespit-uygulamasi",
    version="1.0.0",
    author="Adem Bayhoca",
    author_email="",
    description="Modern ve kapsamlı nesne tespit uygulaması - YOLOv8 ve DeepSORT ile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adembayhoca/nesne-tespit-uygulamasi",
    project_urls={
        "Bug Reports": "https://github.com/adembayhoca/nesne-tespit-uygulamasi/issues",
        "Source": "https://github.com/adembayhoca/nesne-tespit-uygulamasi",
        "Documentation": "https://github.com/adembayhoca/nesne-tespit-uygulamasi#readme",
    },
    packages=find_packages(exclude=["tests*", "docs*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        "Topic :: Multimedia :: Video :: Capture",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Turkish",
        "Natural Language :: English",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "bandit>=1.7",
            "safety>=2.0",
        ],
        "gpu": [
            "torch>=2.0.0",
            "torchvision>=0.15.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nesne-tespit=ana_uygulama:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "*.yml", "*.yaml"],
    },
    keywords=[
        "object detection",
        "yolo",
        "yolov8",
        "computer vision",
        "ai",
        "machine learning",
        "opencv",
        "tkinter",
        "customtkinter",
        "nesne tespit",
        "görüntü işleme",
        "yapay zeka",
        "makine öğrenmesi",
    ],
    platforms=["Windows", "macOS", "Linux"],
    zip_safe=False,
) 