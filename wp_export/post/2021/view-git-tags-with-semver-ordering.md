---
title: "View Git Tags with Semver Ordering"
date: "2021-02-09"
categories: 
  - "misc"
---

If you're like me, you wish all [Git tags](https://git-scm.com/docs/git-tag) adhered to the [Semantic Versioning standard](https://semver.org/). Unfortunately, Semver is just a convention, so Git tags can basically be any string of text. By default when you use the `git tag` command, your output will be in _alphabetical_ order. Being a gopher, almost all the projects I work on are tagged according to Semver standards, which means the default output is fairly useless.

In order to print all the Git tags in a project in Semver order, simply run `git tag -l | sort -V`.

Alternatively, if you're on at least version 2 of Git, you won't even need to use the `sort` command, just run:

```
git tag -l --sort=version:refname
```

If you want the latest tags at the top of the output, use `-version` to inverse the sort:

```
git tag -l --sort=-version:refname
```

If you want your global installation of Git to default to Semver sorting, you can use the following command as of Git v2.1+:

```
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
