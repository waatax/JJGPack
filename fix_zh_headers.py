import os
import glob
import re

def fix_zh_headers(file_path):
    print(f"Fixing ZH header in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the standardized ZH navigation links
    zh_nav_items_desktop = """
                                <a href="/JJGPack/zh-tw/index.html" class="[HOME_CLASS]">首頁</a>
                                <a href="/JJGPack/zh-tw/about.html" class="[ABOUT_CLASS]">關於我們</a>
                                <a href="/JJGPack/zh-tw/products.html" class="[PRODUCTS_CLASS]">產品介紹</a>
                                <a href="/JJGPack/zh-tw/news.html" class="[NEWS_CLASS]">最新消息</a>
                                <a href="/JJGPack/zh-tw/catalog.html" class="[CATALOG_CLASS]">型錄EDM</a>
                                <a href="/JJGPack/zh-tw/contact.html" class="[CONTACT_CLASS]">聯絡我們</a>"""

    zh_nav_items_mobile = """
                                <a href="/JJGPack/zh-tw/index.html" class="[HOME_MOB_CLASS]">首頁</a>
                                <a href="/JJGPack/zh-tw/about.html" class="[ABOUT_MOB_CLASS]">關於我們</a>
                                <a href="/JJGPack/zh-tw/products.html" class="[PRODUCTS_MOB_CLASS]">產品介紹</a>
                                <a href="/JJGPack/zh-tw/news.html" class="[NEWS_MOB_CLASS]">最新消息</a>
                                <a href="/JJGPack/zh-tw/catalog.html" class="[CATALOG_MOB_CLASS]">型錄EDM</a>
                                <a href="/JJGPack/zh-tw/contact.html" class="[CONTACT_MOB_CLASS]">聯絡我們</a>"""

    # Helper to set classes based on current page
    def get_classes(is_mob=False):
        cls_active = "text-[#1A5C38] font-semibold text-[15px]" if not is_mob else "block py-2 px-3 rounded bg-[#F5F0E8] font-semibold text-[#1A5C38]"
        cls_inactive = "text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition" if not is_mob else "block py-2 px-3 rounded hover:bg-[#F5F0E8]"
        
        # New design system in index.html (premium headers)
        if "index.html" in file_path and not "zh-tw" in os.path.dirname(file_path):
            # This is EN index, skip
            pass 

        # We'll use a simpler common style for these subpages unless it's index.html
        res = {}
        pages = ["index.html", "about.html", "products", "news.html", "catalog.html", "contact.html"]
        keys = ["HOME", "ABOUT", "PRODUCTS", "NEWS", "CATALOG", "CONTACT"]
        
        for p, k in zip(pages, keys):
            active = p in file_path
            res[k + ("_MOB" if is_mob else "") + "_CLASS"] = cls_active if active else cls_inactive
        return res

    classes = get_classes(is_mob=False)
    classes_mob = get_classes(is_mob=True)
    all_classes = {**classes, **classes_mob}

    final_nav_dt = zh_nav_items_desktop
    final_nav_mob = zh_nav_items_mobile
    for k, v in all_classes.items():
        final_nav_dt = final_nav_dt.replace(f"[{k}]", v)
        final_nav_mob = final_nav_mob.replace(f"[{k}]", v)

    # 1. Replace Desktop Nav block
    # We look for the container div
    pattern_dt = re.compile(r'<div class="hidden lg:flex items-center gap-8">.*?</div>', re.DOTALL)
    # Also handle index.html style gap-1
    pattern_dt_alt = re.compile(r'<div class="hidden lg:flex items-center gap-1">.*?</div>', re.DOTALL)
    
    if pattern_dt.search(content):
        content = pattern_dt.sub(f'<div class="hidden lg:flex items-center gap-8">{final_nav_dt}\n                        </div>', content)
    elif pattern_dt_alt.search(content):
        content = pattern_dt_alt.sub(f'<div class="hidden lg:flex items-center gap-1">{final_nav_dt}\n                        </div>', content)

    # 2. Replace Mobile Nav block
    pattern_mob = re.compile(r'<div class="px-4 py-4 space-y-2">.*?</div>', re.DOTALL)
    pattern_mob_alt = re.compile(r'<div class="px-6 py-5 space-y-1">.*?</div>', re.DOTALL)

    if pattern_mob.search(content):
        content = pattern_mob.sub(f'<div class="px-4 py-4 space-y-2">{final_nav_mob}\n                        </div>', content)
    elif pattern_mob_alt.search(content):
        content = pattern_mob_alt.sub(f'<div class="px-6 py-5 space-y-1">{final_nav_mob}\n                        </div>', content)

    # 3. Fix Footer (Quick Links) in ZH
    footer_pattern = re.compile(r'<h4 class="text-white font-bold mb-5 text-sm tracking-\[0.15em\]">快速連結</h4>.*?</ul>', re.DOTALL)
    if footer_pattern.search(content):
        footer_nav = f"""<h4 class="text-white font-bold mb-5 text-sm tracking-[0.15em]">快速連結</h4>
                                        <ul class="space-y-3 text-sm">
                                                <li><a href="/JJGPack/zh-tw/index.html" class="hover:text-[#2E8B57] transition">首頁</a></li>
                                                <li><a href="/JJGPack/zh-tw/about.html" class="hover:text-[#2E8B57] transition">關於我們</a></li>
                                                <li><a href="/JJGPack/zh-tw/products.html" class="hover:text-[#2E8B57] transition">產品介紹</a></li>
                                                <li><a href="/JJGPack/zh-tw/news.html" class="hover:text-[#2E8B57] transition">最新消息</a></li>
                                                <li><a href="/JJGPack/zh-tw/catalog.html" class="hover:text-[#2E8B57] transition">型錄EDM</a></li>
                                                <li><a href="/JJGPack/zh-tw/contact.html" class="hover:text-[#2E8B57] transition">聯絡我們</a></li>
                                        </ul>"""
        content = footer_pattern.sub(footer_nav, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to all ZH files
zh_files = glob.glob("zh-tw/**/*.html", recursive=True)
for f in zh_files:
    fix_zh_headers(f)

print("ZH headers standardized.")
