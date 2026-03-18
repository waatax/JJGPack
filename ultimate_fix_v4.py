import os
import re
import glob

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Standardize all types of path-like occurrences of /JJGPack/ (any case)
    # Match strings starting with "/JJGPack/" or attributes
    # We want to replace it with "/" 
    
    # Simple replace is usually safe in this project
    new_content = re.sub(r'/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', '/', content)
    
    # 2. Fix cases where /JJGPack was missed (e.g. at the end of a string without trailing /)
    # BUT wait, the directory is JJGPack.
    # So /JJGPack (no trailing /) could mean the folder.
    # If it's used in a URL, it should be / (root).
    
    # We'll use a safer approach for the end of the string.
    new_content = re.sub(r'([\'\"\=\[ \(])/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]([\'\"\] \)])', r'\1/\2', new_content)

    # 3. Standardize paths (no double slashes // unless it's http://)
    new_content = re.sub(r'(?<!:)/{2,}', '/', new_content)

    # 4. Special fix for the language toggle (again just in case)
    # If in root (EN), 繁中 should point to /zh-tw/current_file
    # If in zh-tw, EN should point to /current_file
    filename = os.path.basename(file_path)
    is_zh = "zh-tw" in file_path
    
    if is_zh:
        new_content = re.sub(r'<a href="#"([^>]*?)>EN</a>', f'<a href="/{filename}"\\1>EN</a>', new_content)
        new_content = re.sub(r'<a href="#"([^>]*?)>繁中</a>', f'<a href="/zh-tw/{filename}"\\1>繁中</a>', new_content)
    else:
        new_content = re.sub(r'<a href="#"([^>]*?)>繁中</a>', f'<a href="/zh-tw/{filename}"\\1>繁中</a>', new_content)
        new_content = re.sub(r'<a href="#"([^>]*?)>EN</a>', f'<a href="/{filename}"\\1>EN</a>', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Apply to all HTML and JS files
files = glob.glob("**/*.html", recursive=True) + glob.glob("**/*.js", recursive=True)
for f in files:
    if "node_modules" in f or "dist" in f:
        continue
    print(f"Aggressively fixing {f}...")
    fix_file(f)

print("Done! Aggressive fix applied.")
