#!/usr/bin/env python3
"""
Svenska Recept - Master Site Generator
Inspirerad av Köket.se och skandinavisk matjournalistik.
Includes:
- Crisp white canvas with Nordic Slate typography
- Google Discover 1900x900 image optimization & max-image-preview:large
- Social Sharing Bar (Facebook, Pinterest, WhatsApp, Copy Link)
- Interactive Reviews & Comments Section (persisted in localStorage)
- Equipment & Drink Pairing Callouts
- Culinary FAQ Section with Google FAQPage Schema
- 100% Google Recipe Schema JSON-LD
"""

import os
import json
from recipes_data import RECIPES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_RECIPES_DIR = os.path.join(BASE_DIR, "recept")
OUTPUT_CATEGORIES_DIR = os.path.join(BASE_DIR, "kategorier")

os.makedirs(OUTPUT_RECIPES_DIR, exist_ok=True)
os.makedirs(OUTPUT_CATEGORIES_DIR, exist_ok=True)

# Strict 16px font-weight matching icons
ICON_SEARCH = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7.5"></circle><line x1="21" y1="21" x2="16.5" y2="16.5"></line></svg>'
ICON_HEART = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>'
ICON_CLOCK = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
ICON_USERS = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'
ICON_FLAME = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2c1 3 4 5.5 4 9a6 6 0 0 1-12 0c0-3.5 3-6 4-9 1 2 3 3 4 0z"></path></svg>'
ICON_CHEF = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><path d="M6 13.8a4.5 4.5 0 1 1 2.6-8.2 5 5 0 0 1 9.8 1.4A4.5 4.5 0 1 1 18 13.8"></path><path d="M6 17h12"></path><path d="M6 21h12"></path></svg>'
ICON_LIGHTBULB = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M12 2a7 7 0 0 0-7 7c0 2.5 1.5 4.5 3 6h8c1.5-1.5 3-3.5 3-6a7 7 0 0 0-7-7z"></path></svg>'
ICON_STAR = '<svg class="svg-icon icon-star" width="14" height="14" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
ICON_SHARE = '<svg class="svg-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>'
ICON_ARROW_RIGHT = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>'
ICON_ARROW_LEFT = '<svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>'
ICON_JUMP = '<svg class="svg-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>'

def get_header_html(active_nav="", depth="../"):
    return f'''  <header class="site-header">
    <div class="container header-inner">
      <a href="{depth}index.html" class="site-logo">
        <img src="{depth}assets/images/logo.svg" alt="Svenska Recept Provkök" class="site-logo-img" width="220" height="44">
      </a>
      <nav class="site-nav">
        <a href="{depth}index.html" class="{'active' if active_nav=='hem' else ''}">Hem</a>
        <a href="{depth}recept.html" class="{'active' if active_nav=='alla' else ''}">Alla Recept</a>
        <a href="{depth}kategorier/husmanskost.html" class="{'active' if active_nav=='husmanskost' else ''}">Husmanskost</a>
        <a href="{depth}kategorier/fika-och-bakning.html" class="{'active' if active_nav=='fika' else ''}">Fika & Bakning</a>
        <a href="{depth}kategorier/hogtider-och-smorgasbord.html" class="{'active' if active_nav=='smorgasbord' else ''}">Högtider</a>
      </nav>
      <div class="header-actions">
        <a href="{depth}recept.html" class="favorites-header-btn" title="Sparade favoritrecept">
          {ICON_HEART} <span class="fav-text">Favoriter</span> <span class="favorites-badge-count">0</span>
        </a>
        <a href="{depth}recept.html" class="btn-icon-action" aria-label="Sök recept">
          {ICON_SEARCH} Sök
        </a>
        <button class="mobile-menu-btn" aria-label="Meny">☰</button>
      </div>
    </div>
  </header>'''

