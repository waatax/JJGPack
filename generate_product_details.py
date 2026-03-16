import os

# Product data
products = [
    {
        "id": "bakery-side-window-bag",
        "category": "Greaseproof",
        "category_zh": "防油紙",
        "name": "Bakery Side Window Bag",
        "name_zh": "麵包側窗紙袋",
        "image": "/proimages/detail/bakery-side-window.jpg",
        "desc": "Natural Kraft / PE laminated greaseproof paper bag with a high-clarity transparent window. Perfect for displaying fresh bakery products while maintaining hygiene and freshness.",
        "desc_zh": "天然牛皮紙 / PE 淋膜防油紙袋，配有高透明度視窗。 非常適合展示新鮮烘焙產品，同時保持衛生和新鮮度。",
        "features": [
            "PE laminated for superior grease resistance",
            "High-clarity polypropylene window",
            "Food-grade material and ink",
            "Custom printing available (up to 6 colors)"
        ],
        "features_zh": [
            "PE 淋膜具有優異的防油性能",
            "高透明度聚丙烯視窗",
            "食品級材料和油墨",
            "可客製印刷（最多 6 色）"
        ],
        "specs": [
            {"label": "Material", "value": "Natural Kraft + PE + PP Window"},
            {"label": "Usage", "value": "Bakery, Donuts, Pastries"},
            {"label": "Size", "value": "Customizable"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "天然牛皮紙 + PE + PP 視窗"},
            {"label": "用途", "value": "麵包、甜甜圈、糕點"},
            {"label": "尺寸", "value": "可客製化"}
        ]
    },
    {
        "id": "square-paper-bag",
        "category": "Kraft",
        "category_zh": "牛皮紙",
        "name": "Square Bottom Paper Bag",
        "name_zh": "方底紙袋 (SOS)",
        "image": "/proimages/detail/square-bag.jpg",
        "desc": "Traditional square bottom paper bag (SOS bag) made from high-strength long-fiber kraft paper. The self-standing design makes it efficient for quick filling in retail and food service environments.",
        "desc_zh": "傳統方底紙袋（SOS 袋），由高強度長纖維牛皮紙製成。 自立式設計使其在零售和餐飲服務環境中能夠高效快速地填充。",
        "features": [
            "Self-standing for easy filling",
            "High-strength long-fiber kraft paper",
            "100% Recyclable and Biodegradable",
            "Available in various standard sizes"
        ],
        "features_zh": [
            "自立式，方便填充",
            "高強度長纖維牛皮紙",
            "100% 可回收且可生物分解",
            "提供多種標準尺寸"
        ],
        "specs": [
            {"label": "Material", "value": "Brown Kraft / White Kraft"},
            {"label": "Usage", "value": "Grocery, Retail, Takeout"},
            {"label": "Certification", "value": "FSC Optional"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "赤牛皮紙 / 白牛皮紙"},
            {"label": "用途", "value": "雜貨、零售、外帶"},
            {"label": "認證", "value": "可選 FSC"}
        ]
    },
    {
        "id": "flat-handle-bag",
        "category": "Flat Handle",
        "category_zh": "扁繩手提袋",
        "name": "Flat Handle Paper Bag",
        "name_zh": "扁繩手提紙袋",
        "image": "/proimages/detail/flat-handle-bag.jpg",
        "desc": "Durable shopping bag featuring comfortable flat handles. Made from premium kraft paper with strong adhesive bonding for reliable load-bearing capacity.",
        "desc_zh": "高品質手提袋，配有舒適的扁平提手。 由優質牛皮紙製成，採用強力粘合，具有可靠的承重能力。",
        "features": [
            "Comfortable flat handles",
            "Strong side and bottom gussets",
            "Water-based food-grade ink",
            "Eco-friendly alternative to plastic"
        ],
        "features_zh": [
            "舒適的扁平提手",
            "強韌的側邊和底邊設計",
            "水性食品級油墨",
            "塑料袋的環保替代品"
        ],
        "specs": [
            {"label": "Material", "value": "Virgin Kraft / Recycled Kraft"},
            {"label": "Handle", "value": "Flat Paper Handle"},
            {"label": "Max Load", "value": "Up to 5kg (Standard)"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "長纖牛皮紙 / 回收牛皮紙"},
            {"label": "提手", "value": "扁平紙提手"},
            {"label": "最大承重", "value": "最高 5kg（標準型）"}
        ]
    },
    {
        "id": "white-kraft-bag",
        "category": "White Kraft",
        "category_zh": "白牛皮紙",
        "name": "White Kraft Paper Bag",
        "name_zh": "白牛皮紙袋",
        "image": "/proimages/detail/white-kraft-bag.png",
        "desc": "Premium white kraft paper bag with a clean, professional aesthetic. Ideal for high-end retail, pharmaceuticals, and gift packaging.",
        "desc_zh": "高品質白牛皮紙袋，具有簡潔專業的美感。 非常適合高端零售、製藥和禮品包裝。",
        "features": [
            "Premium clean white finish",
            "Breathability pinholes optional",
            "Sharp contrast for custom printing",
            "Variety of grammage options"
        ],
        "features_zh": [
            "高級純白飾面",
            "可選透氣針孔",
            "客製印刷效果鮮明",
            "多種克重選擇"
        ],
        "specs": [
            {"label": "Material", "value": "Bleached Kraft Paper"},
            {"label": "Color", "value": "Natural White"},
            {"label": "Finish", "value": "Smooth / Ribbed"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "漂白牛皮紙"},
            {"label": "顏色", "value": "天然白"},
            {"label": "表面", "value": "平滑 / 條紋"}
        ]
    },
    {
        "id": "aluminum-foil-bag",
        "category": "Aluminum Foil",
        "category_zh": "鋁箔紙",
        "name": "Aluminum Foil Paper Bag",
        "name_zh": "鋁箔紙袋",
        "image": "/proimages/detail/aluminum-foil-bag.png",
        "desc": "Heat-insulated and oil-resistant bags specifically designed for hot food takeout. The aluminum lining keeps food warm and prevents oil leakage.",
        "desc_zh": "專為熱食外帶設計的隔熱且耐油的包裝袋。 鋁箔內層可保持食物溫度並防止油脂滲漏。",
        "features": [
            "Excellent heat retention",
            "High grease and oil resistance",
            "Leak-proof construction",
            "Ideal for roasted chicken and ribs"
        ],
        "features_zh": [
            "優異的保溫性能",
            "高度耐油脂",
            "防漏構造",
            "烤雞和肋排的理想選擇"
        ],
        "specs": [
            {"label": "Material", "value": "Kraft Paper + Aluminum Foil"},
            {"label": "Temp Limit", "value": "Up to 100°C"},
            {"label": "Sizes", "value": "Multiple standard sizes"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "牛皮紙 + 鋁箔"},
            {"label": "耐溫", "value": "最高 100°C"},
            {"label": "尺寸", "value": "多種標準尺寸"}
        ]
    },
    {
        "id": "mango-bag",
        "category": "Fruit Protection",
        "category_zh": "水果套袋",
        "name": "Mango Protection Bag",
        "name_zh": "凱特1號-雙層 (芒果套袋)",
        "image": "/proimages/detail/mango-bag.jpg",
        "desc": "Double-layer protection bag designed for mangoes. Protects fruit from pests, birds, and harsh weather conditions while allowing proper airflow and biological development.",
        "desc_zh": "專為芒果設計的雙層保護袋。 保護水果免受病蟲害、鳥類和惡劣天氣條件的影響，同時允許空氣流通和生物發育。",
        "features": [
            "Double-layer for maximum protection",
            "Biodegradable materials",
            "Prevents skin damage and scratches",
            "Easy application with integrated wire"
        ],
        "features_zh": [
            "雙層設計提供最大保護",
            "可生物分解材料",
            "防止表皮損傷 和 擦傷",
            "配有鐵絲，容易套袋"
        ],
        "specs": [
            {"label": "Type", "value": "Double-layer (Black/Blue)"},
            {"label": "Material", "value": "Waterproof Treated Paper"},
            {"label": "Target", "value": "Mangoes (Irwin, Keitt)"}
        ],
        "specs_zh": [
            {"label": "類型", "value": "雙層（黑/藍）"},
            {"label": "材質", "value": "防水處理紙"},
            {"label": "對象", "value": "芒果（愛文、凱特）"}
        ]
    },
    {
        "id": "l-bag",
        "category": "PE Lamination",
        "category_zh": "淋膜紙袋",
        "name": "L-bag (Burger Pocket)",
        "name_zh": "L型袋 (雙面開口漢堡袋)",
        "image": "/proimages/detail/l-bag.jpg",
        "desc": "Convenient L-opening bag for quick consumption of burgers, sandwiches, and hot dogs. PE lamination ensures full grease resistance and leak prevention.",
        "desc_zh": "方便的 L 型開口袋，非常適合快速食用漢堡、三明治和熱狗。 PE 淋膜確保完全防油並防止滲漏。",
        "features": [
            "L-side opening for easy eating",
            "Full PE lamination for liquid barrier",
            "High grease resistance",
            "Space-saving flat storage"
        ],
        "features_zh": [
            "L型側面開口，方便食用",
            "全 PE 淋膜，阻隔液體",
            "高度耐油脂",
            "節省空間的扁平儲存"
        ],
        "specs": [
            {"label": "Material", "value": "Kraft / White Paper + PE"},
            {"label": "Usage", "value": "Burgers, Waffles, Crepes"},
            {"label": "Print", "value": "Standard Generic / Custom"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "牛皮紙 / 白紙 + PE"},
            {"label": "用途", "value": "漢堡、鬆餅、可麗餅"},
            {"label": "印刷", "value": "標準通用 / 客製化"}
        ]
    },
    {
        "id": "paper-straw",
        "category": "Paper Straw",
        "category_zh": "紙吸管",
        "name": "Biodegradable Paper Straw",
        "name_zh": "環保紙吸管",
        "image": "/proimages/detail/paper-straw.jpg",
        "desc": "100% biodegradable and compostable paper straws. Made from premium virgin wood pulp, providing a sturdy and high-quality drinking experience without the environmental impact of plastic.",
        "desc_zh": "100% 可生物分解和可堆肥的紙吸管。 由優質原生木漿製成，提供堅固高品質的飲用體驗，且不會像塑料那樣對環境造成影響。",
        "features": [
            "100% Taiwan made",
            "FSC primary long fiber pulp",
            "Sturdy construction (non-soggy)",
            "Safe for adults and children"
        ],
        "features_zh": [
            "100% 台灣製造",
            "FSC 原生長纖維紙漿",
            "構造堅固（不易軟化）",
            "成人和兒童均可安全使用"
        ],
        "specs": [
            {"label": "Material", "value": "Food Grade Virgin Pulp"},
            {"label": "Standard", "value": "FDA / LFGB Compliant"},
            {"label": "Durable", "value": "Up to 6 hours in cold water"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "食品級原生紙漿"},
            {"label": "標準", "value": "符合 FDA / LFGB"},
            {"label": "耐用性", "value": "冷水中可達 6 小時"}
        ]
    },
    {
        "id": "specialty-bags",
        "category": "Others",
        "category_zh": "其他特殊袋",
        "name": "Custom & Specialty Bags",
        "name_zh": "客製化特殊袋",
        "image": "/proimages/detail/bakery-side-window.jpg",
        "desc": "Bespoke packaging solutions for unique product requirements. We specialize in custom sizes, shapes, and material combinations to meet specific industry needs.",
        "desc_zh": "針對獨特產品需求提供客製化包裝解決方案。 我們專注於客製化尺寸、形狀和材料組合，以滿足特定行業的需求。",
        "features": [
            "Tailored material selection",
            "Custom structural design",
            "Advanced multi-color printing",
            "OEM / ODM development partner"
        ],
        "features_zh": [
            "量身定制材料選擇",
            "客製化結構設計",
            "先進多色印刷",
            "OEM / ODM 開發合作夥伴"
        ],
        "specs": [
            {"label": "Material", "value": "Various combinations"},
            {"label": "Customization", "value": "Size, Shape, Printing"},
            {"label": "MOQ", "value": "Depends on specification"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "各種複合材質"},
            {"label": "客製化", "value": "尺寸、形狀、印刷"},
            {"label": "最小起訂量", "value": "視規格而定"}
        ]
    }
]

