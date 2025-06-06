import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re


def get_plugins_from_wpcontent(url):
    plugins_found = set()
    try:
        r = requests.get(url, timeout=10)
        if '/wp-content/plugins/' in r.text:
            matches = re.findall(r'/wp-content/plugins/([^/]+)/', r.text)
            plugins_found.update(matches)
    except Exception as e:
        print(f"[!] Error accessing the site: {e}")
    return list(plugins_found)


def get_plugins_from_sitemap(url):
    plugins_found = set()
    try:
        sitemap_url = urljoin(url, '/sitemap.xml')
        r = requests.get(sitemap_url, timeout=10)
        soup = BeautifulSoup(r.content, 'lxml-xml')
        urls = [loc.text for loc in soup.find_all('loc')]

        for page in urls:
            try:
                resp = requests.get(page, timeout=5)
                matches = re.findall(r'/wp-content/plugins/([^/]+)/', resp.text)
                plugins_found.update(matches)
            except:
                continue
    except Exception as e:
        print(f"[!] Sitemap not accessible: {e}")
    return list(plugins_found)


def detect_plugins(url):
    plugins = set()
    print("[*] Check the home page...")
    plugins.update(get_plugins_from_wpcontent(url))

    print("[*] Check sitemap...")
    plugins.update(get_plugins_from_sitemap(url))

    return list(plugins)
