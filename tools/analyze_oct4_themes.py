import csv

def read_queries():
    with open("/tmp/gsc_oct4/queries.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        return [{"query": r[0], "clicks": int(r[1]) if r[1] else 0, "impr": int(r[2]) if r[2] else 0, "pos": float(r[4]) if r[4] else 0.0} for r in reader if len(r) >= 5]

queries = read_queries()

themes = {
    "Soppor & Grytor": ["soppa", "gryta", "kalops", "gulasch", "stuvning", "chili"],
    "Potatis & Tillbehör": ["potatis", "gratäng", "gratang", "mos", "pure", "hasselback", "råraka", "raggmunk"],
    "Fisk & Skaldjur": ["fisk", "lax", "torsk", "räkor", "sej", "strömming"],
    "Matpajer & Pajer": ["paj", "västerbotten", "quiche"],
    "Bakverk & Fika": ["kaka", "bulle", "muffins", "tårta", "kladdkaka", "småkakor", "bröd", "limpa", "våffl", "pannkak"],
    "Husmanskost Klassiker": ["köttbullar", "kålpudding", "kåldolmar", "köttfärslimpa", "biff", "wallenbergare", "fläsk", "lövbiff"]
}

for theme, words in themes.items():
    matched = [q for q in queries if any(w in q["query"].lower() for w in words)]
    t_c = sum(q["clicks"] for q in matched)
    t_i = sum(q["impr"] for q in matched)
    print(f"=== {theme.upper()} ===")
    print(f"Total queries: {len(matched)} | Clicks: {t_c} | Impressions: {t_i}")
    for q in sorted(matched, key=lambda x: x["impr"], reverse=True)[:5]:
        print(f"   * {q['query']:<35} | Clicks: {q['clicks']:<3} | Impr: {q['impr']:<5} | Pos: {q['pos']:.1f}")
    print()
