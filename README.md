# Boot.dev Blog

This is the source code and content for the Boot.dev blog, which can be found at [https://blog.boot.dev](https://blog.boot.dev).

## Contributing

We would love for you to add your own article, or make improvements to an existing article! You can read the [contributing guide here](/CONTRIBUTING.md) for how to get started.

## License

You can read the [license here](/LICENSE). In short, you're free to copy and edit this blog. That said, all the content in this repository is owned by Boot.dev, and you're _not_ permitted to host or publish it elsewhere. We want you to be able to submit updates and even entire articles if you choose, but be aware that an accepted submission does _not_ give you any ownership over the content in this project.

## Quick start development

Make sure you have `npm` and the latest version of [hugo](https://gohugo.io/getting-started/installing/) installed on your machine.

```bash
npm install
npm run serve
```

## Check for broken links

In one terminal start the server on `localhost:1313`

```bash
npm run serve
```

Then run the check in another terminal:

```bash
go run ./scripts/linkcheck
```

It will print any issues.

## Resize images

Place original images go in the `raw/` directory.

Create a directory `static/img/X` where `X` is the max width of the new images.

```bash
npm image-min
```

This resizes all the images and places them in the new folder and deletes them from `raw/`.

The syntax to include them in a post is:

```md
![alt text here](/img/800/technology.png.webp)
```
