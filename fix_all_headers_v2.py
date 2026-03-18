import os
import re

def standardize_mobile_menu(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine language
    is_zh = 'zh-tw' in filepath.lower()
    
    # 1. Update/Inject x-data on body
    # We first find the body tag
    body_match = re.search(r'<body([^>]*)>', content, re.IGNORECASE)
    if body_match:
        body_tag = body_match.group(0)
        body_attrs = body_match.group(1)
        
        # Check for x-data
        if 'x-data' not in body_attrs:
            # Add it
            new_tag = body_tag.replace('body', 'body x-data="{ mobileMenu: false }"')
            content = content.replace(body_tag, new_tag)
        elif 'mobileMenu' not in body_attrs:
            # If x-data exists, inject mobileMenu into it
            # Matches: x-data="{ ... }"
            new_attrs = re.sub(r'x-data\s*=\s*["\']\{', 'x-data="{ mobileMenu: false, ', body_attrs)
            if new_attrs == body_attrs:
                # If it's a script-based state like x-data="myState()", this is harder.
                # But looking at the codebase, they are all literal objects.
                pass
            content = content.replace(body_tag, f'<body{new_attrs}>')

    # 2. Force Header Style Standardisation (Optional but helpful)
    # Most subpages use sticky, index uses fixed. 
    # Let's at least ensure the button exists and is correct.
    # Pattern: @click="mobileMenu=!mobileMenu"
    if '@click="mobileMenu=!mobileMenu"' not in content:
        # Some might use @click="mobileMenu = !mobileMenu".
        pass 

    # 3. Standardise the Menu Div itself
    # We clean up any div that looks like a mobile menu
    # look for x-show="mobileMenu"
    # This greedy regex is still a bit dangerous but better for standardisation
    content = re.sub(r'\s*<div\s+x-show="mobileMenu".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<div\s+x-show="mobileMenu".*?</div>', '', content, flags=re.DOTALL)

    # Defined the standardized menu
    if is_zh:
        mobile_menu_html = """
    <!-- Mobile Menu -->
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
    <!-- Mobile Menu -->
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

    # Insert it after the first </nav> we find
    nav_end = content.find('</nav>')
    if nav_end != -1:
        content = content[:nav_end+6] + mobile_menu_html + content[nav_end+6:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filepath}")

def main():
    root_dir = "."
    for root, dirs, files in os.walk(root_dir):
        # Exclude directories we don't want to touch
        dirs_to_skip = ['node_modules', 'dist', '.git', 'EDM-Web']
        for skip in dirs_to_skip:
            if skip in dirs:
                dirs.remove(skip)
            
        for file in files:
            if file.endswith(".html"):
                standardize_mobile_menu(os.path.join(root, file))

if __name__ == "__main__":
    main()
