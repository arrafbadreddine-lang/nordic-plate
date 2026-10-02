import urllib.request
import os
import csv

DOC_PERF = "19TDi7aRRf1mupFSWACho0Q4VwajfMAVkl98_ZuclW6M"
DOC_INDEX = "1Fjbzd1DhGb-uZHUIcbhMz9joZA0zK5WD15jW6xKjzgw"

OUT_DIR = "/tmp/gsc_data"
os.makedirs(OUT_DIR, exist_ok=True)

PERF_TABS = {
    "dates": "650182541",
    "queries": "581526479",
    "pages": "587221956",
    "countries": "1354984137",
    "devices": "2078152404",
    "appearance": "244984359"
}

INDEX_TABS = {
    "index_trend": "1503191695",
    "critical": "1997295978",
    "non_critical": "389602399"
}

for name, gid in PERF_TABS.items():
    url = f"https://docs.google.com/spreadsheets/d/{DOC_PERF}/export?format=csv&gid={gid}"
    out_file = os.path.join(OUT_DIR, f"perf_{name}.csv")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        data = urllib.request.urlopen(req).read()
        with open(out_file, "wb") as f:
            f.write(data)
        print(f"Downloaded perf_{name}.csv ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

for name, gid in INDEX_TABS.items():
    url = f"https://docs.google.com/spreadsheets/d/{DOC_INDEX}/export?format=csv&gid={gid}"
    out_file = os.path.join(OUT_DIR, f"index_{name}.csv")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        data = urllib.request.urlopen(req).read()
        with open(out_file, "wb") as f:
            f.write(data)
        print(f"Downloaded index_{name}.csv ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

print("\nDownload complete! Examining content...")
