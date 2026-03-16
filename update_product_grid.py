import os
import re

# Final grid items for products.html (WITHOUT /JJGPACK/ prefix)
grid_items_en = """
                        <!-- FLAT HANDLE -->
                        <div x-show="activeCategory==='all'||activeCategory==='flathandle'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/flat-handle/flat-handle-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/flat-handle-bag.jpg" alt="Flat Handle Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Flat Handle</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/flat-handle/flat-handle-bag.html" class="hover:text-[#2E8B57]">Flat Handle Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">High stability, comfortable grip, food-grade water-based ink.</p>
                                    <a href="/products/flat-handle/flat-handle-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- BROWN KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='kraft'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/kraft/square-paper-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/square-bag.jpg" alt="Square Bottom Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Brown Kraft</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/kraft/square-paper-bag.html" class="hover:text-[#2E8B57]">Square Bottom Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">Self-standing design, high-strength long-fiber kraft paper.</p>
                                    <a href="/products/kraft/square-paper-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- GREASEPROOF -->
                        <div x-show="activeCategory==='all'||activeCategory==='greaseproof'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/greaseproof/bakery-side-window-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/bakery-side-window.jpg" alt="Bakery Side Window Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Greaseproof</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/greaseproof/bakery-side-window-bag.html" class="hover:text-[#2E8B57]">Bakery Side Window Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">PE laminated, grease-resistant with high-clarity transparent window.</p>
                                    <a href="/products/greaseproof/bakery-side-window-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- WHITE KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='white'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/white-kraft/white-kraft-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/white-kraft-bag.png" alt="White Kraft Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">White Kraft</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/white-kraft/white-kraft-bag.html" class="hover:text-[#2E8B57]">White Kraft Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">Premium white kraft, clean appearance for retail and medical use.</p>
                                    <a href="/products/white-kraft/white-kraft-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- ALUMINUM FOIL -->
                        <div x-show="activeCategory==='all'||activeCategory==='foil'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/aluminum-foil/aluminum-foil-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/aluminum-foil-bag.png" alt="Aluminum Foil Paper Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Aluminum Foil</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/aluminum-foil/aluminum-foil-bag.html" class="hover:text-[#2E8B57]">Aluminum Foil Paper Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">Excellent heat retention for roasted chicken and takeaways.</p>
                                    <a href="/products/aluminum-foil/aluminum-foil-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- PE LAMINATION -->
                        <div x-show="activeCategory==='all'||activeCategory==='pe'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/pe-lamination/l-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/l-bag.jpg" alt="PE Lamination L-Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">PE Lamination</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/pe-lamination/l-bag.html" class="hover:text-[#2E8B57]">Burger Pocket L-Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">Leak-proof and grease-resistant burger and sandwich pocket.</p>
                                    <a href="/products/pe-lamination/l-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- FRUIT PROTECTION -->
                        <div x-show="activeCategory==='all'||activeCategory==='fruit'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/fruit-protection/mango-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/mango-bag.jpg" alt="Fruit Protection Bag"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Fruit Protection</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/fruit-protection/mango-bag.html" class="hover:text-[#2E8B57]">Mango Protection Bag</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">Double-layer protection from pests and weather for growing fruits.</p>
                                    <a href="/products/fruit-protection/mango-bag.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- PAPER STRAW -->
                        <div x-show="activeCategory==='all'||activeCategory==='straw'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/paper-straw/paper-straw.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/paper-straw.jpg" alt="Paper Straw"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">Paper Straw</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/paper-straw/paper-straw.html" class="hover:text-[#2E8B57]">Biodegradable Paper Straw</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">100% Taiwan made, plastic-free, eco-friendly drinking solution.</p>
                                    <a href="/products/paper-straw/paper-straw.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>

                        <!-- OTHERS / SPECIALTY -->
                        <div x-show="activeCategory==='all'||activeCategory==='others'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/products/others/specialty-bags.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/bakery-side-window.jpg" alt="Specialty Bags"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold uppercase tracking-wider text-[#666] bg-gray-100 px-2 py-0.5 rounded-full">Others</span>
                                    <h3 class="font-['Playfair_Display',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/products/others/specialty-bags.html" class="hover:text-[#2E8B57]">Custom & Specialty Bags</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">Bespoke solutions for unique requirements and custom material needs.</p>
                                    <a href="/products/others/specialty-bags.html" class="text-[#1A5C38] font-semibold text-sm hover:text-[#2E8B57]">View Details →</a>
                                </div>
                        </div>
"""

