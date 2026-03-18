import os
import glob
import re

def sanitize_content(content, path):
    # 1. Fix Mojibake in Meta/Title based on the common strings
    # Replace any sequences of non-ascii garbage in common spots
    # We'll just force the correct strings for ZH and EN
    is_zh = "zh-tw" in path
    
    if is_zh:
        correct_title = "<title>JJG Paper Bag | Professional Paper Bag Manufacturer - 壯佳果包裝</title>"
        correct_desc = '<meta name="description" content="壯佳果股份有限公司 — Professional paper bag manufacturer in Taiwan with 70+ years of experience. PFAS-free, eco-friendly packaging solutions." />'
    else:
        correct_title = "<title>JJG Paper Bag | Professional Paper Bag Manufacturer - 壯佳果包裝</title>"
        correct_desc = '<meta name="description" content="壯佳果股份有限公司 — Professional paper bag manufacturer in Taiwan with 70+ years of experience. PFAS-free, eco-friendly packaging solutions." />'

    # Aggressive replacement of the head titles and descriptions
    content = re.sub(r'<title>.*?</title>', correct_title, content, flags=re.DOTALL)
    content = re.sub(r'<meta name="description".*?/>', correct_desc, content, flags=re.DOTALL)

    # 2. Fix malformed footer tag (missing <)
    content = content.replace('footer class="bg-[#1A1A1A]', '<footer class="bg-[#1A1A1A]')
    
    # 3. Standardize Navigation completely (V8)
    # Re-enforce the correct header if it was mangled
    # I'll use the same logic as V7 but be more careful
    
    # Fix Links (ensure /JJGPack/ prefix and no duplicates)
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/JJGPack//", "/JJGPack/")
    
    # 4. Final check for logo path
    content = content.replace('src="/images/index-logo.png"', 'src="/JJGPack/images/index-logo.png"')
    content = content.replace('href="/style.css"', 'href="/JJGPack/style.css"')
    
    return content

def main():
    # 1. Sanitize all existing files
    all_html = glob.glob("**/*.html", recursive=True)
    template_en = ""
    template_zh = ""
    
    for path in all_html:
        if "node_modules" in path or "dist" in path: continue
        print(f"Sanitizing {path}...")
        try:
            with open(path, 'r', encoding='utf-8') as f: content = f.read()
        except:
            with open(path, 'r', encoding='latin-1') as f: content = f.read()
            
        content = sanitize_content(content, path)
        
        # Save as clean template for catalog
        if path == "about.html": template_en = content
        if path == "zh-tw/about.html": template_zh = content
        
        with open(path, 'w', encoding='utf-8') as f: f.write(content)

    # 2. Re-generate Catalog Pages correctly
    def gen_catalog_v2(template, is_zh):
        # We want everything from start until the end of <header>
        header_end = template.find('</header>') + 9
        footer_start = template.find('<!-- ========== FOOTER ========== -->')
        if footer_start == -1: footer_start = template.find('<footer')
        
        header_part = template[:header_end]
        footer_part = template[footer_start:]
        
        title_text = "E-Catalog | JJG Paper Bag" if not is_zh else "型錄EDM | 壯佳果包裝"
        header_part = re.sub(r'<title>.*?</title>', f'<title>{title_text}</title>', header_part)
        
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

        body = f"""
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
        return header_part + body + footer_part

    if template_en:
        with open('catalog.html', 'w', encoding='utf-8') as f: f.write(gen_catalog_v2(template_en, False))
    if template_zh:
        with open('zh-tw/catalog.html', 'w', encoding='utf-8') as f: f.write(gen_catalog_v2(template_zh, True))
    
    print("Sanitization complete.")

if __name__ == "__main__": main()
