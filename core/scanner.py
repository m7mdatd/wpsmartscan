from plugins.wp_plugin_detector import detect_plugins
from api.wpscan_client import fetch_plugin_vulnerabilities

PLUGIN_ALIASES = {
    "wp-logo-showcase-responsive-slider-slider": "logo-showcase-responsive-slider",
    "mh-magazine": "mh-magazine-lite",
}

def display_vulnerabilities(plugin_name, vulnerabilities, found_in_api):
    if not found_in_api:
        print(f"\n❓ No add-on data found in WPScan: {plugin_name}")
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
            vulns = fetch_plugin_vulnerabilities(slug)
            found = vulns is not None
            display_vulnerabilities(plugin, vulns or [], found)
    else:
        print("❌ No active add-ons were detected on this site..")
