---
title: "Go's Major Versioning Sucks - From a Fanboy"
author: Lane Wagner
date: "2020-09-15"
categories: 
  - "golang"
---

I'm normally a fan of the rigidity within the Go toolchain. In fact, we use Go on the [front and backend at Qvault](https://qvault.io), and we've found that it's wonderful to have standardized formatting, vetting, and testing across the entire language. The first real criticism I've had is with the way Go modules handle major versions. It's over-the-top opinionated and slows down development in a significant number of scenarios.

## Refresher on "Go Mod"

Go modules, and the associated commands `go mod` and `go get` can be thought of as Go's equivalents to NPM and Yarn. The Go toolchain provides a way to manage dependencies and lock the versions that a collection of code depends on.

One of the most common operations is to update a dependency in an existing module. For example:

```bash
# update all dependencies
go get -u ./...

# add missing and remove unused dependencies
go mod tidy

# save all dependency code in the project's "vendor" folder
go mod vendor
```

## Semantic Versioning

Go modules use git tags and semantic versioning to keep track of the versions of dependencies that are compatible with the module in question. Semantic versioning is a way to format version numbers and it looks like this: `v{MAJOR}.{MINOR}.{PATCH}`. For example, `v1.2.3`.

Each number is to be incremented according to the following standards:

```
MAJOR version when you make incompatible API changes,
MINOR version when you add functionality in a backwards compatible manner, and
PATCH version when you make backwards compatible bug fixes.
```

## Package-Side Problems

Go has decided that all versions beyond `v0` and `v1` are required to use the major version in the module path. There are two ways to accomplish this.

**The first and recommended way** is laid out in an example on the [Go Blog](https://blog.golang.org/v2-go-modules#TOC_4.):

> To start development on `v2` of `github.com/googleapis/gax-go`, we'll create a new `v2/` directory and copy our package into it.

In other words, for every major version, we are encouraged to maintain a new copy of the entire codebase. This is also the only way to do it if you want pre-modules users to be able to use your package.

**The second way** is to just change the name of your module in `go.mod`. Fore example, `module github.com/lane-c-wagner/go-tinydate` would become `module github.com/lane-c-wagner/go-tinydate/v2`. Besides this not working for older versions of Go, I also find it problematic because it breaks (in my mind) one of the most useful things about module names - they reflect the file path.

## Package-Side Solutions

Allow package maintainers to specify the major version simply by updating git tags, no module name changes required. There is no need for two sources of truth.

We can enforce safe updating by adding warnings or prompts to the `go get` CLI. We don't have to add unnecessary time-consuming policies.

## Client-Side Problems

When new versions of dependencies are released we have a simple command to get the newest stuff: `go get -u`. The problem is that this command has no way to automatically update to a new major version. It will only download new minor changes and patches. There isn't even a console message to inform you that a new major version exists!

That said, the reason for not auto-updating is clear, and to be fair, well-founded:

> If an old package and a new package have the same import path, the new package must be backwards compatible with the old package.
> 
> [Import compatibility rule](https://research.swtch.com/vgo-import)

In other words, we should only increment major versions when making breaking changes, and if breaking changes are made they can't have the same import path. While this makes sense, I think a simple console warning would have been a better solution than forcing a cumbersome updating strategy on the community.

**Another problem** on the client-side is that we don't only need to update `go.mod`, but we actually need to `grep` through our codebase and change each import statement to point to the new major version:

> Users who wanted to use `v2` had to change their package imports and module requirements to `github.com/googleapis/gax-go/v2`.

Instead of a few simple CLI commands to get the latest dependencies, we're making changes to the code itself.

### A Caveat - Diamond Imports

Using different paths for different major versions makes more sense in situations where we may require two different versions of the same package, you know, [diamond imports](https://research.swtch.com/vgo-import#dependency_story) and all that. This is the exception, not the rule, and it seems strange to tap dance around a problem that doesn't exist in most codebases.

## Client-Side Solution

`go get -u` should have an additional command line flag to update major versions, and should default to showing a warning that there is a newer major version you don't have yet.

_Default_ import paths should not change between major versions. If a module requires various versions, those _extra_ versions could be flagged by having a different path.

## Why This Sucks For Me

It is often the case that I want to build a package that has domain-specific logic and will only be used only in services at the small company I work for. For example, we have a repo that holds the `struct{}` definitions for common entities used across our system.

Occasionally we need to make backward-incompatible changes to those struct definitions. If it were an open-source library we wouldn't make changes so often, but because it's internal and we are aware of all the dependencies, we change the names of exported fields _regularly_. We aren't changing names because we chose bad ones to begin with, we are usually changing names because requirements from the business change rapidly in a startup.

This means major version changes are a fairly regular occurrence. Some say that we should just stay on `v0`, and that's a reasonable solution. The problem is these ARE production packages that are being used by a wide number of services. We WANT to Semver.

Go makes updating major versions so cumbersome that in the majority of cases, we have opted to just increment minor versions when we should increment major versions. We want to follow the proper versioning scheme, we just don't want to add the unnecessary steps to our dev process.

## Hey - I Get It

I understand why these decisions were made - and I even think in a lot of cases they were great decisions. For any open-source or public facing module this makes great sense. The Go toolchain is enforcing strict rules that encourage good API design.

In their effort to make public APIs great, they made it unnecessarily hard to have good "local" package design.

There is an [open issue on Github](https://github.com/golang/go/issues/40323) that would make new major versions more discoverable from the CLI. Take a look at that if you are interested.

Go still has the best toolchain and ecosystem. NPM and PIP can suck it.

If you disagree, @ me on Twitter.
