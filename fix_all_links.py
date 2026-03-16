import os
import re

BASE_OLD = r'href="/'
BASE_NEW = 'href="/jjgpack/'
SRC_OLD = r'src="/'
SRC_NEW = 'src="/jjgpack/'

def fix_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Prefix links with /jjgpack/ if they aren't already
    # We look for href="/ and make sure it's not href="/jjgpack/
    content = re.sub(r'href="/(?!jjgpack/)', 'href="/jjgpack/', content)
    # Same for images
    content = re.sub(r'src="/(?!jjgpack/)', 'src="/jjgpack/', content)
    
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
