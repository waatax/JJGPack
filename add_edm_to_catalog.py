import os
import glob
import re

def get_edm_html(lang):
    path_suffix = "en" if lang == "en" else "cn"
    files = glob.glob(f"public/edm/{path_suffix}/*.jpg")
    files = [os.path.basename(f) for f in files]
    files.sort()
    
    # User requested to remove the green title "型錄EDM" / "JJG PACK EDM" from this section
    # But ONLY for Chinese? I'll make it configurable or just remove for both to be safe and clean.
    # The user said: "請幫我拿掉 '綠色的 型錄EDM '"
    
    html = f"""
    <!-- EDM Section -->
    <section class="py-20 bg-[#F9F7F2]">
        <div class="max-w-[1400px] mx-auto px-4 lg:px-8">
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-12">
    """
    
    for f in files:
        title = f.replace(".jpg", "")
        if lang == "en":
            if "-" in title and len(title) > 10 and title[0].isdigit():
                parts = title.split("-", 1)
                if len(parts) > 1:
                    title = parts[1]
            title = title.replace("JJG PACK ", "").replace(" EDM", "").replace(".jpg", "")
        
        html += f"""
                <div class="group cursor-pointer">
                    <a href="/edm/{path_suffix}/{f}" target="_blank" class="block flex flex-col items-center">
                        <div class="aspect-[1/1.414] w-[85%] mx-auto mb-6 overflow-hidden rounded-lg shadow-premium hover:shadow-2xl transition-all duration-500 bg-white border border-gray-100">
                            <img src="/edm/{path_suffix}/{f}" alt="{title}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        </div>
                        <div class="text-center w-[85%]">
                            <h3 class="text-[14px] font-bold text-[#1A1A1A] mb-2 line-clamp-2 uppercase tracking-tight group-hover:text-[#1A5C38] transition-colors">{title}</h3>
                            <div class="h-0.5 w-0 group-hover:w-8 bg-[#1A5C38] mx-auto transition-all duration-300"></div>
                        </div>
                    </a>
                </div>
        """
        
    html += """
            </div>
        </div>
    </section>
    <!-- /EDM Section -->
    """
    return html

def update_catalog(file_path, lang):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update Hero Title style
    if lang == "zh":
        # Change <h1 class="text-4xl md:text-5xl font-bold mb-4">型錄EDM</h1>
        # To <h1 class="text-3xl font-bold mb-4 text-[#1A5C38]">型錄EDM</h1>
        content = re.sub(r'<h1 class="text-4xl md:text-5xl font-bold mb-4">型錄EDM</h1>', 
                         r'<h1 class="text-3xl font-bold mb-4 text-[#1A5C38]">型錄EDM</h1>', content)
    
    # 2. Add/Refresh EDM Section
    content = re.sub(r'<!-- EDM Section -->.*?<!-- /EDM Section -->', '', content, flags=re.DOTALL)
    
    edm_section = get_edm_html(lang)
    
    if "<!-- Catalog Grid -->" in content:
        content = content.replace("<!-- Catalog Grid -->", edm_section + "<!-- Catalog Grid -->")
    else:
        sections = list(re.finditer(r'<section', content))
        if len(sections) >= 2:
            second_section_start = sections[1].start()
            content = content[:second_section_start] + edm_section + content[second_section_start:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

update_catalog("catalog.html", "en")
update_catalog("zh-tw/catalog.html", "zh")

print("Catalog pages updated: Removed green redundant title and updated Hero style on Chinese page.")
