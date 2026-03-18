import os
import re
import glob

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the pattern to find any occurrence of /JJGPack/ or /jjgpack/ that looks like a path prefix
    # This matches:
    # 1. /JJGPack/ at the beginning of a quoted string or attribute
    # 2. /JJGPack/ inside a JavaScript array or string
    # We use optional quotes around it.
    
    # Simple strategy: Replace all occurrences of "/JJGPack/" and "/jjgpack/" with "/"
    # BUT we should be careful about just "/" as it might result in //
    
    # Match "[/JJGPack/" or "'/JJGPack/" or "="/JJGPack/"
    # Actually, let's just replace all /JJGPack/ (case insensitive) with /
    # And then fix any resulting double slashes // 
    
    # 1. Standardize case-insensitive JJGPack prefix to /
    # We look for / prefixed with " or ' or = or [
    new_content = re.sub(r'([\"\'\=\[])/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', r'\1/', content)
    
    # 2. Also handle cases where it's at the start of a string in a template
    new_content = re.sub(r'\([\"\'\=\[])/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', r'\1/', new_content)

    # 3. Special fix for the Hero banner array in index.html which I saw earlier
    # "['/JJGPack/proimages/banner/..." 
    new_content = re.sub(r'([\'\"])/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', r'\1/', new_content)

    # 4. Final sweep: any /JJGPack/ -> /
    # Be careful not to replace something that isn't a path
    # But in this project, it's almost always a path
    new_content = re.sub(r'/[Jj][Jj][Gg][Pp][Aa][Cc][Kk]/', '/', new_content)

    # 5. Fix double slashes resulted from the above
    new_content = re.sub(r'//', '/', new_content)

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
