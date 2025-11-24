import js from "@eslint/js";
import globals from "globals";
import markdown from "@eslint/markdown";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: { globals: { ...globals.browser, ...globals.node } },
  },
  {
    files: ["**/*.md"],
    plugins: { markdown },
    language: "markdown/gfm",
    extends: ["markdown/recommended"],
    rules: {
      "markdown/fenced-code-language": "off",
      "markdown/heading-increment": "warn",
      "markdown/no-missing-atx-heading-space": "warn",
      "markdown/no-missing-label-refs": "warn",
      "markdown/no-space-in-emphasis": "warn",
      "markdown/require-alt-text": "off",
    },
  },
]);
