#!/usr/bin/env python3
"""
Ping IndexNow (Bing, Yandex, Seznam, Naver) with recipe URLs for immediate crawling.
Usage:
    python3 tools/ping_indexnow.py [url1 url2 ...]
If no URLs are provided, pings the latest 4 published recipes by default.
"""
import sys
import json
import urllib.request
import os

INDEXNOW_KEY = "a2109b2efe5e4c06a52006e841b53b13"
HOST = "svenska-recept.se"

DEFAULT_URLS = [
    "https://svenska-recept.se/recept/klassisk-frasig-hasselbackspotatis.html",
    "https://svenska-recept.se/recept/klassisk-porterstek-svartvinbar-graddsas.html",
    "https://svenska-recept.se/recept/klassisk-vit-kladdkaka-citron-vanilj.html",
    "https://svenska-recept.se/recept/klassiska-frasiga-rarakor-stekt-flask.html",
    "https://svenska-recept.se/recept/klassiska-kladdkakemuffins-choklad.html",
    "https://svenska-recept.se/recept/kramig-kycklingpasta-soltorkade-tomater.html",
    "https://svenska-recept.se/recept/klassisk-hemlagad-vaniljsas.html",
    "https://svenska-recept.se/recept/klassiska-hallongrottor-smor-vanilj.html",
    "https://svenska-recept.se/recept/klassisk-kasslergratang-ris-curry.html",
]

def ping(urls=None):
    if not urls:
        urls = DEFAULT_URLS
    
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://{HOST}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"}
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"✅ [IndexNow] Successfully notified search engines ({resp.status} {resp.reason}) for {len(urls)} URLs:")
            for u in urls:
                print(f"   • {u}")
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ [IndexNow] HTTP Error: {e.code} - {e.read().decode()}")
        return False
    except Exception as e:
        print(f"❌ [IndexNow] Network Error: {e}")
        return False

if __name__ == "__main__":
    target_urls = sys.argv[1:] if len(sys.argv) > 1 else None
    ping(target_urls)
