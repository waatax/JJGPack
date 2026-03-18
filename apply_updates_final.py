import os
import glob
import re

def fix_links_in_content(content):
    CORRECT_BASE = "/JJGPack/"
    # 1. Navigation links
    content = re.sub(r'href="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?\.html|[^"]*?/|(?:"|\'))', r'href="/JJGPack/\1', content)
    
    # 2. Assets (Standard tags)
    content = re.sub(r'src="/JJGPack/([^"]+)"', r'src="/JJGPack/\1"', content, flags=re.IGNORECASE) # ensure it has it
    content = re.sub(r'href="/JJGPack/([^"]+\.(?:css|js|ico|png|jpg|jpeg|svg))"', r'href="/JJGPack/\1"', content, flags=re.IGNORECASE)
    
    # 3. Alpine.js image strings
    content = re.sub(r"(['\"])/(?!JJGPack/|https?://)(images/|proimages/)([^'\"]*?)(\1)", r"\1/JJGPack/\2\3\4", content)
    
    # 4. Final fix for double prefixes
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/jjgpack/", "/JJGPack/")
    return content

def add_catalog_to_header(content, is_zh=False):
    # Desktop Nav
    en_link = '<a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>'
    zh_link = '<a href="/JJGPack/zh-tw/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">型錄EDM</a>'
    
    # Find the Desktop Nav container
    nav_match = re.search(r'<div class="hidden lg:flex items-center gap-1">.*?</div>', content, re.DOTALL)
    if nav_match:
        nav_block = nav_match.group(0)
        target_link = en_link if not is_zh else zh_link
        if target_link not in nav_block:
            # Insert before Contact or at the end
            if 'contact.html' in nav_block:
                new_nav_block = re.sub(r'(<a href="/JJGPack/(?:zh-tw/)?contact\.html".*?>.*?</a>)', target_link + r'\n        \1', nav_block)
            else:
                new_nav_block = nav_block.replace('</div>', '        ' + target_link + '\n      </div>')
            content = content.replace(nav_block, new_nav_block)

    # Mobile Nav
    mob_en = '<a href="/JJGPack/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">E-Catalog</a>'
    mob_zh = '<a href="/JJGPack/zh-tw/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">型錄EDM</a>'
    
    mob_target = mob_en if not is_zh else mob_zh
    if mob_target not in content:
        # Insert after news or before contact
        content = re.sub(r'(<a href="/JJGPack/(?:zh-tw/)?news\.html".*?</a>)', r'\1\n        ' + mob_target, content)
        
    return content

def add_die_cut_bag(content, is_zh=False):
    if "Die Cut Handle Bag" in content or "手提挖孔袋" in content:
        return content
    
    # We look for the products grid
    card_html = f"""        <!-- Die Cut Handle Bag -->
        <div class="bg-white rounded-2xl overflow-hidden shadow-premium card-hover group" data-reveal-child>
          <div class="aspect-[4/3] overflow-hidden img-overlay">
            <img src="https://www.jjgpaperbag.com/proimages/sr/product/DieCut_Bag/DM4.jpg" 
                 alt="Die Cut Handle Bag" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <div class="p-7">
            <span class="inline-block text-xs font-bold uppercase tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-3">Recycled Kraft</span>
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-2 group-hover:text-[#1A5C38] transition">{"Die Cut Handle Bag" if not is_zh else "手提挖孔袋"}</h3>
            <p class="text-sm text-[#666] mb-5">{"Made from 100% recycled paper with custom print available. Ideal for groceries and takeaway orders." if not is_zh else "採用 100% 回收紙製成，可自定義印刷。非常適合雜貨和外賣訂單。"}</p>
            <a href="https://www.jjgpaperbag.com/product-Die-Cut-Handle-paper-bag-brown-kraft-6.html" target="_blank"
               class="inline-flex items-center gap-2 text-[#1A5C38] font-bold text-sm group-hover:gap-3 transition-all">
              {"View Details" if not is_zh else "查看詳情"}
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
            </a>
          </div>
        </div>"""

    # Insertion point: end of the first product grid encountered
    match = re.search(r'(<div class="grid.*?gap-.*?">)(.*?)(</div>)', content, re.DOTALL)
    if match and "Die Cut Handle Bag" not in content:
        # Check if this grid looks like the product grid (contains other products)
        if "Kraft" in match.group(2) or "Greaseproof" in match.group(2):
            content = content[:match.start(3)] + card_html + content[match.start(3):]
            
    return content

def main():
    html_files = glob.glob("**/*.html", recursive=True)
    for f in html_files:
        if "node_modules" in f or "dist" in f: continue
        print(f"Updating {f}...")
        try:
            with open(f, 'r', encoding='utf-8') as fh: content = fh.read()
        except:
            with open(f, 'r', encoding='latin-1') as fh: content = fh.read()
        
        is_zh = "zh-tw" in f
        content = add_catalog_to_header(content, is_zh)
        if "products.html" in f:
            content = add_die_cut_bag(content, is_zh)
        
        content = fix_links_in_content(content)
        
        with open(f, 'w', encoding='utf-8') as fh: fh.write(content)
    print("Updates applied and paths standardized.")

if __name__ == "__main__":
    main()
