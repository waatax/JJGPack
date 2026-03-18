import os
import glob
import re

def fix_product_page(path, is_zh=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix Asset Paths
    content = content.replace('href="/JJGPack/style.css"', 'href="/style.css"')
    content = content.replace('src="/JJGPack/main.js"', 'src="/main.js"')
    content = content.replace('src="/JJGPack/images/', 'src="/images/')
    content = content.replace('href="/JJGPack/images/favicon.ico"', 'href="/images/favicon.ico"')
    
    # Clean up double prefixes if any (especially from nav links)
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    
    # 2. Add Die Cut Bag
    if "Die Cut Handle Bag" not in content and "手提挖孔袋" not in content:
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
        
        # Insert into the first grid
        grid_pattern = r'(<div class="grid md:grid-cols-2 lg:grid-cols-4.*?>)'
        content = re.sub(grid_pattern, r'\1\n' + card, content, count=1)

    # 3. Add E-Catalog to Header
    news_link = "/JJGPack/zh-tw/news.html" if is_zh else "/JJGPack/news.html"
    cat_link = "/JJGPack/zh-tw/catalog.html" if is_zh else "/JJGPack/catalog.html"
    cat_text = "型錄EDM" if is_zh else "E-Catalog"
    
    if cat_link not in content:
        # Desktop
        content = re.sub(f'<a href="{news_link}".*?</a>', r'\g<0>\n                                <a href="' + cat_link + '" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">' + cat_text + '</a>', content)
        # Mobile (clean any previous)
        content = re.sub(f'<a href="{news_link}".*?</a>', r'\g<0>\n                                <a href="' + cat_link + '" class="block py-2 px-3 rounded hover:bg-[#F5F0E8]">' + cat_text + '</a>', content, count=1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_product_page('products.html', False)
fix_product_page('zh-tw/products.html', True)
print("Product pages updated.")
 Sands
