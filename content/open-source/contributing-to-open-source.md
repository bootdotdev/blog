---
title: "6 Things to Avoid When Contributing to Open-Source Projects"
author: Lane Wagner
date: "2020-10-21"
categories: 
  - "open-source"
images:
  - /img/6-Things-to-Avoid-When-Contributing-to-Open-Source-Projects.jpeg
---

With [#HacktoberFest](https://hacktoberfest.digitalocean.com/) being a thing, there has been an influx of devs desperately trying to contribute to their favorite Open-Source projects. Unfortunately, many of these pull requests have been a waste of time, with the maintainers ultimately unable to use the contributions. Maintainers don't want to waste their time reviewing bad PRs, and contributors don't want to waste their time writing code that will never make it into production.

Let's take a look at some common pitfalls that developers fall prey to when working on an open-source project.

## 1\. Pull Requests Should Handle ONE Thing

Don't open a PR like this:

- Fixes bug #543
- Adds new linting rules
- Includes feature #456

Your PR should do _one thing_. Large diffs increase the cognitive load of the reviewer and make it easier to get your code into the main branch. If you have beef with multiple issues in a project then open multiple PRs.

{{< cta1 >}}

## 2\. Don't Break Consistency

This one happens the most often to me in my own projects. Well-intentioned developers open pull requests with any of the following annoyances:

- Omitting semicolons in a project that prefers them
- Using spaces in a project that has clearly been using tabs
- Introducing snake\_case in a camelCase repo

When you contribute to an existing project, use the existing styling. No one gives two hoots about your preference on the "[tabs vs spaces](https://www.youtube.com/watch?v=SsoOG6ZeyUI)" debate in the context of this pull request.

If you think styling needs to change, see points #1 and #3.

## 3\. Don't Start Work Without Approval

If you hop into a Github repo and find something you don't like, don't immediately open a pull request. Follow these steps instead:

- Is there already an issue logged? If not, make one.
- If there is an issue, reach out to the maintainers (just comment on the issue) and let them know you are working on it, and give a quick overview of how you will address it. If they have problems with that approach, they will likely let you know.
- Start work on your PR.

This will help mitigate the creation of pointless PRs that will never be accepted on the basis of a flawed premise.

## 4\. Don't Re-Open Known Problems/Solutions

Some codebases have thousands of open issues, take the [Go language](https://github.com/golang/go) project or the [nocode repository](https://github.com/kelseyhightower/nocode) as an example. No one wants to read your duplicate issue or review your duplicate pull request. Make sure there isn't an existing open _or closed_ issue for what you are trying to address.

{{< cta2 >}}

## 5\. Squash Those Commits

Not every project will require (or care) about [commit squashing](https://github.com/wprig/wprig/wiki/How-to-squash-commits). That said, there are no projects that require _not_ squashing commits. To be on the safe side just give 'em a squash.

## 6\. Be Meaningful

Rewording documentation and other frivolous changes make you look like [these assholes](https://github.com/whatwg/html/pulls?q=is%3Apr+is%3Aclosed+label%3Aspam). This particularly [atrocious example](https://github.com/whatwg/html/pull/6075) is not only scoped to pointless documentation changes but actually makes the documentation _worse_.
