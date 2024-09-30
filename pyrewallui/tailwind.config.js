/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      width: {
        100: '25rem',
        144: '36rem',
        152: '38rem',
        200: '50rem',
      }
    },
  },
  plugins: [],
}

