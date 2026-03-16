import os
import glob

def get_html_files():
    # Find all html files except those in node_modules and dist
    html_files = glob.glob("**/*.html", recursive=True)
    filtered = [f for f in html_files if "node_modules" not in f and "dist" not in f and "public" not in f]
    
    # Create the input map for Vite
    input_map = {}
    for f in filtered:
        # Create a key like 'zh-tw-products-greaseproof-pfas-free'
        key = f.replace(".html", "").replace("\\", "-").replace("/", "-")
        if f == "index.html":
            key = "main"
        clean_path = f.replace("\\", "/")
        input_map[key] = f"resolve(__dirname, '{clean_path}')"
    
    return input_map

input_map = get_html_files()

# Generate the vite.config.js content
config_content = f"""import {{ resolve }} from 'path'
import {{ defineConfig }} from 'vite'

export default defineConfig({{
	base: '/jjgpack/',
	server: {{
		port: 5175,
	}},
	build: {{
		rollupOptions: {{
			input: {{
"""

for key, path in sorted(input_map.items()):
    config_content += f"\t\t\t\t'{key}': {path},\n"

config_content += """			},
		},
	},
})
"""

with open('vite.config.js', 'w', encoding='utf-8') as f:
    f.write(config_content)

print(f"Updated vite.config.js with {len(input_map)} entry points and base: '/jjgpack/'")