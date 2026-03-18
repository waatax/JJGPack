import urllib.request
import os

base_url = "https://waatax.github.io/JJGPack/"
categories = ["flathandle", "foil", "greaseproof", "kraft", "others", "paper-straw", "pe-lamination", "straw", "white", "white-kraft"]
files = []
for c in categories:
    files.append(f"products/{c}.html")
    files.append(f"zh-tw/products/{c}.html")

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
