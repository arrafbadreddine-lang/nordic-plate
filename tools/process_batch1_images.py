import os
import subprocess

BRAIN_DIR = "/Users/baderarraf/.gemini/antigravity/brain/03b4c143-5d4d-4e0d-b419-1de61d70b018"
OUT_DIR = "/Users/baderarraf/.gemini/antigravity/scratch/nordic-plate/assets/images/recept"

NEW_IMAGES = {
    "appelpaj": "knackig_appelpaj_macro_1787497236111.jpg",
    "korvstroganoff": "korv_stroganoff_macro_1787497268329.jpg",
    "flaskpannkaka": "flaskpannkaka_macro_1787497299545.jpg",
    "kantarellpaj": "kantarellpaj_macro_1787497335008.jpg"
}

for name, src_file in NEW_IMAGES.items():
    src_path = os.path.join(BRAIN_DIR, src_file)
    if not os.path.exists(src_path):
        print(f"Error: {src_path} does not exist!")
        continue
    
    # 1900x900 (High-res Full HD Hero)
    p_1900 = os.path.join(OUT_DIR, f"{name}-1900x900.jpg")
    subprocess.run(["sips", "-z", "900", "1900", "-s", "formatOptions", "82", src_path, "--out", p_1900], check=True, stdout=subprocess.DEVNULL)
    
    # 800x500 (Card)
    p_card = os.path.join(OUT_DIR, f"{name}.jpg")
    subprocess.run(["sips", "-z", "500", "800", "-s", "formatOptions", "80", src_path, "--out", p_card], check=True, stdout=subprocess.DEVNULL)
    
    # 16x9 (1200x675)
    p_16x9 = os.path.join(OUT_DIR, f"{name}-16x9.jpg")
    subprocess.run(["sips", "-z", "675", "1200", "-s", "formatOptions", "80", src_path, "--out", p_16x9], check=True, stdout=subprocess.DEVNULL)
    
    # 4x3 (1200x900)
    p_4x3 = os.path.join(OUT_DIR, f"{name}-4x3.jpg")
    subprocess.run(["sips", "-z", "900", "1200", "-s", "formatOptions", "80", src_path, "--out", p_4x3], check=True, stdout=subprocess.DEVNULL)
    
    # 1x1 (800x800)
    p_1x1 = os.path.join(OUT_DIR, f"{name}-1x1.jpg")
    subprocess.run(["sips", "-z", "800", "800", "-s", "formatOptions", "80", src_path, "--out", p_1x1], check=True, stdout=subprocess.DEVNULL)

    size_kb = os.path.getsize(p_1900) / 1024
    print(f"Exported {name} -> 1900x900 is {size_kb:.1f} KB (Full HD Crisp)")

print("Successfully exported all 4 new recipe images!")