grid_items_zh = """
                        <!-- FLAT HANDLE -->
                        <div x-show="activeCategory==='all'||activeCategory==='flathandle'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/flat-handle/flat-handle-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/flat-handle-bag.jpg" alt="扁繩手提紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">扁繩手提袋</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/flat-handle/flat-handle-bag.html" class="hover:text-[#2E8B57]">扁繩手提紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">高穩定性，握感舒適，食品級水性油墨。</p>
                                    <a href="/zh-tw/products/flat-handle/flat-handle-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- BROWN KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='kraft'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/kraft/square-paper-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/square-bag.jpg" alt="方底紙袋 (SOS)"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">牛皮紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/kraft/square-paper-bag.html" class="hover:text-[#2E8B57]">方底紙袋 (SOS)</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">自立式設計方便填充，高強度長纖維牛皮紙。</p>
                                    <a href="/zh-tw/products/kraft/square-paper-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- GREASEPROOF -->
                        <div x-show="activeCategory==='all'||activeCategory==='greaseproof'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/greaseproof/bakery-side-window-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/bakery-side-window.jpg" alt="麵包側窗紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">防油紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/greaseproof/bakery-side-window-bag.html" class="hover:text-[#2E8B57]">麵包側窗紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">PE 淋膜，耐油性佳，配有高透明度視窗。</p>
                                    <a href="/zh-tw/products/greaseproof/bakery-side-window-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- WHITE KRAFT -->
                        <div x-show="activeCategory==='all'||activeCategory==='white'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/white-kraft/white-kraft-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/white-kraft-bag.png" alt="白牛皮紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">白牛皮紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/white-kraft/white-kraft-bag.html" class="hover:text-[#2E8B57]">白牛皮紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">高級白牛皮紙，外觀潔淨，適合零售及藥用包裝。</p>
                                    <a href="/zh-tw/products/white-kraft/white-kraft-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- ALUMINUM FOIL -->
                        <div x-show="activeCategory==='all'||activeCategory==='foil'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/aluminum-foil/aluminum-foil-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/aluminum-foil-bag.png" alt="鋁箔紙袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">鋁箔紙</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/aluminum-foil/aluminum-foil-bag.html" class="hover:text-[#2E8B57]">鋁箔紙袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">優異保溫性能，烤雞、熱食外帶理想選擇。</p>
                                    <a href="/zh-tw/products/aluminum-foil/aluminum-foil-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- PE LAMINATION -->
                        <div x-show="activeCategory==='all'||activeCategory==='pe'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/pe-lamination/l-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/l-bag.jpg" alt="L型袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">淋膜紙袋</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/pe-lamination/l-bag.html" class="hover:text-[#2E8B57]">L型袋 (漢堡袋)</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">防漏耐油，漢堡三明治專用，側面開口方便食用。</p>
                                    <a href="/zh-tw/products/pe-lamination/l-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- FRUIT PROTECTION -->
                        <div x-show="activeCategory==='all'||activeCategory==='fruit'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/fruit-protection/mango-bag.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/mango-bag.jpg" alt="水果套袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">水果套袋</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/fruit-protection/mango-bag.html" class="hover:text-[#2E8B57]">凱特1號-雙層 (芒果袋)</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">雙層保護，防止病蟲害與天氣損傷，促進水果成長。</p>
                                    <a href="/zh-tw/products/fruit-protection/mango-bag.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- PAPER STRAW -->
                        <div x-show="activeCategory==='all'||activeCategory==='straw'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/paper-straw/paper-straw.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/paper-straw.jpg" alt="環保紙吸管"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#2E8B57] bg-[#2E8B57]/10 px-2 py-0.5 rounded-full">紙吸管</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/paper-straw/paper-straw.html" class="hover:text-[#2E8B57]">環保紙吸管</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">100% 台灣製造，無塑料，原生紙漿，環保首選。</p>
                                    <a href="/zh-tw/products/paper-straw/paper-straw.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>

                        <!-- OTHERS -->
                        <div x-show="activeCategory==='all'||activeCategory==='others'"
                                class="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                                <a href="/zh-tw/products/others/specialty-bags.html" class="block aspect-[4/3] overflow-hidden">
                                    <img src="/proimages/detail/bakery-side-window.jpg" alt="客製化特殊袋"
                                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                </a>
                                <div class="p-5">
                                    <span class="text-xs font-semibold tracking-wider text-[#666] bg-gray-100 px-2 py-0.5 rounded-full">其他</span>
                                    <h3 class="font-['Noto_Serif_TC',serif] text-lg font-bold mt-2 mb-1">
                                        <a href="/zh-tw/products/others/specialty-bags.html" class="hover:text-[#2E8B57]">客製化特殊袋</a>
                                    </h3>
                                    <p class="text-[#666] text-sm mb-3">針對獨特產品需求提供客製化包裝解決方案及材質開發。</p>
                                    <a href="/zh-tw/products/others/specialty-bags.html" class="text-[#1A5C38] font-semibold text-sm">完整介紹 →</a>
                                </div>
                        </div>
"""

def update_file(filepath, grid_content):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # regex matches anything between the grid div start and the final closing tag before CTA
    pattern_alt = r'(<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">).*?(</div>\s*</section>)'
    
    replacement = f'\\1{grid_content}                \\2'
    
    new_content = re.sub(pattern_alt, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Failed to match grid pattern in {filepath}")

update_file("products.html", grid_items_en)
update_file("zh-tw/products.html", grid_items_zh)
