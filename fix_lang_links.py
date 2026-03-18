import os
import re
import glob

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(file_path)
    is_zh = "zh-tw" in file_path
    
    # 1. Identify the language toggle block
    # It contains "EN" and "繁中" separated by a pipe |
    # We want to replace the hrefs inside it
    
    # Regex to find the EN link
    en_pattern = r'(<a\s+[^>]*?href=")[^"]*?("[^>]*?>EN</a>)'
    # Regex to find the ZH link
    zh_pattern = r'(<a\s+[^>]*?href=")[^"]*?("[^>]*?>繁中</a>)'
    
    # Determine correct paths
    if is_zh:
        target_en = f"/{filename}"
        target_zh = f"/zh-tw/{filename}"
    else:
        target_en = f"/{filename}"
        target_zh = f"/zh-tw/{filename}"
        
    # Apply fixes
    new_content = re.sub(en_pattern, rf'\1{target_en}\2', content)
    new_content = re.sub(zh_pattern, rf'\1{target_zh}\2', new_content)
    
    # 2. Also fix the active class if possible
    # For simplicity, we just ensure the links are correct.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Apply to all HTML files
html_files = glob.glob("**/*.html", recursive=True)
for f in html_files:
    if "node_modules" in f or "dist" in f:
        continue
    print(f"Fixing language links in {f}...")
    fix_file(f)

print("Done! Language links fixed.")
