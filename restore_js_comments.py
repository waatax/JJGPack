import os
import glob
import re

def fix_js(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rule: Single / at the beginning of a line followed by ===== should be //
    # Or / followed by a space and then some words
    # This is a bit risky but let's try to restore comments
    
    # 1. Look for patterns like / =====
    content = re.sub(r'(\n\s*)/ (=====)', r'\1// \2', content)
    
    # 2. Look for single / at start of line that was probably a comment
    # This is hard. But let's look at what I broke in main.js
    # 7: / ===== SCROLL REVEAL =====
    # 12: / Stagger children
    # 24: / ===== COUNTER ANIMATION =====
    # 35: / Ease out cubic
    # 55: / ===== SMOOTH NAV SHADOW =====
    
    content = re.sub(r'(\n\s*)/ ([A-Z][a-z])', r'\1// \2', content)
    content = re.sub(r'(\n\s*)/ (Stagger)', r'\1// \2', content)
    content = re.sub(r'(\n\s*)/ (Ease)', r'\1// \2', content)
    
    # Actually, a safer way might be to just revert main.js manually if it's the main one.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix JS files
js_files = glob.glob("**/*.js", recursive=True)
for f in js_files:
    if "node_modules" in f or "dist" in f:
        continue
    print(f"Restoring comments in {f}...")
    fix_js(f)
