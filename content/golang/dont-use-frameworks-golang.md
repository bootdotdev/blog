---
title: "The Firepower of a Framework-Free Filosophy"
author: Lane Wagner
date: "2021-06-01"
categories: 
  - "golang"
images:
  - /img/800/hand-signal.webp
draft: true
---

I'm here to convince you of two things:

* To stop looking for a framework for your next Go project
* To stop thinking about building one

## What is a framework? (as defined by yours truly)

Definitions matter when we talk about hot-button topics. Here's how I define a "framework":

> A framework is piece of third-party software that provides a comprehensive set of tools for building entire applications. Your code is used *within a framework*.

Contrast this with how I define a *library*:

> A library is a piece of third-party software that provides a set of tools for building a specific *part* of an application. A library is used *within your code*.

### Examples:

* Ruby on Rails: framework
* React.js: framework (claims to be a library)
* Django: framework

* kyleconroy/sqlc: library
* gorilla/mux: library
* Express.js: library (claims to be a framework)

{{< cta1 >}}

## Why do we use frameworks?

We use frameworks for two primary reasons:

1. To reduce boilerplate
2. To integrate a large set of tools into a single interface

## What's the cost?

Getting started with a framework is easy, sometimes as easy as typing `rails new`. Frankly, when you're starting a new project, all-encompassing frameworks provide an amazing developer experience.

The pain comes later. A framework provides a set of tools for practically everything at the cost of flexibility.

Frameworks make it *much harder* to modularly update your project. Want to use a different authentication library, database driver, or templating engine? Get to hacking.

{{< cta2 >}}

## "It's a Unix system! I know this!"

From the Unix philosophy:

> Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new "features".

Here's some speculation on my part: It's likely that popular web frameworks in other languages arose from the lack of built-in web tools like routing and request handling. Once a framework was written to provide those necessities, feature creep set in. Why not tack on a templating engine and an ORM?

If instead, we build separate libraries that do one thing and do it well we can get 80% of the benefits with 20% of the cost.

I want my applications to *compose libraries* rather than *configure frameworks*.

## We can have the best of both worlds

In Go, the `net/http` package provides a powerful set of tools for building web applications, and luckily many gophers have fostered a culture of avoiding large external dependencies.

Come listen to the talk to find out how we can compose libraries in Go while still avoiding tedious boilerplate!