EN_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name} | JJG Paper Bag</title>
    <meta name="description" content="{desc_meta}" />
    <link rel="icon" href="/images/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet">
    <link href="/style.css" rel="stylesheet">
</head>
<body x-data="{{ mobileMenu: false }}" class="bg-[#F5F0E8] text-[#1A1A1A] font-['Inter',sans-serif]">
    <!-- NAV -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur shadow-sm">
        <nav class="max-w-[1400px] mx-auto px-4 lg:px-8 h-[88px] flex items-center justify-between">
            <a href="/JJGPACK/index.html" class="flex items-center gap-2"><img src="/images/index-logo.png" alt="JJG" class="h-[68px]"></a>
            <div class="hidden lg:flex items-center gap-8">
                <a href="/JJGPACK/index.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">Home</a>
                <a href="/JJGPACK/about.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">About Us</a>
                <a href="/JJGPACK/products.html" class="text-[#1A5C38] font-semibold text-[15px]">Products</a>
                <a href="/JJGPACK/news.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">News</a>
                <a href="/JJGPACK/contact.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">Contact Us</a>
            </div>
            <div class="hidden lg:flex items-center gap-4">
                <a href="/JJGPACK/products/{cat_slug}/{id}.html" class="text-[#1A5C38] text-sm font-semibold">EN</a><span class="text-gray-300">|</span><a href="/JJGPACK/zh-tw/products/{cat_slug}/{id}.html" class="text-[#666] hover:text-[#1A5C38] text-sm font-medium">繁中</a>
                <a href="/JJGPACK/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-5 py-2.5 rounded-lg font-bold text-sm uppercase tracking-wider transition">Contact Us</a>
            </div>
        </nav>
    </header>

    <!-- MAIN PRODUCT SECTION -->
    <main class="max-w-[1400px] mx-auto px-4 lg:px-8 py-12">
        <!-- Breadcrumb -->
        <nav class="text-sm text-[#666] mb-8">
            <a href="/JJGPACK/index.html" class="hover:text-[#2E8B57]">Home</a> <span class="mx-2">›</span> 
            <a href="/JJGPACK/products.html" class="hover:text-[#2E8B57]">Products</a> <span class="mx-2">›</span> 
            <span class="text-[#1A5C38] font-medium">{name}</span>
        </nav>

        <div class="grid lg:grid-cols-2 gap-12 bg-white rounded-3xl overflow-hidden shadow-premium-lg">
            <!-- Product Image -->
            <div class="bg-gray-50 flex items-center justify-center p-8 lg:p-12">
                <div class="relative group cursor-zoom-in">
                    <img src="{image}" alt="{name}" class="rounded-2xl shadow-xl w-full h-auto object-cover max-h-[600px]">
                </div>
            </div>

            <!-- Product Info -->
            <div class="p-8 lg:p-12">
                <span class="text-[#B5813C] uppercase text-sm font-bold tracking-[0.2em] mb-4 inline-block">{category}</span>
                <h1 class="font-['Playfair_Display',serif] text-4xl lg:text-5xl font-bold mb-6 text-[#1A5C38]">{name}</h1>
                <p class="text-[#555] text-lg leading-relaxed mb-8">{desc}</p>
                
                <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
                    <svg class="w-6 h-6 text-[#2E8B57]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                    Key Features
                </h3>
                <ul class="space-y-3 mb-10 text-[#555]">
                    {features}
                </ul>

                <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
                    <svg class="w-6 h-6 text-[#2E8B57]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
                    Specifications
                </h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-10">
                    {specs}
                </div>

                <div class="flex flex-wrap gap-4 pt-4 border-t border-gray-100">
                    <a href="/JJGPACK/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-8 py-4 rounded-xl font-bold text-center transition tracking-wider uppercase flex-1 shadow-lg">Inquire Now</a>
                    <button onclick="window.print()" class="p-4 border border-gray-200 rounded-xl hover:bg-gray-50 transition text-[#666]">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
                    </button>
                </div>
            </div>
        </div>
    </main>

    <!-- FOOTER -->
    <footer class="bg-[#1A1A1A] text-gray-400 py-16">
        <div class="max-w-[1400px] mx-auto px-4 text-center">
            <img src="/images/index-logo.png" alt="JJG" class="h-10 mx-auto mb-6 brightness-200">
            <p class="text-sm">70+ Years of Manufacturing Excellence | Taiwan</p>
        </div>
    </footer>