def get_footer_html(depth="../"):
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div style="margin-bottom: 1.25rem;">
            <a href="{depth}index.html" class="site-logo">
              <img src="{depth}assets/images/logo.svg" alt="Svenska Recept" class="site-logo-img" style="filter: brightness(0) invert(1);" width="200" height="40">
            </a>
          </div>
          <p>Sveriges mest pålitliga provkök för klassisk svensk husmanskost, fika och högtidsmat. Alla recept är provlagade minst tre gånger och näringsberäknade.</p>
        </div>
        <div class="footer-col">
          <h4>Kategorier</h4>
          <ul>
            <li><a href="{depth}kategorier/husmanskost.html">Klassisk Husmanskost</a></li>
            <li><a href="{depth}kategorier/fika-och-bakning.html">Fika & Bageri</a></li>
            <li><a href="{depth}kategorier/hogtider-och-smorgasbord.html">Högtider & Smörgåsbord</a></li>
            <li><a href="{depth}recept.html?q=under-30">Snabba Vardagsmiddagar</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Populära Recept</h4>
          <ul>
            <li><a href="{depth}recept/klassisk-kramig-kladdkaka.html">Klassisk Kladdkaka</a></li>
            <li><a href="{depth}recept/klassiska-svenska-kottbullar-graddsas.html">Svenska Köttbullar</a></li>
            <li><a href="{depth}recept/saftiga-kanelbullar-kardemumma.html">Saftiga Kanelbullar</a></li>
            <li><a href="{depth}recept/traditionell-vasterbottensostpaj.html">Västerbottensostpaj</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Om Provköket</h4>
          <ul>
            <li><a href="{depth}om-oss.html">Om Astrid Lindqvist</a></li>
            <li><a href="{depth}om-oss.html">Redaktionella Riktlinjer</a></li>
            <li><a href="{depth}kontakt.html">Kontakta Redaktionen</a></li>
            <li><a href="{depth}integritetspolicy.html">Integritetspolicy</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Svenska Recept Provkök (svenska-recept.se). Alla rättigheter förbehållna.</p>
        <div class="footer-legal-links">
          <a href="{depth}om-oss.html">Om oss</a>
          <a href="{depth}kontakt.html">Kontakt</a>
          <a href="{depth}integritetspolicy.html">Integritet & Cookies</a>
        </div>
      </div>
    </div>
  </footer>'''

def render_recipe_card(r, depth=""):
    return f'''        <article class="recipe-card" data-category="{r['cat_key']}" data-time="{r['time']}" data-rating="{r['rating']}" data-calories="{r['calories']}">
          <div class="recipe-card-media">
            <a href="{depth}recept/{r['file']}">
              <img src="{depth}assets/images/recept/{r['img']}.jpg" alt="{r['alt']}" class="recipe-card-img" width="600" height="400" loading="lazy">
            </a>
            <span class="recipe-card-badge">{r['category']}</span>
            <button class="card-heart-btn" data-slug="{r['slug']}" aria-label="Spara som favorit">
              {ICON_HEART}
            </button>
          </div>
          <div class="recipe-card-body">
            <div class="recipe-meta-top">
              <span class="recipe-rating">{ICON_STAR} <strong>{r['rating']}</strong> ({r['review_count']})</span>
              <span class="recipe-cooktime">{ICON_CLOCK} {r['time_str']}</span>
            </div>
            <h3 class="recipe-card-title"><a href="{depth}recept/{r['file']}">{r['card_title']}</a></h3>
            <p class="recipe-card-swedish-name">{r['sub']}</p>
            <p class="recipe-card-desc">{r['desc']}</p>
            <div class="recipe-card-footer">
              <span class="recipe-stats-item">{ICON_CLOCK} {r['time_str']}</span>
              <span class="recipe-stats-item">{ICON_FLAME} {r['calories']} kcal</span>
              <span class="recipe-stats-item">{ICON_USERS} {r['portions_num']} {r['portions_unit']}</span>
            </div>
          </div>
        </article>'''

def render_carousel_card(r, depth=""):
    return f'''          <div class="carousel-card">
            <div class="carousel-card-media">
              <a href="{depth}recept/{r['file']}">
                <img src="{depth}assets/images/recept/{r['img']}.jpg" alt="{r['alt']}" width="400" height="267" loading="lazy">
              </a>
              <span class="recipe-card-badge">{r['category']}</span>
              <button class="card-heart-btn" data-slug="{r['slug']}" aria-label="Spara recept">
                {ICON_HEART}
              </button>
            </div>
            <div class="carousel-card-body">
              <div class="carousel-card-meta">
                <span>{ICON_STAR} <strong>{r['rating']}</strong> ({r['review_count']})</span>
                <span>{ICON_CLOCK} {r['time_str']}</span>
              </div>
              <h3 class="carousel-card-title"><a href="{depth}recept/{r['file']}">{r['card_title']}</a></h3>
              <p class="carousel-card-desc">{r['desc']}</p>
              <div class="carousel-card-footer">
                <span>{ICON_FLAME} {r['calories']} kcal</span>
                <span>{ICON_USERS} {r['portions_num']} {r['portions_unit']}</span>
              </div>
            </div>
          </div>'''

def render_horizontal_carousel(title, subtitle, recipes_list, depth=""):
    cards_html = "\n".join([render_carousel_card(r, depth) for r in recipes_list])
    return f'''  <section class="container carousel-section">
    <div class="carousel-header">
      <div class="carousel-title-group">
        <h2>{title}</h2>
        <p>{subtitle}</p>
      </div>
      <div class="carousel-controls">
        <button class="carousel-arrow-btn carousel-prev" aria-label="Föregående recept">{ICON_ARROW_LEFT}</button>
        <button class="carousel-arrow-btn carousel-next" aria-label="Nästa recept">{ICON_ARROW_RIGHT}</button>
      </div>
    </div>
    <div class="carousel-track-wrapper">
      <div class="recipe-carousel">
{cards_html}
      </div>
    </div>
  </section>'''

def render_recipe_page(r):
    # Ingredients HTML
    ing_html = ""
    for grp in r["ingredients"]:
        ing_html += f'<h3 class="ingredient-group-title">{grp["group"]}</h3>\n<ul class="ingredients-list">\n'
        for itm in grp["items"]:
            ing_html += f'''  <li class="ingredient-item">
    <input type="checkbox" class="ingredient-checkbox" aria-label="Bocka av {itm['name']}">
    <span><strong class="ingrediens-mangd" data-base-mangd="{itm['val']}">{itm['val']}</strong> {itm['unit']} {itm['name']}</span>
  </li>\n'''
        ing_html += '</ul>\n'

    # Instructions HTML
    inst_html = ""
    for s in r["instructions"]:
        timer_btn = ""
        if s.get("timer"):
            timer_btn = f'<button class="step-timer-knapp" data-minuter="{s["timer"]}">{ICON_CLOCK} Starta timer ({s["timer"]} min)</button>'
        inst_html += f'''<div class="instruction-step">
  <div class="step-num-badge">{s['step']}</div>
  <div class="step-body">
    <h3 class="step-title">{s['title']}</h3>
    <p class="step-text">{s['text']}</p>
    {timer_btn}
  </div>
