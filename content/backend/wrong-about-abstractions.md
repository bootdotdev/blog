---
title: "I Was Wrong, but Still Don't Learn Frameworks First"
author: Lane Wagner
date: "2023-01-17"
categories: 
  - "backend"
images:
  - /img/800/gophersnakefight.png.webp
imageAlts:
  - "Midjourney prompt: snake fights mongoose 4k midjourney fantasy cinematic"
---

I wrote an article about [not starting with frameworks](/backend/dont-start-with-frameworks/) that got some attention from [/r/programming](https://www.reddit.com/r/programming/) on [Reddit yesterday](https://www.reddit.com/r/programming/comments/10dhhc4/if_youre_learning_backend_dont_start_with/). While a good number of people must have enjoyed the article (some people upvoted? idk) I was rightfully blasted with *a lot* of criticism. Here are some of my favorite comments:

> If you're learning plumbing, don't start with sink taps. Start with mining ore to make pipes.

> Is it bad advice Monday already?

The sad thing is that I agree with a lot of the commenters, which means I did a terrible job of communicating my point. I'm going to try to do better in this post. Not only do I want to clarify my thoughts, but I do think I was outright wrong about what needs to be *emphasized* to new developers.

## Correction: Top-Down "Why" then Bottom-Up "How"

In my last article, I make a case for learning "bottom-up". Paraphrasing myself, I said:

> I think it's a good rule of thumb to go one layer down the stack from where you plan to do most of your work. Learn how that works, and move up the abstraction layers from there.

This skips a *crucial* step that many Redditors pointed out. When I teach a new concept on [Boot.dev](https://boot.dev) I start by zooming out and talking about the "why". For example, let's say you're learning about storing user data on a back-end server.

### 1. Start at a high-level

* Why do we store data on the server?
* When can we get away with storing data on the client?
* What's the difference between variables in my program and persistent storage?

In this example, I'd want the student to take a look at a simple architectural diagram: just simple boxes and lines. Here's where data lives, here's where we send it, etc.

### 2. Build the simplest version, focused on the core of what you're learning

Again, I did a poor job explaining my thoughts here. It's not about building a production web server from *scratch*, it's about building a *simple version* of the thing you're trying to learn without too many abstractions. If your goal is to learn about storing user data, your first application should just save a user's name and email address to a text or JSON file on disk.

### 3. Add abstraction layers as appropriate

Once you've got a minimal HTTP server that saves information to the filesystem, install SQLite or Postgres and learn about the benefits database software provides, namely speed and reliability. Once you've played with that, install an ORM and see how easily the `.save()` method can be used to store a record in a database.

Contrast this approach with my own experience. Without understanding the difference between a `GET` and a `POST` request I spun up a Django server and copy/pasted code from Stack Overflow. Most of the time I was terrified that a small change that a friendly internet stranger suggested could break the whole thing.

## Note: It's not about "learning the right way"

If you learn to code you've won. There is no "wrong way" to learn. If you didn't take the approach I'm suggesting (I didn't) that doesn't mean you're not a real engineerᵗᵐ. If it worked for you, that's fantastic, I've just found that this approach speeds up the process for *a lot* of people.

## Some people need more practical knowledge, some need more theory

One of the [reasons I decided to start Boot.dev](https://blog.boot.dev/about/) was that I saw two prevailing approaches for learning back-end development:

* A 4-year CS degree packed with theory
* An n-month bootcamp rushing through new technologies and frameworks

**As a general rule, bootcamps are too fast and degrees are too slow.** Bootcamps skip theory almost completely while degrees take years to get you to the point where you can build something useful. I think there's a better middle-ground approach: A curriculum that teaches all the career-relevant theory while constantly putting it into practice by building real-world projects.

## Different people need different advice

I talk to a lot of students. Some have a more academic background, and after getting a feel for their situation I often try to push them into building more projects and worrying less about inverting binary trees.

Other students I've worked with are bootcamp graduates or have been self-teaching online. With them, I'm often pointing them to resources that explain the fundamentals of the stuff they're still fuzzy on. Things like my hands-on [HTTP](https://boot.dev/learn/learn-http), [Algorithms](https://boot.dev/learn/learn-algorithms), or [SQL](https://boot.dev/learn/learn-sql) courses.

At the end of the day, it just depends. If you're actively learning to code I hope this helps you figure out what kinds of things you should study *next* to keep moving forward. Good luck!
