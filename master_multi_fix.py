import os
import glob
import re

def master_fix(file_path):
    print(f"Fixing {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_zh = "zh-tw" in file_path.lower()
    
    # 1. Path Fixes (Removing redundant /JJGPack/ for assets)
    # Vite with base: '/JJGPack/' will automatically prefix root-relative paths.
    # So /style.css -> /JJGPack/style.css
    # But /JJGPack/style.css -> /JJGPack/JJGPack/style.css (WRONG)
    
    content = content.replace('href="/JJGPack/style.css"', 'href="/style.css"')
    content = content.replace('src="/JJGPack/main.js"', 'src="/main.js"')
    content = content.replace('href="/JJGPack/images/favicon.ico"', 'href="/images/favicon.ico"')
    
    # Images
    content = content.replace('src="/JJGPack/images/', 'src="/images/')
    content = content.replace('src="/JJGPack/proimages/', 'src="/proimages/')
    
    # Clean up double prefixes in links just in case
    content = content.replace('/JJGPack/JJGPack/', '/JJGPack/')
    
    # 2. Navigation Update (Headers)
    # Desktop Nav
    news_link = "/JJGPack/zh-tw/news.html" if is_zh else "/JJGPack/news.html"
    cat_link = "/JJGPack/zh-tw/catalog.html" if is_zh else "/JJGPack/catalog.html"
    cat_text = "型錄EDM" if is_zh else "E-Catalog"
    
    if cat_link not in content:
        # Insert after News link
        # Desktop
        pattern_en = r'(<a href="/JJGPack/news.html".*?>News</a>)'
        pattern_zh = r'(<a href="/JJGPack/zh-tw/news.html".*?>最新消息</a>)'
        
        if is_zh:
            content = re.sub(pattern_zh, r'\1\n                                <a href="' + cat_link + '" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">' + cat_text + '</a>', content)
        else:
            content = re.sub(pattern_en, r'\1\n                                <a href="' + cat_link + '" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">' + cat_text + '</a>', content)

        # Mobile
        content = re.sub(f'<a href="{news_link}".*?</a>', r'\g<0>\n                                <a href="' + cat_link + '" class="block py-2 px-3 rounded hover:bg-[#F5F0E8]">' + cat_text + '</a>', content, count=1)

    # 3. Highlight active link in header for Catalog page
    if "catalog.html" in file_path.lower():
        # Untag other active links (like About Us which might have been the template)
        content = content.replace('text-[#1A5C38] font-semibold text-[15px]', 'text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition')
        # Tag E-Catalog as active
        content = content.replace(f'href="{cat_link}" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition"', f'href="{cat_link}" class="text-[#1A5C38] font-semibold text-[15px]"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Run on all HTML files
html_files = glob.glob("**/*.html", recursive=True)
for f in html_files:
    if "node_modules" in f or "dist" in f: continue
    master_fix(f)

print("Master multi-path fix completed.")
