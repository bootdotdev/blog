# blog

The blog for Boot.dev, which can be found at [https://blog.boot.dev](https://blog.boot.dev).

## A note on the license

You can read the [license here](/LICENSE). In short, we made this repo public to give students transparent visibility into our code for educational purposes. We do not allow you to distribute this code or content for your own purposes or for use in your own projects, and we retain the copyright to the code regardless of any contributions made.

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

## Check for broken links

In one terminal start the server on `localhost:1313`

```bash
yarn serve
```

Then run the check in another terminal:

```bash
make buildscripts && ./bin/linkcheck
```

It will print any issues.

## Shortcodes

Use the following scripts to manage global shortcodes.

### Build the scripts

```bash
make buildscripts
```

### Add a SHORTCODE to all posts at the end of SECTION_NUMBER

```bash
./bin/addshorts SHORTCODE SECTION_NUMBER
```

### Remove SHORTCODE from all posts

```bash
./bin/rmshorts SHORTCODE
```

### Reset current ctas

```bash
./bin/rmshorts cta1
./bin/rmshorts cta2
./bin/rmshorts cta3

./bin/addshorts cta1 2
./bin/addshorts cta2 4
./bin/addshorts cta3 8
```

## Resize images

Place original images go in the `raw/` directory.

Create a directory `static/img/X` where `X` is the max width of the new images.

```bash
yarn image-min
```

This resizes all the images and places them in the new folder. 

Delete the raw images.

## Docx to markdown

Add `.docx` file to `docx/` directory.

`./scripts/docxmd.sh path_to_docx`
