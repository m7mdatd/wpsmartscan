from core import scanner

def print_banner():
    banner = """
╔════════════════════════════════════════════════════════════╗
║                    🛡️  WPSmartScan v1.0                    ║
║        Smart WordPress Plugin Vulnerability Scanner       ║
║             Developed by: @m7mdatd (2025)             ║
╚════════════════════════════════════════════════════════════╝
"""
    print(banner)

def main():
    print_banner()
    url = input('🌐 Enter your WordPress website link (example: https://example.com): ').strip()
    if not url.startswith('http'):
        url = 'https://' + url
    scanner.scan(url)

if __name__ == '__main__':
    main()
