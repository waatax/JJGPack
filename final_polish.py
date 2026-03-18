import os
import glob
import re

def final_polish():
    html_files = glob.glob(os.path.join(os.getcwd(), "**/*.html"), recursive=True)
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Standardize main assets
        content = re.sub(r'(src|href)="/(main\.js|style\.css)"', r'\1="/JJGPack/\2"', content)
        
        # 2. Standardize favicon
        content = re.sub(r'href="/images/favicon\.ico"', r'href="/JJGPack/images/favicon.ico"', content)
        
        # 3. Standardize common images (logo, etc)
        content = re.sub(r'src="/images/index-logo\.png"', r'src="/JJGPack/images/index-logo.png"', content)
        
        # 4. Standardize proimages
        content = re.sub(r'src="/proimages/', r'src="/JJGPack/proimages/', content)
        
        # 5. Cleanup double prefixes
        content = content.replace('/JJGPack//JJGPack/', '/JJGPack/')
        content = content.replace('/JJGPack/JJGPack/', '/JJGPack/')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    print("Final polish complete.")

if __name__ == "__main__":
    final_polish()
