/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./university/templates/**/*.{html,js}'],
    theme: {
        extend: {
            fontFamily: {
                robotoSlab: ['"Roboto Slab"', '"serif"'],
            },
            colors: {
                primary: '#E89A24',
            },
            keyframes: {
                heroTextDown: {
                    '0%': { 'margin-bottom': '180px', opacity: '0.4' },
                    '100%': { 'margin-bottom': '52px', opacity: '1' },
                },
            },
            animation: {
                'hero-txt-dwn': 'heroTextDown 2s ease-in-out',
            },
        },
    },
    plugins: [],
};
