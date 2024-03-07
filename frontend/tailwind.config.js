/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./scripts/*.js"],
  theme: {
    extend: {
      fontFamily: {
        poppins: ["Poppins", "sans-serif"]
      },
      backgroundColor: {
        main: {
          light: '#f9f9f9',
          dark: '#5f5950'
        },
        sec: {
          sec: {
            light: '#ffcf88',
            med: '#ffb03b',
            dark: '#FF9B08'
            }
        }
      },
      colors: {
        main: {
          light: '#f7f7f7',
          dark: '#5f5950'
        },
        dark: '5f5950',
        sec: {
        light: '#ffcf88',
        med: '#ffb03b',
        dark: '#FF9B08'
        }
      },
      borderColor: {
        sec: {
          light: '#ffcf88',
          med: '#ffb03b',
          dark: '#FF9B08'
          }
      },
    }
  },
  plugins: [],
}
