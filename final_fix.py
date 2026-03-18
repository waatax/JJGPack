import os
import glob
import re

def safe_write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_links(content):
    # Enforce /JJGPack/ but avoid doubling
    # 1. Assets and Internal Links
    content = re.sub(r'(href|src)="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?)(\.html|/|(?:"|\')|(?:\.(?:css|js|ico|png|jpg|jpeg|svg|pdf|ico)))', r'\1="/JJGPack/\2\3', content)
    
    # 2. Cleanup double prefixes
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    content = content.replace("/JJGPack//", "/JJGPack/")
    content = content.replace("/jjgpack/jjgpack/", "/JJGPack/")
    
    return content

def apply_nav(content, is_zh=False):
    # Desktop
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
    
    content = re.sub(r'<div class="hidden lg:flex items-center gap-1">.*?</div>', '<div class="hidden lg:flex items-center gap-1">\n' + links + '\n      </div>', content, flags=re.DOTALL)
    
    # Mobile
    m_links = links.replace('px-4 py-2', 'block py-2.5 px-4 rounded-lg hover:bg-[#1A5C38]/5').replace('relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all', '')
    content = re.sub(r'<div class="px-6 py-5 space-y-1">.*?</div>', '<div class="px-6 py-5 space-y-1">\n' + m_links + '\n      </div>', content, flags=re.DOTALL)
    
    return content

def add_die_cut(content, is_zh=False):
    if "Die Cut Handle Bag" in content: return content
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
    
    # Simple append to the first grid
    content = re.sub(r'(<div class="grid md:grid-cols-2 lg:grid-cols-4.*?>)', r'\1\n' + card, content, 1)
    return content

def main():
    all_html = glob.glob("**/*.html", recursive=True)
    for p in all_html:
        if "node_modules" in p or "dist" in p: continue
        try:
            with open(p, 'r', encoding='utf-8') as f: content = f.read()
            print(f"Processing {p}...")
        except:
            continue
            
        is_zh = "zh-tw" in p
        
        # 1. Standardize Title (Prevent Mojibake)
        title_text = "JJG Pack | Professional Paper Bag Manufacturer - 壯佳果包裝"
        content = re.sub(r'<title>.*?</title>', f'<title>{title_text}</title>', content, flags=re.DOTALL)
        
        # 2. Fix Nav
        content = apply_nav(content, is_zh)
        
        # 3. Add Die Cut Bag
        if "products.html" in p:
            content = add_die_cut(content, is_zh)
            
        # 4. Standardize Links
        content = fix_links(content)
        
        # 5. Fix any malformed tags
        content = content.replace('<<footer', '<footer')
        content = content.replace('title>JJG Pack', '<title>JJG Pack') # Ensure opening bracket
        
        safe_write(p, content)

    # Re-generate Catalog Pages
    try:
        with open('about.html', 'r', encoding='utf-8') as f: tmpl = f.read()
        # simplified catalog body
        items = [
            ("JJG PACK Imperial Units Catalog", "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-imperial-units-catalog.pdf", "https://www.jjgpaperbag.com/proimages/service/s_1636528751.jpg"),
            ("JJG PACK Metric System Catalog", "https://www.jjgpaperbag.com/proimages/e-catalog/cover/jjg-pack-metric-system-catalog.pdf", "https://www.jjgpaperbag.com/proimages/service/s_1636528775.jpg"),
            ("USA STANDARD CATALOGUE", "https://www.jjgpaperbag.com/proimages/e-catalog/usa_standard_catalogue/mobile/index.html", "https://www.jjgpaperbag.com/proimages/service/s_1636528414.jpg"),
            ("General Catalog", "https://www.jjgpaperbag.com/proimages/e-catalog/general_catalog/mobile/index.html", "https://www.jjgpaperbag.com/proimages/service/s_1636528574.jpg"),
            ("Product Catalog", "https://www.jjgpaperbag.com/proimages/e-catalog/2019-products/mobile/index.html", "https://www.jjgpaperbag.com/proimages/service/s_1636528701.jpg"),
            ("Catalog", "https://www.jjgpaperbag.com/proimages/e-catalog/2019-e-catalog/mobile/index.html", "https://www.jjgpaperbag.com/proimages/service/s_1636528628.jpg")
        ]
        def gen(tmpl_str, is_zh):
            h = tmpl_str.split('</header>')[0] + '</header>'
            f = tmpl_str.split('<!-- ========== FOOTER ========== -->')[1]
            itms = "".join([f'<div class="bg-white rounded-2xl p-6 shadow-premium card-hover text-center"><img src="{i[2]}" class="w-full mb-4 rounded-xl"><h3 class="font-bold mb-4">{i[0]}</h3><a href="{i[1]}" target="_blank" class="btn-primary w-full text-center"><span>View Catalog</span></a></div>' for i in items])
            body = f'<section class="pt-32 pb-20 bg-white"><div class="max-w-[1200px] mx-auto px-6"><h1 class="text-4xl font-bold text-center mb-12">{"E-Catalog" if not is_zh else "型錄EDM"}</h1><div class="grid md:grid-cols-3 gap-8">{itms}</div></div></section>'
            return fix_links(h + body + '<!-- ========== FOOTER ========== -->\n' + f)
        
        safe_write('catalog.html', gen(tmpl, False))
        # same for zh
        with open('zh-tw/about.html', 'r', encoding='utf-8') as f: tmpl_z = f.read()
        safe_write('zh-tw/catalog.html', gen(tmpl_z, True))
    except: pass

    print("Final delivery fixes applied.")

if __name__ == "__main__": main()
