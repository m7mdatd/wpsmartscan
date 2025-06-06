import requests
from config import WPSCAN_API_TOKEN

def fetch_plugin_vulnerabilities(plugin_slug):
    api_url = f"https://wpscan.com/api/v3/plugins/{plugin_slug}"
    headers = {
        "Authorization": f"Token token={WPSCAN_API_TOKEN}"
    }
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            vulnerabilities = data.get("vulnerabilities", [])
            return [
                {
                    "title": vuln.get("title"),
                    "cve": vuln.get("cve") or "N/A",
                    "severity": vuln.get("cvss", {}).get("score", "unknown"),
                    "reference": vuln.get("references", {}).get("url", [""])[0]
                }
                for vuln in vulnerabilities
            ]
        else:
            print(f"⚠️ فشل في جلب بيانات {plugin_slug} (Status {response.status_code})")
            return []
    except Exception as e:
        print(f"⚠️ خطأ أثناء الاتصال بـ WPScan API: {e}")
        return []
