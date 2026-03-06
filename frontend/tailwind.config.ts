import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        eco: {
          green: "#22c55e",
          dark: "#14532d",
          light: "#dcfce7",
        },
      },
    },
  },
  plugins: [],
};

export default config;
