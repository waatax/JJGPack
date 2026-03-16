import os
import re
import glob

def fix_links_in_content(content):
    # 1. Navigation links (.html, directories)
    # Ensure they HAVE /jjgpack/
    # We match href="/..." where ... is NOT jjgpack/, not external, not fragment, and is a page.
    content = re.sub(
        r'href="/(?!jjgpack/|https?://|#|images/|proimages/|style\.css|main\.js|[^"]*?\.(?:css|js|ico|webmanifest|png|jpg|jpeg|gif|svg))([^"]*?)"',
        r'href="/jjgpack/\1"',
        content
    )

    # Specific fix for root "/" and sub-roots
    content = re.sub(r'href="/jjgpack/"', 'href="/jjgpack/index.html"', content)
    content = re.sub(r'href="/jjgpack/zh-tw/"', 'href="/jjgpack/zh-tw/index.html"', content)

    # 2. Assets (CSS, JS, Images, Icons)
    # Ensure they DO NOT have the manual /jjgpack/ prefix because Vite will add it.
    # Patterns like src="/jjgpack/images/..." -> src="/images/..."
    # Patterns like href="/jjgpack/style.css" -> href="/style.css"
    
    # Images and Assets in src
    content = re.sub(r'src="/jjgpack/([^"]*?\.(?:png|jpg|jpeg|gif|svg|webp|js))"', r'src="/\1"', content)
    
    # 3. Handle root-relative paths in JS datasets or Alpine attributes (like banners)
    # Match patterns like '/proimages/banner/...' inside single or double quotes
    # starting with / and followed by proimages or images or other asset dirs.
    content = re.sub(
        r"(['\"])/(images/|proimages/|proimages/banner/)(?!jjgpack/)([^'\"]*?)(['\"])",
        r"\1/jjgpack/\2\3\4",
        content
    )

    # Cleanup: remove any double jjgpack that escaped
    content = re.sub(r'/jjgpack/jjgpack/', '/jjgpack/', content)

    return content

def process_all_files():
    html_files = glob.glob("**/*.html", recursive=True)
    for file_path in html_files:
        if "node_modules" in file_path or "dist" in file_path:
            continue
            
        print(f"Processing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = fix_links_in_content(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Updated {file_path}")
        else:
            print(f"  No changes for {file_path}")

if __name__ == "__main__":
    process_all_files()
    print("Done fixing links in all HTML files.")
