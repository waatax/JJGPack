/** @type {import('tailwindcss').Config} */
export default {
        content: [
                "./index.html",
                "./src/**/*.{js,ts,jsx,tsx,html}",
        ],
        theme: {
                extend: {
                        colors: {
                                primary: '#1A5C38', // Forest Green
                                secondary: '#B5813C', // Kraft Brown
                                accent: '#2E8B57', // Eco Teal
                                background: '#F5F0E8', // Warm Cream
                                surface: '#FFFFFF', // Pure White
                                'text-primary': '#1A1A1A', // Deep Charcoal
                                'text-secondary': '#666666', // Medium Gray
                                warning: '#4CAF50', // Leaf Green
                        },
                        fontFamily: {
                                serif: ['Playfair Display', 'Noto Serif TC', 'serif'],
                                sans: ['Inter', 'Noto Sans TC', 'sans-serif'],
                        }
                },
        },
        plugins: [],
}
