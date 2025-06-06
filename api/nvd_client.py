# api/nvd_client.py

import requests

def fetch_plugin_vulnerabilities(plugin_slug):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    headers = {"User-Agent": "WPSmartScan/1.0"}

    try:
        params = {
            "keywordSearch": plugin_slug,
            "startIndex": 0,
            "resultsPerPage": 20
        }
        response = requests.get(base_url, params=params, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            results = []
            for item in data.get("vulnerabilities", []):
                cve_id = item.get("cve", {}).get("id", "N/A")
                description = item.get("cve", {}).get("descriptions", [{}])[0].get("value", "No description")
                severity = item.get("cve", {}).get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseSeverity", "N/A")
                url = f"https://nvd.nist.gov/vuln/detail/{cve_id}"

                results.append({
                    "cve": cve_id,
                    "title": description[:150],  # قص العنوان إن كان طويلًا
                    "severity": severity,
                    "reference": url,
                })
            return results

        else:
            print(f"⚠ NVD API request failed with status {response.status_code}")
            return []
    except Exception as e:
        print(f"⚠ Error during NVD lookup: {e}")
        return []
