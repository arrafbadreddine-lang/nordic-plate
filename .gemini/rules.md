# Svenska Recept (nordic-plate) - AI Agent Rules & Project Guidelines

This project powers **[svenska-recept.se](https://svenska-recept.se/)**, a high-performance Swedish recipe platform with 100% Google Rich Results schema compliance.

---

## 1. Core Principles
- **Language**: All user-facing content (recipe titles, descriptions, ingredients, step instructions, pro tips, FAQs, image alt text) MUST be in **Swedish**.
- **Communication with User**: Always in **English**.

---

## 2. Source of Truth
- **`tools/recipes_data.py`** -> The `RECIPES` list is the **sole source of truth**.
- **NEVER** edit files inside `recept/` or `kategorier/` directly — they are statically compiled and will be overwritten on the next build.

---

## 3. Image Generation & Processing Pipeline
Every recipe requires its own unique set of 5 responsive images:
1. **Master Image**: `assets/images/recept/<img>.jpg` (800x500 card, quality 80)
2. **Hero Image**: `assets/images/recept/<img>-1900x900.jpg` (1900x900, quality 82)
3. **Card 16x9**: `assets/images/recept/<img>-16x9.jpg` (1200x675, quality 80)
4. **Card 4x3**: `assets/images/recept/<img>-4x3.jpg` (1200x900, quality 80)
5. **Square 1x1**: `assets/images/recept/<img>-1x1.jpg` (800x800, quality 80)

### macOS `sips` batch command:
```bash
sips -z 500 800 -s formatOptions 80 <SRC> --out assets/images/recept/<img>.jpg
sips -z 900 1900 -s formatOptions 82 <SRC> --out assets/images/recept/<img>-1900x900.jpg
sips -z 675 1200 -s formatOptions 80 <SRC> --out assets/images/recept/<img>-16x9.jpg
sips -z 900 1200 -s formatOptions 80 <SRC> --out assets/images/recept/<img>-4x3.jpg
sips -z 800 800 -s formatOptions 80 <SRC> --out assets/images/recept/<img>-1x1.jpg
```

---

## 4. Build & Validation Step (MANDATORY before committing)
Run the following build commands whenever `tools/recipes_data.py` is updated:
```bash
python3 tools/generate_site_koket.py
python3 tools/validate_schemas.py
```
This updates:
- `index.html` (trending carousel & featured sections)
- `recept.html` (search & filter catalog)
- `kategorier/*.html` (category hubs)
- `recept/<slug>.html` (individual recipe pages)
- `sitemap.xml` & `sitemap_sv.xml`

---

## 5. Automated Deployment
This repository is connected to **GitHub Actions**:
- Branch: `main`
- Remote: `git@github.com:arrafbadreddine-lang/nordic-plate.git`
- Deploy method: Simply commit and push:
```bash
git add -A && git commit -m "feat: add <Dish Name> recipe" && git push origin main
```
GitHub Actions will automatically deploy all changes live to **https://svenska-recept.se/** in ~10 seconds.