</body>
</html>"""

ZH_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name_zh} | 壯佳果包裝 - JJG Paper Bag</title>
    <meta name="description" content="{desc_meta}" />
    <link rel="icon" href="/images/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@700;900&display=swap" rel="stylesheet">
    <link href="/style.css" rel="stylesheet">
</head>
<body x-data="{{ mobileMenu: false }}" class="bg-[#F5F0E8] text-[#1A1A1A] font-['Inter','Noto_Sans_TC',sans-serif]">
    <!-- NAV -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur shadow-sm">
        <nav class="max-w-[1400px] mx-auto px-4 lg:px-8 h-[88px] flex items-center justify-between">
            <a href="/JJGPACK/zh-tw/index.html" class="flex items-center gap-2"><img src="/images/index-logo.png" alt="JJG" class="h-[68px]"></a>
            <div class="hidden lg:flex items-center gap-8">
                <a href="/JJGPACK/zh-tw/index.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">首頁</a>
                <a href="/JJGPACK/zh-tw/about.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">關於我們</a>
                <a href="/JJGPACK/zh-tw/products.html" class="text-[#1A5C38] font-semibold text-[15px]">產品介紹</a>
                <a href="/JJGPACK/zh-tw/news.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">最新消息</a>
                <a href="/JJGPACK/zh-tw/contact.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">聯絡我們</a>
            </div>
            <div class="hidden lg:flex items-center gap-4">
                <a href="/JJGPACK/products/{cat_slug}/{id}.html" class="text-[#666] hover:text-[#1A5C38] text-sm font-medium">EN</a><span class="text-gray-300">|</span><a href="/JJGPACK/zh-tw/products/{cat_slug}/{id}.html" class="text-[#1A5C38] text-sm font-semibold">繁中</a>
                <a href="/JJGPACK/zh-tw/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-5 py-2.5 rounded-lg font-bold text-sm tracking-wider transition">聯絡我們</a>
            </div>
        </nav>
    </header>

    <!-- MAIN PRODUCT SECTION -->
    <main class="max-w-[1400px] mx-auto px-4 lg:px-8 py-12">
        <!-- Breadcrumb -->
        <nav class="text-sm text-[#666] mb-8">
            <a href="/JJGPACK/zh-tw/index.html" class="hover:text-[#2E8B57]">首頁</a> <span class="mx-2">›</span> 
            <a href="/JJGPACK/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a> <span class="mx-2">›</span> 
            <span class="text-[#1A5C38] font-medium">{name_zh}</span>
        </nav>

        <div class="grid lg:grid-cols-2 gap-12 bg-white rounded-3xl overflow-hidden shadow-premium-lg">
            <!-- Product Image -->
            <div class="bg-gray-50 flex items-center justify-center p-8 lg:p-12">
                <div class="relative group cursor-zoom-in">
                    <img src="{image}" alt="{name_zh}" class="rounded-2xl shadow-xl w-full h-auto object-cover max-h-[600px]">
                </div>
            </div>

            <!-- Product Info -->
            <div class="p-8 lg:p-12">
                <span class="text-[#B5813C] uppercase text-sm font-bold tracking-[0.2em] mb-4 inline-block">{category_zh}</span>
                <h1 class="font-['Noto_Serif_TC',serif] text-4xl lg:text-5xl font-bold mb-6 text-[#1A5C38]">{name_zh}</h1>
                <p class="text-[#555] text-lg leading-relaxed mb-8">{desc_zh}</p>
                
                <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
                    <svg class="w-6 h-6 text-[#2E8B57]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                    產品特色
                </h3>
                <ul class="space-y-3 mb-10 text-[#555]">
                    {features_zh}
                </ul>

                <h3 class="text-xl font-bold mb-4 flex items-center gap-2">
                    <svg class="w-6 h-6 text-[#2E8B57]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
                    產品規格
                </h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-10">
                    {specs_zh}
                </div>

                <div class="flex flex-wrap gap-4 pt-4 border-t border-gray-100">
                    <a href="/JJGPACK/zh-tw/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-8 py-4 rounded-xl font-bold text-center transition flex-1 shadow-lg">立即詢價</a>
                    <button onclick="window.print()" class="p-4 border border-gray-200 rounded-xl hover:bg-gray-50 transition text-[#666]">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
                    </button>
                </div>
            </div>
        </div>
    </main>

    <!-- FOOTER -->
    <footer class="bg-[#1A1A1A] text-gray-400 py-16">
        <div class="max-w-[1400px] mx-auto px-4 text-center">
            <img src="/images/index-logo.png" alt="JJG" class="h-10 mx-auto mb-6 brightness-200">
            <p class="text-sm">70 餘年製造經驗 | 台灣專業紙袋廠</p>
        </div>
    </footer>
</body>
</html>"""

