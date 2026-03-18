import os
import glob
import re

def fix_links_in_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Define the correct base
    CORRECT_BASE = "/JJGPack/"
    
    # 2. Fix href="/..."
    # Match href="/ but not href="/JJGPack/ and not href="http or href="# or href="tel or href="mailto
    content = re.sub(r'href="/(?!JJGPack/|https?://|#|tel:|mailto:)', f'href="{CORRECT_BASE}', content)
    
    # 3. Fix src="/..."
    # Match src="/ but not src="/JJGPack/ and not src="http
    content = re.sub(r'src="/(?!JJGPack/|https?://)', f'src="{CORRECT_BASE}', content)

    # 4. Clean up any lowercase or uppercase duplicates
    content = content.replace("/jjgpack/", CORRECT_BASE)
    content = content.replace("/JJGPACK/", CORRECT_BASE)
    
    # Avoid nested duplicates like /JJGPack/JJGPack/
    content = content.replace(f"{CORRECT_BASE}{CORRECT_BASE}", CORRECT_BASE)
    
    # 5. Fix specific JS strings if found in x-data or similar
    # e.g. activeImage: '/proimages/...'
    content = re.sub(r"(['\"])/ (?!JJGPack/|https?://)", r"\1" + CORRECT_BASE, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Get all HTML files
    html_files = glob.glob("**/*.html", recursive=True)
    for f in html_files:
        if "node_modules" in f or "dist" in f:
            continue
        fix_links_in_file(f)
    print("All HTML files updated with /JJGPack/ prefix.")

if __name__ == "__main__":
    main()
