import os
import glob
import re

def fix_en_headers(file_path):
    # Only for root HTML files (not in zh-tw)
    if "zh-tw" in file_path: return
    
    print(f"Fixing EN header in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the standardized EN navigation links
    en_nav_items_desktop = """
                                <a href="/JJGPack/index.html" class="[HOME_CLASS]">Home</a>
                                <a href="/JJGPack/about.html" class="[ABOUT_CLASS]">About Us</a>
                                <a href="/JJGPack/products.html" class="[PRODUCTS_CLASS]">Products</a>
                                <a href="/JJGPack/news.html" class="[NEWS_CLASS]">News</a>
                                <a href="/JJGPack/catalog.html" class="[CATALOG_CLASS]">E-Catalog</a>
                                <a href="/JJGPack/contact.html" class="[CONTACT_CLASS]">Contact Us</a>"""

    en_nav_items_mobile = """
                                <a href="/JJGPack/index.html" class="[HOME_MOB_CLASS]">Home</a>
                                <a href="/JJGPack/about.html" class="[ABOUT_MOB_CLASS]">About Us</a>
                                <a href="/JJGPack/products.html" class="[PRODUCTS_MOB_CLASS]">Products</a>
                                <a href="/JJGPack/news.html" class="[NEWS_MOB_CLASS]">News</a>
                                <a href="/JJGPack/catalog.html" class="[CATALOG_MOB_CLASS]">E-Catalog</a>
                                <a href="/JJGPack/contact.html" class="[CONTACT_MOB_CLASS]">Contact Us</a>"""

    # Helper to set classes
    def get_classes(is_mob=False):
        cls_active = "text-[#1A5C38] font-semibold text-[15px]" if not is_mob else "block py-2 px-3 rounded bg-[#F5F0E8] font-semibold text-[#1A5C38]"
        cls_inactive = "text-[#666] hover:text-[#2E8B57] font-medium text-[15px] transition" if not is_mob else "block py-2 px-3 rounded hover:bg-[#F5F0E8]"
        
        # New design system in index.html (premium headers)
        if "index.html" in file_path:
             cls_active = "relative px-4 py-2 text-[#1A5C38] font-semibold text-[15px] after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-5 after:h-0.5 after:bg-[#1A5C38] after:rounded-full"
             cls_inactive = "px-4 py-2 text-[#555] hover:text-[#1A5C38] font-medium text-[15px] transition-all relative after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-0 after:h-0.5 after:bg-[#1A5C38] after:rounded-full hover:after:w-5 after:transition-all"

        res = {}
        pages = ["index.html", "about.html", "products.html", "news.html", "catalog.html", "contact.html"]
        keys = ["HOME", "ABOUT", "PRODUCTS", "NEWS", "CATALOG", "CONTACT"]
        
        for p, k in zip(pages, keys):
            active = p in file_path
            res[k + ("_MOB" if is_mob else "") + "_CLASS"] = cls_active if active else cls_inactive
        return res

    classes = get_classes(is_mob=False)
    classes_mob = get_classes(is_mob=True)
    all_classes = {**classes, **classes_mob}

    final_nav_dt = en_nav_items_desktop
    final_nav_mob = en_nav_items_mobile
    for k, v in all_classes.items():
        final_nav_dt = final_nav_dt.replace(f"[{k}]", v)
        final_nav_mob = final_nav_mob.replace(f"[{k}]", v)

    # 1. Replace Desktop Nav block
    pattern_dt = re.compile(r'<div class="hidden lg:flex items-center gap-8">.*?</div>', re.DOTALL)
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

    # 3. Footer
    pattern_footer = re.compile(r'<h4 class="text-white font-bold mb-4 uppercase text-sm tracking-wider">Quick\s+Links</h4>.*?</ul>', re.DOTALL)
    pattern_footer_alt = re.compile(r'<h4 class="text-white font-bold mb-5 text-sm tracking-\[0.15em\]">Quick Links</h4>.*?</ul>', re.DOTALL)

    footer_nav = """<h4 class="text-white font-bold mb-5 text-sm tracking-[0.15em]">Quick Links</h4>
                                        <ul class="space-y-3 text-sm">
                                                <li><a href="/JJGPack/index.html" class="hover:text-[#2E8B57] transition">Home</a></li>
                                                <li><a href="/JJGPack/about.html" class="hover:text-[#2E8B57] transition">About Us</a></li>
                                                <li><a href="/JJGPack/products.html" class="hover:text-[#2E8B57] transition">Products</a></li>
                                                <li><a href="/JJGPack/news.html" class="hover:text-[#2E8B57] transition">News</a></li>
                                                <li><a href="/JJGPack/catalog.html" class="hover:text-[#2E8B57] transition">E-Catalog</a></li>
                                                <li><a href="/JJGPack/contact.html" class="hover:text-[#2E8B57] transition">Contact Us</a></li>
                                        </ul>"""

    if pattern_footer.search(content):
        content = pattern_footer.sub(footer_nav, content)
    elif pattern_footer_alt.search(content):
        content = pattern_footer_alt.sub(footer_nav, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply
en_files = glob.glob("*.html")
for f in en_files:
    fix_en_headers(f)
