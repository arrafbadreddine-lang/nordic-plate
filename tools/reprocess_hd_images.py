import os
import subprocess

BRAIN_DIR = "/Users/baderarraf/.gemini/antigravity/brain/03b4c143-5d4d-4e0d-b419-1de61d70b018"
OUT_DIR = "/Users/baderarraf/.gemini/antigravity/scratch/nordic-plate/assets/images/recept"

os.makedirs(OUT_DIR, exist_ok=True)

IMAGE_MAP = {
    "kladdkaka": "swedish_kladdkaka_1787398429101.jpg",
    "kottbullar": "swedish_meatballs_1787398453695.jpg",
    "kanelbullar": "swedish_kanelbullar_1787398472128.jpg",
    "vasterbotten": "vasterbottensost_paj_1787398492329.jpg",
    "skagen": "toast_skagen_1787398528471.jpg",
    "wallenbergare": "swedish_wallenbergare_1787398552099.jpg",
    "raggmunk": "swedish_raggmunk_1787398682366.jpg",
    "janssons": "janssons_frestelse_1787398716113.jpg",
    "gravlax": "gravad_lax_1787398752122.jpg",
    "tosca": "swedish_toscakaka_1787398897599.jpg",
    "semlor": "swedish_semlor_1787398990265.jpg",
    "lingon": "rarorda_lingon_1787399029328.jpg",
    "laxsoppa": "macro_laxsoppa_melted_1787436912574.jpg",
    "karleksmums": "macro_karleksmums_melted_1787436960201.jpg",
    "flygande-jacob": "macro_flygande_jacob_melted_1787437020760.jpg",
    "kalops": "macro_kalops_melted_1787437078512.jpg"
}

for name, src_file in IMAGE_MAP.items():
    src_path = os.path.join(BRAIN_DIR, src_file)
    if not os.path.exists(src_path):
        print(f"Warning: {src_path} does not exist!")
        continue
    
    # 1. Full HD Discover Hero (1900x900) - High Quality (82)
    p_1900 = os.path.join(OUT_DIR, f"{name}-1900x900.jpg")
    subprocess.run(["sips", "-z", "900", "1900", "-s", "formatOptions", "82", src_path, "--out", p_1900], check=True, stdout=subprocess.DEVNULL)
    
    # 2. Main Card Image (800x500)
    p_main = os.path.join(OUT_DIR, f"{name}.jpg")
    subprocess.run(["sips", "-z", "500", "800", "-s", "formatOptions", "80", src_path, "--out", p_main], check=True, stdout=subprocess.DEVNULL)
    
    # 3. 16x9 Schema Image (1200x675)
    p_16x9 = os.path.join(OUT_DIR, f"{name}-16x9.jpg")
    subprocess.run(["sips", "-z", "675", "1200", "-s", "formatOptions", "80", src_path, "--out", p_16x9], check=True, stdout=subprocess.DEVNULL)
    
    # 4. 4x3 Schema Image (1200x900)
    p_4x3 = os.path.join(OUT_DIR, f"{name}-4x3.jpg")
    subprocess.run(["sips", "-z", "900", "1200", "-s", "formatOptions", "80", src_path, "--out", p_4x3], check=True, stdout=subprocess.DEVNULL)
    
    # 5. 1x1 Schema Image (800x800)
    p_1x1 = os.path.join(OUT_DIR, f"{name}-1x1.jpg")
    subprocess.run(["sips", "-z", "800", "800", "-s", "formatOptions", "80", src_path, "--out", p_1x1], check=True, stdout=subprocess.DEVNULL)
    
    size_kb = os.path.getsize(p_1900) / 1024
    print(f"Processed {name}: Full HD 1900x900 is {size_kb:.1f} KB (Crystal Clear)")

print("All 16 recipe image sets re-processed to Full HD crisp quality successfully!")
