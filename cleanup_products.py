from pathlib import Path
import shutil
import os

root = Path.cwd()
paths_to_remove = [
    'products/flathandle.html',
    'products/foil.html',
    'products/fruit.html',
    'products/pe.html',
    'products/straw.html',
    'products/white.html',
    'products/flathandle',
    'products/foil',
    'products/fruit',
    'products/pe',
    'products/straw',
    'products/white',
    'zh-tw/products/flathandle.html',
    'zh-tw/products/foil.html',
    'zh-tw/products/fruit.html',
    'zh-tw/products/pe.html',
    'zh-tw/products/straw.html',
    'zh-tw/products/white.html',
    'zh-tw/products/flathandle',
    'zh-tw/products/foil',
    'zh-tw/products/fruit',
    'zh-tw/products/pe',
    'zh-tw/products/straw',
    'zh-tw/products/white'
]

for p in paths_to_remove:
    target = root / p
    if target.exists():
        try:
            if target.is_dir():
                shutil.rmtree(target)
                print(f"Removed dir: {target}")
            else:
                target.unlink()
                print(f"Removed file: {target}")
        except Exception as e:
            print(f"Failed to remove {target}: {e}")
    else:
        print(f"Not found: {target}")