</div>\n'''

    # Equipment Chips
    eq_chips = "".join([f'<span class="equipment-chip">{eq}</span>' for eq in r.get("equipment", [])])
    equipment_html = f'''<div class="recipe-equipment-box">
  <h3>Köksutrustning</h3>
  <div class="equipment-chips">
    {eq_chips}
  </div>
</div>''' if eq_chips else ""

    # Drink Pairing Box
    drink_html = f'''<div class="recipe-drink-box">
  <h4>🍷 Kockens Dryckestips</h4>
  <p>{r.get("drink_pairing", "")}</p>
</div>''' if r.get("drink_pairing") else ""

    # FAQ Section & Schema
    faq_schema_items = []
    faq_accordion_items = ""
    for faq in r.get("faqs", []):
        faq_schema_items.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })
        faq_accordion_items += f'''<div class="faq-item">
  <h3 class="faq-question">❓ {faq["q"]}</h3>
  <p class="faq-answer">{faq["a"]}</p>
</div>\n'''

    faq_section_html = f'''<section class="recipe-faq-section">
  <h2>Vanliga Frågor om Receptet</h2>
  <div class="faq-list">
    {faq_accordion_items}
  </div>
</section>''' if faq_accordion_items else ""

    # Pre-populated Reviews HTML
    comments_html = ""
    for rev in r.get("community_reviews", []):
        stars = "★" * rev["rating"] + "☆" * (5 - rev["rating"])
        comments_html += f'''<div class="comment-card">
  <div class="comment-meta">
    <span class="comment-author">{rev["name"]} <span class="comment-verified-badge">✓ Verifierad provlagare</span></span>
    <span>{rev["date"]}</span>
  </div>
  <div style="color: #F59E0B; font-size: 1rem; margin-bottom: 0.4rem; letter-spacing: 0.1em;">{stars}</div>
  <p class="comment-text">{rev["comment"]}</p>
