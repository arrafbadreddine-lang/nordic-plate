import os
import subprocess
import shutil

BRAIN_DIR = "/Users/baderarraf/.gemini/antigravity/brain/03b4c143-5d4d-4e0d-b419-1de61d70b018"
OUT_DIR = "/Users/baderarraf/.gemini/antigravity/scratch/nordic-plate/assets/images/recept"
os.makedirs(OUT_DIR, exist_ok=True)

BATCH27_IMAGES = {
    "raggmunk-i-langpanna": "raggmunk_langpanna_macro_1790929074070.jpg",
    "tunna-pannkakor": "tunna_pannkakor_macro_1790949586045.jpg",
    "svampstuvning": "svampstuvning_macro_1790949628230.jpg",
    "champinjonsoppa": "champinjonsoppa_macro_1790949655619.jpg"
}

TMP_DIR = "/tmp/batch27_crop"
os.makedirs(TMP_DIR, exist_ok=True)

for name, src_file in BATCH27_IMAGES.items():
    src_path = os.path.join(BRAIN_DIR, src_file)
    if not os.path.exists(src_path):
        print(f"Error: {src_path} does not exist!")
        continue

    print(f"\nProcessing {name} from {src_file}...")

    # 1. 1900x900 (High-res Full HD Hero, aspect 19:9 ~ 2.11)
    # Native is 1376x768. Height needed: 1376 * 900 / 1900 = 652
    t_1900 = os.path.join(TMP_DIR, f"{name}_1900.jpg")
    shutil.copy2(src_path, t_1900)
    subprocess.run(["sips", "-c", "652", "1376", t_1900], check=True, stdout=subprocess.DEVNULL)
    p_1900 = os.path.join(OUT_DIR, f"{name}-1900x900.jpg")
    subprocess.run(["sips", "-z", "900", "1900", "-s", "formatOptions", "82", t_1900, "--out", p_1900], check=True, stdout=subprocess.DEVNULL)

    # 2. 800x500 (Card Image, aspect 1.6:1)
    # Target width for 768 height: 768 * 1.6 = 1228
    t_card = os.path.join(TMP_DIR, f"{name}_card.jpg")
    shutil.copy2(src_path, t_card)
    subprocess.run(["sips", "-c", "768", "1228", t_card], check=True, stdout=subprocess.DEVNULL)
    p_card = os.path.join(OUT_DIR, f"{name}.jpg")
    subprocess.run(["sips", "-z", "500", "800", "-s", "formatOptions", "80", t_card, "--out", p_card], check=True, stdout=subprocess.DEVNULL)

    # 3. 16x9 (1200x675) - Native is already 16:9
    p_16x9 = os.path.join(OUT_DIR, f"{name}-16x9.jpg")
    subprocess.run(["sips", "-z", "675", "1200", "-s", "formatOptions", "80", src_path, "--out", p_16x9], check=True, stdout=subprocess.DEVNULL)

    # 4. 4x3 (1200x900, aspect 1.333:1)
    # Target width for 768 height: 768 * 4 / 3 = 1024
    t_4x3 = os.path.join(TMP_DIR, f"{name}_4x3.jpg")
    shutil.copy2(src_path, t_4x3)
    subprocess.run(["sips", "-c", "768", "1024", t_4x3], check=True, stdout=subprocess.DEVNULL)
    p_4x3 = os.path.join(OUT_DIR, f"{name}-4x3.jpg")
    subprocess.run(["sips", "-z", "900", "1200", "-s", "formatOptions", "80", t_4x3, "--out", p_4x3], check=True, stdout=subprocess.DEVNULL)

    # 5. 1x1 (800x800, aspect 1:1)
    # Target width for 768 height: 768
    t_1x1 = os.path.join(TMP_DIR, f"{name}_1x1.jpg")
    shutil.copy2(src_path, t_1x1)
    subprocess.run(["sips", "-c", "768", "768", t_1x1], check=True, stdout=subprocess.DEVNULL)
    p_1x1 = os.path.join(OUT_DIR, f"{name}-1x1.jpg")
    subprocess.run(["sips", "-z", "800", "800", "-s", "formatOptions", "80", t_1x1, "--out", p_1x1], check=True, stdout=subprocess.DEVNULL)

    size_kb = os.path.getsize(p_1900) / 1024
    print(f"Exported {name} -> 1900x900 is {size_kb:.1f} KB (Full HD Crisp, no distortion)")

shutil.rmtree(TMP_DIR, ignore_errors=True)
print("\nSuccessfully processed all 4 Batch 27 recipe images into 20 responsive crops!")
