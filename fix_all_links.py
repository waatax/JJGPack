import os
import re

BASE_OLD = r'href="/'
BASE_NEW = 'href="/jjgpack/'
SRC_OLD = r'src="/'
SRC_NEW = 'src="/jjgpack/'

def fix_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Navigation links (.html or root folders) need the /jjgpack/ prefix.
    # But ONLY if they don't already have it.
    content = re.sub(r'href="/(?!jjgpack/|https?://|#)([^"]*\.html|zh-tw/|(?:"|\'))', r'href="/jjgpack/\2', content)
    
    # Special case for root links that might have been partially fixed
    content = re.sub(r'href="/jjgpack/jjgpack/', 'href="/jjgpack/', content)
    
    # 2. Assets (css, js, images) should NOT have the /jjgpack/ prefix.
    # Vite will add it automatically during build/dev if base is set.
    content = re.sub(r'href="/jjgpack/([^"]+\.(?:css|js|ico|webmanifest))"', r'href="/\1"', content)
    content = re.sub(r'src="/jjgpack/([^"]+)"', r'src="/\1"', content)
    # Ensure images/favicons etc are root-relative for Vite to process
    content = re.sub(r'src="/(?!jjgpack/)', 'src="/', content) # Ensure it starts with /
    content = re.sub(r'href="/(?!jjgpack/)([^"]+\.(?:css|js|ico))"', r'href="/\1"', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Main pages to fix
main_pages = [
    'index.html', 'about.html', 'products.html', 'news.html', 'contact.html',
    'zh-tw/index.html', 'zh-tw/about.html', 'zh-tw/products.html', 'zh-tw/news.html', 'zh-tw/contact.html'
]

for p in main_pages:
    abs_p = os.path.join(os.getcwd(), p)
    if os.path.exists(abs_p):
        fix_links(abs_p)
        print(f"Fixed links in {p}")

print("Internal links standardized to include /jjgpack/ base path.")
