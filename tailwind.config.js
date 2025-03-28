module.exports = {
  content: ["./layouts/**/*.{html,js}"],
  theme: {
    extend: {},
    boxShadow: {
      sm: "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
      DEFAULT:
        "0 1px 3px 0 rgba(0, 0, 0, 0.3), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
      md: "0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
      lg: "0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
      xl: "0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
      "2xl": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
      "3xl": "0 35px 60px -15px rgba(0, 0, 0, 0.3)",
      inner: "inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)",
      none: "none",
    },
    colors: ({ colors }) => ({
      black: colors.black,
      white: colors.white,
      gray: {
        50: "hsl(235, 10%, 97%)",
        100: "hsl(235, 9%, 94%)",
        150: "hsl(235, 8%, 90%)",
        200: "hsl(235, 7%, 86%)",
        250: "hsl(235, 6%, 81%)",
        300: "hsl(235, 5%, 76%)",
        350: "hsl(235, 4%, 69%)",
        400: "hsl(235, 3%, 62%)",
        450: "hsl(235, 2%, 56%)",
        500: "hsl(235, 1%, 50%)",
        550: "hsl(235, 2%, 45%)",
        600: "hsl(234, 3%, 39%)",
        650: "hsl(234, 4%, 32%)",
        700: "hsl(235, 5%, 24%)",
        750: "hsl(235, 6%, 18%)",
        800: "hsl(236, 7%, 13%)",
        850: "hsl(236, 8%, 10%)",
        900: "hsl(240, 9%, 6%)",
        950: "hsl(240, 10%, 3%)",
      },
      blue: {
        50: "hsl(235, 100%, 93%)",
        100: "hsl(235, 99%, 93%)",
        150: "hsl(235, 97%, 93%)",
        200: "hsl(235, 95%, 89%)",
        250: "hsl(235, 93%, 85%)",
        300: "hsl(235, 91%, 81%)",
        350: "hsl(235, 89%, 77%)",
        400: "hsl(235, 88%, 73%)",
        450: "hsl(235, 87%, 69%)",
        500: "hsl(235, 86%, 65%)",
        550: "hsl(235, 87%, 61%)",
        600: "hsl(235, 89%, 57%)",
        650: "hsl(235, 91%, 53%)",
        700: "hsl(235, 93%, 49%)",
        750: "hsl(235, 95%, 45%)",
        800: "hsl(235, 97%, 41%)",
        850: "hsl(235, 99%, 37%)",
        900: "hsl(235, 100%, 33%)",
      },
      green: {
        150: "#ECFDF2",
        200: "#D9FCE4",
        250: "#C7FAD7",
        300: "#B4F8CA",
        350: "#A1F7BC",
        400: "#8DF6AF",
        450: "#7AF5A1",
        500: "#57F287",
        550: "#54F286",
        600: "#41F179",
        650: "#2EEF6B",
        700: "#1BEE5E",
        750: "#11E454",
        800: "#10D14D",
        850: "#0EBE46",
        900: "#0DAB3F",
      },
      pink: {
        100: "#FBDAEB",
        150: "#F9C8E1",
        200: "#F7B6D8",
        250: "#F391C5",
        300: "#F391C5",
        350: "#F17EBB",
        400: "#EF6BB2",
        450: "#EE59A8",
        500: "#EB459E",
        550: "#EA3495",
        600: "#E8218B",
        650: "#DE1781",
        700: "#CB1576",
        750: "#B9136C",
        800: "#A61161",
        850: "#941056",
        900: "#810E4B",
      },
      yellow: {
        50: "#fffaeb",
        100: "#fef4d1",
        150: "#fde9b0",
        200: "#fddf8f",
        250: "#fcd570",
        300: "#f6bd45",
        350: "#eeb23f",
        400: "#e5ae3c",
        450: "#dca336",
        500: "#efbb03",
        550: "#d69e02",
        600: "#c18500",
        650: "#a96f06",
        700: "#905a0a",
        750: "#7b4d0c",
        800: "#64400e",
        850: "#4e3310",
        900: "#3b2710",
        950: "#2a1c0c",
      },
      red: {
        100: "#FCD9DA",
        150: "#FAC7C8",
        200: "#F8B4B5",
        250: "#F7A1A3",
        300: "#F58F91",
        350: "#F37C7E",
        400: "#F16A6C",
        450: "#EF575A",
        500: "#ED4245",
        550: "#EC3235",
        600: "#EA1F22",
        650: "#E01518",
        700: "#CD1316",
        750: "#BB1114",
        800: "#A81012",
        850: "#950E10",
        900: "#830C0E",
      },
    }),
  },
  plugins: [
    require("@tailwindcss/forms")({
      strategy: "class",
    }),
  ],
};
