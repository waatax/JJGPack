import json
import os

# 1. Load Data
try:
    with open('greaseproof_data.json', 'r', encoding='utf-8') as f:
        greaseproof_data = json.load(f)
except FileNotFoundError:
    greaseproof_data = []

# Manually define the other data from the scratchpad extraction
categories_data = {
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

# 2. Config
BASE_URL = '/'

category_names = {
    'zh-tw': {
        'greaseproof': "防油紙袋",
        'kraft': "牛皮紙袋",
        'flathandle': "平把手提袋",
        'white': "白牛皮紙袋",
        'foil': "鋁箔紙袋",
        'pe': "淋膜紙袋",
        'straw': "紙吸管",
        'others': "其他產品"
    },
    'en': {
        'greaseproof': "Greaseproof Bags",
        'kraft': "Brown Kraft Bags",
        'flathandle': "Flat Handle Bags",
        'white': "White Kraft Bags",
        'foil': "Aluminum Foil Bags",
        'pe': "PE-Lamination Bags",
        'straw': "Paper Straws",
        'others': "Other Products"
    }
}

nav_labels = {
    'zh-tw': {"home": "首頁", "about": "關於我們", "products": "產品介紹", "news": "最新消息", "contact": "聯絡我們", "lang": "繁中"},
    'en': {"home": "Home", "about": "About", "products": "Products", "news": "News", "contact": "Contact", "lang": "EN"}
}

def slugify(text):
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-').replace('--', '-').replace('#', '').strip('-')

# 3. HTML Template Generator
def generate_html(lang, title, content, extra_x_data="", current_path=""):
    other_lang = 'en' if lang == 'zh-tw' else 'zh-tw'
    
    # Path logic for lang switcher
    if lang == 'zh-tw':
        en_path = current_path.replace("zh-tw/", "")
        zh_path = current_path
    else:
        en_path = current_path
        zh_path = "zh-tw/" + current_path
    
    if en_path == "": en_path = "index.html"
    
    header = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | JJG Paper Bag</title>
    <link rel="icon" href="{BASE_URL}images/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700&display=swap" rel="stylesheet">
    <link href="{BASE_URL}style.css" rel="stylesheet">
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body x-data="{{ mobileMenu: false {extra_x_data} }}" class="bg-[#F5F0E8] text-[#1A1A1A] font-['Inter','Noto_Sans_TC',sans-serif]">
    <header class="fixed top-0 left-0 right-0 z-50 glass">
        <nav class="max-w-[1440px] mx-auto px-6 lg:px-10 h-[76px] flex items-center justify-between">
            <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}index.html">
                <img src="{BASE_URL}images/index-logo.png" alt="JJG" class="h-11">
            </a>
            <div class="hidden lg:flex items-center gap-1">
                <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px]">{nav_labels[lang]['home']}</a>
                <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px]">{nav_labels[lang]['about']}</a>
                <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}products.html" class="px-4 py-2 text-[#1A5C38] font-semibold text-[15px]">{nav_labels[lang]['products']}</a>
                <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px]">{nav_labels[lang]['news']}</a>
                <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px]">{nav_labels[lang]['contact']}</a>
            </div>
            <div class="hidden lg:flex items-center gap-5">
                <a href="{BASE_URL}{en_path}" class="text-sm {'text-[#1A5C38] font-bold' if lang=='en' else 'text-[#888]'}">EN</a>
                <a href="{BASE_URL}{zh_path}" class="text-sm {'text-[#1A5C38] font-bold' if lang=='zh-tw' else 'text-[#888]'}">繁中</a>
                <a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}contact.html" class="btn-primary text-sm !py-2.5 !px-6 !rounded-lg"><span>{nav_labels[lang]['contact']}</span></a>
            </div>
            <button @click="mobileMenu=!mobileMenu" class="lg:hidden p-2"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg></button>
        </nav>
    </header>
    <div class="pt-[76px] min-h-[80vh]">
        {content}
    </div>
    <footer class="bg-[#111] text-gray-400 pt-16 pb-8">
        <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
            <div class="grid md:grid-cols-4 gap-10 pb-10 border-b border-white/10">
                <div><img src="{BASE_URL}images/index-logo.png" alt="JJG" class="h-10 mb-4 brightness-200"></div>
                <div><h4 class="text-white font-bold mb-4 text-sm">{nav_labels[lang]['home']}</h4><ul class="space-y-2 text-sm"><li><a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}products.html" class="hover:text-[#2E8B57]">{nav_labels[lang]['products']}</a></li></ul></div>
                <div><h4 class="text-white font-bold mb-4 text-sm">Links</h4><ul class="space-y-2 text-sm"><li><a href="{BASE_URL}{'zh-tw/' if lang=='zh-tw' else ''}contact.html" class="hover:text-[#2E8B57]">{nav_labels[lang]['contact']}</a></li></ul></div>
            </div>
            <div class="pt-6 text-center text-xs text-gray-600">© 2026 JJG Paper Bag</div>
        </div>
    </footer>
</body>
</html>"""
    return header

# 4. Generator Loop
for lang in ['en', 'zh-tw']:
    for cat_id, products in categories_data.items():
        # A. Category Listing Page
        cat_file_path = f"{'' if lang=='en' else 'zh-tw/'}products/{cat_id}.html"
        os.makedirs(os.path.dirname(cat_file_path), exist_ok=True)
        
        cards = []
        for prod in products:
            prod_slug = slugify(prod['name'])
            prod_path = f"{'' if lang=='en' else 'zh-tw/'}products/{cat_id}/{prod_slug}.html"
            card = f"""
            <div class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 group">
                <div class="aspect-[4/3] overflow-hidden bg-white flex items-center justify-center p-4">
                    <img src="{prod['images'][0]}" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-5">
                    <h3 class="font-bold text-lg mb-2">{prod['name']}</h3>
                    <a href="{BASE_URL}{prod_path}" class="text-[#1A5C38] font-bold text-sm">{'View Details' if lang=='en' else '查看詳情'} →</a>
                </div>
            </div>"""
            cards.append(card)
            
        cat_content = f"""
        <div class="max-w-[1440px] mx-auto px-6 lg:px-10 py-12">
            <h1 class="text-4xl font-bold mb-8">{category_names[lang][cat_id]}</h1>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">{"".join(cards)}</div>
        </div>"""
        
        with open(cat_file_path, 'w', encoding='utf-8') as f:
            f.write(generate_html(lang, category_names[lang][cat_id], cat_content, current_path=cat_file_path))

        # B. Product Detail Pages
        prod_dir = f"{'' if lang=='en' else 'zh-tw/'}products/{cat_id}"
        os.makedirs(prod_dir, exist_ok=True)
        
        for prod in products:
            prod_slug = slugify(prod['name'])
            detail_path = f"{prod_dir}/{prod_slug}.html"
            main_img = prod['images'][0] if prod['images'] else ""
            
            gal_bits = [f'<button @click="activeImage=\'{img}\'" class="aspect-square border-2" :class="activeImage===\'{img}\' ? \'border-[#1A5C38]\' : \'border-transparent\'"><img src="{img}" class="w-full h-full object-cover"></button>' for img in prod['images']]
            
            detail_content = f"""
            <div class="max-w-[1440px] mx-auto px-6 lg:px-10 py-12">
                <div class="grid lg:grid-cols-2 gap-16">
                    <div class="space-y-4">
                        <div class="bg-white rounded-2xl aspect-[4/3] flex items-center justify-center p-8 shadow-sm">
                            <img :src="activeImage" class="max-w-full max-h-full object-contain">
                        </div>
                        <div class="grid grid-cols-4 gap-4">{"".join(gal_bits)}</div>
                    </div>
                    <div>
                        <h1 class="text-4xl font-bold mb-6">{prod['name']}</h1>
                        <p class="text-lg text-gray-600 mb-8">{prod.get('description', '')}</p>
                        <div class="bg-white p-8 rounded-2xl shadow-sm mb-8">
                            <h2 class="text-xl font-bold mb-4">{'Specifications' if lang=='en' else '產品規格'}</h2>
                            <div class="whitespace-pre-line text-gray-700">{prod.get('specs', prod.get('specification', 'Contact us for details.'))}</div>
                        </div>
                        <a href="{BASE_URL}{'' if lang=='en' else 'zh-tw/'}contact.html" class="btn-primary inline-block"><span>{'Inquire Now' if lang=='en' else '立即詢價'}</span></a>
                    </div>
                </div>
            </div>"""
            
            with open(detail_path, 'w', encoding='utf-8') as f:
                f.write(generate_html(lang, prod['name'], detail_content, extra_x_data=f", activeImage: '{main_img}'", current_path=detail_path))

print("Regenerated all EN and ZH pages with fixed base-relative links and language switcher.")
