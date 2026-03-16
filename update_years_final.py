import os
import re

def update_years_final(directory):
    for root, dirs, files in os.walk(directory):
        if any(exc in root for exc in ['node_modules', '.git', 'dist']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Update data-count attributes for the counter animation
                content = content.replace('data-count="60"', 'data-count="70"')
                
                # 2. Update general text patterns
                content = content.replace('60+', '70+')
                content = content.replace('60-year', '70-year')
                content = content.replace('60 year', '70 year')
                content = content.replace('60 餘年', '70 餘年')
                content = content.replace('超過 60 年', '超過 70 年')
                content = content.replace('60年經驗', '70年經驗')
                
                # 3. Specific fix for instances where there might be a space like "60 +" or similar
                content = re.sub(r'60\s*\+', '70+', content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file_path}")

if __name__ == "__main__":
    update_years_final('.')
    print("Final years update complete.")
