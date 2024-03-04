/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./university/templates/*/*.{html,js}'],
    theme: {
        extend: {
            fontFamily: {
                robotoSlab: ['"Roboto Slab"', '"serif"'],
            },
            colors: {
                primary: '#E89A24',
            },
        },
    },
    plugins: [],
};
