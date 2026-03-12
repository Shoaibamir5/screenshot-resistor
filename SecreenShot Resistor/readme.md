# 🛡️ Screenshot Resistor

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A lightweight Windows application that detects screenshot attempts and provides instant visual feedback and notifications.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Screenshot Detection** | Detects PrintScreen, Win+Shift+S, Alt+PrintScreen, and Snipping Tool |
| ⚡ **Real-time Monitoring** | Continuous keyboard and process monitoring |
| 🔔 **Instant Alerts** | Desktop notifications and persistent visual warnings |
| 🛡️ **Visual Protection** | Black overlay flashes when screenshot detected |
| 🎨 **Modern UI** | Clean, light-themed interface with status indicators |
| 🖥️ **Windows Native** | Built for Windows 10/11 |

---

## 🚀 Quick Start

### Prerequisites
- Windows 10 or Windows 11
- Python 3.8+ (for source installation)

### Installation

```bash
# Clone repository
git clone https://github.com/Shoaibamir5/screenshot-resistor.git
cd screenshot-resistor

# Install dependencies
pip install -r requirements.txt

# Run application
python gui.py
```

---

## 📋 Requirements

```
tkinter
pynput
psutil
plyer
```

---

## 🎮 Usage

1. **Launch** the application
2. **Enable Protection** - Check the "Enable Protection" checkbox  
3. **Test** - Take a screenshot. You'll see:
   - Black overlay flash
   - Status change to "⚠ Screenshot Captured!"
   - Yellow persistent warning message
   - Desktop notification

### Detection Methods

- ✅ **PrintScreen** key
- ✅ **Win+Shift+S** (Snipping Tool shortcut)
- ✅ **Alt+PrintScreen** (Active window capture)
- ✅ **Snipping Tool** process detection

---

## 🔧 Technical Details

### How It Works

1. **Keyboard Monitoring** - Global hotkey detection via `pynput`
2. **Process Monitoring** - Detects Snipping Tool via `psutil`
3. **Visual Feedback** - Black overlay appears for 1 second when detected
4. **Persistent Warning** - Yellow warning message stays visible

### Architecture

| Component | Technology |
|-----------|------------|
| GUI | Tkinter |
| Keyboard Monitor | pynput |
| Process Monitor | psutil |
| Notifications | plyer |

---

## 📁 Project Structure

```
Screenshot-Resistor/
│
├── gui.py              # Main application & GUI
├── keymonitor.py       # Keyboard monitoring
├── requirements.txt    # Dependencies
├── README.md          # Documentation
└── LICENSE            # MIT License
```

---

## ⚠️ Note

This application **detects** screenshot attempts and provides **visual alerts**, but cannot truly prevent OS-level screenshots from being captured. It serves as a:
- Privacy awareness tool
- Deterrent against unauthorized screenshots
- Alert system for sensitive content protection

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Shoaib Amir**

---

<p align="center">
  Made with ❤️ for privacy-conscious users
</p>


## Demo

### Application Interface
![Interface](screenshots/Interface.png)


### Detection/Protection
![Protection](screenshots/Protection.png)





