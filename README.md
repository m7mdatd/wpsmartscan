```
╔════════════════════════════════════════════════════════════╗
║                    🛡️  WPSmartScan v1.0                    ║
║        Smart WordPress Plugin Vulnerability Scanner        ║
║             Developed by X: @m7mdatd (2025)                ║
╚════════════════════════════════════════════════════════════╝
```

# WPScan - WordPress Plugin Vulnerability Scanner

**WPScan** is a smart and lightweight tool for detecting WordPress plugins and checking their known vulnerabilities via the [WPScan API](https://wpscan.com). It helps security researchers and developers quickly assess the exposure of WordPress-based websites.


## 🛠 Features
- 🔍 Automatically detects active WordPress plugins on any target site
- ☁️ Fetches real-time vulnerability data from WPScan API
- ✅ Indicates severity level (CVSS) and known CVEs (if available)
- 📄 Clean CLI interface with colorized output
- 💻 Lightweight and easy to install (works on Kali Linux and other Linux distros)

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/m7mdatd/wpsmartscan.git
cd wpsmartscan
```

### Install dependencies
```bash
pip install -r requirements.txt
```

If you're on **Kali Linux** or a fresh system, you can also run:

```bash
chmod +x install.sh
./install.sh
```

---

## 🧪 Usage
```bash
python3 main.py
```

You will be prompted to enter the URL of a WordPress-based website:

```
🌐 Enter your WordPress website link (example: https://example.com): https://example.org
```

The tool will:
1. Scan the site for active plugins  
2. Query WPScan API for known vulnerabilities  
3. Show results directly in your terminal

---

## 📦 Requirements
- Python 3.7+
- WPScan API token (free from [https://wpscan.com](https://wpscan.com))

### Save your API token in `config.py` like this:
```python
WPSCAN_API_TOKEN = "your-api-key-here"
```

---

## 📁 Project Structure
.
├── api/                   # WPScan API integration logic
├── core/                  # Main scanner logic
├── plugins/               # Plugin detection logic
├── data/                  # Optional local plugin DB
├── reports/               # (Coming soon) HTML reporting
├── utils/                 # Helper functions
├── main.py                # Entry point
├── config.py              # API token config
├── install.sh             # Optional installer for Kali Linux
└── requirements.txt       # Python dependencies
```

---

## 👨‍💻 Author
Made with ❤️ by [@m7mdatd](https://github.com/m7mdatd) — 2025  
📧 Contact: `m@twal.sa`
Feel free to contribute, fork, or share feedback!

---

## 📜 License
This project is licensed under the **MIT License**.
