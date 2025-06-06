
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░        ░▒▓███████▓▒░       ░▒▓██████▓▒░        ░▒▓██████▓▒░       ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░        ░▒▓██████▓▒░       ░▒▓█▓▒░             ░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░                    ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░                    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█████████████▓▒░       ░▒▓█▓▒░             ░▒▓███████▓▒░        ░▒▓██████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                          
                                                                                                                          
╔════════════════════════════════════════════════════════════╗
║                    🛡️  WPSmartScan v1.0                    ║
║        Smart WordPress Plugin Vulnerability Scanner        ║
║             Developed by X: @m7mdatd (2025)                ║
╚════════════════════════════════════════════════════════════╝

# WPSmartScan - WordPress Plugin Vulnerability Scanner

**WPSmartScan** is a smart and lightweight tool that detects WordPress plugins and checks for their known vulnerabilities using **both** [WPScan API](https://wpscan.com) and the [National Vulnerability Database (NVD)](https://nvd.nist.gov/). It helps security researchers and developers quickly assess the exposure of WordPress-based websites.

---

## 🛠 Features
- 🔍 Automatically detects active WordPress plugins on any target site
- ☁️ Fetches real-time vulnerability data from **WPScan API**
- 🗂 Falls back to **NVD** if WPScan fails (e.g., due to rate limits or missing records)
- 📊 Displays severity level (CVSS) and CVEs (if available)
- 💻 Clean, colorized CLI output for better visibility
- 🐧 Lightweight and works smoothly on Kali Linux and other Linux distros

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

For Kali Linux or fresh environments:
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
🌐 Enter your WordPress website link (example: https://example.com)
```

The tool will:
1. Scan the site for active plugins  
2. Query **WPScan API** for known vulnerabilities  
3. If WPScan fails or returns nothing, query **NVD**  
4. Display detailed results in the terminal

---

## 📦 Requirements
- Python 3.7+
- WPScan API token (free from [https://wpscan.com](https://wpscan.com))

### Save your API token in `config.py`:
```python
WPSCAN_API_TOKEN = "your-api-key-here"
```

---

## 📁 Project Structure
```
.
├── api/                   # API clients (WPScan + NVD)
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
