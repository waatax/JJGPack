import os
import glob
import re

def fix_links_in_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    CORRECT_BASE = "/JJGPack/"
    
    # 1. Navigation links (a href) HAVE the prefix
    # Matches href="/... but not if it's already /JJGPack/
    # Only for .html files or directories
    content = re.sub(r'href="/(?!JJGPack/|https?://|#|tel:|mailto:)([^"]*?\.html|[^"]*?/|(?:"|\'))', r'href="/JJGPack/\1', content)
    
    # 2. Assets (src, link href) REMOVE the prefix
    # This ensures Vite doesn't double-prefix them.
    # We remove both /JJGPack/ and /jjgpack/ (case insensitive)
    content = re.sub(r'src="/JJGPack/([^"]+)"', r'src="/\1"', content, flags=re.IGNORECASE)
    content = re.sub(r'href="/JJGPack/([^"]+\.(?:css|js|ico|png|jpg|jpeg|svg))"', r'href="/\1"', content, flags=re.IGNORECASE)
    
    # 3. Alpine.js image strings (JS arrays etc.) MUST have the prefix
    # because Vite doesn't transform them.
    content = re.sub(r"(['\"])/(?!JJGPack/|https?://)(images/|proimages/)([^'\"]*?)(\1)", r"\1/JJGPack/\2\3\4", content)
    
    # 4. Clean up any accidental double prefixes
    content = content.replace("/JJGPack/JJGPack/", "/JJGPack/")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = glob.glob("**/*.html", recursive=True)
    for f in html_files:
        if "node_modules" in f or "dist" in f:
            continue
        fix_links_in_file(f)
    print("Links cleaned up again.")

if __name__ == "__main__":
    main()
