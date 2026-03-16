import json
import os

# 1. Load Data
# Greaseproof is already in a clean JSON
with open('greaseproof_data.json', 'r', encoding='utf-8') as f:
    greaseproof_data = json.load(f)

# Manually define the other data from the scratchpad extraction
# (I'll process it into a dictionary mapping category ID to data)
categories_map = {
    'greaseproof': greaseproof_data,
    'kraft': [
        {"name": "To-Go SOS Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/4.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/8.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/12.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/Square_bag.JPG"], "description": "To-Go SOS Bags", "specs": "Sizes: 4#, 6#, 8#, 10#, 12#, 20#. Features: High-quality brown kraft. Customizable printing."},
        {"name": "Merchandise Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/841.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/842.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/843.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/844.jpg"], "description": "Merchandise Bags", "specs": "Features: Offered in a variety of sizes. High-quality white and brown kraft. Customizable logo printing."},
        {"name": "Bakery window bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/france_bakery_bag_01.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Bakery_Bag/IMG_1829_LR.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/france_bakery_bag_03.jpg"], "description": "Bakery window bag", "specs": "Natural Kraft paper, PE laminated, grease-resistant. Transparent window. Ideal for bakeries."},
        {"name": "Baguette Bakery bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Brown_kraft_bag-bakery_bag1.JPG", "https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Brown_kraft_bag-bakery_bag2.JPG"], "description": "Baguette Bakery bag", "specs": "Natural Kraft paper, PE laminated, grease-resistant. Ideal for French baguettes."},
        {"name": "Flat Handle Grocery Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Brown_Carry_Paper_Bag/carry_bag_1.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Brown_Carry_Paper_Bag/carry_bag_2.jpg"], "description": "Flat Handle Grocery Bags", "specs": "Eco-friendly, sturdy flat handles. Suitable for grocery and take-out."},
        {"name": "Die Cut Handle bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Die_cut_handle-bag1.JPG", "https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Die_cut_handle-bag2.JPG"], "description": "Die Cut Handle bag", "specs": "Die-cut handles for easy carrying. Clean and modern look."},
        {"name": "SOS White Take Out Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/SOS-White-Take-Out-Bags-3.jpg"], "description": "SOS White Take Out Bags", "specs": "4#: W127xH245xG77 (1,500pcs/CTN). 8#: W156xH312xG102 (1,000pcs/CTN)."},
        {"name": "Cream Color Square Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/Cream-Color--Square-Bag-1.jpg", "https://www.jjgpaperbag.com/proimages/sr/Cream-Color--Square-Bag-3.jpg"], "description": "Cream Color Square Bag", "specs": "Kraft Handle Bag: W210xH275xG90 (400pcs). Square Bag(12#): W190xH300xG110 (500pcs)."},
        {"name": "8# Square Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/8號方袋.jpg"], "description": "8# Square Bottom Paper Bag", "specs": "Multiple SKUs (S8001-S8021). Range of sizes available."},
        {"name": "Christmas Series Square Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/聖誕節方袋.jpg"], "description": "Christmas Series Square Bottom Paper Bag", "specs": "Holiday themed prints on square bottom bags."},
        {"name": "Hexagonal Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/0901-2.jpg"], "description": "Hexagonal Bottom Paper Bag", "specs": "Patented hexagonal bottom design for unique packaging needs."},
        {"name": "Bakery Series Paper Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/烘焙麵包窗袋.jpg"], "description": "Bakery Series Paper Bags", "specs": "Natural Kraft paper, PE laminated, grease-resistant. Visible window."}
    ],
    'flathandle': [
        {"name": "Single Color Shopping Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/112.01.06-JJG-PACK-Single-Color-Shopping-Bags-1.jpg"], "description": "Shopping Bag. Paper Material: Brown Virgin / 100% Recycled Kraft. Ideal for take away, fast food, and bakery goods.", "specs": "CM4~CM7: Up to 4 colors on 4 sides. 1/6BBL: Up to 3 colors on 4 sides."},
        {"name": "Cream Color Flat Handle Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/Cream-Color-Flat-Handle-Bag-1.jpg", "https://www.jjgpaperbag.com/proimages/sr/Cream-Color-Flat-Handle-Bag-2.jpg"], "description": "Cream Color Flat Handle Bag", "specs": "CM01/CM02: 210x275x90 mm, 400pcs."},
        {"name": "Macaron Color Flat Handle Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/Macaron-Color-Flat-Handle-Bag-1.jpg", "https://www.jjgpaperbag.com/proimages/sr/Macaron-Color-Flat-Handle-Bag-2.jpg", "https://www.jjgpaperbag.com/proimages/sr/Macaron-Color-Flat-Handle-Bag-3.jpg"], "description": "Macaron Color Flat Handle Bag", "specs": "Size: 210x275x90 mm, 400pcs."},
        {"name": "Christmas Series Flat Handle Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/聖誕CM4提袋-1-2.jpg", "https://www.jjgpaperbag.com/proimages/sr/聖誕CM4提袋-2-2.jpg"], "description": "Holiday themed flat handle bags.", "specs": "CM4-3: 220x235x120 (400pcs). S8275-1: 156x312x102 (1,500pcs). S12A275-1: 190x350x120 (1,000pcs)."},
        {"name": "Recycled Kraft Flat handle Sacks", "images": ["https://www.jjgpaperbag.com/proimages/sr/環牛扁把提袋-1.jpg"], "description": "Strong, efficient, and convenient to use. Self-standing for easy loading.", "specs": "1/7 BBL: 305x170x355 (300 Qty). 1/6 BBL: 305x170x425 (300 Qty)."}
    ],
    'white': [
        {"name": "White Kraft Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/JJG-B1.png"], "description": "White Kraft Bags", "specs": "White#1 to White#6, Material: White kraft, 50g, various dimensions."},
        {"name": "Recycled Kraft Grocery Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/環方-3.jpg"], "description": "Recycled Kraft Grocery Bags", "specs": "4275-R L3: 127x245x77. 8260-R L3: 156x312x102."},
        {"name": "New Flate Handle Paper Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/114.03.03-全新扁把提袋（COFFEE款）.jpg"], "description": "Bags for Coffee, Bakery, Burger and Souvenir shops.", "specs": "CM4-R3: 220x235x120mm. CM4-S2: 220x235x120mm."},
        {"name": "Take Out Bags Square Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/114.03.04-爆脆方袋.jpg"], "description": "CRIX08 crispy bag for fried food.", "specs": "CRIX08 size."}
    ],
    'foil': [
        {"name": "Aluminum Foil Lined Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/pro5-1.png"], "description": "Aluminum Foil Lined Bags for heat retention and grease resistance.", "specs": "JUMBO/XL/L/S and LONG1/2 sizes. Material: Aluminum Foil, 67g."}
    ],
    'pe': [
        {"name": "Burger pocket paper bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/PE-Lamination-paper-1.jpg"], "description": "Burger pocket paper bag", "specs": "LS1919-1PE: W190xH190. BL1-1515SL: W150xH150. PE-Lamination, 43g."},
        {"name": "Deli Wrap Paper", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/pro3-2.png"], "description": "Food Wrapping Liners. Greaseproof or PE-Laminated.", "specs": "Sizes: 300x300, 200x200. PE-Lamination, 43g."},
        {"name": "Toast Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/0901-4.jpg"], "description": "V-shape paper bags for burgers and snacks.", "specs": "Standard V-shape sizes."}
    ],
    'straw': [
        {"name": "Paper Straw (Brown)", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Paper_straw/IMG_5540_s.jpg"], "description": "Sustainable brown paper straws. Bare / Single / Box packaging.", "specs": "Flat and Blade Design. Made in Taiwan."},
        {"name": "Biodegradable Bamboo Straw", "images": ["https://www.jjgpaperbag.com/proimages/sr/竹吸-1.jpg"], "description": "Biodegradable Bamboo Straw.", "specs": "Bamboo material."}
    ],
    'others': [
        {"name": "Paper Placement", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Paper_placement.jpg"], "description": "Paper Placement / Placemats.", "specs": "DF60-4028: W400xH280, 2,250/Carton."},
        {"name": "Bakery side window bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Bakery_side_window_bag_01.jpg"], "description": "Natural Kraft paper, PE laminated, grease-resistant. Visible window.", "specs": "BV2W124S: W145xH240xG45, 2,000/Carton."},
        {"name": "Wonderful Time Paper Placemats", "images": ["https://www.jjgpaperbag.com/proimages/sr/餐墊紙1.jpg"], "description": "Public edition paper placemats.", "specs": "P004-P102: 400x280 or 390x280 mm."}
    ]
}

