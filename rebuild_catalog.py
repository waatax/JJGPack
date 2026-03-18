import os
import re

def build_catalog(template_path, is_zh=False):
    with open(template_path, 'r', encoding='utf-8') as f:
        tmpl = f.read()
    
    # 1. Fix Head
    title = "E-Catalog | JJG Pack" if not is_zh else "型錄EDM | 壯佳果包裝"
    tmpl = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', tmpl)
    
    # 2. Add E-Catalog to Header
    # Simple insertion after News link
    news_link = "/JJGPack/zh-tw/news.html" if is_zh else "/JJGPack/news.html"
    cat_link = "/JJGPack/zh-tw/catalog.html" if is_zh else "/JJGPack/catalog.html"
    cat_text = "型錄EDM" if is_zh else "E-Catalog"
    
    # Desktop Nav
    pattern = f'<a href="{news_link}".*?</a>'
    new_nav = f'<a href="{news_link}" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">{"最新消息" if is_zh else "News"}</a>'
    new_nav += f'\n                                <a href="{cat_link}" class="text-[#1A5C38] font-semibold text-[15px]">{cat_text}</a>'
    tmpl = re.sub(pattern, new_nav, tmpl)
    
    # Mobile Nav (clean up any previous messes)
    tmpl = re.sub(r'<a href="/JJGPack/catalog.html".*?E-Catalog</a>', '', tmpl, flags=re.DOTALL)
    tmpl = re.sub(r'<a href="/JJGPack/zh-tw/catalog.html".*?型錄EDM</a>', '', tmpl, flags=re.DOTALL)
    
    pattern_mob = f'<a href="{news_link}".*?</a>'
    replacement_mob = f'<a href="{news_link}" class="block py-2 px-3 rounded hover:bg-[#F5F0E8]">{"最新消息" if is_zh else "News"}</a>'
    replacement_mob += f'\n                                <a href="{cat_link}" class="block py-2 px-3 rounded bg-[#F5F0E8] font-semibold text-[#1A5C38]">{cat_text}</a>'
    tmpl = re.sub(pattern_mob, replacement_mob, tmpl)

    # 3. Main Content
    catalog_items = [
        {"title": "JJG PACK Imperial Units Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-imperial-units-catalog.pdf", "img": "/proimages/service/s_1636528751.jpg"},
        {"title": "JJG PACK Metric System Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-metric-system-catalog.pdf", "img": "/proimages/service/s_1636528775.jpg"},
        {"title": "USA STANDARD CATALOGUE", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/usa_standard_catalogue/mobile/index.html", "img": "/proimages/service/s_1636528414.jpg"},
        {"title": "General Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/general_catalog/mobile/index.html", "img": "/proimages/service/s_1636528574.jpg"},
        {"title": "Product Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-products/mobile/index.html", "img": "/proimages/service/s_1636528701.jpg"},
        {"title": "Catalog", "link": "https://www.jjgpaperbag.com/proimages/e-catalog/2019-e-catalog/mobile/index.html", "img": "/proimages/service/s_1636528628.jpg"}
    ]
    
    grid_html = ""
    for item in catalog_items:
        t = item['title']
        if is_zh:
            zt = {"JJG PACK Imperial Units Catalog": "JJG PACK 英制單位型錄", "JJG PACK Metric System Catalog": "JJG PACK 公制單位型錄", "USA STANDARD CATALOGUE": "美國標準型錄", "General Catalog": "綜合型錄", "Product Catalog": "產品型錄", "Catalog": "型錄"}
            t = zt.get(t, t)
        grid_html += f"""
                <div class="bg-white rounded-2xl p-6 shadow-premium card-hover flex flex-col items-center text-center">
                    <div class="aspect-[3/4] w-full mb-6 overflow-hidden rounded-xl bg-gray-50 border border-gray-100">
                        <img src="{item['img']}" alt="{t}" class="w-full h-full object-contain p-2">
                    </div>
                    <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-4">{t}</h3>
                    <a href="{item['link']}" target="_blank" class="w-full py-3 bg-[#1A5C38] text-white rounded-lg font-bold hover:bg-[#2E8B57] transition">{"View Catalog" if not is_zh else "查看型錄"}</a>
                </div>"""

    content = f"""
        <!-- Hero Section -->
        <section class="pt-20 pb-12 bg-[#F5F0E8]">
            <div class="max-w-[1400px] mx-auto px-4 lg:px-8 text-center">
                <h1 class="text-4xl md:text-5xl font-bold mb-4">{cat_text}</h1>
                <p class="text-[#666] max-w-2xl mx-auto">{"Access our comprehensive product catalogs and standard specifications below." if not is_zh else "在下方查看我們的綜合產品型錄和標準規格。"}</p>
            </div>
        </section>

        <!-- Catalog Grid -->
        <section class="py-20 bg-white">
            <div class="max-w-[1400px] mx-auto px-4 lg:px-8">
                <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
                    {grid_html}
                </div>
            </div>
        </section>"""
    
    # Find start of main content in about.html and replace until footer
    header_end = tmpl.find('</header>') + 9
    footer_start = tmpl.find('<!-- ========== FOOTER ========== -->')
    if footer_start == -1: footer_start = tmpl.find('<footer')
    
    final = tmpl[:header_end] + content + tmpl[footer_start:]
    
    # 4. Final path cleanup for Vite
    # Assets should be root-relative without base prefix
    final = final.replace('href="/JJGPack/style.css"', 'href="/style.css"')
    final = final.replace('src="/JJGPack/main.js"', 'src="/main.js"')
    final = final.replace('src="/JJGPack/images/index-logo.png"', 'src="/images/index-logo.png"')
    final = final.replace('href="/JJGPack/images/favicon.ico"', 'href="/images/favicon.ico"')

    return final

# Create the pages
os.makedirs('zh-tw', exist_ok=True)
with open('catalog.html', 'w', encoding='utf-8') as f:
    f.write(build_catalog('about.html', False))
with open('zh-tw/catalog.html', 'w', encoding='utf-8') as f:
    f.write(build_catalog('zh-tw/about.html', True))

print("Catalog pages rebuilt successfully.")
