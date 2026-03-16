import os

# Updated grid items for products.html
grid_items_en = """
                        <!-- FLAT HANDLE -->
                        <div x-show="activeCategory==='all'||activeCategory==='flathandle'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/flat-handle/flat-handle-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/flat-handle-bag.jpg" alt="Flat Handle Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Flat Handle</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/flat-handle/flat-handle-bag.html" class="hover:text-[#2E8B57]">Flat Handle Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">High stability, comfortable grip, food-grade water-based ink.</p>
                                    <a href="/JJGPACK/products/flat-handle/flat-handle-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- BROWN KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='kraft'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/kraft/square-paper-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/square-bag.jpg" alt="Square Bottom Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Brown Kraft</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/kraft/square-paper-bag.html" class="hover:text-[#2E8B57]">Square Bottom Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">Self-standing design, high-strength long-fiber kraft paper.</p>
                                    <a href="/JJGPACK/products/kraft/square-paper-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- GREASEPROOF -->
                        <div x-show="activeCategory==='all'||activeCategory==='greaseproof'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/greaseproof/bakery-side-window-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/bakery-side-window.jpg" alt="Bakery Side Window Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Greaseproof</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/greaseproof/bakery-side-window-bag.html" class="hover:text-[#2E8B57]">Bakery Side Window Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">PE laminated, grease-resistant with high-clarity transparent window.</p>
                                    <a href="/JJGPACK/products/greaseproof/bakery-side-window-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- WHITE KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='white'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/white-kraft/white-kraft-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/white-kraft-bag.png" alt="White Kraft Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">White Kraft</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/white-kraft/white-kraft-bag.html" class="hover:text-[#2E8B57]">White Kraft Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">Premium white kraft, clean appearance for retail and medical use.</p>
                                    <a href="/JJGPACK/products/white-kraft/white-kraft-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- ALUMINUM FOIL -->
                        <div x-show="activeCategory==='all'||activeCategory==='foil'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/aluminum-foil/aluminum-foil-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/aluminum-foil-bag.png" alt="Aluminum Foil Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Aluminum Foil</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/aluminum-foil/aluminum-foil-bag.html" class="hover:text-[#2E8B57]">Aluminum Foil Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">Excellent heat retention for roasted chicken and takeaways.</p>
                                    <a href="/JJGPACK/products/aluminum-foil/aluminum-foil-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- PE LAMINATION -->
                        <div x-show="activeCategory==='all'||activeCategory==='pe'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/pe-lamination/l-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/l-bag.jpg" alt="PE Lamination L-Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">PE Lamination</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/pe-lamination/l-bag.html" class="hover:text-[#2E8B57]">Burger Pocket L-Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">Leak-proof and grease-resistant burger and sandwich pocket.</p>
                                    <a href="/JJGPACK/products/pe-lamination/l-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- FRUIT PROTECTION -->
                        <div x-show="activeCategory==='all'||activeCategory==='fruit'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/fruit-protection/mango-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/mango-bag.jpg" alt="Fruit Protection Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Fruit Protection</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/fruit-protection/mango-bag.html" class="hover:text-[#2E8B57]">Mango Protection Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">Double-layer protection from pests and weather for growing fruits.</p>
                                    <a href="/JJGPACK/products/fruit-protection/mango-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- PAPER STRAW -->
                        <div x-show="activeCategory==='all'||activeCategory==='straw'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/products/paper-straw/paper-straw.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/paper-straw.jpg" alt="Paper Straw"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Paper Straw</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/products/paper-straw/paper-straw.html" class="hover:text-[#2E8B57]">Biodegradable Paper Straw</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3 text-line-clamp-2">100% Taiwan made, plastic-free, eco-friendly drinking solution.</p>
                                    <a href="/JJGPACK/products/paper-straw/paper-straw.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>
"""