for p in products:
    cat_slug = p['category'].lower().replace(' ', '-')
    
    # EN
    os.makedirs(f"products/{cat_slug}", exist_ok=True)
    features_en = "\n".join([f'                    <li class="flex items-start gap-2"><svg class="w-5 h-5 text-[#2E8B57] mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4" /></svg> {f}</li>' for f in p['features']])
    specs_en = "\n".join([f'                    <div class="bg-[#F9F7F4] p-4 rounded-lg"><p class="text-xs text-[#888] uppercase mb-1">{s["label"]}</p><p class="font-semibold">{s["value"]}</p></div>' for s in p['specs']])
    
    en_html = EN_TEMPLATE.format(
        name=p['name'],
        desc_meta=p['desc'][:160].replace('"', '&quot;'),
        desc=p['desc'],
        category=p['category'],
        cat_slug=cat_slug,
        id=p['id'],
        image=p['image'],
        features=features_en,
        specs=specs_en
    )
    with open(f"products/{cat_slug}/{p['id']}.html", "w", encoding="utf-8") as f:
        f.write(en_html)

    # ZH-TW
    os.makedirs(f"zh-tw/products/{cat_slug}", exist_ok=True)
    features_zh = "\n".join([f'                    <li class="flex items-start gap-2"><svg class="w-5 h-5 text-[#2E8B57] mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4" /></svg> {f}</li>' for f in p['features_zh']])
    specs_zh = "\n".join([f'                    <div class="bg-[#F9F7F4] p-4 rounded-lg"><p class="text-xs text-[#888] mb-1">{s["label"]}</p><p class="font-semibold font-[\'Noto_Sans_TC\',sans-serif]">{s["value"]}</p></div>' for s in p['specs_zh']])
    
    zh_html = ZH_TEMPLATE.format(
        name_zh=p['name_zh'],
        desc_meta=p['desc_zh'][:160].replace('"', '&quot;'),
        desc_zh=p['desc_zh'],
        category_zh=p['category_zh'],
        cat_slug=cat_slug,
        id=p['id'],
        image=p['image'],
        features_zh=features_zh,
        specs_zh=specs_zh
    )
    with open(f"zh-tw/products/{cat_slug}/{p['id']}.html", "w", encoding="utf-8") as f:
        f.write(zh_html)

print("Detail pages generated successfully.")
