---
title: "If You're Learning Back-end, Don't Start with Frameworks"
author: lane
date: "2023-01-16"
categories:
  - "backend"
images:
  - /img/800/pythongopherblue.png.webp
imageAlts:
  - "Midjourney prompt: gopher fighter python fantasy blue dark"
---

Look, I don't hate frameworks. I'm not as starry-eyed as some other developers, especially when it comes to _back-end_ frameworks, but I don't think there's anything wrong with using tools that make you productive. On the contrary, I'm _always_ trying to find tools that make me as productive as possible.

That said, I'm adamant that you should not _start_ with frameworks when you're [learning back-end development](https://www.boot.dev). I'm not saying you shouldn't use them at all, but I am saying that they are a poor tool for learning.

## Frameworks automate the boring stuff

Frameworks are _great_ at automating all that boring stuff like boilerplate code, authentication, and [database migrations](https://blog.boot.dev/clean-code/death-taxes-and-database-migrations/). Who wants to invent the wheel over and over again? _Not me_.

Trouble is, when you're just starting, those boring details are _exactly_ the things you need to learn. They're the building blocks of back-end applications, the foundations of what you need to know. And when you use a framework, you're missing out on all that good stuff.

Like any good developer, I use a library and call `sha256.Hash(text)` when I need to hash some data. I don't try to write my cryptography from scratch! That said, I've taken the time to learn and understand _why_ [sha256](https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/) is a good choice in a given scenario, and what security it provides me. Similarly, when you're learning back-end development, frameworks are just too high-level to be a good starting point.

## Frameworks are easy to learn, that's the whole point

The entire selling point of a framework like Django, Flask, or Rails is that they're easy to use. They take the repetitive, boring stuff and give you an opinionated way to do it. With just a few CLI commands, you can have a fully-functional web application up and running!

The problem with starting this way is that you'll have an entire codebase, with mountains of dependencies, and you'll understand how almost none of it works under the hood. When you encounter issues (and you will) you'll be spending hours trying to work backward. The problem is very similar to one of my favorite memes: _"Hours of debugging can save you minutes of reading the docs!"_

![hours of debugging](https://pbs.twimg.com/media/E2A3GwaXsAA_GwQ?format=jpg&name=small)

In the long run, it will be a lot faster to learn the basics of back-end servers. You can always learn a framework later, it's _really_ not hard at that point because you will already understand the pieces that are magically taken care of.

## I made the mistake of starting with Django

When I was getting my [CS degree](https://blog.boot.dev/jobs/is-coding-bootcamp-worth-it/), I decided I wanted to build a web app, and up until that point, I hadn't done much with the web yet. All I had done was write little Python scripts. RESTful servers, HTTP requests, SQL databases -- I had no idea what any of that was.

Anyhow, I heard Django was popular, so I decided to use it to build a website. I followed "hello world" style tutorials and in just a few days I had a working website! I understood how to change variables here and there to make the page display what I wanted, but boy howdy I had _no idea_ what was going on under the hood.

I stressed for weeks trying to make sure my site was "secure". Every blog post online kept telling me I had to set this configuration, or that setting, if I wanted to be able to run my Django server in production. I avoided interacting with the database like the plague, instead opting to use Django's ORM and admin panel to make changes to my data. I'm embarrassed to admit that at the time I didn't even understand that the database was a separate thing from the web server.

Anyhow, a year later when I [learned Go](https://www.boot.dev/courses/learn-golang) and built an API without any frameworks, _everything started to come together for me_. I finally understood all the moving parts.

Since then, I've worked with minimalistic Go apps, Django, Flask, Rails and Express servers. I'm no longer stressed when I build a server in Django because I know what tradeoffs are being made. Django and Rails are not bad tools for building web apps, they're just bad tools to start your learning process with.

## How far down the rabbit hole do I need to go?

![apple pie carl sagan](https://blog.boot.dev/img/800/applepie.png.webp)

> If you wish to make an apple pie from scratch, you must first invent the universe.
>
> -- Carl Sagan

You might be thinking, "Okay, I get it, I shouldn't start with a framework. But where should I start?"

It's a fair question. Following fallacious "slippery slope" logic, we might think something like:

- Before a framework, build a web server from scratch
- Before a web server, build the HTTP protocol from scratch
- Before HTTP, build the operating system from scratch
- etc...

That's not what I'm saying. If you want to be a professional in any industry, I think it's a good rule of thumb to go one layer down the stack from where you plan to do most of your work.

- Want to build operating systems? It will help to understand the kernel.
- Want to write an ORM? It will help to understand databases.
- Want to write Rails apps? It will help to understand web servers.

## Lastly, full-stack and back-end development are different

One last thing I want to point out is that full-stack and back-end are _not_ the same thing. I think many developers who start with [front-end](https://blog.boot.dev/backend/frontend-vs-backend-meaning/) get a bit confused about this. They think that the back-end is just the thing that serves the front-end.

That certainly _can_ be the case in smaller applications, but as a company grows, the back-end tends to become larger and more complex. Frankly, the servers that serve up the front-end might be some of the simplest parts of the stack.

While I still think it's best to write a server from scratch at least once, it's even more important if you want to be a _back-end_ engineer rather than a _full-stack_ engineer. If you're a back-end engineer, you'll be spending most of your time working on the back-end, and you'll be digging into more niche problems where a deeper understanding of server architecture will be more helpful.

I hope this helps you avoid some of the pain I experienced, and as always, best of luck! If you're interested in learning back-end development, [check out Boot.dev](https://www.boot.dev), I think it will help.

After thought-provoking feedback, I've since added a [follow-up article here](/backend/wrong-about-abstractions/).
