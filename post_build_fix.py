import os
import re
import glob
import sys

def fix_links_in_content(content, base_path='/JJGPACK'):
    # This script adds the base_path prefix to absolute internal links and assets.
    # It avoids double-prefixing.
    
    # 1. Navigation links and assets that start with / but NOT with base_path or http
    # We use a negative lookahead to exclude base_path, http, etc.
    # Regex: (href|src)="/(?!base_path/|https?://|#)([^"]*?)"
    
    # Escape base_path for regex if needed, but JJGPACK is simple
    bp = base_path.strip('/')
    
    # Fix src and href
    content = re.sub(
        r'(href|src)="/(?!' + bp + r'/|https?://|#)([^"]*?)"',
        r'\1="/' + bp + r'/\2"',
        content
    )
    
    # 2. Handle specific root cases
    content = content.replace('href="/"', f'href="/{bp}/index.html"')
    content = content.replace('href="/zh-tw/"', f'href="/{bp}/zh-tw/index.html"')
    
    # 3. Handle Alpine.js strings in arrays
    # Look for '/proimages/ or '/images/ or '/main.js' etc.
    content = re.sub(
        r"(['\"])/(?!' + bp + r'/|https?://|#)(images/|proimages/|main\.js|style\.css)([^'\"]*?)(['\"])",
        r"\1/" + bp + r"/\2\3\4",
        content
    )
    
    return content

def process_directory(directory):
    html_files = glob.glob(os.path.join(directory, "**/*.html"), recursive=True)
    for file_path in html_files:
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
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    process_directory(target_dir)
    print(f"Done fixing links in {target_dir}.")
