---
title: "Put that Framework Down Before Someone Gets Hurt"
author: Lane Wagner
date: "2023-11-06"
categories: 
  - "webdev"
  - "golang"
images:
  - /img/800/frameworkhouse.png.webp
---

There is only one question that ignites my inner rage more than "How do I get a developer job in 3 months?"? That question is:

> What [web framework](/backend/dont-start-with-frameworks/) should I use?

It's not that I think frameworks are evil, scary, or even bad. I'm just bothered by the *assumption* that to build an online thing, you *must* start with a framework.

## What do I mean by "framework"?

The JavaScript ecosystem has had its way with the definition of the term "web framework". The JS community seems to excel at keeping us from having nice things.

I like to define the terms "library" and "framework" as follows:

* **Library**: Code that you import into your project.
* **Framework**: A structure that you import your code into.

A framework provides nearly as much project lock-in as a programming language. If I choose to build my application in Next.js, it's impossible to move to SvelteKit without a rewrite.

A library is hot-swappable. If I use a library for database operations, and a new one comes out that seems to do a better job, only a small part of my application needs to be updated.

**Hey Next.js devs, React is a framework.** Neither Dan Abramov nor God himself can convince me that React is just a library. I understand that it can kinda be used as one, but no one does that.

And while we're at it, Express.js isn't a framework. It's just a routing library. *(yes I know it says framework on the homepage, but see my previous comments about the JS ecosystem)*

## Put that hammer down

Story time. I was working at a company about 5 years ago where we were maintaining an ETL pipeline that processed anywhere from 100 to 1000 messages per second. There were some micro-services involved that did a bunch of different things. For example:

* Translating messages from one language to another
* Sorting the messages into categories based on keywords in the content
* Sending alerts based on the aforementioned categories

One day I was tasked with figuring out why one of our services was choking at a mere 30 messages per second. This service was responsible for taking messages from a queue and placing them into different Postgres databases depending on which customer cared about the message. In theory, it was literally this simple:

1. Message comes in
2. If the  `customer_id` on the message is in the map of `customer_id` -> `database_url`, then insert the message into the database at `database_url`

I hopped into the project and was immediately dismayed to learn it was a Ruby project. But not *just* a Ruby project, it was a Ruby on *Rails* project.

![Ruby on Rails Kalm/Panik](/img/800/kalmpanicrails.png.webp)

Look, I have no problem with Ruby on Rails. There are plenty of examples of companies that have made millions or even billions of dollars on the back of Rails projects.

But this isn't a monolithic web application. This is a *tiny* service that's supposed to quickly dump messages into a Postgres database. Why do I need an HTTP router? Why do I need an auth library? Why do I need all the other junk?

I need two things:

* A way to concurrently pull messages from a Rabbit queue
* A way to insert messages into a database asynchronously

Go and JavaScript both have *super* easy and lightweight ways to accomplish this. I just need a few lines of code, and not much by way of dependencies. After a couple of hours poking through this Rails monstrosity (that for some reason also used Redis to track progress) I just wrote a single worker in Go, which took less than an hour, deployed the new service, tested it in production, and archived the Ruby project.

## But could it have worked in Rails?

Yes. I'm sure that I could have just refactored that Rails project, found the hot paths, and optimized the performance bottlenecks. I mean, it's unlikely that it was ever going to be as fast or as lightweight as a Go service, but the project was I/O bound so it could have been fine.

The point is that sometimes as software engineers we find a hammer that we really love. It's such a fun hammer! It's so ergonomic! So *clean*! And we're so good at wielding it! So, it's natural that we go around swinging it at every goddamn nail we see.

## It's a question of defaults

At Boot.dev we use Nuxt.js for our front-end UI. It's a great framework. But when I write a Discord Bot you won't catch me running `nuxi init`.

I'm not just saying:

> "Use the right tool for the job"

Instead, I'm saying:

> "Use the simplest tool for the job"

It's easy to add complexity as you need it to accomplish your goals. It's much harder to remove it.
