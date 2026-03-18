import urllib.request
import os

base_url = "https://waatax.github.io/JJGPack/"
files = [
    "index.html", "about.html", "products.html", "news.html", "contact.html",
    "zh-tw/index.html", "zh-tw/about.html", "zh-tw/products.html", "zh-tw/news.html", "zh-tw/contact.html"
]

# Adding some product subpages if known
# I'll just start with these and then crawl more if needed.

for f in files:
    url = base_url + f
    dir_name = os.path.dirname(f)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    print(f"Downloading {url}...")
    try:
        with urllib.request.urlopen(url) as response, open(f, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Restored {f}")
    except Exception as e:
        print(f"Failed to download {f}: {e}")
