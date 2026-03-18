import os
import re

def standardize_mobile_menu(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine language
    is_zh = 'zh-tw' in filepath.lower()
    
    # 1. Standardise x-data on body or header/nav
    # We'll just ensure x-data="{ mobileMenu: false, ... }" is on the <body> tag.
    body_match = re.search(r'<body([^>]*)>', content, re.IGNORECASE)
    if body_match:
        body_attrs = body_match.group(1)
        if 'x-data' not in body_attrs:
            # We don't want to double "body" tag if we use replace wrongly.
            full_body_tag = body_match.group(0)
            parts = full_body_tag.split('body', 1)
            new_tag = parts[0] + 'body x-data="{ mobileMenu: false }"' + parts[1]
            content = content.replace(full_body_tag, new_tag)
        elif 'mobileMenu' not in body_attrs:
            # Add mobileMenu to existing x-data
            # This is tricky because it could be x-data="{...}" or x-data="myState()" or even x-data="{ mobileMenu: false }" already with different spacing
            if 'x-data="{ ' in body_attrs:
                new_attrs = body_attrs.replace('x-data="{ ', 'x-data="{ mobileMenu: false, ')
            elif 'x-data="{' in body_attrs:
                new_attrs = body_attrs.replace('x-data="{', 'x-data="{ mobileMenu: false, ')
            else:
                 # fallback: just wrap entire content
                 pass # We skip if it's too complex to avoid breaking script tags
    
    # 2. Find and Replace (or Insert) the mobile menu container.
    # We first REMOVE any existing mobile menu container to standardize.
    # Pattern: a div with x-show="mobileMenu"
    # We look for <div x-show="mobileMenu" ... </div>
    # This regex is a bit risky for nested divs, but we'll try to find a block.
    # Actually, better search for the specific mobile menu classes we used before.
    content = re.sub(r'<div x-show="mobileMenu".*?</div>\s*</div>', 'REMOVE_PLACEHOLDER', content, flags=re.DOTALL)
    # Also clean up any simpler ones.
    content = re.sub(r'<div x-show="mobileMenu".*?</div>', 'REMOVE_PLACEHOLDER', content, flags=re.DOTALL)

    # Now define the new menu
    if is_zh:
        mobile_menu_html = """
    <div x-show="mobileMenu" x-transition:enter="transition ease-out duration-300"
      x-transition:enter-start="opacity-0 -translate-y-2" x-transition:enter-end="opacity-100 translate-y-0"
      x-transition:leave="transition ease-in duration-200" x-transition:leave-start="opacity-100"
      x-transition:leave-end="opacity-0 -translate-y-2" class="lg:hidden glass border-t border-gray-200/50"
      style="display:none">
      <div class="px-6 py-5 space-y-1">
        <a href="/zh-tw/index.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">首頁</a>
        <a href="/zh-tw/about.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">關於我們</a>
        <a href="/zh-tw/products.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">產品介紹</a>
        <a href="/zh-tw/news.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">最新消息</a>
        <a href="/zh-tw/catalog.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">型錄EDM</a>
        <a href="/zh-tw/contact.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">聯絡我們</a>
      </div>
    </div>"""
    else:
        mobile_menu_html = """
    <div x-show="mobileMenu" x-transition:enter="transition ease-out duration-300"
      x-transition:enter-start="opacity-0 -translate-y-2" x-transition:enter-end="opacity-100 translate-y-0"
      x-transition:leave="transition ease-in duration-200" x-transition:leave-start="opacity-100"
      x-transition:leave-end="opacity-0 -translate-y-2" class="lg:hidden glass border-t border-gray-200/50"
      style="display:none">
      <div class="px-6 py-5 space-y-1">
        <a href="/index.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">Home</a>
        <a href="/about.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">About Us</a>
        <a href="/products.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">Products</a>
        <a href="/news.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">News</a>
        <a href="/catalog.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">E-Catalog</a>
        <a href="/contact.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">Contact Us</a>
      </div>
    </div>"""

    if 'REMOVE_PLACEHOLDER' in content:
        content = content.replace('REMOVE_PLACEHOLDER', mobile_menu_html, 1) # Insert it at first placeholder
        content = content.replace('REMOVE_PLACEHOLDER', '') # Clean any others
    else:
        # Fallback: find </nav> and insert
        nav_end = content.find('</nav>')
        if nav_end != -1:
            content = content[:nav_end+6] + mobile_menu_html + content[nav_end+6:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Standardized {filepath}")

def main():
    root_dir = "."
    for root, dirs, files in os.walk(root_dir):
        # Exclude directories we don't want to touch
        for exclude in ['node_modules', 'dist', '.git', 'EDM-Web']:
            if exclude in dirs:
                dirs.remove(exclude)
            
        for file in files:
            if file.endswith(".html"):
                standardize_mobile_menu(os.path.join(root, file))

if __name__ == "__main__":
    main()
