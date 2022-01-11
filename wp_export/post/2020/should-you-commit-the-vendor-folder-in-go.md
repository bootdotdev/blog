---
title: "Should You Commit the Vendor Folder in Go?"
date: "2020-11-16"
categories: 
  - "golang"
---

The answer to the age-old question of, "_should I commit the vendor dependencies in my Go project to source control?_" is "_almost always_". As an FYI, we here at [Qvault](https://qvault.io) use Go for all of our backend work, and we always commit our vendor folders. Let's take a look at the reasoning behind my claim that committing dependencies is ideal.

## What Is the Vendor Folder?

If you are coming from Node.js land, Golang's vendor folder is basically the same as Node's `node_modules`. It is a folder found at the root of a module that stores a copy of all the code the module depends on. The code is used to compile the final executable when the `go build` command is run. As you can imagine, at the heart of the "_should we commit vendor?_" discussion is the problem of repo size.

`node_modules` is infamous for its large size.

![node_modules is the heaviest object in the universe](images/tfugj4n3l6ez-300x216.png)

As a result, conventional wisdom in the Node community is to add `node_modules` to the `.gitignore` file in order to save space. After all, a quick `npm install` (or in Go's case `go get`) will grab everything right?

Yeah. Yeah it will. Most of the time.

## Reproducible Builds

`npm Err! 404 'left-pad' is not in the npm registry`

The error code above famously [plagued the developer world](https://qz.com/646467/how-one-programmer-broke-the-internet-by-deleting-a-tiny-piece-of-code/) because developers were too lazy, or perhaps too sloppy, to write a few simple lines of code. Had a copy of the dependency been committed to all the projects that depended on `leftpad` then nothing would have been broken when the package was removed from `NPM`.

```
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

Luckily, up to this point, the [Go community has been much more rigorous](https://research.swtch.com/deps) about upholding the virtues of keeping dependencies to a minimum. When dependencies are kept to a minimum, it's easy to commit the entire `vendor` folder without incurring the huge data cost that the average `node_modules` folder would demand.

## Final Verdict

Just like the flow chart at the beginning of the post outlines, if you don't have an insane amount of dependencies, just commit those dependencies! You save yourself the headache of worrying about their source repos being deleted or not having network access when you build your project. On the other hand, if you do have a metric shitload of external code, maybe you should work on cutting the fat.
