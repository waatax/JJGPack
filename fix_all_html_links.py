import os
import re
import glob

def fix_links_in_content(content):
    # 1. Navigation links (.html, directories)
    # Ensure they HAVE /jjgpack/ if they are local routes.
    # Exclude images, styles, and other assets from being prefixed here.
    content = re.sub(
        r'href="/(?!jjgpack/|https?://|#|images/|proimages/|style\.css|main\.js|[^"]*?\.(?:css|js|ico|webmanifest|png|jpg|jpeg|gif|svg|pdf))([^"]*?)"',
        r'href="/jjgpack/\1"',
        content
    )

    # Specific fix for root "/"
    content = re.sub(r'href="/jjgpack/"', 'href="/jjgpack/index.html"', content)
    # Specific fix for "zh-tw/"
    content = re.sub(r'href="/jjgpack/zh-tw/"', 'href="/jjgpack/zh-tw/index.html"', content)

    # 2. Assets (CSS, JS, Images)
    # We want these to start with / so Vite handles them, but WITHOUT the manual /jjgpack/ prefix.
    # If they already have /jjgpack/, remove it.
    
    # Remove manual prefix from src and href for assets
    content = re.sub(r'src="/jjgpack/([^"]*?\.(?:png|jpg|jpeg|gif|svg|webp|js|ico))"', r'src="/\1"', content)
    content = re.sub(r'href="/jjgpack/([^"]*?\.(?:css|js|ico|webmanifest))"', r'href="/\1"', content)

    # Also handle cases where it's src="jjgpack/..." (no leading slash)
    content = re.sub(r'src="jjgpack/([^"]*?\.(?:png|jpg|jpeg|gif|svg|webp|js|ico))"', r'src="/\1"', content)
    content = re.sub(r'href="jjgpack/([^"]*?\.(?:css|js|ico|webmanifest))"', r'href="/\1"', content)

    # 3. Hero Banners / Alpine.js dynamic paths
    # These often need the prefix manually if Vite doesn't parse the JS strings.
    # We will ensure they have it exactly once.
    content = re.sub(
        r"(['\"])/(images/|proimages/)(?!jjgpack/)([^'\"]*?)(['\"])",
        r"\1/jjgpack/\2\3\4",
        content
    )

    # Direct string replacements for common asset folders to ensure cleanup
    content = content.replace('src="/jjgpack/images/', 'src="/images/')
    content = content.replace('src="/jjgpack/proimages/', 'src="/proimages/')
    content = content.replace('src="/jjgpack/proimages/index/', 'src="/proimages/index/')
    content = content.replace('href="/jjgpack/style.css"', 'href="/style.css"')
    content = content.replace('src="/jjgpack/main.js"', 'src="/main.js"')
    content = content.replace('href="/jjgpack/images/favicon.ico"', 'href="/images/favicon.ico"')

    # Also handle non-leading slash cases if any
    content = content.replace('src="jjgpack/images/', 'src="/images/')
    content = content.replace('src="jjgpack/proimages/', 'src="/proimages/')

    # Final cleanup: Ensure no double jjgpack
    content = content.replace('/jjgpack/jjgpack/', '/jjgpack/')

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
