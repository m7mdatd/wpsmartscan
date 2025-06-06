import time
from plugins.wp_plugin_detector import detect_plugins
from api.wpscan_client import fetch_plugin_vulnerabilities as fetch_wpscan
from api.nvd_client import fetch_plugin_vulnerabilities as fetch_nvd

PLUGIN_ALIASES = {
    "wp-logo-showcase-responsive-slider-slider": "logo-showcase-responsive-slider",
    "mh-magazine": "mh-magazine-lite",
}

def display_vulnerabilities(plugin_name, vulnerabilities, found_in_any):
    if not found_in_any:
        print(f"\n❓ No vulnerability data found for plugin: {plugin_name}")
    elif vulnerabilities:
        print(f"\n🚨 Vulnerabilities discovered in the add-on: {plugin_name}")
        for vuln in vulnerabilities:
            title = vuln.get("title", "No title")
            cve = vuln.get("cve", "N/A")
            severity = vuln.get("severity", "unknown")
            reference = vuln.get("reference", "No reference")
            print(f" - [CVSS {severity}] {title} ({cve})")
            print(f"   ↪ {reference}")
    else:
        print(f"\n✅ There are no known vulnerabilities in the add-on: {plugin_name}")

def scan(url):
    print(f"🔍 Start the site scan: {url}")
    plugins = detect_plugins(url)

    if plugins:
        print(f"\n✅ has been discovered {len(plugins)} plugin:")
        for plugin in plugins:
            print(f" - {plugin}")

        print("\n📡 Verify WPScan API...")
        for plugin in plugins:
            slug = PLUGIN_ALIASES.get(plugin, plugin)
            print(f"\n🔎 Checking in progress: {plugin} (slug: {slug})")

            # Try WPScan first
            vulns = fetch_wpscan(slug)
            found_in_wpscan = vulns is not None and len(vulns) > 0

            # If WPScan failed or returned empty, try NVD
            if not found_in_wpscan:
                vulns = fetch_nvd(slug)
                found_in_nvd = vulns is not None and len(vulns) > 0
                display_vulnerabilities(plugin, vulns or [], found_in_nvd)
            else:
                display_vulnerabilities(plugin, vulns or [], True)

            time.sleep(1.5)
    else:
        print("❌ No active add-ons were detected on this site..")
