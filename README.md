# blog

## Quick start development

Make sure you have `yarn` and the latest version of [hugo](https://gohugo.io/getting-started/installing/) installed on your local machine.

```bash
yarn install
yarn serve
```

## Recommended VS code plugins

* Spellchecker by Michael Vernier
* Markdown All in One by Yu Zhang
* Eslint by Microsoft

## Shortcodes

Use the following scripts to manage global shortcodes.

### Add a SHORTCODE to all posts after PARAGRAPH_NUMBER

```bash
make buildscripts
./bin/addshorts SHORTCODE PARAGRAPH_NUMBER
```

### Remove SHORTCODE from all posts

```bash
make buildscripts
./bin/rmshorts SHORTCODE
```
