import os
import glob
import re

def refine_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update large vertical padding for mobile
    # Tailwind py-24 is 6rem (96px), too big for mobile. Change to py-16 md:py-24
    content = re.sub(r'\bpy-24\b', 'py-16 md:py-24', content)
    # Change py-20 to py-16 md:py-20
    content = re.sub(r'\bpy-20\b', 'py-16 md:py-20', content)
    
    # 2. Update horizontal padding for smaller screens
    content = content.replace('px-6 lg:px-10', 'px-5 sm:px-8 lg:px-10')
    content = content.replace('px-4 lg:px-8', 'px-5 sm:px-6 lg:px-8')
    
    # 3. Hero Text Adjustments
    # Make mobile titles slightly smaller but keep desktop large
    content = content.replace('text-5xl md:text-6xl lg:text-7xl', 'text-[42px] leading-[1.2] md:text-6xl lg:text-7xl')
    content = content.replace('text-4xl md:text-5xl', 'text-3xl md:text-5xl')
    
    # 4. Grid gaps
    content = content.replace('gap-8', 'gap-6 md:gap-8')
    content = content.replace('gap-12', 'gap-8 md:gap-12')
    
    # 5. Fix Hero height
    # h-[92vh] can be weird on iOS Safari with bottom bars.
    content = content.replace('h-[92vh]', 'h-[100svh] lg:h-[92vh]')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to main pages
html_files = glob.glob('*.html') + glob.glob('zh-tw/*.html')

for f in html_files:
    refine_html(f)

print("Applied aesthetic and responsive refinements to all main pages.")
