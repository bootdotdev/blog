# blog

The blog for Boot.dev, which can be found at [https://blog.boot.dev](https://blog.boot.dev).

## Contributing

We would love for you to add your own article, or make improvements to an existing article! You can read the [contributing guide here](/CONTRIBUTING.md) for how to get started.

## License

You can read the [license here](/LICENSE). In short, you're free to copy and edit this blog. That said, all the content in this repository is owned by Boot.dev, and you're *not* permitted to host or publish it elsewhere. We want you to be able to submit updates and even entire articles if you choose, but be aware that an accepted submission does *not* give you any ownership over the content in this project.

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