grid_items_zh = """
                        <!-- FLAT HANDLE -->
                        <div x-show="activeCategory==='all'||activeCategory==='flathandle'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/flat-handle/flat-handle-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/flat-handle-bag.jpg" alt="扁繩手提紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">扁繩手提袋</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/flat-handle/flat-handle-bag.html" class="hover:text-[#2E8B57]">扁繩手提紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">高穩定性，握感舒適，食品級水性油墨。</p>
                                    <a href="/JJGPACK/zh-tw/products/flat-handle/flat-handle-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- BROWN KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='kraft'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/kraft/square-paper-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/square-bag.jpg" alt="方紙袋 (SOS)"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">牛皮紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/kraft/square-paper-bag.html" class="hover:text-[#2E8B57]">方底紙袋 (SOS)</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">自立式設計方便填充，高強度長纖維牛皮紙。</p>
                                    <a href="/JJGPACK/zh-tw/products/kraft/square-paper-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- GREASEPROOF -->
                        <div x-show="activeCategory==='all'||activeCategory==='greaseproof'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/greaseproof/bakery-side-window-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/bakery-side-window.jpg" alt="麵包側窗紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">防油紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/greaseproof/bakery-side-window-bag.html" class="hover:text-[#2E8B57]">麵包側窗紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">PE 淋膜，耐油性佳，配有高透明度視窗。</p>
                                    <a href="/JJGPACK/zh-tw/products/greaseproof/bakery-side-window-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- WHITE KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='white'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/white-kraft/white-kraft-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/white-kraft-bag.png" alt="白牛皮紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">白牛皮紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/white-kraft/white-kraft-bag.html" class="hover:text-[#2E8B57]">白牛皮紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">高級白牛皮紙，外觀潔淨，適合零售及藥用包裝。</p>
                                    <a href="/JJGPACK/zh-tw/products/white-kraft/white-kraft-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- ALUMINUM FOIL -->
                        <div x-show="activeCategory==='all'||activeCategory==='foil'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/aluminum-foil/aluminum-foil-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/aluminum-foil-bag.png" alt="鋁箔紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">鋁箔紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/aluminum-foil/aluminum-foil-bag.html" class="hover:text-[#2E8B57]">鋁箔紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">優異保溫性能，烤雞、熱食外帶理想選擇。</p>
                                    <a href="/JJGPACK/zh-tw/products/aluminum-foil/aluminum-foil-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- PE LAMINATION -->
                        <div x-show="activeCategory==='all'||activeCategory==='pe'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/pe-lamination/l-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/l-bag.jpg" alt="L型袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">淋膜紙袋</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/pe-lamination/l-bag.html" class="hover:text-[#2E8B57]">L型袋 (漢堡袋)</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">防漏耐油，漢堡三明治專用，側面開口方便食用。</p>
                                    <a href="/JJGPACK/zh-tw/products/pe-lamination/l-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- FRUIT PROTECTION -->
                        <div x-show="activeCategory==='all'||activeCategory==='fruit'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/fruit-protection/mango-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/mango-bag.jpg" alt="水果套袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">水果套袋</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/fruit-protection/mango-bag.html" class="hover:text-[#2E8B57]">凱特1號-雙層 (芒果袋)</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">雙層保護，防止病蟲害與天氣損傷，促進水果成長。</p>
                                    <a href="/JJGPACK/zh-tw/products/fruit-protection/mango-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- PAPER STRAW -->
                        <div x-show="activeCategory==='all'||activeCategory==='straw'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/JJGPACK/zh-tw/products/paper-straw/paper-straw.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/paper-straw.jpg" alt="環保紙吸管"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">紙吸管</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/JJGPACK/zh-tw/products/paper-straw/paper-straw.html" class="hover:text-[#2E8B57]">環保紙吸管</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">100% 台灣製造，無塑料，原生紙漿，環保首選。</p>
                                    <a href="/JJGPACK/zh-tw/products/paper-straw/paper-straw.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">完整介紹 →</a>
                                </div>
                        </div>
"""

# Apply to products.html
with open("products.html", "r", encoding="utf-8") as f:
    en_content = f.read()

# Replace the grid content
# Find the start and end of the grid items
import re
new_en_content = re.sub(r'<!-- Product Grid.*?<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">(.*?)</div>\s*</section>', 
                       f'<!-- Product Grid -->\\n        <section id="product-grid" class="max-w-[1400px] mx-auto px-4 lg:px-8 pb-20">\\n                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">{grid_items_en}                </div>\\n        </section>', 
                       en_content, flags=re.DOTALL)

with open("products.html", "w", encoding="utf-8") as f:
    f.write(new_en_content)

# Apply to zh-tw/products.html
with open("zh-tw/products.html", "r", encoding="utf-8") as f:
    zh_content = f.read()

new_zh_content = re.sub(r'<!-- Product Grid.*?<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">(.*?)</div>\s*</section>', 
                       f'<!-- 產品列表 -->\\n        <section id="product-grid" class="max-w-[1400px] mx-auto px-4 lg:px-8 pb-20">\\n                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">{grid_items_zh}                </div>\\n        </section>', 
                       zh_content, flags=re.DOTALL)

with open("zh-tw/products.html", "w", encoding="utf-8") as f:
    f.write(new_zh_content)

print("Product grid updated successfully.")
