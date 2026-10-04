import urllib.request
import re
import os

doc_id = "1-z7Dw3_FixhPJDcfa7I3VzjZccSb3WSNsRudHWjhbzs"
url = f"https://docs.google.com/spreadsheets/d/{doc_id}/edit?usp=sharing"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8")

target = '[[0,0,\\"'
pos = 0
tabs = []
while True:
    idx = html.find(target, pos)
    if idx == -1:
        break
    name_start = idx + len(target)
    name_end = html.find('\\"', name_start)
    name = html[name_start:name_end]
    before = html[max(0, idx-60):idx]
    gids = re.findall(r'(\d{5,12})', before)
    gid = gids[-1] if gids else "0"
    tabs.append((name, gid))
    pos = idx + 1

print("Found tabs:", tabs)
