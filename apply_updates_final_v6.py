import os
import glob
import re

def fix_links(content):
    CORRECT_BASE = "/JJGPack/"
    # Standardize links to absolute paths under /JJGPack/
    content = re.sub(r'(href|src)="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?)(\.html|/|(?:"|\')|(?:\.(?:css|js|ico|png|jpg|jpeg|svg|pdf)))', r'\1="/JJGPack/\2\3', content)
    # Alpine image strings
    content = re.sub(r"(['\"])/(?!JJGPack/|https?://)(images/|proimages/)([^'\"]*?)(\1)", r"\1/JJGPack/\2\3\4", content)
    # Clean up
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/jjgpack/", "/JJGPack/")
    content = content.replace("/JJGPack//", "/JJGPack/")
    return content

def get_header(content, is_zh=False):
    if is_zh:
        links = '''        <a href="/JJGPack/zh-tw/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">首頁</a>
        <a href="/JJGPack/zh-tw/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">關於我們</a>
        <a href="/JJGPack/zh-tw/products.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">產品介紹</a>
        <a href="/JJGPack/zh-tw/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">最新消息</a>
        <a href="/JJGPack/zh-tw/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">型錄EDM</a>
        <a href="/JJGPack/zh-tw/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">聯絡我們</a>'''
    else:
        links = '''        <a href="/JJGPack/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Home</a>
        <a href="/JJGPack/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">About Us</a>
        <a href="/JJGPack/products.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Products</a>
        <a href="/JJGPack/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">News</a>
        <a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>
        <a href="/JJGPack/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Contact</a>'''
    
    # Replace Desktop Nav
    content = re.sub(r'<div class="hidden lg:flex items-center gap-1">.*?</div>', '<div class="hidden lg:flex items-center gap-1">\n' + links + '\n      </div>', content, flags=re.DOTALL)
    
    # Replace Mobile Nav
    if is_zh:
        m_links = links.replace('px-4 py-2', 'block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5').replace('relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all', '')
    else:
        m_links = links.replace('px-4 py-2', 'block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5').replace('relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all', '')

    content = re.sub(r'<div class="px-6 py-5 space-y-1">.*?</div>', '<div class="px-6 py-5 space-y-1">\n' + m_links + '\n      </div>', content, flags=re.DOTALL)
    
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
    
    # Try to find the grid container more robustly
    grids = list(re.finditer(r'<div class="grid md:grid-cols-2 lg:grid-cols-4(.*?)">', content, re.DOTALL))
    if grids:
        # We'll use the first match
        target = grids[0]
        # Find closing div
        depth = 0
        for i in range(target.end(), len(content)):
            if content[i:i+4] == '<div': depth += 1
            if content[i:i+6] == '</div>':
                if depth == 0:
                    return content[:i] + card + content[i:]
                depth -= 1
    return content

def create_catalog_html(template, is_zh=False):
    catalog_items = [
        {"title": "JJG PACK Imperial Units Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-imperial-units-catalog.pdf", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528751.jpg"},
        {"title": "JJG PACK Metric System Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-metric-system-catalog.pdf", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528775.jpg"},
        {"title": "USA STANDARD CATALOGUE", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/usa_standard_catalogue/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528414.jpg"},
        {"title": "General Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/general_catalog/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528574.jpg"},
        {"title": "Product Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-products/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528701.jpg"},
        {"title": "Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-e-catalog/mobile/index.html", "img": "https://www.jjgpaperbag.com/proimages/service/s_1636528628.jpg"}
    ]

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
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-4">{t}</h3>
            <a href="{item['link']}" target="_blank" class="btn-primary w-full text-center"><span>{"View Catalog" if not is_zh else "查看型錄"}</span></a>
        </div>"""

    hero_section = f"""
  <!-- ========== HERO ========== -->
  <section class="pt-32 pb-12 bg-[#F5F0E8]">
    <div class="max-w-[1440px] mx-auto px-6 lg:px-10 text-center">
        <h1 class="font-['Playfair_Display',serif] text-5xl font-bold mb-4">{"E-Catalog" if not is_zh else "型錄EDM"}</h1>
        <p class="text-gray-600 max-w-2xl mx-auto">{"Access our comprehensive product catalogs and standard specifications below." if not is_zh else "在下方查看我們的綜合產品型錄和標準規格。"}</p>
    </div>
  </section>"""

    main_section = f"""
  <section class="py-20 bg-white reveal">
    <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {items_html}
      </div>
    </div>
  </section>"""

    # Keep Header and Footer from template
    parts_header = template.split('</header>')
    parts_footer = template.split('<!-- ========== FOOTER ========== -->')
    if len(parts_footer) < 2: parts_footer = template.split('<footer')
    
    header = parts_header[0] + '</header>'
    footer = '<!-- ========== FOOTER ========== -->\n' + parts_footer[1]
    
    # Finalize E-Catalog page
    page = header + hero_section + main_section + footer
    # Fix SEO
    page = re.sub(r'<title>.*?</title>', f'<title>{"E-Catalog | JJG Paper Bag" if not is_zh else "型錄EDM | 壯佳果包裝"}</title>', page)
    return page

def main():
    # 1. Gather templates
    try:
        with open('about.html', 'r', encoding='utf-8') as f: template_en = f.read()
    except:
        with open('about.html', 'r', encoding='latin-1') as f: template_en = f.read()
    
    try:
        with open('zh-tw/about.html', 'r', encoding='utf-8') as f: template_zh = f.read()
    except:
        with open('zh-tw/about.html', 'r', encoding='latin-1') as f: template_zh = f.read()

    # 2. Process all files
    all_html = glob.glob("**/*.html", recursive=True)
    for path in all_html:
        if "node_modules" in path or "dist" in path: continue
        is_zh = "zh-tw" in path
        
        print(f"Processing {path}...")
        try:
            with open(path, 'r', encoding='utf-8') as f: content = f.read()
        except:
            with open(path, 'r', encoding='latin-1') as f: content = f.read()
            
        content = update_header(content, is_zh)
        if "products.html" in path:
            content = add_die_cut_bag(content, is_zh)
        
        content = fix_links(content)
        
        with open(path, 'w', encoding='utf-8') as f: f.write(content)

    # 3. Create/Update E-Catalog pages
    with open('catalog.html', 'w', encoding='utf-8') as f:
        f.write(fix_links(create_catalog_html(template_en, False)))
    with open('zh-tw/catalog.html', 'w', encoding='utf-8') as f:
        f.write(fix_links(create_catalog_html(template_zh, True)))
    
    print("All tasks completed successfully.")

if __name__ == "__main__": main()
