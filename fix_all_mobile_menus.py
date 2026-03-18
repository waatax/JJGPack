import os
import re

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine language
    is_zh = 'zh-tw' in filepath.lower()
    
    # 1. Ensure x-data on body includes mobileMenu: false
    # Look for <body ...>
    body_match = re.search(r'<body([^>]*)>', content, re.IGNORECASE)
    if body_match:
        body_attrs = body_match.group(1)
        if 'x-data' not in body_attrs:
            new_body = f'<body x-data="{{ mobileMenu: false }}"{body_attrs}>'
            content = content.replace(body_match.group(0), new_body)
        elif 'mobileMenu' not in body_attrs:
            # Inject mobileMenu into existing x-data
            new_attrs = re.sub(r'x-data\s*=\s*["\']\{([^}]*)\}["\']', r'x-data="{ mobileMenu: false, \1 }"', body_attrs)
            content = content.replace(body_match.group(0), f'<body{new_attrs}>')

    # 2. Check if mobile menu div exists
    if 'x-show="mobileMenu"' in content:
        # It exists, but let's make sure it's correct/standardized if possible
        # For now, if it exists, we skip to avoid breaking custom implementations
        # unless it's obviously broken.
        pass
    else:
        # Search for </nav> inside <header>
        # We find the first </nav> and insert after it
        nav_end = content.find('</nav>')
        if nav_end != -1:
            if is_zh:
                mobile_menu_html = """
                <div x-show="mobileMenu" x-transition:enter="transition ease-out duration-300"
                        x-transition:enter-start="opacity-0 -translate-y-2"
                        x-transition:enter-end="opacity-100 translate-y-0"
                        x-transition:leave="transition ease-in duration-200"
                        x-transition:leave-start="opacity-100"
                        x-transition:leave-end="opacity-0 -translate-y-2"
                        class="lg:hidden glass border-t border-gray-200/50" style="display:none">
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
                        x-transition:enter-start="opacity-0 -translate-y-2"
                        x-transition:enter-end="opacity-100 translate-y-0"
                        x-transition:leave="transition ease-in duration-200"
                        x-transition:leave-start="opacity-100"
                        x-transition:leave-end="opacity-0 -translate-y-2"
                        class="lg:hidden glass border-t border-gray-200/50" style="display:none">
                        <div class="px-6 py-5 space-y-1">
                                <a href="/index.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">Home</a>
                                <a href="/about.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">About Us</a>
                                <a href="/products.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">Products</a>
                                <a href="/news.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">News</a>
                                <a href="/catalog.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">E-Catalog</a>
                                <a href="/contact.html" class="block py-2 px-3 rounded hover:bg-[#F5F0E8] transition-colors">Contact Us</a>
                        </div>
                </div>"""
            
            # Insert after </nav>
            content = content[:nav_end+6] + mobile_menu_html + content[nav_end+6:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filepath}")

def main():
    root_dir = "."
    for root, dirs, files in os.walk(root_dir):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if 'dist' in dirs:
            dirs.remove('dist')
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith(".html"):
                fix_html_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
