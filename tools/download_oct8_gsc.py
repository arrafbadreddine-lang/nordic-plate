import urllib.request
import os

DOC_ID = "156oFVn-5vAsgDwjsJoSPQjrpH7GYlnlTlcl-3NZJWrs"
OUT_DIR = "/tmp/gsc_oct8"
os.makedirs(OUT_DIR, exist_ok=True)

TABS = {
    "dates": "231180398",
    "queries": "2012317231",
    "pages": "1541715539",
    "countries": "92055986",
    "devices": "1496992019",
    "appearance": "874250731"
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

print("Downloaded all Oct 8 GSC tabs successfully into /tmp/gsc_oct8/!")
