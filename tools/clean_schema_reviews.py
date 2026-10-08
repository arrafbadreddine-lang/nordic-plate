#!/usr/bin/env python3
"""
clean_schema_reviews.py
Removes hardcoded aggregateRating JSON-LD schema blocks across all recipe HTML files in recept/.
Ensures structured data strictly complies with Google's Search Essentials and eliminates algorithmic review spam flags.
"""

import os
import re
import json

RECIPES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recept")
PATTERN = re.compile(
    r'\n\s*\"aggregateRating\":\s*\{\s*\"@type\":\s*\"AggregateRating\".*?\},(?=\s*\n\s*\"recipeIngredient\")',
    re.DOTALL
)

def clean_all_recipes():
    if not os.path.exists(RECIPES_DIR):
        raise FileNotFoundError(f"Directory {RECIPES_DIR} not found.")

    files = [f for f in sorted(os.listdir(RECIPES_DIR)) if f.endswith(".html")]
    print(f"Processing {len(files)} recipe files in {RECIPES_DIR}...")

    cleaned_count = 0
    error_count = 0

    for filename in files:
        filepath = os.path.join(RECIPES_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if PATTERN.search(content):
            new_content = PATTERN.sub("", content)

            # Validate JSON-LD syntax
            match = re.search(r'<script type="application/ld\+json">(.*?)</script>', new_content, re.DOTALL)
            if not match:
                print(f"❌ Error: No JSON-LD block found in {filename}")
                error_count += 1
                continue

            try:
                data = json.loads(match.group(1))
                # Verify Recipe schema still exists and has required fields
                recipe_node = None
                for node in data.get("@graph", []):
                    if node.get("@type") == "Recipe":
                        recipe_node = node
                        break

                if not recipe_node:
                    print(f"❌ Error: No Recipe node in @graph for {filename}")
                    error_count += 1
                    continue

                if "aggregateRating" in recipe_node:
                    print(f"❌ Error: aggregateRating still present in {filename}")
                    error_count += 1
                    continue

                for req in ["name", "image", "recipeIngredient", "recipeInstructions"]:
                    if req not in recipe_node:
                        print(f"❌ Error: Missing required field '{req}' in {filename}")
                        error_count += 1
                        continue

            except json.JSONDecodeError as e:
                print(f"❌ JSON parse error in {filename}: {e}")
                error_count += 1
                continue

            # Write clean content
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            cleaned_count += 1
        else:
            print(f"⚠️ Notice: aggregateRating pattern not found in {filename}")

    print(f"\n=======================================================")
    print(f"✅ Successfully cleaned {cleaned_count}/{len(files)} recipe files.")
    print(f"❌ Errors: {error_count}")
    print(f"=======================================================")

if __name__ == "__main__":
    clean_all_recipes()
