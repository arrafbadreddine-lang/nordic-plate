import csv
import os

DATA_DIR = "/tmp/gsc_oct4"
PREV_DIR = "/tmp/gsc_new"
OLD_DIR = "/tmp/gsc_data"

def read_csv(dirpath, filename):
    path = os.path.join(dirpath, filename)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows

# 1. Dates / Totals
_, r_dates_oct4 = read_csv(DATA_DIR, "dates.csv")
total_clicks_oct4 = sum(int(r[1]) for r in r_dates_oct4 if r[1])
total_impr_oct4 = sum(int(r[2]) for r in r_dates_oct4 if r[2])

_, r_dates_oct2 = read_csv(PREV_DIR, "dates.csv")
total_clicks_oct2 = sum(int(r[1]) for r in r_dates_oct2 if r[1])
total_impr_oct2 = sum(int(r[2]) for r in r_dates_oct2 if r[2])

print("=" * 60)
print("=== GOOGLE SEARCH CONSOLE AUDIT - OCT 4, 2026 ===")
print("=" * 60)
print(f"Total Clicks:       {total_clicks_oct4:,} (vs Oct 2: {total_clicks_oct2:,} [+{(total_clicks_oct4 - total_clicks_oct2):,} clicks, +{((total_clicks_oct4/total_clicks_oct2 - 1)*100):.1f}%])")
print(f"Total Impressions:  {total_impr_oct4:,} (vs Oct 2: {total_impr_oct2:,} [+{(total_impr_oct4 - total_impr_oct2):,} impr, +{((total_impr_oct4/total_impr_oct2 - 1)*100):.1f}%])")
print(f"Overall CTR:        {(total_clicks_oct4 / total_impr_oct4 * 100):.2f}%")

print("\n--- DAILY VELOCITY (LAST 10 DAYS) ---")
dates_summary = []
for row in r_dates_oct4:
    if len(row) >= 5 and row[1]:
        d = row[0]
        c = int(row[1]) if row[1] else 0
        im = int(row[2]) if row[2] else 0
        ctr = row[3]
        pos = float(row[4]) if row[4] else 0.0
        dates_summary.append((d, c, im, ctr, pos))

for d, c, im, ctr, pos in dates_summary[-10:]:
    bar = "█" * int(c / 10)
    print(f"  {d} | Clicks: {c:<3} | Impr: {im:<5} | CTR: {ctr:<6} | Pos: {pos:.1f} | {bar}")

# 2. Pages Analysis
_, r_p_oct4 = read_csv(DATA_DIR, "pages.csv")
pages_oct4 = []
for r in r_p_oct4:
    if len(r) >= 5:
        p_url = r[0].replace("https://svenska-recept.se/", "")
        c = int(r[1]) if r[1] else 0
        im = int(r[2]) if r[2] else 0
        ctr_val = float(r[3].replace("%", "").strip()) if r[3] else 0.0
        pos_val = float(r[4]) if r[4] else 0.0
        pages_oct4.append({"page": p_url, "clicks": c, "impr": im, "ctr": ctr_val, "pos": pos_val})

pages_oct4.sort(key=lambda x: x["clicks"], reverse=True)

print("\n--- TOP 20 LANDING PAGES BY CLICKS ---")
for p in pages_oct4[:20]:
    print(f"  {p['page']:<45} | Clicks: {p['clicks']:<4} | Impr: {p['impr']:<5} | CTR: {p['ctr']:.1f}% | Pos: {p['pos']:.1f}")

# Pages Gainers
_, r_p_oct2 = read_csv(PREV_DIR, "pages.csv")
pages_oct2_map = {}
for r in r_p_oct2:
    if len(r) >= 5:
        p_url = r[0].replace("https://svenska-recept.se/", "")
        pages_oct2_map[p_url] = {"clicks": int(r[1]) if r[1] else 0, "impr": int(r[2]) if r[2] else 0}

page_gainers = []
for p in pages_oct4:
    prev = pages_oct2_map.get(p["page"], {"clicks": 0, "impr": 0})
    diff_c = p["clicks"] - prev["clicks"]
    diff_im = p["impr"] - prev["impr"]
    page_gainers.append((p["page"], diff_c, p["clicks"], diff_im, p["impr"], p["pos"]))

page_gainers.sort(key=lambda x: (x[1], x[3]), reverse=True)
print("\n--- TOP 15 FASTEST GROWING PAGES (LAST 48H) ---")
for p, dc, tc, dim, tim, pos in page_gainers[:15]:
    print(f"  {p:<45} | +{dc:<3} clicks (tot {tc:<3}) | +{dim:<4} impr (tot {tim:<4}) | Pos: {pos:.1f}")

