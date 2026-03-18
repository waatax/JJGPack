import os
import glob
import re

def final_sweep(path):
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_zh = "zh-tw" in path

    # 1. Assets
    content = content.replace('href="/JJGPack/style.css"', 'href="/style.css"')
    content = content.replace('src="/JJGPack/main.js"', 'src="/main.js"')
    content = content.replace('src="/JJGPack/images/', 'src="/images/')
    content = content.replace('href="/JJGPack/images/favicon.ico"', 'href="/images/favicon.ico"')
    
    # Clean double prefix
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    
    # 2. Add E-Catalog to Header if missing
    news_link = "/JJGPack/zh-tw/news.html" if is_zh else "/JJGPack/news.html"
    cat_link = "/JJGPack/zh-tw/catalog.html" if is_zh else "/JJGPack/catalog.html"
    cat_text = "型錄EDM" if is_zh else "E-Catalog"
    
    if cat_link not in content:
        # Desktop
        content = re.sub(f'<a href="{news_link}".*?</a>', r'\g<0>\n                                <a href="' + cat_link + '" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">' + cat_text + '</a>', content)
        # Mobile
        content = re.sub(f'<a href="{news_link}".*?</a>', r'\g<0>\n                                <a href="' + cat_link + '" class="block py-2 px-3 rounded hover:bg-[#F5F0E8]">' + cat_text + '</a>', content, count=1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

pages = ['about.html', 'news.html', 'contact.html', 'zh-tw/about.html', 'zh-tw/news.html', 'zh-tw/contact.html']
for p in pages:
    final_sweep(p)
print("Final sweep complete.")
