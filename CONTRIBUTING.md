# Contributing to Nesne Tespit Uygulaması

First off, thank you for considering contributing to this Object Detection Application! It's people like you that make this project better.

## 🤝 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues to see if the problem has already been reported. When creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what behavior you expected**
- **Include screenshots if possible**
- **Specify your OS, Python version, and dependency versions**

### 💡 Suggesting Enhancements

Enhancement suggestions are welcome! When suggesting an enhancement:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the enhancement**
- **Explain why this enhancement would be useful**

### 🔧 Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Create a pull request** with a clear title and description

## 📋 Development Setup

1. **Clone your fork**
```bash
git clone https://github.com/your-username/nesne-tespit-uygulamasi.git
cd nesne-tespit-uygulamasi
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

## 📝 Coding Standards

### Python Code Style
- Follow **PEP 8** guidelines
- Use **Turkish** for variable names, function names, and comments (as per project convention)
- Avoid Turkish characters in code (use Turkish words without special characters)
- Maximum line length: 88 characters
- Use meaningful names for variables and functions

### Example:
```python
def nesne_tespit_et(goruntu_yolu, guven_esigi=0.5):
    """
    Verilen görüntüde nesne tespiti yapar.
    
    Args:
        goruntu_yolu (str): Tespit edilecek görüntünün dosya yolu
        guven_esigi (float): Tespit için güven eşiği
    
    Returns:
        list: Tespit edilen nesnelerin listesi
    """
    tespit_sonuclari = []
    # Implementation here...
    return tespit_sonuclari
```

### Documentation
- **Turkish comments** for implementation details
- **Turkish docstrings** for functions and classes
- Update README files when adding new features
- Include examples in documentation

### Testing
- Write tests for new functionality
- Ensure existing tests still pass
- Test on different Python versions if possible
- Test UI changes thoroughly

## 🗂️ Project Structure

```
nesne-tespit-uygulamasi/
├── ana_uygulama.py         # Ana uygulama dosyası
├── giris.py                # Giriş sistemi
├── canli_tespit.py         # Canlı tespit modülü
├── video_tespit.py         # Video tespit modülü
├── resim_tespit.py         # Resim tespit modülü
├── tespit_raporlari.py     # Raporlama modülü
├── ayarlar.py              # Ayarlar modülü
├── yardim.py               # Yardım modülü
├── hakkinda.py             # Hakkında modülü
├── iletisim.py             # İletişim modülü
├── sifre_degistir.py       # Şifre değiştirme modülü
└── requirements.txt        # Bağımlılıklar
```

## 🎯 What to Contribute

### 🔥 High Priority
- Performance optimizations
- Bug fixes
- UI/UX improvements
- Documentation improvements
- Test coverage

### 💡 Feature Ideas
- New object detection models integration
- Additional export formats
- Real-time performance monitoring
- Multi-language support expansion
- Cloud storage integration
- Mobile app companion
- Web interface
- API development

### 🎨 UI/UX Improvements
- Better responsive design
- Accessibility features
- Dark/light theme enhancements
- Keyboard shortcuts
- Drag and drop functionality

## 🧪 Testing Guidelines

### Manual Testing
- Test all major features after changes
- Verify UI responsiveness
- Test with different image/video formats
- Verify database operations
- Check error handling

### Automated Testing (Future)
- Unit tests for core functions
- Integration tests for modules
- UI automation tests
- Performance benchmarks

## 📚 Documentation

### Code Documentation
- Add Turkish comments for complex logic
- Document function parameters and return values
- Include usage examples
- Explain algorithm choices

### User Documentation
- Update README files for new features
- Add screenshots for UI changes
- Create video tutorials if applicable
- Update help documentation

## 🌍 Internationalization

- Keep Turkish as the primary language for development
- Use consistent terminology
- Avoid hardcoded strings in UI
- Consider future English localization

## 📋 Code Review Process

1. **Self Review**: Review your own code before submitting
2. **Automated Checks**: Ensure code passes any automated checks
3. **Peer Review**: At least one maintainer will review your PR
4. **Testing**: Verify that tests pass and functionality works
5. **Documentation**: Check that documentation is updated

## 🏷️ Commit Message Guidelines

Use clear and meaningful commit messages:

```
feat: yeni video format desteği eklendi
fix: kamera başlatma hatası düzeltildi
docs: README dosyası güncellendi
style: kod formatlaması düzeltildi
refactor: tespit algoritması yeniden düzenlendi
test: yeni test senaryoları eklendi
```

## 🚀 Release Process

1. Version bump in relevant files
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Update documentation

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: Contact maintainers directly for sensitive issues

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

## 🙏 Thank You

Thank you for your interest in contributing! Every contribution, no matter how small, is valuable and appreciated.

---

**Happy Coding! 🚀** 