import os
import glob
import re

def repair(content, is_zh=False):
    # 1. Fix Hash Assets to Source Assets
    content = re.sub(r'<script type="module" crossorigin src="/JJGPack/assets/main-.*?\.js"></script>', '<script type="module" src="/main.js"></script>', content)
    content = re.sub(r'<link rel="stylesheet" crossorigin href="/JJGPack/assets/style-.*?\.css">', '<link rel="stylesheet" href="/style.css">', content)
    
    # 2. Fix Double Brackets / Syntax
    content = content.replace('<<title>', '<title>')
    content = content.replace('<<footer', '<footer')
    
    # 3. Ensure Header/Footer standard links
    # Re-apply the nav logic one last time but purely on the strings
    links = '''        <a href="/JJGPack/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Home</a>
        <a href="/JJGPack/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">About Us</a>
        <a href="/JJGPack/products.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Products</a>
        <a href="/JJGPack/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">News</a>
        <a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>
        <a href="/JJGPack/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Contact</a>'''
    if is_zh:
        links = links.replace('index.html', 'zh-tw/index.html').replace('about.html', 'zh-tw/about.html').replace('products.html', 'zh-tw/products.html').replace('news.html', 'zh-tw/news.html').replace('catalog.html', 'zh-tw/catalog.html').replace('contact.html', 'zh-tw/contact.html')
        links = links.replace('Home', '首頁').replace('About Us', '關於我們').replace('Products', '產品介紹').replace('News', '最新消息').replace('E-Catalog', '型錄EDM').replace('Contact', '聯絡我們')

    content = re.sub(r'<div class="hidden lg:flex items-center gap-1">.*?</div>', '<div class="hidden lg:flex items-center gap-1">\n' + links + '\n      </div>', content, flags=re.DOTALL)
    
    # 4. Global Link Standardizer
    # For dev, we'll try using root-relative paths for EVERYTHING (starting with /)
    # BUT we must have /JJGPack/ for links that are NOT handled by Vite (external or routing)
    # Actually, let's keep /JJGPack/ for internal .html links.
    
    return content

def main():
    for p in glob.glob("**/*.html", recursive=True):
        if "node_modules" in p or "dist" in p: continue
        print(f"Repairing {p}...")
        try:
            with open(p, 'r', encoding='utf-8') as f: content = f.read()
        except: continue
        
        new_content = repair(content, "zh-tw" in p)
        with open(p, 'w', encoding='utf-8') as f: f.write(new_content)
    print("Repair complete.")

if __name__ == "__main__": main()
