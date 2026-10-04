import urllib.request
import os
import csv

DOC_ID = "1-37wc7QKMAMMAgeL5OGSX1UQMF3OUPTlY-_pxDIwKSo"
OUT_DIR = "/tmp/gsc_new"
os.makedirs(OUT_DIR, exist_ok=True)

TABS = {
    "dates": "1048008613",
    "queries": "1684223000",
    "pages": "74196432",
    "countries": "750461394",
    "devices": "1337456678",
    "appearance": "1819873977"
}

for name, gid in TABS.items():
    url = f"https://docs.google.com/spreadsheets/d/{DOC_ID}/export?format=csv&gid={gid}"
    out_file = os.path.join(OUT_DIR, f"{name}.csv")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        data = urllib.request.urlopen(req).read()
        with open(out_file, "wb") as f:
            f.write(data)
        print(f"Downloaded {name}.csv ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

print("Downloaded all new GSC tabs successfully!")
