import re
import os

def update_file(filepath, mapping, old_link_pattern):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for title, new_path in mapping:
        # escapes the title just in case
        safe_title = re.escape(title)
        # Regex to find the title, then any content until the first href pointing to the old pattern
        # We look for href="old_link_pattern"
        pattern = rf"({safe_title}.*?href=\")({re.escape(old_link_pattern)})(\")"
        
        def replace_func(match):
            print(f"Found match for {title}, replacing with {new_path}")
            return match.group(1) + new_path + match.group(3)

        new_content, count = re.subn(pattern, replace_func, content, count=1, flags=re.DOTALL)
        if count == 0:
            print(f"No match found for: {title}")
        content = new_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    en_mapping = [
        ("Flat Handle Paper Bag", "/products/flat-handle/flat-handle-bag.html"),
        ("Square Bottom Paper Bag", "/products/kraft/square-paper-bag.html"),
        ("Greaseproof Satchel Bag", "/products/greaseproof/bakery-series-paper-bags.html"),
        ("2-Side Open Burger Bag", "/products/pe-lamination/l-bag.html"),
        ("Bakery Window Bag", "/products/greaseproof/bakery-side-window-bag.html"),
        ("Deli Wrap Paper", "/products/greaseproof/deli-wrap.html")
    ]
    
    zh_mapping = [
        ("平把手提紙袋", "/zh-tw/products/flat-handle/flat-handle-bag.html"),
        ("方底牛皮紙袋", "/zh-tw/products/kraft/square-paper-bag.html"),
        ("防油紙袋", "/zh-tw/products/greaseproof/bakery-series-paper-bags.html"),
        ("雙面開口漢堡袋", "/zh-tw/products/pe-lamination/l-bag.html"),
        ("開窗麵包袋", "/zh-tw/products/greaseproof/bakery-side-window-bag.html"),
        ("防油包裝紙", "/zh-tw/products/greaseproof/deli-wrap.html")
    ]

    print("Updating index.html...")
    update_file('index.html', en_mapping, '/products.html')
    
    print("\nUpdating zh-tw/index.html...")
    update_file('zh-tw/index.html', zh_mapping, '/zh-tw/products.html')
