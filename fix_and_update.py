import os
import glob
import re

def fix_links(content, is_zh=False):
    # 1. Fix Assets (Dev Mode)
    # Revert hashed assets to source paths
    content = re.sub(r'<script type="module" crossorigin src="/JJGPack/assets/main-.*?\.js"></script>', '<script type="module" src="/main.js"></script>', content)
    content = re.sub(r'<link rel="stylesheet" crossorigin href="/JJGPack/assets/style-.*?\.css">', '<link rel="stylesheet" href="/style.css">', content)
    
    # Standardize image paths (let Vite handle the base)
    content = re.sub(r'src="/JJGPack/images/', 'src="/images/', content)
    content = re.sub(r'href="/JJGPack/images/favicon.ico"', 'href="/images/favicon.ico"', content)
    
    # 2. Standardize Navigation Links (routing)
    # These MUST have the /JJGPack/ prefix for the dev server with 'base' config to work correctly
    # and for GitHub Pages subfolder deployment.
    # We find href="/... and add /JJGPack/ if not present.
    def nav_link_replace(match):
        path = match.group(2)
        if path.startswith("JJGPack/") or path.startswith("http") or path.startswith("#") or path.startswith("mailto") or path.startswith("tel"):
            return match.group(0)
        return f'href="/JJGPack/{path}"'
    
    content = re.sub(r'href="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?)(\.html|/|(?:"|\'))', r'href="/JJGPack/\1\2', content)

    # Clean up double prefixes if any
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    
    return content

def add_catalog_to_nav(content, is_zh=False):
    # Add to Desktop Nav (find News and insert after)
    item_en = '<a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>'
    item_zh = '<a href="/JJGPack/zh-tw/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">型錄EDM</a>'
    
    target = item_zh if is_zh else item_en
    if target not in content:
        # Desktop Nav insertion
        news_link = '/JJGPack/zh-tw/news.html' if is_zh else '/JJGPack/news.html'
        pattern = f'(<a href="{news_link}".*?</a>)'
        content = re.sub(pattern, r'\1\n        ' + target, content)
        
        # Mobile Nav insertion
        mob_item_en = '<a href="/JJGPack/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">E-Catalog</a>'
        mob_item_zh = '<a href="/JJGPack/zh-tw/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">型錄EDM</a>'
        mob_target = mob_item_zh if is_zh else mob_item_en
        content = re.sub(pattern, r'\1\n        ' + mob_target, content)
        
    return content

