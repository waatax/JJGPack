import json
import os
import re
from pathlib import Path

# --- CONFIGURATION ---
BASE_URL = "/JJGPack/"

# --- DATA ---
# (Extracted from bulk_generate_all.py and greaseproof_data.json)

with open('greaseproof_data.json', 'r', encoding='utf-8') as f:
    greaseproof_data = json.load(f)

CATEGORIES = {
    'greaseproof': {
        'en': 'Greaseproof Paper Bag',
        'zh': '防油紙袋',
        'desc_en': 'Professional grease-resistant packaging for bakery and fast food.',
        'desc_zh': '專業防油包裝，適用於烘焙和速食產品。',
        'items': greaseproof_data
    },
    'kraft': {
        'en': 'Brown Kraft Bag',
        'zh': '牛皮紙袋',
        'desc_en': 'Eco-friendly and durable brown kraft paper bags for retail and food.',
        'desc_zh': '環保耐用的牛皮紙袋，適用於零售和食品。',
        'items': [
            {"name": "To-Go SOS Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/4.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/8.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/12.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Square_Bag/Square_bag.JPG"], "description": "Ideal for take-away and delivery.", "specs": "Sizes: 4#, 6#, 8#, 10#, 12#, 20#. Features: High-quality brown kraft. Customizable printing."},
            {"name": "Merchandise Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/841.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/842.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/843.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Merchandise_Bags/844.jpg"], "description": "Standard merchandise bags for general retail.", "specs": "Features: Offered in a variety of sizes. High-quality white and brown kraft. Customizable logo printing."},
            {"name": "Bakery window bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/france_bakery_bag_01.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Bakery_Bag/IMG_1829_LR.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/france_bakery_bag_03.jpg"], "description": "Bakery window bag with clear display.", "specs": "Natural Kraft paper, PE laminated, grease-resistant. Transparent window. Ideal for bakeries."},
            {"name": "Baguette Bakery bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Brown_kraft_bag-bakery_bag1.JPG", "https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Brown_kraft_bag-bakery_bag2.JPG"], "description": "Long bags specifically for baguettes.", "specs": "Natural Kraft paper, PE laminated, grease-resistant. Ideal for French baguettes."},
            {"name": "Flat Handle Grocery Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Brown_Carry_Paper_Bag/carry_bag_1.jpg", "https://www.jjgpaperbag.com/proimages/sr/product/Brown_Carry_Paper_Bag/carry_bag_2.jpg"], "description": "Eco-friendly, sturdy flat handles.", "specs": "Eco-friendly, sturdy flat handles. Suitable for grocery and take-out."},
            {"name": "Die Cut Handle bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Die_cut_handle-bag1.JPG", "https://www.jjgpaperbag.com/proimages/sr/product/Brown_Kraft_Bag/Die_cut_handle-bag2.JPG"], "description": "Die-cut handles for easy carrying.", "specs": "Die-cut handles for easy carrying. Clean and modern look."},
            {"name": "SOS White Take Out Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/SOS-White-Take-Out-Bags-3.jpg"], "description": "Clean white take out bags.", "specs": "4#: W127xH245xG77 (1,500pcs/CTN). 8#: W156xH312xG102 (1,000pcs/CTN)."},
            {"name": "Cream Color Square Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/Cream-Color--Square-Bag-1.jpg", "https://www.jjgpaperbag.com/proimages/sr/Cream-Color--Square-Bag-3.jpg"], "description": "Elegant cream color options.", "specs": "Kraft Handle Bag: W210xH275xG90 (400pcs). Square Bag(12#): W190xH300xG110 (500pcs)."},
            {"name": "8# Square Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/8號方袋.jpg"], "description": "Standard 8# square bottom bag.", "specs": "Multiple SKUs (S8001-S8021). Range of sizes available."},
            {"name": "Christmas Series Square Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/聖誕節方袋.jpg"], "description": "Festive holiday designs.", "specs": "Holiday themed prints on square bottom bags."},
            {"name": "Hexagonal Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/0901-2.jpg"], "description": "Unique hexagonal base for better stability.", "specs": "Patented hexagonal bottom design for unique packaging needs."},
            {"name": "Bakery Series Paper Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/烘焙麵包窗袋.jpg"], "description": "Complete collection for bakeries.", "specs": "Natural Kraft paper, PE laminated, grease-resistant. Visible window."}
        ]
    },
    'flat-handle': {
        'en': 'Flat Handle Paper Bag',
        'zh': '平把手提袋',
        'desc_en': 'Comfortable and strong flat handle bags for shopping and takeaway.',
        'desc_zh': '舒適且堅固的平把手提袋，適用於購物和外送。',
        'items': [
            {"name": "Flat Handle Paper Bag", "images": ["/JJGPack/proimages/detail/flat-handle-bag.jpg"], "description": "High stability, comfortable grip, food-grade water-based ink.", "specs": "Standard flat handle grocery bag."},
            {"name": "Single Color Shopping Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/112.01.06-JJG-PACK-Single-Color-Shopping-Bags-1.jpg"], "description": "Shopping Bag. Paper Material: Brown Virgin / 100% Recycled Kraft.", "specs": "CM4~CM7: Up to 4 colors on 4 sides. 1/6BBL: Up to 3 colors on 4 sides."},
            {"name": "Cream Color Flat Handle Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/Cream-Color-Flat-Handle-Bag-1.jpg", "https://www.jjgpaperbag.com/proimages/sr/Cream-Color-Flat-Handle-Bag-2.jpg"], "description": "Premium cream color finish.", "specs": "CM01/CM02: 210x275x90 mm, 400pcs."},
            {"name": "Macaron Color Flat Handle Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/Macaron-Color-Flat-Handle-Bag-1.jpg", "https://www.jjgpaperbag.com/proimages/sr/Macaron-Color-Flat-Handle-Bag-2.jpg", "https://www.jjgpaperbag.com/proimages/sr/Macaron-Color-Flat-Handle-Bag-3.jpg"], "description": "Vibrant macaron colors for a modern look.", "specs": "Size: 210x275x90 mm, 400pcs."},
            {"name": "Christmas Series Flat Handle Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/聖誕CM4提袋-1-2.jpg", "https://www.jjgpaperbag.com/proimages/sr/聖誕CM4提袋-2-2.jpg"], "description": "Special edition holiday designs.", "specs": "CM4-3: 220x235x120 (400pcs). S8275-1: 156x312x102 (1,500pcs). S12A275-1: 190x350x120 (1,000pcs)."},
            {"name": "Recycled Kraft Flat handle Sacks", "images": ["https://www.jjgpaperbag.com/proimages/sr/環牛扁把提袋-1.jpg"], "description": "High-strength recycled kraft.", "specs": "1/7 BBL: 305x170x355 (300 Qty). 1/6 BBL: 305x170x425 (300 Qty)."}
        ]
    },
    'white-kraft': {
        'en': 'White Kraft Bag',
        'zh': '白牛皮紙袋',
        'desc_en': 'Clean and elegant white kraft paper bags for premium packaging.',
        'desc_zh': '潔淨優雅的白牛皮紙袋，適用於高端包裝。',
        'items': [
            {"name": "White Kraft Paper Bag", "images": ["/JJGPack/proimages/detail/white-kraft-bag.png"], "description": "Premium white kraft, clean appearance for retail and medical use.", "specs": "High quality white kraft paper."},
            {"name": "White Kraft Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/JJG-B1.png"], "description": "High-quality white kraft material.", "specs": "White#1 to White#6, Material: White kraft, 50g, various dimensions."},
            {"name": "Recycled Kraft Grocery Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/環方-3.jpg"], "description": "Eco-friendly grocery bags.", "specs": "4275-R L3: 127x245x77. 8260-R L3: 156x312x102."},
            {"name": "New Flate Handle Paper Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/114.03.03-全新扁把提袋（COFFEE款）.jpg"], "description": "Modern flat handle designs.", "specs": "CM4-R3: 220x235x120mm. CM4-S2: 220x235x120mm."},
            {"name": "Take Out Bags Square Bottom Paper Bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/114.03.04-爆脆方袋.jpg"], "description": "Special crispy fried food bags.", "specs": "CRIX08 size."}
        ]
    },
    'aluminum-foil': {
        'en': 'Aluminum Foil Bag',
        'zh': '鋁箔紙袋',
        'desc_en': 'Heat-insulating aluminum foil lined bags for warm food delivery.',
        'desc_zh': '保溫鋁箔內襯袋，適用於熱食外送。',
        'items': [
            {"name": "Aluminum Foil Paper Bag", "images": ["/JJGPack/proimages/detail/aluminum-foil-bag.png"], "description": "Excellent heat retention for roasted chicken and takeaways.", "specs": "Standard aluminum foil lined heat retention bag."},
            {"name": "Aluminum Foil Lined Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/pro5-1.png"], "description": "Excellent heat retention.", "specs": "JUMBO/XL/L/S and LONG1/2 sizes. Material: Aluminum Foil, 67g."}
        ]
    },
    'pe-lamination': {
        'en': 'PE-Lamination Bag',
        'zh': '淋膜紙袋',
        'desc_en': 'Leak-proof PE-laminated bags for greasy and moist foods.',
        'desc_zh': '防漏 PE 淋膜袋，適用於油膩和潮濕的食品。',
        'items': [
            {"name": "Burger Pocket L-Bag", "images": ["/JJGPack/proimages/detail/l-bag.jpg"], "description": "Leak-proof and grease-resistant burger and sandwich pocket.", "specs": "Standard PE laminated L-bag."},
            {"name": "Burger pocket paper bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/PE-Lamination-paper-1.jpg"], "description": "Perfect for burgers and sandwiches.", "specs": "LS1919-1PE: W190xH190. BL1-1515SL: W150xH150. PE-Lamination, 43g."},
            {"name": "Deli Wrap Paper", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/pro3-2.png"], "description": "Multi-purpose deli wrapping sheets.", "specs": "Sizes: 300x300, 200x200. PE-Lamination, 43g."},
            {"name": "Toast Bags", "images": ["https://www.jjgpaperbag.com/proimages/sr/0901-4.jpg"], "description": "Reliable toast and snack bags.", "specs": "Standard V-shape sizes."}
        ]
    },
    'paper-straw': {
        'en': 'Paper Straw',
        'zh': '紙吸管',
        'desc_en': 'Eco-friendly and biodegradable paper straws for a greener planet.',
        'desc_zh': '環保且可生物降解的紙吸管，為地球盡一份心力。',
        'items': [
            {"name": "Biodegradable Paper Straw", "images": ["/JJGPack/proimages/detail/paper-straw.jpg"], "description": "100% Taiwan made, plastic-free, eco-friendly drinking solution.", "specs": "Standard paper straw."},
            {"name": "Paper Straw (Brown)", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Paper_straw/IMG_5540_s.jpg"], "description": "Durable and sustainable brown paper straws.", "specs": "Flat and Blade Design. Made in Taiwan."},
            {"name": "Biodegradable Bamboo Straw", "images": ["https://www.jjgpaperbag.com/proimages/sr/竹吸-1.jpg"], "description": "Natural bamboo alternative.", "specs": "Bamboo material."}
        ]
    },
    'fruit-protection': {
        'en': 'Fruit Protection Bag',
        'zh': '水果套袋',
        'desc_en': 'High-quality protection bags for growing fruits like mangoes and grapes.',
        'desc_zh': '高品質的水果套袋，適用於芒果、葡萄等水果。',
        'items': [
            {"name": "Mango Protection Bag", "images": ["/JJGPack/proimages/detail/mango-bag.jpg"], "description": "Double-layer protection from pests and weather for growing fruits.", "specs": "Specially designed for mango protection. Double-layer paper. High pest resistance."}
        ]
    },
    'others': {
        'en': 'Other Products',
        'zh': '其他產品',
        'desc_en': 'Placemats, specialty bags, and custom packaging solutions.',
        'desc_zh': '餐墊紙、特殊袋類和定制包裝解決方案。',
        'items': [
            {"name": "Custom & Specialty Bags", "images": ["/JJGPack/proimages/detail/bakery-side-window.jpg"], "description": "Bespoke solutions for unique requirements and custom material needs.", "specs": "Contact us for custom requests."},
            {"name": "Paper Placement", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Paper_placement.jpg"], "description": "Customizable paper placemats for restaurants.", "specs": "DF60-4028: W400xH280, 2,250/Carton."},
            {"name": "Bakery side window bag", "images": ["https://www.jjgpaperbag.com/proimages/sr/product/Bakery_side_window_bag_01.jpg"], "description": "Extra visibility for bakery items.", "specs": "BV2W124S: W145xH240xG45, 2,000/Carton."},
            {"name": "Wonderful Time Paper Placemats", "images": ["https://www.jjgpaperbag.com/proimages/sr/餐墊紙1.jpg"], "description": "Pre-printed stylish placemats.", "specs": "P004-P102: 400x280 or 390x280 mm."}
        ]
    }
}

# --- TEMPLATES ---

NAV_EN = """
      <div class="hidden lg:flex items-center gap-1">
        <a href="/JJGPack/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Home</a>
        <a href="/JJGPack/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">About Us</a>
        <a href="/JJGPack/products.html" class="px-4 py-2 text-[#1A5C38] font-semibold text-[15px] relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-5 after:h-0.5 after:bg-[#1A5C38] after:rounded-full">Products</a>
        <a href="/JJGPack/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">News</a>
        <a href="/JJGPack/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">E-Catalog</a>
        <a href="/JJGPack/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">Contact Us</a>
      </div>
"""

NAV_ZH = """
      <div class="hidden lg:flex items-center gap-1">
        <a href="/JJGPack/zh-tw/index.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">首頁</a>
        <a href="/JJGPack/zh-tw/about.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">關於我們</a>
        <a href="/JJGPack/zh-tw/products.html" class="px-4 py-2 text-[#1A5C38] font-semibold text-[15px] relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-5 after:h-0.5 after:bg-[#1A5C38] after:rounded-full">產品介紹</a>
        <a href="/JJGPack/zh-tw/news.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">最新消息</a>
        <a href="/JJGPack/zh-tw/catalog.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">型錄EDM</a>
        <a href="/JJGPack/zh-tw/contact.html" class="px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all">聯絡我們</a>
      </div>
"""

HEADER = """<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | JJG Pack - 壯佳果包裝</title>
  <link rel="icon" href="/JJGPack/images/favicon.ico" />
  <script type="module" src="/JJGPack/main.js"></script>
  <link rel="stylesheet" href="/JJGPack/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&family=Noto+Serif+TC:wght@700;900&family=Playfair+Display:wght@400;700;900&display=swap" rel="stylesheet">
</head>
<body x-data="{{ mobileMenu: false {extra_x_data} }}" class="bg-[#F5F0E8] text-[#1A1A1A] font-['Inter','Noto_Sans_TC',sans-serif]">
  <header class="fixed top-0 left-0 right-0 z-50 glass transition-all duration-500">
    <nav class="max-w-[1440px] mx-auto px-6 h-[92px] flex items-center justify-between">
      <a href="{home_link}" class="flex items-center gap-3"><img src="/JJGPack/images/index-logo.png" alt="JJG" class="h-[62px]"></a>
      {nav_html}
      <div class="hidden lg:flex items-center gap-5">
        <div class="flex items-center gap-1 text-sm">
          <a href="{en_link}" class="{en_class}">EN</a>
          <a href="{zh_link}" class="{zh_class}">繁中</a>
        </div>
        <a href="{contact_link}" class="btn-primary text-sm !py-2.5 !px-6 !rounded-lg"><span>{contact_text}</span></a>
      </div>
      <button @click="mobileMenu=!mobileMenu" class="lg:hidden p-2"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg></button>
    </nav>
  </header>
  <div class="pt-[92px]">
"""

FOOTER = """
  </div>
  <footer class="bg-[#111] text-gray-400 pt-20 pb-8">
    <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-12 pb-12 border-b border-white/10">
        <div><img src="/JJGPack/images/index-logo.png" alt="JJG" class="h-[68px] mb-5 brightness-200"><p class="text-sm leading-relaxed text-gray-500">{footer_desc}</p></div>
        <div><h4 class="text-white font-bold mb-5 text-sm tracking-[0.15em] uppercase">{quick_links}</h4><ul class="space-y-3 text-sm"><li><a href="{home_link}" class="hover:text-[#2E8B57] transition">{home_text}</a></li><li><a href="{products_link}" class="hover:text-[#2E8B57] transition">{products_text}</a></li><li><a href="{contact_link}" class="hover:text-[#2E8B57] transition">{contact_text}</a></li></ul></div>
        <div><h4 class="text-white font-bold mb-5 text-sm tracking-[0.15em] uppercase">{footer_products}</h4><ul class="space-y-3 text-sm"><li><a href="{products_link}" class="hover:text-[#2E8B57] transition">{all_products}</a></li></ul></div>
        <div><h4 class="text-white font-bold mb-5 text-sm tracking-[0.15em] uppercase">{contact_info}</h4><ul class="space-y-4 text-sm"><li>📍 No.6, You 9th Rd. Dajia Dist., Taichung City 43769 Taiwan</li><li>📞 +886-4-26223215</li><li>✉️ export@jjgpaperbag.com</li></ul></div>
      </div>
      <div class="pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-xs text-gray-600">© 2026 壯佳果股份有限公司 Juang Jia Guoo Co., Ltd. All rights reserved.</p>
        <div class="flex gap-4 text-xs text-gray-600"><a href="/JJGPack/zh-tw/index.html" class="hover:text-[#2E8B57] transition">繁體中文</a><span>|</span><a href="/JJGPack/index.html" class="hover:text-[#2E8B57] transition">English</a></div>
      </div>
    </div>
  </footer>
</body>
</html>
"""

# --- UTILS ---

def slugify(text):
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-').replace('--', '-').replace('#', '').strip('-')

def write_page(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# --- GENERATION ---

def generate():
    for cat_id, cat_data in CATEGORIES.items():
        # EN CATEGORY PAGE
        gen_category_page(cat_id, cat_data, 'en')
        # ZH CATEGORY PAGE
        gen_category_page(cat_id, cat_data, 'zh')
        
        # INDIVIDUAL PRODUCTS
        for prod in cat_data['items']:
            gen_product_page(cat_id, prod, 'en')
            gen_product_page(cat_id, prod, 'zh')

def gen_category_page(cat_id, cat_data, lang):
    is_zh = (lang == 'zh')
    title = cat_data['zh'] if is_zh else cat_data['en']
    desc = cat_data['desc_zh'] if is_zh else cat_data['desc_en']
    
    home_link = "/JJGPack/zh-tw/index.html" if is_zh else "/JJGPack/index.html"
    nav_html = NAV_ZH if is_zh else NAV_EN
    en_link = "/JJGPack/products.html" # Simple toggle back
    zh_link = "/JJGPack/zh-tw/products.html"
    en_class = "text-[#888] hover:text-[#1A5C38]" if is_zh else "text-[#1A5C38] font-semibold"
    zh_class = "text-[#1A5C38] font-semibold" if is_zh else "text-[#888] hover:text-[#1A5C38]"
    contact_link = "/JJGPack/zh-tw/contact.html" if is_zh else "/JJGPack/contact.html"
    contact_text = "聯絡我們" if is_zh else "Contact Us"
    
    header = HEADER.format(
        lang="zh-TW" if is_zh else "en",
        title=title,
        home_link=home_link,
        nav_html=nav_html,
        en_link=en_link,
        zh_link=zh_link,
        en_class=en_class,
        zh_class=zh_class,
        contact_link=contact_link,
        contact_text=contact_text,
        extra_x_data=""
    )
    
    cards_html = ""
    for prod in cat_data['items']:
        slug = slugify(prod['name']) + '.html'
        prod_link = f"/JJGPack/{'zh-tw/' if is_zh else ''}products/{cat_id}/{slug}"
        img = prod['images'][0] if prod['images'] else "/JJGPack/images/placeholder.jpg"
        
        cards_html += f"""
        <div class="bg-white rounded-2xl overflow-hidden shadow-premium card-hover group">
          <a href="{prod_link}" class="aspect-[4/3] overflow-hidden block">
            <img src="{img}" alt="{prod['name']}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </a>
          <div class="p-7">
            <span class="inline-block text-xs font-bold uppercase tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-3">{title}</span>
            <h3 class="font-['Playfair_Display',serif] text-xl font-bold mb-2 group-hover:text-[#1A5C38] transition">{prod['name']}</h3>
            <p class="text-sm text-[#666] mb-5 line-clamp-2">{prod.get('description', '')}</p>
            <a href="{prod_link}" class="inline-flex items-center gap-2 text-[#1A5C38] font-bold text-sm group-hover:gap-3 transition-all">
              {"查看詳情" if is_zh else "View Details"}
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
            </a>
          </div>
        </div>"""
        
    body = f"""
    <section class="max-w-[1440px] mx-auto px-6 py-12">
      <nav class="text-sm text-[#666] mb-8">
        <a href="{home_link}" class="hover:text-[#1A5C38]">{"首頁" if is_zh else "Home"}</a> <span class="mx-2">›</span> 
        <a href="/JJGPack/{'zh-tw/' if is_zh else ''}products.html" class="hover:text-[#1A5C38]">{"產品介紹" if is_zh else "Products"}</a> <span class="mx-2">›</span> 
        <span class="text-[#1A5C38] font-medium">{title}</span>
      </nav>
      <h1 class="font-['Playfair_Display',serif] text-4xl md:text-5xl font-bold mb-4">{title}</h1>
      <p class="text-lg text-[#666] max-w-2xl mb-12">{desc}</p>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        {cards_html}
      </div>
    </section>
    """
    
    footer = FOOTER.format(
        footer_desc="壯佳果股份有限公司 — 台灣專業紙袋製造商，擁有 70 多年的生產經驗。" if is_zh else "Professional paper bag manufacturer in Taiwan with 70+ years of experience.",
        quick_links="快速連結" if is_zh else "Quick Links",
        home_text="首頁" if is_zh else "Home",
        home_link=home_link,
        products_text="產品介紹" if is_zh else "Products",
        products_link=f"/JJGPack/{'zh-tw/' if is_zh else ''}products.html",
        contact_text=contact_text,
        contact_link=contact_link,
        footer_products="產品系列" if is_zh else "Products",
        all_products="所有產品" if is_zh else "All Products",
        contact_info="聯絡資訊" if is_zh else "Contact Info"
    )
    
    dest_path = f"zh-tw/products/{cat_id}.html" if is_zh else f"products/{cat_id}.html"
    write_page(dest_path, header + body + footer)

def gen_product_page(cat_id, prod, lang):
    is_zh = (lang == 'zh')
    cat_title = CATEGORIES[cat_id]['zh'] if is_zh else CATEGORIES[cat_id]['en']
    
    home_link = "/JJGPack/zh-tw/index.html" if is_zh else "/JJGPack/index.html"
    nav_html = NAV_ZH if is_zh else NAV_EN
    en_link = "/JJGPack/products.html"
    zh_link = "/JJGPack/zh-tw/products.html"
    en_class = "text-[#888] hover:text-[#1A5C38]" if is_zh else "text-[#1A5C38] font-semibold"
    zh_class = "text-[#1A5C38] font-semibold" if is_zh else "text-[#888] hover:text-[#1A5C38]"
    contact_link = "/JJGPack/zh-tw/contact.html" if is_zh else "/JJGPack/contact.html"
    contact_text = "聯絡我們" if is_zh else "Contact Us"
    
    main_img = prod['images'][0] if prod['images'] else "/JJGPack/images/placeholder.jpg"
    
    header = HEADER.format(
        lang="zh-TW" if is_zh else "en",
        title=prod['name'],
        home_link=home_link,
        nav_html=nav_html,
        en_link=en_link,
        zh_link=zh_link,
        en_class=en_class,
        zh_class=zh_class,
        contact_link=contact_link,
        contact_text=contact_text,
        extra_x_data=f", activeImage: '{main_img}'"
    )
    
    thumbs_html = ""
    for img in prod['images']:
        thumbs_html += f"""
        <button @click="activeImage='{img}'" class="aspect-square rounded-xl overflow-hidden border-2 transition" :class="activeImage==='{img}' ? 'border-[#1A5C38] shadow-md' : 'border-transparent hover:border-gray-200'">
          <img src="{img}" class="w-full h-full object-cover">
        </button>"""
        
    specs = prod.get('specification', prod.get('specs', 'Please contact us for details.' if not is_zh else '請聯繫我們獲取詳情。'))
    
    body = f"""
    <section class="max-w-[1440px] mx-auto px-6 py-8">
      <nav class="text-sm text-[#666] mb-10">
        <a href="{home_link}" class="hover:text-[#1A5C38]">{"首頁" if is_zh else "Home"}</a> <span class="mx-2">›</span> 
        <a href="/JJGPack/{'zh-tw/' if is_zh else ''}products.html" class="hover:text-[#1A5C38]">{"產品介紹" if is_zh else "Products"}</a> <span class="mx-2">›</span> 
        <a href="/JJGPack/{'zh-tw/' if is_zh else ''}products/{cat_id}.html" class="hover:text-[#1A5C38]">{cat_title}</a> <span class="mx-2">›</span> 
        <span class="text-[#1A5C38] font-medium">{prod['name']}</span>
      </nav>

      <div class="grid lg:grid-cols-2 gap-16 items-start">
        <div class="space-y-6">
          <div class="bg-white rounded-3xl overflow-hidden shadow-premium aspect-[4/3] flex items-center justify-center p-4">
            <img :src="activeImage" alt="{prod['name']}" class="w-full h-full object-contain">
          </div>
          <div class="grid grid-cols-4 sm:grid-cols-5 gap-4">
            {thumbs_html}
          </div>
        </div>
        
        <div class="animate-fade-in-right">
          <span class="inline-block text-xs font-bold uppercase tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-4 py-1.5 rounded-full mb-6">{cat_title}</span>
          <h1 class="font-['Playfair_Display',serif] text-4xl md:text-5xl font-bold mb-6">{prod['name']}</h1>
          <p class="text-lg text-[#555] leading-relaxed mb-10">{prod.get('description', '')}</p>
          
          <div class="bg-white rounded-2xl p-8 shadow-premium mb-10 border border-gray-100">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-2">
              <svg class="w-5 h-5 text-[#1A5C38]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
              {"Specifications" if not is_zh else "產品規格"}
            </h2>
            <div class="text-[#555] whitespace-pre-line leading-relaxed space-y-2">
              {specs}
            </div>
          </div>
          
          <div class="flex flex-wrap gap-4">
            <a href="{contact_link}" class="btn-primary !px-10"><span>{"Get a Quote" if not is_zh else "索取報價"}</span></a>
            <a href="mailto:export@jjgpaperbag.com" class="btn-outline">{"Email Inquiry" if not is_zh else "郵件諮詢"}</a>
          </div>
        </div>
      </div>
    </section>
    """
    
    footer = FOOTER.format(
        footer_desc="壯佳果股份有限公司 — 台灣專業紙袋製造商，擁有 70 多年的生產經驗。" if is_zh else "Professional paper bag manufacturer in Taiwan with 70+ years of experience.",
        quick_links="快速連結" if is_zh else "Quick Links",
        home_text="首頁" if is_zh else "Home",
        home_link=home_link,
        products_text="產品介紹" if is_zh else "Products",
        products_link=f"/JJGPack/{'zh-tw/' if is_zh else ''}products.html",
        contact_text=contact_text,
        contact_link=contact_link,
        footer_products="產品系列" if is_zh else "Products",
        all_products="所有產品" if is_zh else "All Products",
        contact_info="聯絡資訊" if is_zh else "Contact Info"
    )
    
    slug = slugify(prod['name']) + '.html'
    dest_path = f"zh-tw/products/{cat_id}/{slug}" if is_zh else f"products/{cat_id}/{slug}"
    write_page(dest_path, header + body + footer)

if __name__ == "__main__":
    generate()
    print("Generation complete.")
