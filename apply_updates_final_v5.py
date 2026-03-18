import os
import glob
import re

def fix_links(content):
    # This script ensures everything starts with /JJGPack/
    # And absolutely prevents double /JJGPack/JJGPack/
    
    # 1. Navigation / Assets
    # Matches href="/... or src="/... but not external or anchors
    content = re.sub(r'(href|src)="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?)(\.html|/|(?:"|\')|(?:\.(?:css|js|ico|png|jpg|jpeg|svg|pdf)))', r'\1="/JJGPack/\2\3', content)
    
    # 2. Alpine image strings (hero banners)
    content = re.sub(r"(['\"])/(?!JJGPack/|https?://)(images/|proimages/)([^'\"]*?)(\1)", r"\1/JJGPack/\2\3\4", content)
    
    # 3. Clean up any accidental double prefixes (global replacement)
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/jjgpack/", "/JJGPack/")
    content = content.replace("/JJGPack//", "/JJGPack/")
    
    return content

def update_header(content, is_zh=False):
    # Update Desktop Nav
    if is_zh:
        new_nav = '''      <div class="hidden lg:flex items-center gap-1">
        <a href="/JJGPack/zh-tw/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">首頁</a>
        <a href="/JJGPack/zh-tw/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">關於我們</a>
        <a href="/JJGPack/zh-tw/products.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">產品介紹</a>
        <a href="/JJGPack/zh-tw/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">最新消息</a>
        <a href="/JJGPack/zh-tw/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">型錄EDM</a>
        <a href="/JJGPack/zh-tw/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">聯絡我們</a>
      </div>'''
    else:
        new_nav = '''      <div class="hidden lg:flex items-center gap-1">
        <a href="/JJGPack/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Home</a>
        <a href="/JJGPack/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">About Us</a>
        <a href="/JJGPack/products.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Products</a>
        <a href="/JJGPack/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">News</a>
        <a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>
        <a href="/JJGPack/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Contact</a>
      </div>'''
    
    # Replace the desktop nav block
    content = re.sub(r'<div class="hidden lg:flex items-center gap-1">.*?</div>', new_nav, content, flags=re.DOTALL)
    
    # Update Mobile Nav
    if is_zh:
        mobile_links = '''        <a href="/JJGPack/zh-tw/index.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">首頁</a>
        <a href="/JJGPack/zh-tw/about.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">關於我們</a>
        <a href="/JJGPack/zh-tw/products.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">產品介紹</a>
        <a href="/JJGPack/zh-tw/news.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">最新消息</a>
        <a href="/JJGPack/zh-tw/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">型錄EDM</a>
        <a href="/JJGPack/zh-tw/contact.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">聯絡我們</a>'''
    else:
        mobile_links = '''        <a href="/JJGPack/index.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">Home</a>
        <a href="/JJGPack/about.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">About Us</a>
        <a href="/JJGPack/products.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">Products</a>
        <a href="/JJGPack/news.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">News</a>
        <a href="/JJGPack/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">E-Catalog</a>
        <a href="/JJGPack/contact.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">Contact</a>'''

    # Replace the mobile link list block (usually inside <div class="px-6 py-5 space-y-1">)
    content = re.sub(r'<div class="px-6 py-5 space-y-1">.*?</div>', '<div class="px-6 py-5 space-y-1">\n' + mobile_links + '\n      </div>', content, flags=re.DOTALL)
    
    return content

def add_die_cut_bag(content, is_zh=False):
    if "Die Cut Handle Bag" in content or "手提挖孔袋" in content: return content
    
    card = f"""        <!-- Die Cut Handle Bag -->
        <div class="bg-white rounded-2xl overflow-hidden shadow-premium card-hover group" data-reveal-child>
          <div class="aspect-[4/3] overflow-hidden img-overlay">
            <img src="https://www.jjgpaperbag.com/proimages/sr/product/DieCut_Bag/DM4.jpg" alt="Die Cut Handle Bag" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <div class="p-7">
            <span class="inline-block text-xs font-bold uppercase tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-3">Recycled Kraft</span>
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-2 group-hover:text-[#1A5C38] transition">{"Die Cut Handle Bag" if not is_zh else "手提挖孔袋"}</h3>
            <p class="text-sm text-[#666] mb-5">{"Ideal for groceries and takeaway orders, featuring die-cut handles for stability and easy carrying." if not is_zh else "適用於雜貨和外賣訂單，採用模切手柄，穩定且易於攜帶。"}</p>
            <a href="https://www.jjgpaperbag.com/product-Die-Cut-Handle-paper-bag-brown-kraft-6.html" target="_blank" class="inline-flex items-center gap-2 text-[#1A5C38] font-bold text-sm group-hover:gap-3 transition-all">
              {"View Details" if not is_zh else "查看詳情"}
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
            </a>
          </div>
        </div>"""
    
    # Insert at the end of the product grid
    grid_matches = list(re.finditer(r'<div class="grid md:grid-cols-2 lg:grid-cols-4.*?>', content))
    if grid_matches:
        # We want the main product grid, which usually contains 'Products' somewhere before it.
        # For simplicity, we'll append to the first large grid found in products.html
        target = grid_matches[0]
        # Find the closing </div> of this grid
        depth = 0
        start_idx = target.end()
        for i in range(start_idx, len(content)):
            if content[i:i+5] == '<div ': depth += 1
            if content[i:i+6] == '</div>':
                if depth == 0:
                    content = content[:i] + card + content[i:]
                    break
                depth -= 1
    return content

def main():
    html_files = glob.glob("**/*.html", recursive=True)
    for f in html_files:
        if "node_modules" in f or "dist" in f: continue
        try:
            with open(f, 'r', encoding='utf-8') as fh: content = fh.read()
        except:
            with open(f, 'r', encoding='latin-1') as fh: content = fh.read()
        
        is_zh = "zh-tw" in f
        content = update_header(content, is_zh)
        if "products.html" in f:
            content = add_die_cut_bag(content, is_zh)
        
        content = fix_links(content)
        
        with open(f, 'w', encoding='utf-8') as fh: fh.write(content)
    print("Done.")

if __name__ == "__main__": main()
