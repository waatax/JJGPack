import re

def update_index_links(filepath, is_zh=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    mapping = []
    if not is_zh:
        mapping = [
            ("Flat Handle Paper Bag", "/products/flat-handle/flat-handle-bag.html"),
            ("Square Bottom Paper Bag", "/products/kraft/square-paper-bag.html"),
            ("Greaseproof Satchel Bag", "/products/greaseproof/bakery-series-paper-bags.html"),
            ("2-Side Open Burger Bag", "/products/pe-lamination/l-bag.html"),
            ("Bakery Window Bag", "/products/greaseproof/bakery-side-window-bag.html"),
            ("Deli Wrap Paper", "/products/greaseproof/deli-wrap.html")
        ]
        old_link = '/products.html'
    else:
        mapping = [
            ("平把手提紙袋", "/zh-tw/products/flat-handle/flat-handle-bag.html"),
            ("方底牛皮紙袋", "/zh-tw/products/kraft/square-paper-bag.html"),
            ("防油紙袋", "/zh-tw/products/greaseproof/bakery-series-paper-bags.html"),
            ("雙面開口漢堡袋", "/zh-tw/products/pe-lamination/l-bag.html"),
            ("開窗麵包袋", "/zh-tw/products/greaseproof/bakery-side-window-bag.html"),
            ("防油包裝紙", "/zh-tw/products/greaseproof/deli-wrap.html")
        ]
        old_link = '/zh-tw/products.html'

    for title, new_path in mapping:
        # Match the block starting with the title and finding the next occurrence of the old link
        # This is a bit safer: find title, then find the first old_link after it
        # We'll use a simple find and replace for the first occurrence after the title
        title_idx = content.find(title)
        if title_idx != -1:
            link_idx = content.find(old_link, title_idx)
            if link_idx != -1 and link_idx - title_idx < 1000: # Ensure it's in the same card
                content = content[:link_idx] + new_path + content[link_idx + len(old_link):]
                print(f"Updated {title} to {new_path}")
            else:
                print(f"Link not found for {title}")
        else:
            print(f"Title not found: {title}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    print("Updating index.html...")
    update_index_links('index.html', is_zh=False)
    print("\nUpdating zh-tw/index.html...")
    update_index_links('zh-tw/index.html', is_zh=True)
