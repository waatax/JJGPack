import os
import re

def update_logo_and_nav_size(directory):
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
                
                # Flexible regex to target the logo in the header
                # Looks for index-logo.png and h-11/h-12 in the same tag
                
                def replace_logo_height(match):
                    tag = match.group(0)
                    if 'h-11' in tag:
                        return tag.replace('h-11', 'h-[62px]')
                    if 'h-12' in tag:
                        return tag.replace('h-12', 'h-[68px]')
                    return tag

                # Match <img> tags that contain index-logo.png
                new_content = re.sub(r'<img[^>]*src="[^"]*index-logo.png"[^>]*>', replace_logo_height, content)

                # 2. Update Nav Height to fit larger logo
                new_content = new_content.replace('h-[76px]', 'h-[92px]')
                new_content = new_content.replace('h-[72px]', 'h-[88px]')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated logo and nav size in {file_path}")

if __name__ == "__main__":
    update_logo_and_nav_size('.')
    print("Logo and nav size update complete.")