# 2. Templates
HEADER_ZH = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | 壯佳果包裝 - JJG Paper Bag</title>
    <meta name="description" content="{desc}" />
    <link rel="icon" href="/images/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+TC:wght@400;500;600;700&family=Noto+Serif+TC:wght@700;900&display=swap" rel="stylesheet">
    <link href="/style.css" rel="stylesheet">
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body x-data="{{ mobileMenu: false {extra_x_data} }}" class="bg-[#F5F0E8] text-[#1A1A1A] font-['Inter','Noto_Sans_TC',sans-serif]">
    <header class="fixed top-0 left-0 right-0 z-50 glass">
        <nav class="max-w-[1440px] mx-auto px-6 lg:px-10 h-[76px] flex items-center justify-between">
            <a href="/zh-tw/"><img src="/images/index-logo.png" alt="壯佳果" class="h-11"></a>
            <div class="hidden lg:flex items-center gap-1">
                <a href="/zh-tw/" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition">首頁</a>
                <a href="/zh-tw/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition">關於我們</a>
                <a href="/zh-tw/products.html" class="px-4 py-2 text-[#1A5C38] font-semibold text-[15px]">產品介紹</a>
                <a href="/zh-tw/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition">最新消息</a>
                <a href="/zh-tw/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition">聯絡我們</a>
            </div>
            <div class="hidden lg:flex items-center gap-5">
                <a href="/" class="text-sm text-[#888]">EN</a>
                <a href="/zh-tw/" class="text-sm text-[#1A5C38] font-semibold">繁中</a>
                <a href="/zh-tw/contact.html" class="btn-primary text-sm !py-2.5 !px-6 !rounded-lg"><span>聯絡我們</span></a>
            </div>
            <button @click="mobileMenu=!mobileMenu" class="lg:hidden p-2"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg></button>
        </nav>
    </header>
    <div class="pt-[76px]">