</div>\n'''

    # Related recipes (same category)
    same_cat = [x for x in RECIPES if x["cat_key"] == r["cat_key"] and x["slug"] != r["slug"]]
    if len(same_cat) < 3:
        same_cat = [x for x in RECIPES if x["slug"] != r["slug"]][:4]

    # Other recipes (other categories)
    other_cat = [x for x in RECIPES if x["cat_key"] != r["cat_key"]]

    carousel_same = render_horizontal_carousel(f"Mer inom {r['category']}", "Fler provlagade favoriter från samma kategori", same_cat, depth="../")
    carousel_other = render_horizontal_carousel("Andra populära kategorier", "Upptäck fler älskade klassiker från vårt provkök", other_cat, depth="../")

    # JSON-LD Schema
    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Hem", "item": "https://svenska-recept.se/"},
                    {"@type": "ListItem", "position": 2, "name": r["category"], "item": f"https://svenska-recept.se/kategorier/{r['cat_slug']}.html"},
                    {"@type": "ListItem", "position": 3, "name": r["card_title"], "item": f"https://svenska-recept.se/recept/{r['file']}"}
                ]
            },
            {
                "@type": "Recipe",
                "@id": f"https://svenska-recept.se/recept/{r['file']}#recipe",
                "name": r["title"],
                "headline": r["title"],
                "image": [
                    f"https://svenska-recept.se/assets/images/recept/{r['img']}-1900x900.jpg",
                    f"https://svenska-recept.se/assets/images/recept/{r['img']}-16x9.jpg",
                    f"https://svenska-recept.se/assets/images/recept/{r['img']}-4x3.jpg",
                    f"https://svenska-recept.se/assets/images/recept/{r['img']}-1x1.jpg"
                ],
                "description": r["long_desc"],
                "keywords": r["keywords"],
                "author": {
                    "@type": "Person",
                    "name": "Astrid Lindqvist",
                    "jobTitle": "Receptskapare & Kock",
                    "url": "https://svenska-recept.se/om-oss.html"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Svenska Recept",
                    "url": "https://svenska-recept.se/",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://svenska-recept.se/assets/images/logo.png"
                    }
                },
                "datePublished": "2026-01-15T08:00:00+01:00",
                "dateModified": "2026-08-22T12:00:00+02:00",
                "prepTime": r["prep_time"],
                "cookTime": r["cook_time"],
                "totalTime": r["total_time"],
                "recipeYield": f"{r['portions_num']} {r['portions_unit']}",
                "recipeCategory": r["category"],
                "recipeCuisine": "Svensk",
                "nutrition": {
                    "@type": "NutritionInformation",
                    "calories": f"{r['calories']} calories",
                    "servingSize": f"1 {r['portions_unit'][:-1] if r['portions_unit'].endswith('er') else r['portions_unit']}"
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": str(r["rating"]),
                    "reviewCount": str(r["review_count"]),
                    "bestRating": "5",
                    "worstRating": "1"
                },
                "recipeIngredient": [
                    f"{itm['val']} {itm['unit']} {itm['name']}".strip()
                    for grp in r["ingredients"] for itm in grp["items"]
                ],
                "recipeInstructions": [
                    {"@type": "HowToStep", "name": s["title"], "text": s["text"], "position": s["step"]}
                    for s in r["instructions"]
                ]
            }
        ]
    }

    if faq_schema_items:
        schema_graph["@graph"].append({
            "@type": "FAQPage",
            "mainEntity": faq_schema_items
        })

    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{r['title']} | Svenska Recept</title>
  <meta name="description" content="{r['long_desc']}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://svenska-recept.se/recept/{r['file']}">
  <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
  
  <!-- Open Graph / Google Discover (1900x900) -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{r['title']}">
  <meta property="og:description" content="{r['long_desc']}">
  <meta property="og:image" content="https://svenska-recept.se/assets/images/recept/{r['img']}-1900x900.jpg">
  <meta property="og:image:width" content="1900">
  <meta property="og:image:height" content="900">
  <meta property="og:url" content="https://svenska-recept.se/recept/{r['file']}">
  
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/recipe.css">
  
  <script type="application/ld+json">
{json.dumps(schema_graph, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
{get_header_html(r['cat_key'], depth="../")}

  <!-- Brödsmulor -->
  <div class="breadcrumbs-bar">
    <div class="container">
      <ul class="breadcrumb-list">
        <li><a href="../index.html">Hem</a></li>
        <li><a href="../kategorier/{r['cat_slug']}.html">{r['category']}</a></li>
        <li>{r['card_title']}</li>
      </ul>
    </div>
  </div>

  <!-- Recept Header & Fullbreddsbild -->
  <header class="recipe-header">
    <div class="container recipe-header-container">
      <div class="recipe-header-top">
        <div class="recipe-tag-row">
          <span class="recipe-category-tag">{r['category']}</span>
          <span class="recipe-diet-tag">{r['diet']}</span>
          <span class="recipe-difficulty-tag">Svårighetsgrad: {r.get('difficulty', 'Enkel')}</span>
          <span class="recipe-rating">{ICON_STAR} <strong>{r['rating']}</strong> ({r['review_count']} betyg)</span>
        </div>
        <h1 class="recipe-title">{r['title']}</h1>
        <p class="recipe-lead">{r['long_desc']}</p>
        
        <div class="recipe-author-bar">
          <div class="author-info">
            <div class="author-avatar-initial">AL</div>
            <div>
              <span class="author-name">Astrid Lindqvist</span>
              <div style="font-size: 0.8rem; color: var(--color-text-muted);">Svenska Recept Provkök • Uppdaterad 2026</div>
            </div>
          </div>
          <div class="recipe-action-btns">
            <a href="#recept-start" class="btn-jump-to-recipe">{ICON_JUMP} Hoppa till recept</a>
            <button class="btn-icon-action" id="save-recipe-btn" data-slug="{r['slug']}">{ICON_HEART} Spara recept</button>
            <button class="btn-icon-action" onclick="window.print();" aria-label="Skriv ut recept">🖨️ Skriv ut</button>
          </div>
        </div>

        <!-- Social Delningsrad -->
        <div class="social-share-bar">
          <span class="social-share-label">{ICON_SHARE} Dela receptet:</span>
          <button class="share-btn share-btn-facebook" aria-label="Dela på Facebook">Facebook</button>
          <button class="share-btn share-btn-pinterest" aria-label="Spara på Pinterest">Pinterest</button>
          <button class="share-btn share-btn-whatsapp" aria-label="Dela på WhatsApp">WhatsApp</button>
          <button class="share-btn share-btn-copy" aria-label="Kopiera länk">📋 Kopiera länk</button>
        </div>
      </div>
      
      <!-- Fullbreddsbild 1900x900 Google Discover -->
      <figure class="recipe-hero-fullwidth">
        <img src="../assets/images/recept/{r['img']}-1900x900.jpg" alt="{r['alt']}" width="1900" height="900" fetchpriority="high">
      </figure>
    </div>
  </header>

  <!-- Snabbfakta (Kompakta Pills) -->
  <section class="container" id="recept-start">
    <div class="recipe-meta-bar">
      <div class="meta-pill">
        {ICON_CLOCK} <span><strong>Förberedelse:</strong> {r.get('prep_time_str', '15 min')}</span>
      </div>
      <div class="meta-pill">
        {ICON_CLOCK} <span><strong>Tillagning:</strong> {r.get('cook_time_str', '15 min')}</span>
      </div>
      <div class="meta-pill">
        {ICON_CLOCK} <span><strong>Total tid:</strong> {r['time_str']}</span>
      </div>
      <div class="meta-pill">
        {ICON_USERS} <span><strong>Portioner:</strong> {r['portions_num']} {r['portions_unit']}</span>
      </div>
      <div class="meta-pill">
        {ICON_FLAME} <span><strong>Kalorier:</strong> {r['calories']} kcal</span>
      </div>
      <div class="meta-pill">
        {ICON_CHEF} <span><strong>Kök:</strong> Svensk klassiker</span>
      </div>
    </div>
  </section>

  <!-- Huvudinnehåll: Ingredienser + Gör så här -->
  <main class="container">
    <div class="recipe-body-grid">
      
      <!-- Ingredienskolumn -->
      <aside class="recipe-ingredients-card">
        <div class="ingredients-card-header">
          <h2>Ingredienser</h2>
          <div class="portions-controller">
            <span>Portioner:</span>
            <button class="portion-btn decrease" aria-label="Minska portioner">−</button>
            <strong class="portions-display" data-base-portioner="{r['portions_num']}" data-enhet-text="{r['portions_unit']}">{r['portions_num']} {r['portions_unit']}</strong>
            <button class="portion-btn increase" aria-label="Öka portioner">+</button>
          </div>
        </div>
        {ing_html}
        {equipment_html}
      </aside>

      <!-- Tillagningskolumn -->
      <section class="recipe-instructions-content">
        <h2>Gör så här</h2>
        {inst_html}

        <!-- Kockens Tips -->
        <div class="pro-tips-card">
          <h3>{ICON_LIGHTBULB} Kockens Bästa Tips</h3>
          <p>{r['pro_tips']}</p>
        </div>

        {drink_html}

        <!-- Näringsinformation -->
        <div class="nutrition-facts-box">
          <h3>Näringsvärde per portion</h3>
          <div class="nutrition-facts-grid">
            <div class="nutrition-fact-item">
              <div class="nutrition-val">{r['nutrition']['calories']}</div>
              <div class="nutrition-lbl">Energi</div>
            </div>
            <div class="nutrition-fact-item">
              <div class="nutrition-val">{r['nutrition']['protein']}</div>
              <div class="nutrition-lbl">Protein</div>
            </div>
            <div class="nutrition-fact-item">
              <div class="nutrition-val">{r['nutrition']['carbs']}</div>
              <div class="nutrition-lbl">Kolhydrater</div>
            </div>
            <div class="nutrition-fact-item">
              <div class="nutrition-val">{r['nutrition']['fat']}</div>
              <div class="nutrition-lbl">Fett</div>
            </div>
            <div class="nutrition-fact-item">
              <div class="nutrition-val">{r['nutrition']['sugar']}</div>
              <div class="nutrition-lbl">Socker</div>
            </div>
          </div>
        </div>

        {faq_section_html}

        <!-- Kommentarer & Betyg -->
        <section class="recipe-comments-section">
          <div class="comments-header">
            <h2>Kommentarer & Betyg</h2>
            <div class="comments-rating-summary">
              {ICON_STAR} <strong>{r['rating']} av 5</strong> baserat på {r['review_count']} provlagningar
            </div>
          </div>

          <!-- Skriv kommentar formulär -->
          <div class="comment-form-card">
            <h3>Har du provlagat receptet? Lämna ditt betyg!</h3>
            <form id="recipe-comment-form">
              <div style="margin-bottom: 0.75rem;">
                <label style="display:block; font-size: 0.85rem; font-weight:700; color:var(--color-primary); margin-bottom: 0.35rem;">Ditt betyg:</label>
                <div class="star-rating-picker">
                  <button type="button" class="star-picker-btn" data-rating="1">★</button>
                  <button type="button" class="star-picker-btn" data-rating="2">★</button>
                  <button type="button" class="star-picker-btn" data-rating="3">★</button>
                  <button type="button" class="star-picker-btn" data-rating="4">★</button>
                  <button type="button" class="star-picker-btn selected" data-rating="5">★</button>
                  <input type="hidden" id="selected-rating-val" value="5">
                </div>
              </div>
              <div class="comment-inputs-row">
                <input type="text" id="comment-author-name" class="comment-input" placeholder="Ditt namn *" required>
                <input type="email" class="comment-input" placeholder="Din e-postadress (visas ej)">
              </div>
              <textarea id="comment-text-content" class="comment-textarea" placeholder="Hur blev resultatet? Har du några egna tips eller anpassningar? *" required></textarea>
              <button type="submit" class="btn-koket-search" style="padding: 0.65rem 1.4rem;">Skicka kommentar</button>
            </form>
          </div>

          <!-- Kommentarlista -->
          <div class="comments-list" id="comments-list-container">
            {comments_html}
          </div>
        </section>

      </section>
    </div>
  </main>

  <!-- Relaterade Receptkaruseller (Dubbel Karusell) -->
  <div class="related-carousels-container">
{carousel_same}
{carousel_other}
  </div>

{get_footer_html(depth="../")}

  <script src="../assets/js/recipe-engine.js"></script>
</body>
</html>'''
    
    filepath = os.path.join(OUTPUT_RECIPES_DIR, r["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated recipe: {r['file']}")

def generate_homepage():
    # 2 Large stories (Editorial Highlights)
    large_story_1 = [r for r in RECIPES if r["slug"] == "kramig-svensk-laxsoppa"][0] # Nya Laxsoppa
    large_story_2 = [r for r in RECIPES if r["slug"] == "traditionell-vasterbottensostpaj"][0] # Västerbottensostpaj
    
    # 4 Square tiles
    square_1 = [r for r in RECIPES if r["slug"] == "klassiska-saftiga-karleksmums"][0] # Kärleksmums
    square_2 = [r for r in RECIPES if r["slug"] == "klassisk-flygande-jacob"][0] # Flygande Jacob
    square_3 = [r for r in RECIPES if r["slug"] == "klassisk-toast-skagen"][0] # Toast Skagen
    square_4 = [r for r in RECIPES if r["slug"] == "klassisk-langkokt-kalops"][0] # Kalops

    # 1. New & Trending Carousel (all latest recipes first)
    c_trending = list(reversed(RECIPES))
    # 2. Category Carousels
    c_husman = [r for r in RECIPES if r["cat_key"] == "husmanskost"]
    c_fika = [r for r in RECIPES if r["cat_key"] == "fika"]
    c_smorgasbord = [r for r in RECIPES if r["cat_key"] == "smorgasbord"]
    c_under30 = [r for r in RECIPES if r.get("time", 30) <= 30]

    carousel_trending = render_horizontal_carousel("🔥 Trendande & Nyinkommet i Provköket", "De allra senaste provlagade recepten och hetaste favoriterna just nu", c_trending)
    carousel_husman = render_horizontal_carousel("Klassisk Svensk Husmanskost", "Från saftiga köttbullar till frasiga raggmunkar, Wallenbergare och långkokt Kalops", c_husman)
    carousel_fika = render_horizontal_carousel("Bakat och gott till fikat", "Ljuvliga kanelbullar, kladdkaka, toscakaka, saftiga kärleksmums och semlor", c_fika)
    carousel_smorgasbord = render_horizontal_carousel("Högtider & Smörgåsbord", "Perfekta recept till midsommar, påsk, kräftskiva och julbord", c_smorgasbord)
    carousel_under30 = render_horizontal_carousel("⏱️ Snabba Vardagsfavoriter under 30 min", "Smakrika och mättande middagar som går blixtsnabbt att laga i vardagen", c_under30)

    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Svenska Recept – 100% Provlagad Svensk Mat & Bageri</title>
  <meta name="description" content="Hitta Sveriges bästa provlagade recept på klassisk husmanskost, fika, kanelbullar, kladdkaka, köttbullar och smörgåsbord.">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://svenska-recept.se/">
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/recipe.css">
</head>
<body>
{get_header_html(active_nav="hem", depth="")}

  <!-- Köket.se Hero Sök: "Vad vill du laga idag?" -->
  <section class="hero-koket-search-section">
    <div class="container hero-search-wrapper">
      <h1 class="hero-search-title-label">Vad vill du laga idag?</h1>
      <p class="hero-search-subtitle">Sök bland 100% provlagade svenska favoriter, klassisk husmanskost och bagerikvalitet.</p>
      
      <form class="koket-search-form" action="recept.html" method="GET">
        <div class="koket-search-input-box">
          <span class="search-icon">{ICON_SEARCH}</span>
          <input type="text" name="q" placeholder="Sök recept, råvaror & matinspiration (t.ex. lax, kladdkaka, köttbullar...)" aria-label="Sök recept">
          <button type="submit" class="btn-koket-search">{ICON_SEARCH} Sök</button>
        </div>
      </form>

      <!-- Snabbvals-chips -->
      <div class="koket-quick-tips-row">
        <a href="#trending-section" class="koket-tip-chip">🔥 Nyinkommet & Trendande</a>
        <a href="kategorier/husmanskost.html" class="koket-tip-chip">Klassisk Husmanskost</a>
        <a href="kategorier/fika-och-bakning.html" class="koket-tip-chip">Bakat & Fika</a>
        <a href="recept.html?q=under-30" class="koket-tip-chip">Under 30 min</a>
        <a href="kategorier/hogtider-och-smorgasbord.html" class="koket-tip-chip">Högtider & Smörgåsbord</a>
        <a href="recept/kramig-svensk-laxsoppa.html" class="koket-tip-chip">Krämig Laxsoppa</a>
        <a href="om-oss.html" class="koket-tip-chip alt-blue">Om Provköket</a>
      </div>
    </div>
  </section>

  <!-- 1. TRENDANDE & NYINKOMMET I PROVKÖKET (NEWEST RECIPES FIRST) -->
  <div id="trending-section">
{carousel_trending}
  </div>

  <!-- Mosaik Hero Grid (Köket.se Editorial Signature) -->
  <section class="container mosaic-section">
    <div class="mosaic-grid">
      
      <!-- 2 Stora Huvudartiklar -->
      <a href="recept/{large_story_1['file']}" class="mosaic-item-large">
        <img src="assets/images/recept/{large_story_1['img']}.jpg" alt="{large_story_1['alt']}" width="800" height="500" loading="eager">
        <div class="mosaic-item-overlay">
          <span class="mosaic-tag">Nyhet i Provköket</span>
          <h2 class="mosaic-title-large">{large_story_1['card_title']} med Dill & Purjolök</h2>
          <p class="mosaic-desc-large">{large_story_1['desc']}</p>
        </div>
      </a>

      <a href="recept/{large_story_2['file']}" class="mosaic-item-large">
        <img src="assets/images/recept/{large_story_2['img']}.jpg" alt="{large_story_2['alt']}" width="800" height="500" loading="eager">
        <div class="mosaic-item-overlay">
          <span class="mosaic-tag">Fest & Smörgåsbord</span>
          <h2 class="mosaic-title-large">{large_story_2['card_title']} med Löjrom & Gräddfil</h2>
          <p class="mosaic-desc-large">{large_story_2['desc']}</p>
        </div>
      </a>

      <!-- 4 Kvadratiska Receptpuffar -->
      <a href="recept/{square_1['file']}" class="mosaic-item-square">
        <img src="assets/images/recept/{square_1['img']}.jpg" alt="{square_1['alt']}" width="400" height="300" loading="lazy">
        <div class="mosaic-item-overlay">
          <h3 class="mosaic-title-square">{square_1['card_title']} med Kaffeglasyr</h3>
        </div>
      </a>

      <a href="recept/{square_2['file']}" class="mosaic-item-square">
        <img src="assets/images/recept/{square_2['img']}.jpg" alt="{square_2['alt']}" width="400" height="300" loading="lazy">
        <div class="mosaic-item-overlay">
          <h3 class="mosaic-title-square">{square_2['card_title']} med Banan & Bacon</h3>
        </div>
      </a>

      <a href="recept/{square_3['file']}" class="mosaic-item-square">
        <img src="assets/images/recept/{square_3['img']}.jpg" alt="{square_3['alt']}" width="400" height="300" loading="lazy">
        <div class="mosaic-item-overlay">
          <h3 class="mosaic-title-square">{square_3['card_title']} med Handskalade Räkor</h3>
        </div>
      </a>

      <a href="recept/{square_4['file']}" class="mosaic-item-square">
        <img src="assets/images/recept/{square_4['img']}.jpg" alt="{square_4['alt']}" width="400" height="300" loading="lazy">
        <div class="mosaic-item-overlay">
          <h3 class="mosaic-title-square">{square_4['card_title']} med Kryddpeppar</h3>
        </div>
      </a>

    </div>
  </section>

  <!-- Kategori-Karuseller -->
{carousel_husman}
{carousel_fika}
{carousel_smorgasbord}
{carousel_under30}

{get_footer_html(depth="")}

  <script src="assets/js/recipe-engine.js"></script>
</body>
</html>'''

    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated homepage index.html")

def generate_catalog():
    cards_html = "\n".join([render_recipe_card(r, depth="") for r in RECIPES])

    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alla Svenska Recept – Sök & Filtrera | Svenska Recept</title>
  <meta name="description" content="Sök bland alla våra provlagade svenska recept. Filtrera på husmanskost, fika, högtider, tillagningstid och vegetariskt.">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://svenska-recept.se/recept.html">
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/recipe.css">
</head>
<body>
{get_header_html(active_nav="alla", depth="")}

  <main class="container section-padding">
    <div style="max-width: 800px; margin: 0 auto 2.5rem; text-align: center;">
      <h1 class="hero-search-title-label" style="font-size: clamp(1.85rem, 6vw, 2.8rem); margin-bottom: 0.5rem;">Receptkatalog</h1>
      <p style="color: var(--color-text-muted); font-size: 1.05rem;">Sök bland alla våra provlagade favoriter eller filtrera efter kategori och tid.</p>
      
      <div class="koket-search-input-box" style="margin-top: 1.5rem;">
        <span class="search-icon">{ICON_SEARCH}</span>
        <input type="text" id="recipe-search-input" placeholder="Sök recept eller råvara (t.ex. lax, kladdkaka...)" aria-label="Sök recept" style="min-width: 0;">
      </div>

      <!-- Filter-chips -->
      <div class="filter-chips-row" style="justify-content: center; margin-top: 1.25rem;">
        <button class="filter-chip active" data-filter="all">Alla Recept</button>
        <button class="filter-chip" data-filter="husmanskost">Husmanskost</button>
        <button class="filter-chip" data-filter="fika">Fika & Bakning</button>
        <button class="filter-chip" data-filter="smorgasbord">Högtider</button>
        <button class="filter-chip" data-filter="under-30">Under 30 min</button>
        <button class="filter-chip" data-filter="vegetariskt">Vegetariskt</button>
      </div>

      <div id="filter-results-count" style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.75rem;">Visar {len(RECIPES)} recept</div>
    </div>

    <!-- Recept Grid -->
    <div class="recipe-grid" id="recipes-catalog-grid">
{cards_html}
    </div>
  </main>

{get_footer_html(depth="")}

  <script src="assets/js/recipe-engine.js"></script>
  <script src="assets/js/search-filter.js"></script>
</body>
</html>'''

    with open(os.path.join(BASE_DIR, "recept.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated recept.html catalog")

CATEGORIES = [
    {"slug": "husmanskost", "key": "husmanskost", "title": "Klassisk Svensk Husmanskost", "desc": "Traditionella svenska rätter tillagade från grunden med kärlek och äkta smör. Från köttbullar till Wallenbergare, raggmunk och krämig korv stroganoff."},
    {"slug": "fika-och-bakning", "key": "fika", "title": "Svensk Fika & Bageri", "desc": "Sveriges godaste bakverk. Saftiga kanelbullar med nymortlad kardemumma, knäckig äppelpaj, kladdkaka, toscakaka och klassiska semlor."},
    {"slug": "hogtider-och-smorgasbord", "key": "smorgasbord", "title": "Högtider & Smörgåsbord", "desc": "Recepten som förgyller midsommar, påsk, kräftskiva och julbordet. Krämig kantarellpaj, Västerbottensostpaj, gravad lax och Toast Skagen."}
]

def generate_categories():
    for cat in CATEGORIES:
        cat_recipes = [r for r in RECIPES if r["cat_key"] == cat["key"]]
        cards_html = "\n".join([render_recipe_card(r, depth="../") for r in cat_recipes])

        html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cat['title']} – Bästa Provlagade Recepten | Svenska Recept</title>
  <meta name="description" content="{cat['desc']}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://svenska-recept.se/kategorier/{cat['slug']}.html">
  <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/recipe.css">
</head>
<body>
{get_header_html(active_nav=cat['key'], depth="../")}

  <main class="container section-padding">
    <div style="max-width: 800px; margin-bottom: 2.5rem;">
      <a href="../recept.html" style="font-size: 0.875rem; color: var(--color-text-muted); font-weight: 600; display: inline-flex; align-items: center; gap: 0.35rem; margin-bottom: 0.75rem;">← Tillbaka till alla recept</a>
      <h1 class="hero-search-title-label" style="font-size: 2.8rem; margin-bottom: 0.5rem;">{cat['title']}</h1>
      <p style="color: var(--color-text-muted); font-size: 1.1rem; line-height: 1.6;">{cat['desc']}</p>
    </div>

    <div class="recipe-grid">
{cards_html}
    </div>
  </main>

{get_footer_html(depth="../")}

  <script src="../assets/js/recipe-engine.js"></script>
</body>
</html>'''

        with open(os.path.join(OUTPUT_CATEGORIES_DIR, f"{cat['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated category: {cat['slug']}.html")

def generate_sitemaps():
    from datetime import date
    today = str(date.today())
    
    xml_urls = []
    # Static pages
    xml_urls.append(f'''  <url>
    <loc>https://svenska-recept.se/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://svenska-recept.se/recept.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://svenska-recept.se/om-oss.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://svenska-recept.se/kontakt.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://svenska-recept.se/integritetspolicy.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>''')

    # Categories
    for c in CATEGORIES:
        xml_urls.append(f'''  <url>
    <loc>https://svenska-recept.se/kategorier/{c['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>''')

    # Recipes
    for r in RECIPES:
        xml_urls.append(f'''  <url>
    <loc>https://svenska-recept.se/recept/{r['file']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>''')

    sitemap_xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(xml_urls)}
</urlset>'''

    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml_content)
    with open(os.path.join(BASE_DIR, "sitemap_sv.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml_content)
    print("Generated dynamic sitemaps (sitemap.xml & sitemap_sv.xml)")

def main():
    for r in RECIPES:
        render_recipe_page(r)
    generate_homepage()
    generate_catalog()
    generate_categories()
    generate_sitemaps()

if __name__ == "__main__":
    main()
