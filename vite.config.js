import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
        build: {
                rollupOptions: {
                        input: {
                                main: resolve(__dirname, 'index.html'),
                                about: resolve(__dirname, 'about.html'),
                                products: resolve(__dirname, 'products.html'),
                                contact: resolve(__dirname, 'contact.html'),
                                news: resolve(__dirname, 'news.html'),
                                'zh-tw-index': resolve(__dirname, 'zh-tw/index.html'),
                                'zh-tw-about': resolve(__dirname, 'zh-tw/about.html'),
                                'zh-tw-products': resolve(__dirname, 'zh-tw/products.html'),
                                'zh-tw-contact': resolve(__dirname, 'zh-tw/contact.html'),
                                'zh-tw-news': resolve(__dirname, 'zh-tw/news.html'),
                                'zh-tw-p-greaseproof': resolve(__dirname, 'zh-tw/products/greaseproof.html'),
                                'zh-tw-p-kraft': resolve(__dirname, 'zh-tw/products/kraft.html'),
                                'zh-tw-p-flathandle': resolve(__dirname, 'zh-tw/products/flathandle.html'),
                                'zh-tw-p-white': resolve(__dirname, 'zh-tw/products/white.html'),
                                'zh-tw-p-foil': resolve(__dirname, 'zh-tw/products/foil.html'),
                                'zh-tw-p-fruit': resolve(__dirname, 'zh-tw/products/fruit.html'),
                                'zh-tw-p-pe': resolve(__dirname, 'zh-tw/products/pe.html'),
                                'zh-tw-p-straw': resolve(__dirname, 'zh-tw/products/straw.html'),
                                'zh-tw-p-others': resolve(__dirname, 'zh-tw/products/others.html'),
                        },
                },
        },
})