# 3. Queries Analysis
_, r_q_oct4 = read_csv(DATA_DIR, "queries.csv")
q_oct4_map = {}
for r in r_q_oct4:
    if len(r) >= 5:
        q = r[0]
        c = int(r[1]) if r[1] else 0
        im = int(r[2]) if r[2] else 0
        ctr_val = float(r[3].replace("%", "").strip()) if r[3] else 0.0
        pos_val = float(r[4]) if r[4] else 0.0
        q_oct4_map[q] = {"clicks": c, "impr": im, "ctr": ctr_val, "pos": pos_val}

_, r_q_oct2 = read_csv(PREV_DIR, "queries.csv")
q_oct2_map = {}
for r in r_q_oct2:
    if len(r) >= 5:
        q = r[0]
        c = int(r[1]) if r[1] else 0
        im = int(r[2]) if r[2] else 0
        ctr_val = float(r[3].replace("%", "").strip()) if r[3] else 0.0
        pos_val = float(r[4]) if r[4] else 0.0
        q_oct2_map[q] = {"clicks": c, "impr": im, "ctr": ctr_val, "pos": pos_val}

query_gainers = []
for q, data in q_oct4_map.items():
    prev = q_oct2_map.get(q, {"clicks": 0, "impr": 0})
    dc = data["clicks"] - prev["clicks"]
    dim = data["impr"] - prev["impr"]
    query_gainers.append((q, dc, data["clicks"], dim, data["impr"], data["pos"]))

query_gainers.sort(key=lambda x: (x[1], x[3]), reverse=True)
print("\n--- TOP 20 QUERY GAINERS (LAST 48H) ---")
for q, dc, tc, dim, tim, pos in query_gainers[:20]:
    print(f"  {q:<35} | +{dc:<3} clicks (tot {tc:<3}) | +{dim:<4} impr (tot {tim:<4}) | Pos: {pos:.1f}")

# 4. Spotlights: Kanelbullar & Fika
print("\n--- SPOTLIGHT: KANELBULLENS DAG & FIKA ---")
kanel_queries = [item for item in q_oct4_map.items() if any(k in item[0].lower() for k in ["kanel", "kardemumma", "bulle", "bullar"])]
kanel_queries.sort(key=lambda x: x[1]["clicks"], reverse=True)
tot_k_c = sum(v["clicks"] for _, v in kanel_queries)
tot_k_im = sum(v["impr"] for _, v in kanel_queries)
print(f"Total Kanelbulle/Bulle Queries: {len(kanel_queries)} | Clicks: {tot_k_c} | Impr: {tot_k_im}")
for q, v in kanel_queries[:12]:
    print(f"  {q:<35} | Clicks: {v['clicks']:<3} | Impr: {v['impr']:<4} | CTR: {v['ctr']:.1f}% | Pos: {v['pos']:.1f}")

# 5. Opportunity Queries: High Impressions (>50), Pos <= 5, but Low CTR (< 5%)
print("\n--- CTR OPPORTUNITY QUERIES (High Impressions, High Rank, Low CTR) ---")
opps = []
for q, v in q_oct4_map.items():
    if v["impr"] >= 50 and v["pos"] <= 5.0 and v["ctr"] < 4.0:
        opps.append((q, v["clicks"], v["impr"], v["ctr"], v["pos"]))
opps.sort(key=lambda x: x[2], reverse=True)
for q, c, im, ctr, pos in opps[:15]:
    print(f"  {q:<35} | Clicks: {c:<3} | Impr: {im:<5} | CTR: {ctr:.1f}% | Pos: {pos:.1f}")

# 6. Content Gap Queries: High Impressions (>40) but Pos > 7 or Clicks == 0
print("\n--- CONTENT GAP QUERIES (High Impressions, Site Ranking but No Focused Page) ---")
gaps = []
for q, v in q_oct4_map.items():
    if v["impr"] >= 40 and v["clicks"] <= 1 and v["pos"] > 5.0:
        gaps.append((q, v["clicks"], v["impr"], v["ctr"], v["pos"]))
gaps.sort(key=lambda x: x[2], reverse=True)
for q, c, im, ctr, pos in gaps[:15]:
    print(f"  {q:<35} | Clicks: {c:<3} | Impr: {im:<5} | CTR: {ctr:.1f}% | Pos: {pos:.1f}")

# 7. Check Batch 27 status
print("\n--- BATCH 27 STATUS ---")
batch27 = [
    "klassisk-frasig-raggmunk-i-langpanna.html",
    "klassiska-tunna-pannkakor.html",
    "klassisk-kramig-svampstuvning.html",
    "kramig-champinjonsoppa-timjan.html"
]
for slug in batch27:
    m = [p for p in pages_oct4 if slug in p["page"]]
    if m:
        print(f"  INDEXED & IN REPORT: {slug} -> Clicks: {m[0]['clicks']}, Impr: {m[0]['impr']}, Pos: {m[0]['pos']:.1f}")
    else:
        print(f"  AWAITING GSC LOG:     {slug}")
