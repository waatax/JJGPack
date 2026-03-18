import { resolve, relative, extname } from 'path'
import { defineConfig } from 'vite'
import { globSync } from 'glob'
import { fileURLToPath } from 'url'

const __dirname = fileURLToPath(new RegExp('/[^/]+$').test(import.meta.url) ? new URL('./', import.meta.url) : new URL('.', import.meta.url));

// Automatically find all .html files as build entry points
const htmlFiles = globSync('**/*.html', {
  ignore: ['node_modules/**', 'dist/**']
}).reduce((entries, file) => {
  // Use relative path from root to generate entry name
  // e.g. 'zh-tw/catalog.html' -> 'zh-tw/catalog'
  const name = relative('.', file.slice(0, file.length - extname(file).length)).replace(/\\/g, '/')
  entries[name] = resolve(import.meta.dirname, file)
  return entries
}, {})

export default defineConfig({
  base: '/', // Base is root-relative for local dev and we handle prefixing in post-build for GH Pages
  server: {
    port: 5175,
  },
  build: {
    rollupOptions: {
      input: htmlFiles,
    },
  },
})
