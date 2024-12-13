# Contributing

Want to publish or update an article on the Boot.dev blog? You can!

## Editing an article

Editing is really easy - just open a pull request that modifies the articles markdown file. All of the content can be found in the [/content](/content) directory.

## Publishing a new article

### Why should you publish on Boot.dev's blog?

By writing and publishing your ideas publicly, you can:

- Impress future employers
- Help you solidify what you've recently learned
- Help others find answers that took you a long time to research
- Gain traffic and domain authority for your own blogs and projects
- Get helpful feedback on your writing skills from our editorial team

### Style guide and quality standards

We are _very_ picky about the quality of articles we publish. Don't be discouraged if your submissions get rejected! Feel free to publish the rejected work on your own blog, and come back and submit to Boot.dev again with new content in the future. Here are some guidelines that will help you as you craft stories for us to accept:

- The article _must_ be related to programming, ideally back-end development.
- No "blog-a-day" or "stream of consciousness" posts.
- Cite **all** sources.
- Bring data as needed.
- Bring quotes as needed.
- Bring original data visualizations as needed.
- Write at least 500 words, preferably 1000+.
- Avoid clickbait titles.
- Do not hot-link images, add images to the `static/img/{size}` directory.
- Use a descriptive, evergreen URL path (filename) for your post.
- Use a grammar plugin like Grammarly to avoid typos.
- Structure text with bullet points, lists, etc. Avoid walls of paragraph text.
- Use code blocks. We support syntax highlighting for popular programming languages.
- Nest your headings properly. For example, you shouldn't have an `h3` within an `h1`.
- You may include _tasteful_ links back to your own site and projects. It is perfectly fine to have a one-sentence call-to-action for your product at the end of your story.
- No affiliate links.
- The Boot.dev version of your article _must_ be the canonical version. If you're unsure what this means, do not cross post your content on other sites. You're only allowed to cross post to other sites if you set the canonical URL on those sites to point back to the Boot.dev post.
- Proof read your article, then proof read it again.

### How to submit

1. Fork this repository into your own GitHub account
2. Make changes to your version of the repo
3. Submit a pull request from your version to the `main` branch on this repo
4. Wait for approval. All feedback will be given directly in the pull request.

### Using Hugo

We use [Hugo](https://gohugo.io/) as our static site generator. All articles are written in Markdown.

To contribute an article, all you need to do is:

- Add your Markdown file
- Add any images that will be used within your article (we'll handle to cover image)

### Add your Markdown file

All guest submissions belong in the `content/stories` directory. You can look at any of the existing articles in there as an example of how to format your markdown file.

Make sure to add your title, author name, date, and categories to the [frontmatter](https://gohugo.io/content-management/front-matter/).

Be sure to add `draft: true` to the frontmatter. This will prevent your article from being published until we have a chance to add an image and edit it.

### Adding images

Do _not_ worry about a cover image - we will add one for you.

All images go in the `static/img/{size}` directory, where `size` is the width. Use `webp` images, and make sure they're properly sized. You can use our [image resizer script](https://github.com/bootdotdev/blog#resize-images) if you're comfortable using [yarn](https://yarnpkg.com/).

Link to the image using a relative link. The root is the `img` directory, e.g. `![alt text here](/img/800/my-image.webp)`.

### Wait for approval

We'll usually get back to you quickly, certainly within a few days. We may leave comments on your pull request and ask for changes. If the article is "too far off" in terms of quality, we'll simply give you a rejection message and close the pull request. If that happens, feel free to publish your work elsewhere, and come back to us with different content in the future.

### Getting approved

Once approved, we'll merge your pull request! As soon as it's merged, our CI/CD system will rebuild the site and your story will be live. That usually only takes a couple of minutes. If your article is in a file called `my-story.md`, your story will be published at `https://blog.boot.dev/stories/my-story`.

## License

Boot.dev retains the rights to all content submitted to and published via this public repository. You _may not_ host this site elsewhere. That said, you may ask us to remove an article you have previously authored for us and we will do so as quickly as we reasonably can. If you do ask us to remove content, you likely will be unable to contribute again in the future, we don't want to be dealing with take-downs and dead URLs often.
