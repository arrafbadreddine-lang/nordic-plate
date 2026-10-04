import urllib.request
import os

DOC_ID = "1-z7Dw3_FixhPJDcfa7I3VzjZccSb3WSNsRudHWjhbzs"
OUT_DIR = "/tmp/gsc_oct4"
os.makedirs(OUT_DIR, exist_ok=True)

TABS = {
    "dates": "1242392372",
    "queries": "1560733592",
    "pages": "1731557873",
    "countries": "561384602",
    "devices": "661677735",
    "appearance": "1774904551"
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

print("Downloaded all Oct 4 GSC tabs successfully!")