def create_catalog_pages(template_en, template_zh):
    catalog_items = [
        {"title": "JJG PACK Imperial Units Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-imperial-units-catalog.pdf", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528751.jpg"},
        {"title": "JJG PACK Metric System Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-metric-system-catalog.pdf", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528775.jpg"},
        {"title": "USA STANDARD CATALOGUE", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/usa_standard_catalogue/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528414.jpg"},
        {"title": "General Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/general_catalog/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528574.jpg"},
        {"title": "Product Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-products/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528701.jpg"},
        {"title": "Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-e-catalog/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528628.jpg"}
    ]

    def build_page(tmpl, is_zh):
        content_html = ""
        for item in catalog_items:
            t = item['title']
            if is_zh:
                zt = {"JJG PACK Imperial Units Catalog": "JJG PACK 英制單位型錄", "JJG PACK Metric System Catalog": "JJG PACK 公制單位型錄", "USA STANDARD CATALOGUE": "美國標準型錄", "General Catalog": "綜合型錄", "Product Catalog": "產品型錄", "Catalog": "型錄"}
                t = zt.get(t, t)
            
            content_html += f"""
        <div class="bg-white rounded-2xl p-6 shadow-premium card-hover flex flex-col items-center text-center">
            <div class="aspect-[3/4] w-full mb-6 overflow-hidden rounded-xl bg-gray-50 border border-gray-100">
                <img src="{item['img']}" alt="{t}" class="w-full h-full object-contain p-2">
            </div>
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-4 whitespace-normal">{t}</h3>
            <a href="{item['link']}" target="_blank" class="btn-primary w-full text-center"><span>{"View Catalog" if not is_zh else "查看型錄"}</span></a>
        </div>"""

        main_section = f"""
  <section class="pt-32 pb-12 bg-[#F5F0E8]">
    <div class="max-w-[1440px] mx-auto px-6 lg:px-10 text-center">
        <h1 class="font-['Playfair_Display',serif] text-5xl font-bold mb-4">{"E-Catalog" if not is_zh else "型錄EDM"}</h1>
        <p class="text-gray-600 max-w-2xl mx-auto">{"Access our comprehensive product catalogs and standard specifications below." if not is_zh else "在下方查看我們的綜合產品型錄和標準規格。"}</p>
    </div>
  </section>
  <section class="py-20 bg-white">
    <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {content_html}
      </div>
    </div>
  </section>"""
        
        # Replace breadcrumbs content or insert between header and footer
        # We split by <!-- ========== HEADER ========== --> if possible
        header_end = tmpl.find('</header>') + 9
        footer_start = tmpl.find('<!-- ========== FOOTER ========== -->')
        if footer_start == -1: footer_start = tmpl.find('<footer')
        
        final = tmpl[:header_end] + main_section + tmpl[footer_start:]
        final = re.sub(r'<title>.*?</title>', f'<title>{"E-Catalog | JJG Pack" if not is_zh else "型錄EDM | JJG Pack"}</title>', final)
        return final

    with open('catalog.html', 'w', encoding='utf-8') as f:
        f.write(build_page(template_en, False))
    with open('zh-tw/catalog.html', 'w', encoding='utf-8') as f:
        f.write(build_page(template_zh, True))

def add_die_cut_bag(content, is_zh=False):
    if "Die Cut Handle Bag" in content or "丸孔手提袋" in content or "手提挖孔袋" in content:
        return content
        
    card_html = f"""        <!-- Die Cut Handle Bag -->
        <div class="bg-white rounded-2xl overflow-hidden shadow-premium card-hover group" data-reveal-child>
          <div class="aspect-[4/3] overflow-hidden img-overlay">
            <img src="https://www.jjgpaperbag.com/proimages/sr/product/DieCut_Bag/DM4.jpg" alt="Die Cut Handle Bag" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <div class="p-7">
            <span class="inline-block text-xs font-bold uppercase tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-3">Recycled Kraft</span>
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-2 group-hover:text-[#1A5C38] transition">{"Die Cut Handle Bag" if not is_zh else "丸孔手提袋"}</h3>
            <p class="text-sm text-[#666] mb-5">{"Ideal for groceries and takeaway orders, featuring die-cut handles for stability and easy carrying." if not is_zh else "適用於雜貨和外賣訂單，採用模切手柄，穩定且易於攜帶。"}</p>
            <a href="https://www.jjgpaperbag.com/product-Die-Cut-Handle-paper-bag-brown-kraft-6.html" target="_blank" class="inline-flex items-center gap-2 text-[#1A5C38] font-bold text-sm group-hover:gap-3 transition-all">
              {"View Details" if not is_zh else "查看詳情"}
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
            </a>
          </div>
        </div>"""
    
    # Insert at the end of the first product grid encountered in products.html
    grid_matches = list(re.finditer(r'<div class="grid md:grid-cols-2 lg:grid-cols-4(.*?)">', content, re.DOTALL))
    if grid_matches:
        target = grid_matches[0]
        # Find closing div of this grid
        depth = 0
        for i in range(target.end(), len(content)):
            if content[i:i+4] == '<div': depth += 1
            if content[i:i+6] == '</div>':
                if depth == 0:
                    return content[:i] + card_html + content[i:]
                depth -= 1
    return content

def main():
    tmpl_en = ""
    tmpl_zh = ""
    
    files = glob.glob("**/*.html", recursive=True)
    for path in files:
        if "node_modules" in path or "dist" in path: continue
        is_zh = "zh-tw" in path
        print(f"Processing {path}...")
        try:
            with open(path, 'r', encoding='utf-8') as f: content = f.read()
        except: continue
        
        content = fix_links(content, is_zh)
        content = add_catalog_to_nav(content, is_zh)
        if "products.html" in path:
            content = add_die_cut_bag(content, is_zh)
            
        with open(path, 'w', encoding='utf-8') as f: f.write(content)
        
        if path == "about.html": tmpl_en = content
        if path == "zh-tw/about.html": tmpl_zh = content

    if tmpl_en and tmpl_zh:
        create_catalog_pages(tmpl_en, tmpl_zh)
    print("Updates applied and paths standardized.")

if __name__ == "__main__":
    main()
