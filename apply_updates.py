import os
import glob
import re

def fix_links_in_content(content, is_zh=False):
    CORRECT_BASE = "/JJGPack/"
    # 1. Navigation links
    content = re.sub(r'href="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?\.html|[^"]*?/|(?:"|\'))', r'href="/JJGPack/\1', content)
    # 2. Assets (remove prefix)
    content = re.sub(r'src="/JJGPack/([^"]+)"', r'src="/\1"', content, flags=re.IGNORECASE)
    content = re.sub(r'href="/JJGPack/([^"]+\.(?:css|js|ico|png|jpg|jpeg|svg))"', r'href="/\1"', content, flags=re.IGNORECASE)
    # 3. Alpine.js image strings
    content = re.sub(r"(['\"])/(?!JJGPack/|https?://)(images/|proimages/)([^'\"]*?)(\1)", r"\1/JJGPack/\2\3\4", content)
    # 4. Cleanup
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/jjgpack/", "/JJGPack/")
    return content

def add_catalog_to_header(content, is_zh=False):
    # Desktop
    if is_zh:
        link_html = '<a href="/JJGPack/zh-tw/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">型錄EDM</a>'
        pattern = r'(<a href="/JJGPack/zh-tw/news\.html".*?News</a>|<a href="/JJGPack/zh-tw/news\.html".*?新闻</a>)'
    else:
        link_html = '<a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>'
        pattern = r'(<a href="/JJGPack/news\.html".*?News</a>)'

    if link_html not in content:
        content = re.sub(pattern, r'\1\n        ' + link_html, content)
    
    # Mobile
    if is_zh:
        mobile_link = '<a href="/JJGPack/zh-tw/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">型錄EDM</a>'
    else:
        mobile_link = '<a href="/JJGPack/catalog.html" class="block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5 text-[#555] transition">E-Catalog</a>'
    
    if mobile_link not in content:
        content = re.sub(r'(<a href="/JJGPack/(?:zh-tw/)?news\.html".*?News</a>|<a href="/JJGPack/(?:zh-tw/)?news\.html".*?新闻</a>)', r'\1\n        ' + mobile_link, content)
        
    return content

def update_products_list(content, is_zh=False):
    if "Die-Cut Bag" in content or "手提挖孔袋" in content:
        return content
        
    die_cut_html = f"""        <div class="bg-white rounded-2xl overflow-hidden shadow-premium card-hover group" data-reveal-child>
          <div class="aspect-[4/3] overflow-hidden img-overlay"><img src="https://www.jjgpaperbag.com/proimages/sr/product/DieCut_Bag/DM4.jpg"
              alt="Die Cut Handle Bag"
              class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"></div>
          <div class="p-7"><span
              class="inline-block text-xs font-bold uppercase tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-3">Recycled Kraft</span>
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-2 group-hover:text-[#1A5C38] transition">
              {"Die Cut Handle Bag" if not is_zh else "手提挖孔袋"}</h3>
            <p class="text-sm text-[#666] mb-5">{"Ideal for groceries and takeaway orders, featuring die-cut handles for stability and easy carrying." if not is_zh else "適用於雜貨和外賣訂單，採用模切手柄，穩定且易於攜帶。"}</p>
            <a href="https://www.jjgpaperbag.com/product-Die-Cut-Handle-paper-bag-brown-kraft-6.html"
              class="inline-flex items-center gap-2 text-[#1A5C38] font-bold text-sm group-hover:gap-3 transition-all">{"View Details" if not is_zh else "查看詳情"} <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg></a>
          </div>
        </div>"""
    
    # Check if it's the products page grid
    if '<h2 class="font-[\'Playfair_Display\',serif] text-4xl md:text-5xl font-bold mb-6">Our Products</h2>' in content or '<h2 class="font-[\'Playfair_Display\',serif] text-4xl md:text-5xl font-bold mb-6">所有產品</h2>' in content:
        content = content.replace('<!-- ========== WHY CHOOSE US ========== -->', die_cut_html + '\n      </div>\n    </div>\n  </section>\n\n  <!-- ========== WHY CHOOSE US ========== -->')
    
    return content

def main():
    catalog_items = [
        {"title": "JJG PACK Imperial Units Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-imperial-units-catalog.pdf", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528751.jpg"},
        {"title": "JJG PACK Metric System Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-metric-system-catalog.pdf", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528775.jpg"},
        {"title": "USA STANDARD CATALOGUE", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/usa_standard_catalogue/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528414.jpg"},
        {"title": "General Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/general_catalog/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528574.jpg"},
        {"title": "Product Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-products/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528701.jpg"},
        {"title": "Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-e-catalog/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528628.jpg"}
    ]

    html_files = glob.glob("**/*.html", recursive=True)
    template_content = ""
    template_zh_content = ""

    for f in html_files:
        if "node_modules" in f or "dist" in f: continue
        print(f"Processing {f}...")
        try:
            with open(f, 'r', encoding='utf-8') as fh: content = fh.read()
        except UnicodeDecodeError:
            with open(f, 'r', encoding='latin-1') as fh: content = fh.read()
            
        if os.path.basename(f) == "about.html":
            if "zh-tw" in f: template_zh_content = content
            else: template_content = content
        
        content = add_catalog_to_header(content, "zh-tw" in f)
        content = update_products_list(content, "zh-tw" in f)
        content = fix_links_in_content(content, "zh-tw" in f)
        
        with open(f, 'w', encoding='utf-8') as fh: fh.write(content)
            
    def create_catalog_html(template, is_zh):
        title = "E-Catalog | JJG Paper Bag" if not is_zh else "型錄EDM | 壯佳果包裝"
        content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', template)
        
        items_html = ""
        for item in catalog_items:
            t = item['title']
            if is_zh:
                zh_titles = {"JJG PACK Imperial Units Catalog": "JJG PACK 英制單位型錄", "JJG PACK Metric System Catalog": "JJG PACK 公制單位型錄", "USA STANDARD CATALOGUE": "美國標準型錄", "General Catalog": "綜合型錄", "Product Catalog": "產品型錄", "Catalog": "型錄"}
                t = zh_titles.get(t, t)
            items_html += f"""
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
        {items_html}
      </div>
    </div>
  </section>"""
        # Split template to keep header/footer
        parts = content.split('<!-- ========== HERO ========== -->')
        if len(parts) < 2: parts = content.split('<header') # fallback
        header = parts[0]
        footer_parts = content.split('<!-- ========== FOOTER ========== -->')
        footer = footer_parts[1] if len(footer_parts) > 1 else ""
        
        final_page = header + main_section + '\n  <!-- ========== FOOTER ========== -->\n' + footer
        return fix_links_in_content(final_page, is_zh)

    if template_content:
        with open('catalog.html', 'w', encoding='utf-8') as f: f.write(create_catalog_html(template_content, False))
    if template_zh_content:
        with open('zh-tw/catalog.html', 'w', encoding='utf-8') as f: f.write(create_catalog_html(template_zh_content, True))

if __name__ == "__main__":
    main()
