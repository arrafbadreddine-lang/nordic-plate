import csv
import os

DATA_DIR = "/tmp/gsc_oct5"
OCT4_DIR = "/tmp/gsc_oct4"

def read_csv(dirpath, filename):
    path = os.path.join(dirpath, filename)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows

print("=" * 70)
print("=== GOOGLE SEARCH CONSOLE AUDIT - OCT 5, 2026 EXPORT ===")
print("=" * 70)

# 1. Dates Analysis
h_dates, r_dates = read_csv(DATA_DIR, "dates.csv")
print(f"Export Date Range: {r_dates[0][0]} to {r_dates[-1][0]} ({len(r_dates)} days)")

total_clicks_9d = sum(int(r[1]) for r in r_dates if r[1])
total_impr_9d = sum(int(r[2]) for r in r_dates if r[2])

print(f"Total Clicks in window:      {total_clicks_9d:,}")
print(f"Total Impressions in window: {total_impr_9d:,}")
print(f"Window CTR:                  {(total_clicks_9d / total_impr_9d * 100):.2f}%")

print("\n--- DAILY PERFORMANCE TABLE ---")
for r in r_dates:
    d = r[0]
    c = int(r[1]) if r[1] else 0
    im = int(r[2]) if r[2] else 0
    ctr = r[3]
    pos = float(r[4]) if r[4] else 0.0
    bar = "█" * int(c / 10)
    note = ""
    if d == "2026-10-03":
        note = " ⭐ NEW ALL-TIME RECORD!"
    elif d == "2026-10-04":
        note = " ⏳ (Partial day in GSC log)"
    elif d == "2026-10-05":
        note = " ⏳ (Today - logging just started)"
    print(f"  {d} | Clicks: {c:<3} | Impr: {im:<5} | CTR: {ctr:<6} | Pos: {pos:.1f} | {bar}{note}")

# Compare Oct 3 consolidated data vs yesterday
_, r_dates_oct4 = read_csv(OCT4_DIR, "dates.csv")
oct4_dates_map = {r[0]: (int(r[1]), int(r[2])) for r in r_dates_oct4 if r[1]}

print("\n--- GSC DATA RECONCILIATION (Consolidated vs Initial) ---")
for r in r_dates:
    d = r[0]
    c = int(r[1]) if r[1] else 0
    im = int(r[2]) if r[2] else 0
    if d in oct4_dates_map:
        prev_c, prev_im = oct4_dates_map[d]
        diff_c = c - prev_c
        diff_im = im - prev_im
        sign_c = f"+{diff_c}" if diff_c >= 0 else str(diff_c)
        sign_im = f"+{diff_im}" if diff_im >= 0 else str(diff_im)
        print(f"  {d}: Clicks: {c} ({sign_c}) | Impressions: {im} ({sign_im})")

# 2. Queries in Oct 5 Export
h_q, r_q = read_csv(DATA_DIR, "queries.csv")
queries = []
for r in r_q:
    if len(r) >= 5:
        q = r[0]
        c = int(r[1]) if r[1] else 0
        im = int(r[2]) if r[2] else 0
        ctr_val = float(r[3].replace("%", "").strip()) if r[3] else 0.0
        pos_val = float(r[4]) if r[4] else 0.0
        queries.append({"query": q, "clicks": c, "impr": im, "ctr": ctr_val, "pos": pos_val})

queries.sort(key=lambda x: x["clicks"], reverse=True)

print(f"\n--- TOP 25 QUERIES IN CURRENT WINDOW ({len(queries)} total queries logged) ---")
for q in queries[:25]:
    print(f"  {q['query']:<35} | Clicks: {q['clicks']:<3} | Impr: {q['impr']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

# 3. Pages in Oct 5 Export
h_p, r_p = read_csv(DATA_DIR, "pages.csv")
pages = []
for r in r_p:
    if len(r) >= 5:
        p_url = r[0].replace("https://svenska-recept.se/", "")
        c = int(r[1]) if r[1] else 0
        im = int(r[2]) if r[2] else 0
        ctr_val = float(r[3].replace("%", "").strip()) if r[3] else 0.0
        pos_val = float(r[4]) if r[4] else 0.0
        pages.append({"page": p_url, "clicks": c, "impr": im, "ctr": ctr_val, "pos": pos_val})

pages.sort(key=lambda x: x["clicks"], reverse=True)

print(f"\n--- TOP 20 LANDING PAGES IN CURRENT WINDOW ({len(pages)} pages active) ---")
for p in pages[:20]:
    print(f"  {p['page']:<48} | Clicks: {p['clicks']:<4} | Impr: {p['impr']:<5} | CTR: {p['ctr']:.1f}% | Pos: {p['pos']:.1f}")

# 4. Kanelbulle & Fika Performance
print("\n--- SPOTLIGHT: KANELBULLENS DAG (OCT 4 SURGE) ---")
kanel_queries = [q for q in queries if any(k in q["query"].lower() for k in ["kanel", "kardemumma", "bulle", "bullar"])]
kanel_queries.sort(key=lambda x: x["clicks"], reverse=True)
tot_kc = sum(q["clicks"] for q in kanel_queries)
tot_kim = sum(q["impr"] for q in kanel_queries)
print(f"Total Bulle queries: {len(kanel_queries)} | Clicks: {tot_kc} | Impressions: {tot_kim}")
for q in kanel_queries[:12]:
    print(f"  {q['query']:<35} | Clicks: {q['clicks']:<3} | Impr: {q['impr']:<4} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

# 5. Devices & Countries
h_dev, r_dev = read_csv(DATA_DIR, "devices.csv")
print("\n--- DEVICES BREAKDOWN ---")
for r in r_dev:
    print(f"  {r[0]:<15} | Clics: {r[1]:<5} | Impressions: {r[2]:<6} | CTR: {r[3]:<6} | Pos: {r[4]}")

h_cou, r_cou = read_csv(DATA_DIR, "countries.csv")
print("\n--- TOP COUNTRIES ---")
for r in r_cou[:5]:
    print(f"  {r[0]:<15} | Clics: {r[1]:<5} | Impressions: {r[2]:<6} | CTR: {r[3]:<6} | Pos: {r[4]}")
