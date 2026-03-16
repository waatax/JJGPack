import os
import re
import glob

def fix_links_in_content(content):
    # 1. Navigation links (.html, directories)
    # Ensure they HAVE /JJGPACK/ if they are local routes.
    content = re.sub(
        r'href="/(?!JJGPACK/|https?://|#)([^"]*?)"',
        r'href="/JJGPACK/\1"',
        content
    )

    # 2. Assets (Images, JS, CSS)
    # Ensure they HAVE /JJGPACK/ if they are local routes.
    content = re.sub(
        r'src="/(?!JJGPACK/|https?://)([^"]*?)"',
        r'src="/JJGPACK/\1"',
        content
    )
    
    # Specific fix for common asset hrefs (like style.css)
    content = re.sub(
        r'href="/(?!JJGPACK/|https?://|#)([^"]*?\.(?:css|js|ico|webmanifest))"',
        r'href="/JJGPACK/\1"',
        content
    )

    # 3. Clean up any double prefixes
    content = content.replace('/JJGPACK/JJGPACK/', '/JJGPACK/')
    content = content.replace('/JJGPACK/jjgpack/', '/JJGPACK/')
    content = content.replace('/jjgpack/', '/JJGPACK/')
    
    # Specific fix for root "/"
    content = content.replace('href="/JJGPACK/"', 'href="/JJGPACK/index.html"')
    content = content.replace('href="/JJGPACK/zh-tw/"', 'href="/JJGPACK/zh-tw/index.html"')

    # 4. Alpine.js / Hero Banners (images and proimages)
    # Ensure they have prefix
    content = re.sub(
        r"(['\"])/(images|proimages)/",
        r"\1/JJGPACK/\2/",
        content
    )
    # Again, clean up double prefix from the above
    content = content.replace('/JJGPACK/JJGPACK/', '/JJGPACK/')

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
    print("Done fixing links in all HTML files.")
