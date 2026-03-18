import os
import glob
import re

def fix_content(content):
    # 1. Fix the mangled title tag (THE MOST CRITICAL FIX)
    # Search for anything matching <title>... title> and replace with clean standard title
    content = re.sub(r'<title>.*?(</title>|(?<!<)/title>)', '<title>JJG Pack | Professional Paper Bag Manufacturer - 壯佳果包裝</title>', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Fix the broken footer tag
    content = content.replace('footer class="bg-[#1A1A1A]', '<footer class="bg-[#1A1A1A]')
    
    # 3. Fix the Mojibake in description (optional but good)
    content = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="壯佳果股份有限公司 — Professional paper bag manufacturer in Taiwan with 70+ years of experience. PFAS-free, eco-friendly packaging solutions." />', content, flags=re.DOTALL)

    # 4. Handle Asset paths correctly
    # If Vite is doubling the prefix, we should try using root-relative paths WITHOUT the prefix
    # BUT let's try just standardizing them first.
    
    # Clean up double prefixes
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/jjgpack/jjgpack/", "/JJGPack/")
    
    return content

def main():
    paths = glob.glob("**/*.html", recursive=True)
    for p in paths:
        if "node_modules" in p or "dist" in p: continue
        print(f"Fixing {p}...")
        try:
            with open(p, 'r', encoding='utf-8') as f: content = f.read()
        except:
            with open(p, 'r', encoding='latin-1') as f: content = f.read()
            
        new_content = fix_content(content)
        
        with open(p, 'w', encoding='utf-8') as f: f.write(new_content)
    print("Optimization and fixes applied.")

if __name__ == "__main__": main()
