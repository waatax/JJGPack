import os
import glob
import re

def fix_links_in_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rule 1: Navigation links (<a> tags) should have the /JJGPack/ prefix
    # Match href="/... but skip external, anchors, and already prefixed
    content = re.sub(r'href="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?\.html|[^"]*?/|(?:"|\'))', r'href="/JJGPack/\1', content)
    
    # Rule 2: Standalone assets (img, script, link) should NOT have the prefix (Vite adds it)
    # Remove it if it exists.
    content = re.sub(r'src="/JJGPack/([^"]+)"', r'src="/\1"', content, flags=re.IGNORECASE)
    content = re.sub(r'<link ([^>]*?)href="/JJGPack/([^"]+\.(?:css|js|ico|png|jpg|jpeg|svg))"', r'<link \1href="/\2"', content, flags=re.IGNORECASE)
    
    # Rule 3: JS strings in attributes (like Alpine.js arrays) MUST have the prefix
    # Matches strings like '/images/...' or '/proimages/...' inside attributes
    # We look for quotes around the path.
    content = re.sub(r"(['\"])/(?!JJGPack/|https?://)(images/|proimages/)([^'\"]*?)(\1)", r"\1/JJGPack/\2\3\4", content)

    # Final cleanup: Ensure no double-prefixing happened accidentally
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")
    
    # Ensure all /jjgpack/ (lowercase) are converted to /JJGPack/
    content = content.replace("/jjgpack/", "/JJGPack/")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = glob.glob("**/*.html", recursive=True)
    for f in html_files:
        if "node_modules" in f or "dist" in f:
            continue
        fix_links_in_file(f)
    print("Optimization complete: Routing prefixed, assets root-relative, JS strings prefixed.")

if __name__ == "__main__":
    main()
