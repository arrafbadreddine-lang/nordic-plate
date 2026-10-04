import csv
import os

DATA_DIR = "/tmp/gsc_new"
OLD_DIR = "/tmp/gsc_data"

def read_csv(dirpath, filename):
    path = os.path.join(dirpath, filename)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows

# 1. Dates / Overall Trend
h_dates, r_dates = read_csv(DATA_DIR, "dates.csv")
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

print(f"=== CURRENT GSC REPORT OVERVIEW ===")
print(f"Total Clicks: {total_clicks} (vs previous 1618 clicks -> +{total_clicks - 1618})")
print(f"Total Impressions: {total_impressions} (vs previous 32859 -> +{total_impressions - 32859})")
print(f"Date Range: {dates_summary[0][0]} to {dates_summary[-1][0]}")

print("\n--- LAST 10 DAYS DAILY BREAKDOWN ---")
for d, c, i, ctr, p in dates_summary[-10:]:
    print(f"  {d} | Clicks: {c:<3} | Impressions: {i:<5} | CTR: {ctr:<6} | Pos: {p:.1f}")

# 2. Queries Comparison
h_q, r_q = read_csv(DATA_DIR, "queries.csv")
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
print("\n--- TOP 20 QUERIES BY CLICKS ---")
for q in queries_by_clicks[:20]:
    print(f"{q['query']:<35} | Clicks: {q['clicks']:<4} | Impr: {q['impressions']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

queries_by_impr = sorted(queries, key=lambda x: x["impressions"], reverse=True)
print("\n--- TOP 20 QUERIES BY IMPRESSIONS ---")
for q in queries_by_impr[:20]:
    print(f"{q['query']:<35} | Clicks: {q['clicks']:<4} | Impr: {q['impressions']:<5} | CTR: {q['ctr']:.1f}% | Pos: {q['pos']:.1f}")

# 3. Top Pages
h_p, r_p = read_csv(DATA_DIR, "pages.csv")
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

# 4. Check specific search terms: kanelbulle, raggmunk, tosca, äppelpaj
print("\n--- SPOTLIGHT TOPICS ---")
for term in ['kanel', 'raggmunk', 'tosca', 'äppel', 'soppa', 'pannkak']:
    term_queries = [q for q in queries if term in q['query'].lower()]
    t_clicks = sum(q['clicks'] for q in term_queries)
    t_impr = sum(q['impressions'] for q in term_queries)
    print(f"Topic '{term}': {len(term_queries)} queries | {t_clicks} clicks | {t_impr} impressions")
    for q in sorted(term_queries, key=lambda x: x['clicks'], reverse=True)[:3]:
        print(f"   • {q['query']} -> {q['clicks']} clicks, {q['impressions']} impr (pos {q['pos']:.1f})")
