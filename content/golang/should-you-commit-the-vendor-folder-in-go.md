---
title: "Should You Commit the Vendor Folder in Go?"
author: Lane Wagner
date: "2020-11-16"
lastmod: "2022-04-19"
categories: 
  - "golang"
images:
  - /img/800/Should-You-Commit-Your-Vendor-Folder_.webp
---

If you're asking "should I commit the vendor folder in my Go project to Git?", the answers is "almost always". Let's talk about why commiting is generally better than not.

## What is the vendor folder anyways?

If you are coming from Node.js land, Golang's vendor directory is basically the same as Node's `node_modules`. It is a directory found at the root of a Go module that stores a copy of all the code the module depends on. The vendored code is used to compile the final executable when the `go build` command is run. As you can imagine, at the heart of the "should we commit vendor?" discussion is the problem of repo size.

`node_modules` is infamous for its large size.

![node_modules is the heaviest object in the universe](/img/800/tfugj4n3l6ez-300x216.png)

As a result, conventional wisdom in the Node community is to add `node_modules` to the `.gitignore` file in order to save space. After all, a quick `npm install` (or in Go's case `go get`) will pull down all the dependencies everything right?

Yeah. Yeah it will. Most of the time...

> left-pad has entered the chat

`npm Err! 404 'left-pad' is not in the npm registry`

The error code above famously [plagued the developer world](https://qz.com/646467/how-one-programmer-broke-the-internet-by-deleting-a-tiny-piece-of-code/) because developers were too lazy, or perhaps too sloppy, to write a few simple lines of code. Had a copy of the dependency been committed to all the projects that depended on `leftpad`, nothing would have been broken when the package was removed from the central `NPM` servers.

```js
// the entire left-pad library
module.exports = leftpad;
function leftpad (str, len, ch) {
  str = String(str);
  var i = -1;
  if (!ch && ch !== 0) ch = ' ';
  len = len - str.length;
  while (++i < len) {
    str = ch + str;
  }
  return str;
}
```

## Why should Go's vendor folder be any different than node_modules?

Luckily, up to this point, the [Go community has been much more rigorous](https://research.swtch.com/deps) about using few dependencies. When dependencies are kept to a minimum, it's easy to commit the entire `vendor` folder without incurring the huge data cost that the average `node_modules` folder would demand.

That said, once dependencies get out of control, the only option is to stop commiting the folder to source control. If you're working on a sufficiently large project, it might make sense to you and your team to add `vendor` to your `.gitignore`. You'll just miss out on some amazing benefits of having all the code required to build your app stored in your source control, including:

1. Reproducible builds. You never need to worry about missing source code.
2. Simple CI/CD. You're CI/CD pipelines don't need access to remote repos, or permissions to remote *private* repos to build and test your code.
3. Developer friendliness. There isn't a laundry list of setup instructions you'll commonly find with Node.js projects. No `npm install` required.

## Final verdict

Just like the flow chart at the beginning of the post outlines, if you don't have an insane amount of dependencies, just commit those dependencies! Reap the benefits as long as you can. On the other hand, if you do have a metric shitload of external code, maybe you should work on cutting the fat. When dieting isn't an option due to the size of your codebase, it might be time to remove `vendor` from your source control.