"""

FOOTER_ZH = """    </div>
    <footer class="bg-[#111] text-gray-400 pt-16 pb-8">
        <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
            <div class="grid md:grid-cols-4 gap-10 pb-10 border-b border-white/10">
                <div><img src="/images/index-logo.png" alt="JJG" class="h-10 mb-4 brightness-200"><p class="text-sm text-gray-500">台灣專業紙袋製造商</p></div>
                <div><h4 class="text-white font-bold mb-4 text-sm">快速連結</h4><ul class="space-y-2 text-sm"><li><a href="/zh-tw/" class="hover:text-[#2E8B57]">首頁</a></li><li><a href="/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a></li><li><a href="/zh-tw/contact.html" class="hover:text-[#2E8B57]">聯絡我們</a></li></ul></div>
                <div><h4 class="text-white font-bold mb-4 text-sm">產品系列</h4><ul class="space-y-2 text-sm"><li><a href="/zh-tw/products/greaseproof.html" class="hover:text-[#2E8B57]">防油紙袋</a></li><li><a href="/zh-tw/products/kraft.html" class="hover:text-[#2E8B57]">牛皮紙袋</a></li><li><a href="/zh-tw/products/flathandle.html" class="hover:text-[#2E8B57]">平把手提袋</a></li></ul></div>
                <div><h4 class="text-white font-bold mb-4 text-sm">聯絡資訊</h4><ul class="space-y-2 text-sm"><li>📍 台中市大甲區游九路6號</li><li>📞 +886-4-26223215</li><li>✉️ export@jjgpaperbag.com</li></ul></div>
            </div>
            <div class="pt-6 text-center text-xs text-gray-600">© 2026 壯佳果股份有限公司</div>
        </div>
    </footer>
    <script type="module" src="/main.js"></script>
</body>
</html>"""

def slugify(text):
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-').replace('--', '-').replace('#', '').strip('-')

category_names_zh = {
    'greaseproof': "防油紙袋",
    'kraft': "牛皮紙袋",
    'flathandle': "平把手提袋",
    'white': "白牛皮紙袋",
    'foil': "鋁箔紙袋",
    'pe': "淋膜紙袋",
    'straw': "紙吸管",
    'others': "其他產品"
}

# 3. Generate individual product pages
for cat_id, products in categories_map.items():
    cat_dir = f"zh-tw/products/{cat_id}"
    os.makedirs(cat_dir, exist_ok=True)
    
    for prod in products:
        slug = slugify(prod['name']) + '.html'
        main_img = prod['images'][0] if prod['images'] else ""
        
        # Gallery bits
        gal_bits = []
        for img in prod['images']:
            bit = f'<button @click="activeImage=\'{img}\'" class="aspect-square rounded-lg overflow-hidden border-2 transition" :class="activeImage===\'{img}\' ? \'border-[#1A5C38]\' : \'border-transparent hover:border-gray-200\'"><img src="{img}" class="w-full h-full object-cover"></button>'
            gal_bits.append(bit)

        html = HEADER_ZH.format(
            title=prod['name'],
            desc=prod.get('description', '')[:100],
            extra_x_data=f", activeImage: '{main_img}'"
        )
        
        html += f"""
        <div class="max-w-[1440px] mx-auto px-6 lg:px-10 py-4">
            <nav class="text-sm text-[#666]">
                <a href="/zh-tw/" class="hover:text-[#2E8B57]">首頁</a> <span class="mx-2">›</span> 
                <a href="/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a> <span class="mx-2">›</span> 
                <a href="/zh-tw/products/{cat_id}.html" class="hover:text-[#2E8B57]">{category_names_zh[cat_id]}</a> <span class="mx-2">›</span> 
                <span class="text-[#1A5C38] font-medium">{prod['name']}</span>
            </nav>
        </div>

        <section class="max-w-[1440px] mx-auto px-6 lg:px-10 pb-20">
            <div class="grid lg:grid-cols-2 gap-16 items-start">
                <div class="space-y-4">
                    <div class="rounded-2xl overflow-hidden shadow-premium-lg bg-white aspect-[4/3] flex items-center justify-center">
                        <img :src="activeImage" alt="{prod['name']}" class="w-full h-full object-contain p-4">
                    </div>
                    <div class="grid grid-cols-4 gap-4">{"".join(gal_bits)}</div>
                </div>
                <div>
                    <span class="inline-block text-xs font-bold tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-4">{category_names_zh[cat_id]}</span>
                    <h1 class="font-['Noto_Serif_TC',serif] text-3xl md:text-4xl font-bold mb-6">{prod['name']}</h1>
                    <p class="text-[#555] text-lg leading-relaxed mb-8">{prod.get('description', '專業食品級包裝解決方案。')}</p>
                    <div class="bg-white rounded-2xl p-8 shadow-premium mb-8">
                        <h2 class="font-['Noto_Serif_TC',serif] text-xl font-bold mb-6 border-b border-gray-100 pb-4">產品特點與規格</h2>
                        <div class="text-[#555] whitespace-pre-line leading-loose">{prod.get('specs', prod.get('specification', '請聯繫我們獲取詳細規格。'))}</div>
                    </div>
                    <div class="flex flex-wrap gap-4"><a href="/zh-tw/contact.html" class="btn-primary"><span>索取報價</span></a></div>
                </div>
            </div>
        </section>
        """
        html += FOOTER_ZH
        
        with open(os.path.join(cat_dir, slug), 'w', encoding='utf-8') as f:
            f.write(html)

# 4. Generate Category Landing Pages
for cat_id, products in categories_map.items():
    cards = []
    for prod in products:
        slug = slugify(prod['name']) + '.html'
        card = f"""
        <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
            <div class="aspect-[4/3] overflow-hidden bg-white flex items-center justify-center">
                <img src="{prod['images'][0]}" alt="{prod['name']}" class="w-full h-full object-contain p-4 group-hover:scale-105 transition-transform duration-500">
            </div>
            <div class="p-5">
                <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">{category_names_zh[cat_id]}</span>
                <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">{prod['name']}</h3>
                <a href="/zh-tw/products/{cat_id}/{slug}" class="text-[#1A5C38] font-semibold text-sm">查看詳情 →</a>
            </div>
        </div>"""
        cards.append(card)

    html = HEADER_ZH.format(title=category_names_zh[cat_id], desc=f"壯佳果{category_names_zh[cat_id]}系列", extra_x_data="")
    html += f"""
    <div class="max-w-[1440px] mx-auto px-6 lg:px-10 py-4">
        <nav class="text-sm text-[#666]"><a href="/zh-tw/" class="hover:text-[#2E8B57]">首頁</a> <span class="mx-2">›</span> <a href="/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a> <span class="mx-2">›</span> <span class="text-[#1A5C38] font-medium">{category_names_zh[cat_id]}</span></nav>
    </div>
    <section class="max-w-[1440px] mx-auto px-6 lg:px-10 pb-12">
        <h1 class="font-['Noto_Serif_TC',serif] text-4xl md:text-5xl font-bold mb-6">{category_names_zh[cat_id]}</h1>
    </section>
    <section class="max-w-[1440px] mx-auto px-6 lg:px-10 pb-20">
        <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">{"".join(cards)}</div>
    </section>
    """
    html += FOOTER_ZH
    
    with open(f"zh-tw/products/{cat_id}.html", 'w', encoding='utf-8') as f:
        f.write(html)

print("Bulk generation complete for all categories.")
