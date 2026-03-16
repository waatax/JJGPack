import os
import re
import glob

def fix_links_in_content(content):
    # 1. Navigation links (.html, directories)
    # Ensure they HAVE /jjgpack/ if they are local routes.
    # Exclude images, styles, and other assets from being prefixed here.
    content = re.sub(
        r'href="/(?!JJGPACK/|https?://|#|images/|proimages/|style\.css|main\.js|[^"]*?\.(?:css|js|ico|webmanifest|png|jpg|jpeg|gif|svg|pdf))([^"]*?)"',
        r'href="/JJGPACK/\1"',
        content
    )

    # Specific fix for root "/"
    content = re.sub(r'href="/JJGPACK/"', 'href="/JJGPACK/index.html"', content)
    # Specific fix for "zh-tw/"
    content = re.sub(r'href="/JJGPACK/zh-tw/"', 'href="/JJGPACK/zh-tw/index.html"', content)

    # 2. Assets (CSS, JS, Images)
    # We want these to start with / so Vite handles them, but WITHOUT the manual /jjgpack/ prefix.
    # If they already have /jjgpack/, remove it.
    
    # Remove manual prefix from src and href for assets
    content = re.sub(r'src="/JJGPACK/([^"]*?\.(?:png|jpg|jpeg|gif|svg|webp|js|ico))"', r'src="/\1"', content)
    content = re.sub(r'href="/JJGPACK/([^"]*?\.(?:css|js|ico|webmanifest))"', r'href="/\1"', content)

    # Also handle cases where it's src="JJGPACK/..." (no leading slash)
    content = re.sub(r'src="JJGPACK/([^"]*?\.(?:png|jpg|jpeg|gif|svg|webp|js|ico))"', r'src="/\1"', content)
    content = re.sub(r'href="JJGPACK/([^"]*?\.(?:css|js|ico|webmanifest))"', r'href="/\1"', content)

    # 3. Hero Banners / Alpine.js dynamic paths
    # These often need the prefix manually if Vite doesn't parse the JS strings.
    # We will ensure they have it exactly once.
    content = re.sub(
        r"(['\"])/(images/|proimages/)(?!JJGPACK/)([^'\"]*?)(['\"])",
        r"\1/JJGPACK/\2\3\4",
        content
    )

    # Direct string replacements for common asset folders to ensure cleanup
    content = content.replace('src="/JJGPACK/images/', 'src="/images/')
    content = content.replace('src="/JJGPACK/proimages/', 'src="/proimages/')
    content = content.replace('src="/JJGPACK/proimages/index/', 'src="/proimages/index/')
    content = content.replace('href="/JJGPACK/style.css"', 'href="/style.css"')
    content = content.replace('src="/JJGPACK/main.js"', 'src="/main.js"')
    content = content.replace('href="/JJGPACK/images/favicon.ico"', 'href="/images/favicon.ico"')

    # Also handle non-leading slash cases if any
    content = content.replace('src="JJGPACK/images/', 'src="/images/')
    content = content.replace('src="JJGPACK/proimages/', 'src="/proimages/')

    # Final cleanup: Ensure no double JJGPACK and no leftover jjgpack
    content = content.replace('/JJGPACK/JJGPACK/', '/JJGPACK/')
    content = content.replace('/JJGPACK/jjgpack/', '/JJGPACK/')
    content = content.replace('/jjgpack/', '/JJGPACK/')

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
