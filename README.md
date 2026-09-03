# 🇸🇪 Svenska Recept (nordic-plate)

**Svenska Recept** (live at [svenska-recept.se](https://svenska-recept.se/)) is a modern, high-performance Swedish food and recipe website built for maximum SEO, ultra-fast page speeds, and 100% Google Rich Results schema validation.

---

## 📁 Project Architecture

```text
nordic-plate/
├── .gemini/rules.md            # AI Agent guidelines & workspace instructions
├── index.html                  # Homepage with dynamic trending carousel
├── recept.html                 # Complete recipe catalog with live search & filters
├── kategorier/                 # Category hub pages (Husmanskost, Fika & Bakning, etc.)
├── recept/                     # Individual recipe static HTML pages (58+ recipes)
├── assets/
│   ├── css/                    # Clean, lightweight CSS styling
│   ├── js/                     # Vanilla JS search, filters, bookmarking
│   └── images/recept/          # Responsive Full HD recipe images (5 sizes per recipe)
├── tools/
│   ├── recipes_data.py         # ⭐️ Central Source of Truth (All structured recipe data)
│   ├── generate_site_koket.py  # Static site generator (Rebuilds HTML, carousel, sitemaps)
│   └── validate_schemas.py     # Rich Results Schema validator (JSON-LD validation)
├── sitemap_sv.xml              # Swedish XML Sitemap for Google Search Console
└── sitemap.xml                 # Canonical Sitemap
```

---

## ⚡ Quick Start & Development

### 1. Adding a New Recipe
Add the recipe dictionary to `RECIPES` inside [`tools/recipes_data.py`](tools/recipes_data.py).

### 2. Building the Website
Run the compiler script to rebuild all HTML files, catalog, and sitemaps:
```bash
python3 tools/generate_site_koket.py
```

### 3. Validating Google Schema
Verify that 100% of the recipes pass Schema.org Rich Results tests:
```bash
python3 tools/validate_schemas.py
```

### 4. Deploying Live (GitHub Actions)
```bash
git add -A
git commit -m "feat: add new recipes"
git push origin main
```
*GitHub Actions automatically deploys the repository directly to Cloudways / Svenska-Recept.se in ~10 seconds.*
