import csv
import os

DATA_DIR = "/tmp/gsc_data"

def read_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows

# 1. Dates / Overall Trend
h_dates, r_dates = read_csv("perf_dates.csv")
total_clicks = 0
total_impressions = 0
dates_summary = []
for row in r_dates:
    if len(row) >= 5 and row[1]:
        d = row[0]
        clicks = int(row[1]) if row[1] else 0
        impr = int(row[2]) if row[2] else 0
        ctr = row[3]
        pos = float(row[4]) if row[4] else 0.0
        total_clicks += clicks
        total_impressions += impr
        dates_summary.append((d, clicks, impr, ctr, pos))

print(f"=== OVERALL LAST 30 DAYS ===")
print(f"Total Clicks: {total_clicks}")
print(f"Total Impressions: {total_impressions}")
first_day = dates_summary[0]
last_day = dates_summary[-1]
print(f"Start ({first_day[0]}): {first_day[1]} clicks, {first_day[2]} impressions")
print(f"End ({last_day[0]}): {last_day[1]} clicks, {last_day[2]} impressions")
growth_clicks = ((last_day[1] - first_day[1]) / max(1, first_day[1])) * 100
growth_impr = ((last_day[2] - first_day[2]) / max(1, first_day[2])) * 100
print(f"Daily traffic growth: from {first_day[2]} impr/day to {last_day[2]} impr/day!")

# 2. Indexing Trend & Issues
h_idx, r_idx = read_csv("index_index_trend.csv")
print(f"\n=== INDEXING STATUS ===")
if r_idx:
    last_idx = [r for r in r_idx if len(r) >= 3 and r[1] and r[2]][-1]
    print(f"Latest Indexed count ({last_idx[0]}): {last_idx[2]} pages in index, {last_idx[1]} not indexed")

h_crit, r_crit = read_csv("index_critical.csv")
print(f"Critical indexing issues: {len(r_crit)} rows")
for r in r_crit:
    print("  ", r)

# 3. Top Queries
h_q, r_q = read_csv("perf_queries.csv")
print(f"\n=== TOTAL QUERIES: {len(r_q)} ===")

queries = []
for row in r_q:
    if len(row) >= 5:
        q = row[0]
        clicks = int(row[1]) if row[1] else 0
        impr = int(row[2]) if row[2] else 0
        ctr_str = row[3].replace("%", "").strip()
        ctr = float(ctr_str) if ctr_str else 0.0
        pos = float(row[4]) if row[4] else 0.0
        queries.append({"query": q, "clicks": clicks, "impressions": impr, "ctr": ctr, "pos": pos})

queries_by_clicks = sorted(queries, key=lambda x: x["clicks"], reverse=True)
print("\n--- TOP 15 QUERIES BY CLICKS ---")
for q in queries_by_clicks[:15]:
    print(f"{q['query']:<35} | Clicks: {q['clicks']:<4} | Impr: {q['impressions']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

queries_by_impr = sorted(queries, key=lambda x: x["impressions"], reverse=True)
print("\n--- TOP 15 QUERIES BY IMPRESSIONS ---")
for q in queries_by_impr[:15]:
    print(f"{q['query']:<35} | Clicks: {q['clicks']:<4} | Impr: {q['impressions']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

# 4. Striking Distance (Pos 4 - 15 with > 50 impressions)
striking = [q for q in queries if 4.0 <= q["pos"] <= 15.0 and q["impressions"] >= 50]
striking = sorted(striking, key=lambda x: x["impressions"], reverse=True)
print("\n--- STRIKING DISTANCE OPPORTUNITIES (Pos 4-15, >50 impressions) ---")
for q in striking[:15]:
    print(f"{q['query']:<35} | Clicks: {q['clicks']:<4} | Impr: {q['impressions']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

# 5. Low CTR High Impressions (Impr > 100, CTR < 3%)
low_ctr = [q for q in queries if q["impressions"] >= 80 and q["ctr"] < 3.0]
low_ctr = sorted(low_ctr, key=lambda x: x["impressions"], reverse=True)
print("\n--- LOW CTR OPPORTUNITIES (CTR < 3%, >80 impr - Title/Meta optimize) ---")
for q in low_ctr[:15]:
    print(f"{q['query']:<35} | Clicks: {q['clicks']:<4} | Impr: {q['impressions']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

# 6. Top Pages
h_p, r_p = read_csv("perf_pages.csv")
pages = []
for row in r_p:
    if len(row) >= 5:
        p = row[0]
        clicks = int(row[1]) if row[1] else 0
        impr = int(row[2]) if row[2] else 0
        ctr_str = row[3].replace("%", "").strip()
        ctr = float(ctr_str) if ctr_str else 0.0
        pos = float(row[4]) if row[4] else 0.0
        pages.append({"page": p, "clicks": clicks, "impressions": impr, "ctr": ctr, "pos": pos})

pages_by_clicks = sorted(pages, key=lambda x: x["clicks"], reverse=True)
print("\n--- TOP 15 LANDING PAGES BY CLICKS ---")
for p in pages_by_clicks[:15]:
    slug = p['page'].replace("https://svenska-recept.se/", "")
    print(f"{slug:<45} | Clicks: {p['clicks']:<4} | Impr: {p['impressions']:<5} | CTR: {p['ctr']:.1f}% | Pos: {p['pos']:.1f}")

# 7. Countries & Devices
h_c, r_c = read_csv("perf_countries.csv")
print("\n--- TOP COUNTRIES ---")
for r in r_c[:5]:
    print("  ", r)

h_d, r_d = read_csv("perf_devices.csv")
print("\n--- DEVICES ---")
for r in r_d:
    print("  ", r)
