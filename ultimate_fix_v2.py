import os
import re
import glob

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove doubled or hardcoded base path /JJGPack/ and /jjgpack/
    # We want to change it to / so Vite can handle it
    content = re.sub(r'(src|href)="/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', r'\1="/', content)
    
    # 2. Fix language toggles that are href="#"
    # If in root (EN), 繁中 should point to /zh-tw/current_file
    # If in zh-tw, EN should point to /current_file
    filename = os.path.basename(file_path)
    is_zh = "zh-tw" in file_path
    
    if is_zh:
        # We are in zh-tw, fix EN link
        content = re.sub(r'<a href="#"([^>]*?)>EN</a>', f'<a href="/{filename}"\\1>EN</a>', content)
        # Fix the active state for ZH if it's #
        content = re.sub(r'<a href="#"([^>]*?)>繁中</a>', f'<a href="/zh-tw/{filename}"\\1>繁中</a>', content)
    else:
        # We are in EN, fix ZH link
        content = re.sub(r'<a href="#"([^>]*?)>繁中</a>', f'<a href="/zh-tw/{filename}"\\1>繁中</a>', content)
        # Fix the active state for EN if it's #
        content = re.sub(r'<a href="#"([^>]*?)>EN</a>', f'<a href="/{filename}"\\1>EN</a>', content)

    # 3. Special case for footer links if they were missed
    content = re.sub(r'href="/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', 'href="/', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to all HTML files
html_files = glob.glob("**/*.html", recursive=True)
for f in html_files:
    if "node_modules" in f or "dist" in f:
        continue
    print(f"Fixing {f}...")
    fix_file(f)

print("Done! All paths standardized to root-relative for Vite.")
