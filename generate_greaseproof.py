import json
import os

# Load data
with open('greaseproof_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Ensure output directory exists
output_dir = 'zh-tw/products/greaseproof'
os.makedirs(output_dir, exist_ok=True)

# Template
TEMPLATE = """<!DOCTYPE html>
<html lang="zh-TW">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name} | 防油紙袋 | 壯佳果包裝 - JJG Paper Bag</title>
    <meta name="description" content="{description_meta}" />
    <link rel="icon" href="/images/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+TC:wght@400;500;600;700&family=Noto+Serif+TC:wght@700;900&family=Playfair+Display:wght@400;700;900&display=swap"
        rel="stylesheet">
    <link href="/style.css" rel="stylesheet">
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>

<body x-data="{{ mobileMenu: false, activeImage: '{main_image}' }}" class="bg-[#F5F0E8] text-[#1A1A1A] font-['Inter','Noto_Sans_TC',sans-serif]">
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
            <button @click="mobileMenu=!mobileMenu" class="lg:hidden p-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
            </button>
        </nav>
    </header>

    <div class="pt-[76px]">
        <div class="max-w-[1440px] mx-auto px-6 lg:px-10 py-4">
            <nav class="text-sm text-[#666]">
                <a href="/zh-tw/" class="hover:text-[#2E8B57]">首頁</a> <span class="mx-2">›</span> 
                <a href="/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a> <span class="mx-2">›</span> 
                <a href="/zh-tw/products/greaseproof.html" class="hover:text-[#2E8B57]">防油紙袋</a> <span class="mx-2">›</span> 
                <span class="text-[#1A5C38] font-medium">{name}</span>
            </nav>
        </div>

        <section class="max-w-[1440px] mx-auto px-6 lg:px-10 pb-20">
            <div class="grid lg:grid-cols-2 gap-16 items-start">
                <!-- Gallery -->
                <div class="space-y-4">
                    <div class="rounded-2xl overflow-hidden shadow-premium-lg bg-white aspect-[4/3] flex items-center justify-center">
                        <img :src="activeImage" alt="{name}" class="w-full h-full object-contain p-4">
                    </div>
                    <div class="grid grid-cols-4 gap-4">
                        {gallery_html}
                    </div>
                </div>

                <!-- Info -->
                <div>
                    <span class="inline-block text-xs font-bold tracking-wider text-[#1A5C38] bg-[#1A5C38]/8 px-3 py-1 rounded-full mb-4">防油紙袋系列</span>
                    <h1 class="font-['Noto_Serif_TC',serif] text-3xl md:text-4xl font-bold mb-6">{name}</h1>
                    <div class="text-[#555] text-lg leading-relaxed mb-8 space-y-4">
                        <p>{description}</p>
                    </div>
                    
                    <div class="bg-white rounded-2xl p-8 shadow-premium mb-8">
                        <h2 class="font-['Noto_Serif_TC',serif] text-xl font-bold mb-6 border-b border-gray-100 pb-4">產品特點與規格</h2>
                        <div class="text-[#555] whitespace-pre-line leading-loose">
                            {specification}
                        </div>
                    </div>

                    <div class="flex flex-wrap gap-4">
                        <a href="/zh-tw/contact.html" class="btn-primary"><span>索取報價</span></a>
                        <a href="/zh-tw/products/greaseproof.html" class="px-8 py-4 rounded-xl border-2 border-[#1A5C38] text-[#1A5C38] font-bold hover:bg-[#1A5C38]/5 transition">返回列表</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Product Details / Table -->
        <section class="bg-white py-20">
            <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
                <div class="max-w-4xl mx-auto">
                    <h2 class="font-['Noto_Serif_TC',serif] text-2xl font-bold mb-10 text-center">技術資訊</h2>
                    <div class="grid md:grid-cols-2 gap-10">
                        <div class="space-y-4">
                            <h3 class="font-bold text-[#1A5C38]">材質與規範</h3>
                            <ul class="space-y-2 text-[#555] text-sm">
                                <li>• 食品級防油紙 / PE 淋膜</li>
                                <li>• 符合 ISO 22000 & HACCP 認證</li>
                                <li>• 無 PFAS 處理，安全環保</li>
                                <li>• 100% 可生物分解 (視材質)</li>
                            </ul>
                        </div>
                        <div class="space-y-4">
                            <h3 class="font-bold text-[#1A5C38]">客製化服務</h3>
                            <ul class="space-y-2 text-[#555] text-sm">
                                <li>• 支援 1-8 色印刷</li>
                                <li>• 多種尺寸比例調整</li>
                                <li>• 提供樣品確認服務</li>
                                <li>• 專業包裝設計建議</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <footer class="bg-[#111] text-gray-400 pt-16 pb-8">
        <div class="max-w-[1440px] mx-auto px-6 lg:px-10">
            <div class="grid md:grid-cols-4 gap-10 pb-10 border-b border-white/10">
                <div><img src="/images/index-logo.png" alt="JJG" class="h-10 mb-4 brightness-200">
                    <p class="text-sm text-gray-500">台灣專業紙袋製造商</p>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4 text-sm">快速連結</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/zh-tw/" class="hover:text-[#2E8B57]">首頁</a></li>
                        <li><a href="/zh-tw/products.html" class="hover:text-[#2E8B57]">產品介紹</a></li>
                        <li><a href="/zh-tw/contact.html" class="hover:text-[#2E8B57]">聯絡我們</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4 text-sm">產品系列</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/zh-tw/products/greaseproof.html" class="text-white">防油紙袋</a></li>
                        <li><a href="/zh-tw/products/kraft.html" class="hover:text-[#2E8B57]">牛皮紙袋</a></li>
                        <li><a href="/zh-tw/products/flathandle.html" class="hover:text-[#2E8B57]">平把手提袋</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4 text-sm">聯絡資訊</h4>
                    <ul class="space-y-2 text-sm">
                        <li>📍 台中市大甲區游九路6號</li>
                        <li>📞 +886-4-26223215</li>
                        <li>✉️ export@jjgpaperbag.com</li>
                    </ul>
                </div>
            </div>
            <div class="pt-6 text-center text-xs text-gray-600">© 2026 壯佳果股份有限公司</div>
        </div>
    </footer>
    <script type="module" src="/main.js"></script>
</body>

</html>"""

def slugify(text):
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-').replace('--', '-')

for prod in products:
    slug = slugify(prod['name']) + '.html'
    
    gallery_items = []
    for img_url in prod['images']:
        item = f'<button @click="activeImage=\'{img_url}\'" class="aspect-square rounded-lg overflow-hidden border-2 transition" :class="activeImage===\'{img_url}\' ? \'border-[#1A5C38]\' : \'border-transparent hover:border-gray-200\'"><img src="{img_url}" class="w-full h-full object-cover"></button>'
        gallery_items.append(item)
    
    html = TEMPLATE.format(
        name=prod['name'],
        description_meta=prod['description'][:150],
        description=prod['description'] if prod['description'] else "專業食品級包裝解決方案。",
        specification=prod['specification'] if prod['specification'] else "請聯繫我們獲取詳細規格。",
        main_image=prod['images'][0] if prod['images'] else "",
        gallery_html="\n".join(gallery_items)
    )
    
    with open(os.path.join(output_dir, slug), 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Generated {len(products)} product pages in {output_dir}")
