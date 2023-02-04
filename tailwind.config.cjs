/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
        fontFamily: {
            LibreBask: "LibreBaskerville",
            LibreBaskBold: "LibreBaskerville-Bold",
            LibreBaskItalic: "LibreBaskerville-Italic"
        }
    },
  },
  plugins: [],
};
