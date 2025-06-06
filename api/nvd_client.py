# api/nvd_client.py

import requests

def fetch_nvd_vulnerabilities(plugin_slug):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": plugin_slug,
        "resultsPerPage": 5
    }
    headers = {
        "User-Agent": "wpsmartscan"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            vulns = data.get("vulnerabilities", [])
            results = []
            for v in vulns:
                cve_data = v.get("cve", {})
                cve_id = cve_data.get("id", "N/A")
                description = cve_data.get("descriptions", [{}])[0].get("value", "No description")
                severity = "N/A"
                cvss = cve_data.get("metrics", {}).get("cvssMetricV31", [])
                if cvss:
                    severity = cvss[0].get("cvssData", {}).get("baseSeverity", "N/A")

                results.append({
                    "title": description,
                    "cve": cve_id,
                    "severity": severity,
                    "reference": f"https://nvd.nist.gov/vuln/detail/{cve_id}"
                })
            return results
        else:
            return None
    except Exception as e:
        print(f"❌ Error fetching from NVD: {e}")
        return None
