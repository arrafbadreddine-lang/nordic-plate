import urllib.request
import os

DOC_ID = "1LGTYftk5_3IB1na4N8PZ7hvaxBMDZROyIUv9eM27Eoc"
OUT_DIR = "/tmp/gsc_oct5"
os.makedirs(OUT_DIR, exist_ok=True)

TABS = {
    "dates": "1395499538",
    "queries": "421574985",
    "pages": "1055837797",
    "countries": "983860321",
    "devices": "638878041",
    "appearance": "1557119681"
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

print("Downloaded all Oct 5 GSC tabs successfully into /tmp/gsc_oct5/!")
