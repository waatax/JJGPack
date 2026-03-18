import os
import re

def fix_zh_nav(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine which link should be active
    filename = os.path.basename(file_path)
    active_page = None
    if 'index.html' in filename:
        active_page = 'index'
    elif 'about.html' in filename:
        active_page = 'about'
    elif 'products.html' in filename:
        active_page = 'products'
    elif 'news.html' in filename:
        active_page = 'news'
    elif 'catalog.html' in filename:
        active_page = 'catalog'
    elif 'contact.html' in filename:
        active_page = 'contact'

    active_cls = 'relative px-4 py-2 text-[#1A5C38] font-semibold text-[15px] after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-5 after:h-0.5 after:bg-[#1A5C38] after:rounded-full'
    inactive_cls = 'px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all'

    def get_cls(page):
        return active_cls if active_page == page else inactive_cls

    new_nav = f'''<div class="hidden lg:flex items-center gap-1">
                                <a href="/zh-tw/index.html" class="{get_cls('index')}">首頁</a>
                                <a href="/zh-tw/about.html" class="{get_cls('about')}">關於我們</a>
                                <a href="/zh-tw/products.html" class="{get_cls('products')}">產品介紹</a>
                                <a href="/zh-tw/news.html" class="{get_cls('news')}">最新消息</a>
                                <a href="/zh-tw/catalog.html" class="{get_cls('catalog')}">型錄EDM</a>
                                <a href="/zh-tw/contact.html" class="{get_cls('contact')}">聯絡我們</a>
                        </div>'''

    # Find the nav container. It might have gap-1 or gap-8 or similar.
    pattern = r'<div class="hidden lg:flex items-center gap-[0-9]+">.*?</div>'
    
    # We need to find the one that contains Japanese/Chinese characters to avoid touching the EN one if it somehow matches
    # But we are only iterating over zh-tw files.
    
    # Let's be more specific to matching the links inside
    matches = list(re.finditer(pattern, content, re.DOTALL))
    if not matches:
        print(f"Skipping {file_path}: No nav pattern found")
        return

    # Replace the first instance (the main desktop nav)
    new_content = content[:matches[0].start()] + new_nav + content[matches[0].end():]
    
    # Also fix the mobile nav icons if needed, but the user specifically asked for "TAG" (nav items) and "Keep interval" (spacing)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

# Run on all Chinese pages
zh_files = [
    'zh-tw/index.html',
    'zh-tw/about.html',
    'zh-tw/products.html',
    'zh-tw/news.html',
    'zh-tw/catalog.html',
    'zh-tw/contact.html'
]

# Also handle nested products
import glob
zh_product_files = glob.glob('zh-tw/products/**/*.html', recursive=True)
zh_files.extend(zh_product_files)

for f in zh_files:
    if os.path.exists(f):
        fix_zh_nav(f)
    else:
        print(f"Warning: {f} not found")
