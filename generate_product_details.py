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
        "desc": "Premium white kraft paper bag offering a clean and professional look. Ideal for high-end retail, pharmaceuticals, and gift packaging.",
        "desc_zh": "高品質白牛皮紙袋，外觀潔淨專業。 非常適合高端零售、製藥和禮品包裝。",
        "features": [
            "Clean white aesthetic",
            "Strong side and bottom structure",
            "Multiple size options",
            "FSC-certified paper option"
        ],
        "features_zh": [
            "簡約白色美學",
            "強韌的側邊和底部結構",
            "多種尺寸選擇",
            "可選 FSC 認證紙張"
        ],
        "specs": [
            {"label": "Material", "value": "Premium White Kraft"},
            {"label": "Color", "value": "Natural White"},
            {"label": "Usage", "value": "Cosmetics, Pharmacy, Gifts"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "特級白牛皮紙"},
            {"label": "顏色", "value": "原色白"},
            {"label": "用途", "value": "化妝品、藥店、禮品"}
        ]
    },
    {
        "id": "aluminum-foil-bag",
        "category": "Aluminum Foil",
        "category_zh": "鋁箔紙",
        "name": "Aluminum Foil Paper Bag",
        "name_zh": "鋁箔紙袋",
        "image": "/proimages/detail/aluminum-foil-bag.png",
        "desc": "Specialized bag with internal aluminum foil lining for excellent heat retention and grease resistance. The preferred choice for roasted chicken and hot takeaway food.",
        "desc_zh": "內層鋁箔襯裡的特製袋，具有優異的保溫和防油性能。 烤雞和熱外帶食品的首選。",
        "features": [
            "Internal foil for heat retention",
            "Superior grease resistance",
            "Keeps food hot and flavorful",
            "Strong side-seal construction"
        ],
        "features_zh": [
            "內層鋁箔保溫技術",
            "卓越的抗油脂性能",
            "保持食物熱度和風味",
            "強韌的側封結構"
        ],
        "specs": [
            {"label": "Material", "value": "Kraft + Aluminum Foil"},
            {"label": "Heat Retention", "value": "Excellent"},
            {"label": "Usage", "value": "Roasted Chicken, BBQ, Takeout"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "牛皮紙 + 鋁箔"},
            {"label": "保溫性能", "value": "優異"},
            {"label": "用途", "value": "烤雞、燒烤、外帶"}
        ]
    },
    {
        "id": "l-bag",
        "category": "PE Lamination",
        "category_zh": "淋膜紙袋",
        "name": "Burger Pocket L-Bag",
        "name_zh": "L型袋 (漢堡袋)",
        "image": "/proimages/detail/l-bag.jpg",
        "desc": "Convenient L-style open pocket with internal PE lamination. Designed specifically for burgers, sandwiches, and hot dogs to prevent leaks and make on-the-go eating easy.",
        "desc_zh": "內層 PE 淋膜的便捷 L 型開口袋。 專為漢堡、三明治和熱狗設計，防止滲漏，讓旅途中進食變得輕鬆。",
        "features": [
            "L-style opening for easy access",
            "PE-coated for leak-proof performance",
            "Grease-resistant",
            "Compact and space-efficient"
        ],
        "features_zh": [
            "L型開口設計方便食用",
            "PE 淋膜防滲漏性能",
            "耐油處理",
            "輕巧且節省空間"
        ],
        "specs": [
            {"label": "Material", "value": "Paper + PE Coating"},
            {"label": "Opening", "value": "L-Style (Two Sides)"},
            {"label": "Usage", "value": "Burgers, Sandwiches, Waffles"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "紙 + PE 淋膜"},
            {"label": "開口方式", "value": "L型（兩側開口）"},
            {"label": "用途", "value": "漢堡、三明治、格子餅"}
        ]
    },
    {
        "id": "mango-bag",
        "category": "Fruit Protection",
        "category_zh": "水果套袋",
        "name": "Mango Protection Bag",
        "name_zh": "凱特1號-雙層 (芒果袋)",
        "image": "/proimages/detail/mango-bag.jpg",
        "desc": "High-performance double-layer paper bag designed for fruit protection. Shields growing fruit from pests, birds, and harsh weather conditions, ensuring a higher quality harvest.",
        "desc_zh": "高性能雙層水果保護紙袋。 保護生長中的水果免受害蟲、鳥類和惡劣天氣條件的影響，確保更高質量的收成。",
        "features": [
            "Double-layer for maximum protection",
            "Breathable material for fruit growth",
            "Waterproof outer treatment",
            "Easy to attach and secure"
        ],
        "features_zh": [
            "雙層設計提供最大程度的保護",
            "有利於水果生長的透氣材質",
            "外層防水處理",
            "易於安裝與固定"
        ],
        "specs": [
            {"label": "Layer", "value": "Double Layer"},
            {"label": "Color", "value": "Customized per fruit type"},
            {"label": "Eco Impact", "value": "100% Biodegradable"}
        ],
        "specs_zh": [
            {"label": "層數", "value": "雙層設計"},
            {"label": "顏色", "value": "根據水果類型客製"},
            {"label": "環保影響", "value": "100% 可生物分解"}
        ]
    },
    {
        "id": "paper-straw",
        "category": "Paper Straw",
        "category_zh": "紙吸管",
        "name": "Biodegradable Paper Straw",
        "name_zh": "環保紙吸管",
        "image": "/proimages/detail/paper-straw.jpg",
        "desc": "Sustainable alternative to plastic straws, made in Taiwan from 100% biodegradable materials. High structural integrity and safe for all types of beverages.",
        "desc_zh": "塑料吸管的可持續替代品，100% 由可生物分解材料在台灣製造。 結構完整性高，對所有類型的飲料都安全。",
        "features": [
            "100% Biodegradable and PFAS-Free",
            "Stable in liquid for extended periods",
            "Smooth edges and premium feel",
            "Available in multiple diameters"
        ],
        "features_zh": [
            "100% 可生物分解且不含 PFAS",
            "在液體中長時間保持穩定",
            "邊緣光滑，手感優質",
            "提供多種直徑選擇"
        ],
        "specs": [
            {"label": "Material", "value": "Virgin Pulp Paper"},
            {"label": "Compliance", "value": "FDA, SGS Certified"},
            {"label": "Origin", "value": "100% Made in Taiwan"}
        ],
        "specs_zh": [
            {"label": "材質", "value": "原生木漿紙"},
            {"label": "合規性", "value": "FDA, SGS 認證"},
            {"label": "產地", "value": "100% 台灣製造"}
        ]
    },
    {
        "id": "specialty-bags",
        "category": "Others",
        "category_zh": "其他",
        "name": "Custom & Specialty Bags",
        "name_zh": "客製化特殊袋",
        "image": "/proimages/detail/bakery-side-window.jpg",
        "desc": "Bespoke packaging solutions for unique product requirements. We combine different materials, printing techniques, and constructions to create the perfect bag for your brand.",
        "desc_zh": "針對獨特產品需求提供量身定制的包裝解決方案。 我們結合不同的材質、印刷技術和結構，為您的品牌打造完美的包裝袋。",
        "features": [
            "Custom material combinations",
            "Specialized coatings and finishes",
            "Unique size and shape development",
            "Full brand integration"
        ],
        "features_zh": [
            "多樣化材質組合",
            "特種塗層與飾面處理",
            "獨特的尺寸和形狀開發",
            "品牌完整整合方案"
        ],
        "specs": [
            {"label": "Type", "value": "OEM / ODM Custom"},
            {"label": "MOQ", "value": "Please contact for details"},
            {"label": "Design", "value": "Full Customization"}
        ],
        "specs_zh": [
            {"label": "類型", "value": "OEM / ODM 客製"},
            {"label": "起訂量", "value": "請聯繫詳洽"},
            {"label": "設計", "value": "完全客製化"}
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
            <a href="/index.html" class="flex items-center gap-2"><img src="/images/index-logo.png" alt="JJG" class="h-[68px]"></a>
            <div class="hidden lg:flex items-center gap-8">
                <a href="/index.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">Home</a>
                <a href="/about.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">About Us</a>
                <a href="/products.html" class="text-[#1A5C38] font-semibold text-[15px]">Products</a>
                <a href="/news.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">News</a>
                <a href="/contact.html" class="text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition">Contact Us</a>
            </div>
            <div class="hidden lg:flex items-center gap-4">
                <a href="/products/{cat_slug}/{id}.html" class="text-[#1A5C38] text-sm font-semibold">EN</a><span class="text-gray-300">|</span><a href="/zh-tw/products/{cat_slug}/{id}.html" class="text-[#666] hover:text-[#1A5C38] text-sm font-medium">繁中</a>
                <a href="/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-5 py-2.5 rounded-lg font-bold text-sm uppercase tracking-wider transition">Contact Us</a>
            </div>
        </nav>
    </header>

    <!-- MAIN PRODUCT SECTION -->
    <main class="max-w-[1400px] mx-auto px-4 lg:px-8 py-12">
        <!-- Breadcrumb -->
        <nav class="text-sm text-[#666] mb-8">
            <a href="/index.html" class="hover:text-[#2E8B57]">Home</a> <span class="mx-2">›</span> 
            <a href="/products.html" class="hover:text-[#2E8B57]">Products</a> <span class="mx-2">›</span> 
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
                    <a href="/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-8 py-4 rounded-xl font-bold text-center transition tracking-wider uppercase flex-1 shadow-lg">Inquire Now</a>
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
            <a href="/zh-tw/index.html" class="flex items-center gap-2"><img src="/images/index-logo.png" alt="JJG" class="h-[68px]"></a>
            <div class="hidden lg:flex items-center gap-8">
                <a href="/zh-tw/index.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">首頁</a>
                <a href="/zh-tw/about.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">關於我們</a>
                <a href="/zh-tw/products.html" class="text-[#1A5C38] font-semibold text-[15px]">產品介紹</a>
                <a href="/zh-tw/news.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">最新消息</a>
                <a href="/zh-tw/contact.html" class="text-[#666] hover:text-[#1A5C38] font-medium text-[15px] transition">聯絡我們</a>
            </div>
            <div class="hidden lg:flex items-center gap-4">
                <a href="/products/{cat_slug}/{id}.html" class="text-[#666] hover:text-[#1A5C38] text-sm font-medium">EN</a><span class="text-gray-300">|</span><a href="/zh-tw/products/{cat_slug}/{id}.html" class="text-[#1A5C38] text-sm font-semibold">繁中</a>
                <a href="/zh-tw/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-5 py-2.5 rounded-lg font-bold text-sm tracking-wider transition">聯絡我們</a>
            </div>
        </nav>
    </header>

    <!-- MAIN PRODUCT SECTION -->
    <main class="max-w-[1400px] mx-auto px-4 lg:px-8 py-12">
        <!-- Breadcrumb -->
        <nav class="text-sm text-[#666] mb-8">
            <a href="/zh-tw/index.html" class="hover:text-[#2E8B57]">首頁</a> <span class="mx-2">›</span> 
            <a href="/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a> <span class="mx-2">›</span> 
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
                    詳細規格
                </h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-10">
                    {specs_zh}
                </div>

                <div class="flex flex-wrap gap-4 pt-4 border-t border-gray-100">
                    <a href="/zh-tw/contact.html" class="bg-[#1A5C38] hover:bg-[#2E8B57] text-white px-8 py-4 rounded-xl font-bold text-center transition tracking-wider uppercase flex-1 shadow-lg">立即詢價</a>
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
            <p class="text-sm">壯佳果股份有限公司 | 70年以上製造經驗 | 台灣製造</p>
        </div>
    </footer>
</body>
</html>"""

def generate():
    for p in products:
        cat_slug = p['category'].lower().replace(' ', '-')
        
        # English Version
        features_html = ""
        for f in p['features']:
            features_html += f'<li class="flex items-start gap-3"><span class="w-1.5 h-1.5 rounded-full bg-[#2E8B57] mt-2 shrink-0"></span>{f}</li>\n'
        
        specs_html = ""
        for s in p['specs']:
            specs_html += f'''
<div class="bg-gray-50 p-4 rounded-xl">
    <span class="text-xs text-[#999] uppercase font-bold tracking-wider block mb-1">{s['label']}</span>
    <span class="text-[#1A1A1A] font-semibold">{s['value']}</span>
</div>'''
        
        en_content = EN_TEMPLATE.format(
            id=p['id'],
            name=p['name'],
            category=p['category'],
            cat_slug=cat_slug,
            image=p['image'],
            desc=p['desc'],
            desc_meta=p['desc'][:160],
            features=features_html,
            specs=specs_html
        )
        
        out_dir = f"products/{cat_slug}"
        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/{p['id']}.html", "w", encoding="utf-8") as f:
            f.write(en_content)
            
        # Chinese Version
        features_zh_html = ""
        for f in p['features_zh']:
            features_zh_html += f'<li class="flex items-start gap-3"><span class="w-1.5 h-1.5 rounded-full bg-[#2E8B57] mt-2 shrink-0"></span>{f}</li>\n'
        
        specs_zh_html = ""
        for s in p['specs_zh']:
            specs_zh_html += f'''
<div class="bg-gray-50 p-4 rounded-xl">
    <span class="text-xs text-[#999] uppercase font-bold tracking-wider block mb-1">{s['label']}</span>
    <span class="text-[#1A1A1A] font-semibold">{s['value']}</span>
</div>'''
        
        zh_content = ZH_TEMPLATE.format(
            id=p['id'],
            name_zh=p['name_zh'],
            category_zh=p['category_zh'],
            cat_slug=cat_slug,
            image=p['image'],
            desc_zh=p['desc_zh'],
            desc_meta=p['desc_zh'][:160],
            features_zh=features_zh_html,
            specs_zh=specs_zh_html
        )
        
        out_dir_zh = f"zh-tw/products/{cat_slug}"
        os.makedirs(out_dir_zh, exist_ok=True)
        with open(f"{out_dir_zh}/{p['id']}.html", "w", encoding="utf-8") as f:
            f.write(zh_content)

if __name__ == "__main__":
    generate()
    print("Detail pages generated successfully.")
