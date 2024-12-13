---
title: "View Git Tags with Semver Ordering"
author: lane
date: "2021-02-09"
categories:
  - "misc"
images:
  - /img/800/semver-info.webp
---

If you're like me, you wish all [Git tags](https://git-scm.com/docs/git-tag) adhered to the [Semantic Versioning standard](https://semver.org/). Unfortunately, Semver is just a convention, so Git tags can basically be any string of text. By default when you use the `git tag` command, your output will be in _alphabetical_ order. Being a gopher, almost all the projects I work on are tagged according to Semver standards, which means the default output is fairly useless.

To print all the Git tags in a project in Semver order, simply run `git tag -l | sort -V`.

Alternatively, if you're on at least version 2 of Git, you won't even need to use the `sort` command, just run:

```bash
git tag -l --sort=version:refname
```

If you want the latest tags at the top of the output, use `-version` to inverse the sort:

```bash
git tag -l --sort=-version:refname
```

If you want your global installation of Git to default to Semver sorting, you can use the following command as of Git v2.1+:

```bash
git config --global tag.sort version:refname
```

## Examples of Git standard output

### Default alphabetical sorting

```
v0.0.0
v0.0.1
v0.0.12
v0.0.2
v0.1.0
v0.10.0
v1.0.0
v1.1.1
v1.11.0
v1.12.0
v10.0.0
v2.0.0
```

### Semver sorting

```
v0.0.0
v0.0.1
v0.0.2
v0.0.12
v0.1.0
v0.10.0
v1.0.0
v1.1.1
v1.11.0
v1.12.0
v2.0.0
v10.0.0
```

If all this weird tag stuff is going over your head, you might want to [check out ThePrimeagen's full Git course here](https://www.boot.dev/courses/learn-git).
