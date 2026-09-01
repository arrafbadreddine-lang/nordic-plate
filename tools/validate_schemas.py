#!/usr/bin/env python3
"""
Svenska Recept - Valideringsskript för Google Recipe Schema JSON-LD
Verifierar att samtliga receptfiler i recept/ uppfyller Google Search Centrals
obligatoriska och rekommenderade krav för Recipe Rich Snippets och Recipe Gallery.
"""

import os
import re
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECIPES_DIR = os.path.join(BASE_DIR, "recept")

REQUIRED_FIELDS = [
    "name",
    "image",
    "description",
    "recipeIngredient",
    "recipeInstructions"
]

RECOMMENDED_FIELDS = [
    "prepTime",
    "cookTime",
    "totalTime",
    "recipeYield",
    "recipeCategory",
    "recipeCuisine",
    "nutrition",
    "aggregateRating",
    "author",
    "publisher"
]

def validera_recept():
    if not os.path.exists(RECIPES_DIR):
        print(f"❌ Mappen {RECIPES_DIR} finns inte.")
        sys.exit(1)

    html_filer = [f for f in os.listdir(RECIPES_DIR) if f.endswith(".html")]
    if not html_filer:
        print(f"❌ Inga HTML-receptfiler hittades i {RECIPES_DIR}.")
        sys.exit(1)

    print(f"🔍 Validerar {len(html_filer)} svenska recept mot Googles Recipe Schema...\n")

    godkanda = 0
    felaktiga = 0

    for filnamn in sorted(html_filer):
        filvag = os.path.join(RECIPES_DIR, filnamn)
        with open(filvag, "r", encoding="utf-8") as f:
            innehall = f.read()

        # Extrahera JSON-LD
        match = re.search(r'<script type="application/ld\+json">(.*?)</script>', innehall, re.DOTALL)
        if not match:
            print(f"❌ [{filnamn}] Saknar JSON-LD script-tagg.")
            felaktiga += 1
            continue

        try:
            data = json.loads(match.group(1))
        except Exception as e:
            print(f"❌ [{filnamn}] Ogiltig JSON-syntax: {e}")
            felaktiga += 1
            continue

        # Kontrollera @context
        has_context = data.get("@context") == "https://schema.org" or data.get("@context") == "http://schema.org"

        # Hitta Recipe-noden
        recept_objekt = None
        if isinstance(data, dict):
            if data.get("@type") == "Recipe":
                recept_objekt = data
            elif "@graph" in data:
                for nod in data["@graph"]:
                    if nod.get("@type") == "Recipe":
                        recept_objekt = nod
                        break

        if not recept_objekt:
            print(f"❌ [{filnamn}] Inget objekt med @type: 'Recipe' hittades.")
            felaktiga += 1
            continue

        if not has_context and recept_objekt.get("@context") not in ["https://schema.org", "http://schema.org"]:
            print(f"❌ [{filnamn}] Saknar giltig @context: 'https://schema.org'")
            felaktiga += 1
            continue

        # Kontrollera obligatoriska fält
        saknade_obligatoriska = [f for f in REQUIRED_FIELDS if f not in recept_objekt]
        if saknade_obligatoriska:
            print(f"❌ [{filnamn}] Saknar obligatoriska fält: {saknade_obligatoriska}")
            felaktiga += 1
            continue

        # Kontrollera ingredienser
        ingredienser = recept_objekt.get("recipeIngredient", [])
        if not isinstance(ingredienser, list) or len(ingredienser) == 0:
            print(f"❌ [{filnamn}] recipeIngredient måste vara en icke-tom array.")
            felaktiga += 1
            continue

        # Kontrollera instruktioner
        instruktioner = recept_objekt.get("recipeInstructions", [])
        if not isinstance(instruktioner, list) or len(instruktioner) == 0:
            print(f"❌ [{filnamn}] recipeInstructions måste vara en icke-tom array.")
            felaktiga += 1
            continue

        # Kontrollera rekommenderade fält
        saknade_rekommenderade = [f for f in RECOMMENDED_FIELDS if f not in recept_objekt]
        rekommenderad_status = f"(Saknar: {', '.join(saknade_rekommenderade)})" if saknade_rekommenderade else "100% fullständig (Alla rekommenderade fält finns!)"

        print(f"✅ [{filnamn}] GODKÄND - {recept_objekt.get('name')} -> {rekommenderad_status}")
        godkanda += 1

    print("\n" + "=" * 70)
    print(f"📊 Sammanfattning: {godkanda}/{len(html_filer)} recept godkända med 100% giltig Google Schema.")
    print("=" * 70)

    if felaktiga > 0:
        sys.exit(1)

if __name__ == "__main__":
    validera_recept()
