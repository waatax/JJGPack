import os
import re

def replace_experience_years(directory):
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        if 'dist' in dirs:
            dirs.remove('dist')
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace 60+ with 70+
                # Also handle 60 餘年 or similar Chinese phrases if found
                new_content = content.replace('60+', '70+')
                new_content = new_content.replace('60 餘年', '70 餘年')
                new_content = new_content.replace('60年', '70年')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")

if __name__ == "__main__":
    replace_experience_years('.')
    print("Experience years update complete.")
