---
title: "I Don't Framework, and You Can't Too"
author: Lane Wagner
date: "2020-04-02"
categories: 
  - "golang"
  - "open-source"
images:
  - /img/800/everyday-myths-time.jpeg
draft: true
---

There is only one question that ignites my inner range more than "How do I get a developer job in 3 months?"? That question is:

> What framework should I use?

It's not that I think frameworks are evil, scary, or even bad. I just hate the *assumption* that to build an online thing, you *must* start with a framework.

## What do I mean by "framework"?

The JavaScript ecosystem has had its way with the definition of the term "web framework". The JS community seems to excel at keeping us from having nice things.

I like to define the terms "library" and "framework" as follows:

* **Library**: Code that you import into your project.
* **Framework**: A structure that you import your code into.

A framework provides nearly as much project lock-in as a programming language. If I choose to build my application in Ruby on Rails, it's impossible to move to Python Django without a full rewrite.

A library is hot-swappable. If I use a library for database access, and a new one comes out that seems to do a better job, only a small part of my application needs to be updated.

**Hey Next.js devs, React is a framework.** Neither Dan Abramov nor God himself can convince me that React is just a library. I understand that it can kinda be used as one, but no one does that.

And while we're at it, Express.js isn't a framework. It's just a routing library. *(yes I know it says framework on the homepage, but see my preview comments about the JS ecosystem)*

## It's a matter of defaults

It's story time. I was working at a company 5 years ago where we were maintaining an ETL pipeline that processed anywhere from 100 to 1000 messages per second. There were a bunch of microservices involved that did a bunch of different things. For example:

* Translating messages from one language to another
* Looking for keywords in the messages and sorting them into categories
* Sending alerts based on which messages were sorted into which categories

One day I was tasked with figuring out why one of our services was choking at a mere 30 messages per second. This service was responsible for taking messages from a queue and placing them into a different Postgres database server depending on which customer cares about the message. In theory, it was literally this simple:

1. Message comes in
2. If the  `customer_id` on the message is in the map of `customer_id` -> `database_url`, then insert the message into the database at `database_url`

I hopped into the project, and was immediately dismayed to learn it was a Ruby project. But not *just* a Ruby project, it was a Ruby on Rails project. 
