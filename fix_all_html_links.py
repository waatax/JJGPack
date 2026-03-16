import os
import re
import glob

def fix_links_in_content(content):
    # This script will REMOVE the manual /JJGPACK/ prefix from paths
    # and ensure they are absolute root-relative paths starting with /
    
    # 1. Remove manual prefix from src and href
    content = re.sub(r'href="/JJGPACK/([^"]*?)"', r'href="/\1"', content)
    content = re.sub(r'src="/JJGPACK/([^"]*?)"', r'src="/\1"', content)
    
    # 2. Handle specific root cases
    content = content.replace('href="/JJGPACK/"', 'href="/"')
    content = content.replace('href="/JJGPACK/index.html"', 'href="/index.html"')
    content = content.replace('href="/JJGPACK/zh-tw/"', 'href="/zh-tw/index.html"')
    
    # 3. Handle lowercase /jjgpack/
    content = content.replace('/jjgpack/', '/')
    
    # 4. Handle Alpine.js/JS strings in attributes
    content = content.replace("'/JJGPACK/", "'/")
    content = content.replace('"/JJGPACK/', '"/')
    
    # Simple strings in JS that might not be in quotes (less likely in HTML attributes but just in case)
    # content = content.replace(':/JJGPACK/', ':/') # e.g. :src="'/JJGPACK/images/...' "
    
    return content

def process_all_files():
    html_files = glob.glob("**/*.html", recursive=True)
    for file_path in html_files:
        if "node_modules" in file_path or "dist" in file_path:
            continue
            
        print(f"Processing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = fix_links_in_content(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Updated {file_path}")
        else:
            print(f"  No changes for {file_path}")

if __name__ == "__main__":
    process_all_files()
    print("Done cleaning up links in all HTML files.")
