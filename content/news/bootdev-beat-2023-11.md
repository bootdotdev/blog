---
title: "The Boot.dev Beat. November 2023"
author: Lane Wagner
date: "2023-10-30"
categories:
  - "news"
images:
  - /img/800/novemberdrums.png.webp
imageAlts:
  - "Boot.dev Beat Drum"
dofollows:
  - "https://salt.security"
  - "https://www.se-radio.net"
  - "https://realpython.com"
---

Hope you had a fantastic Halloween. I spent last weekend in Seattle with Allan and Hunter (the other two full-timers here at Boot.dev) at the DotA 2 International. Absolute blast. I've never been to such an enormous gaming event in person. Ah, well, back to coding.

Regards, Lane

## Patch notes

### 1. New Unit Test Lesson Type

This is a massive change that we've been wanting to pull the trigger on for awhile now, and finally have! We now have distinct kinds of "in browser coding" lessons:

* Standard output tests
* Unit tests

Up until now, all lessons were tested based on standard output (what's printed to the console). If it matches, you pass. If not, you fail. That kind of testing is still good for some of the lessons, but for the majority of lessons, the new unit test type is a better experience.

With the unit tests, instead of checking stdout, we check to make sure your function returns the correct values, and we do that programmatically. This has a few great benefits:

* You can leave in your debugging "print" statements
* You have nicely formatted feedback on each test with pass/fail conditions
* The test code is in a separate read-only file so you don't accidentally modify it
* You get practice working in a test-driven style

### 2. New Explainer Videos

Now that we've started to get into an efficient routine with the podcast, I'm turning my attention back to making some more explainer videos for the courses themselves. I'm working on a new style of video that's more visual and fast paced. Here are a few examples:

* [Should you learn Python?](https://www.youtube.com/watch?v=kLdw64oBeCI)
* [The Queue Data Structure Explained](https://www.youtube.com/watch?v=CH6yLUtMZ28)
* [Bitwise & Operator Explained](https://www.youtube.com/watch?v=LNlIP2zCXD4)

They're obviously not perfect, but I'm happy with the *idea* and we'll keep working to improve them.

## What is yet to come

* "Learn Kubernetes" course development is underway
* Challenges and reworking of the "Learn JavaScript" course
* Updates to make sharpshooter less painful and more rewarding
* Lore for Boots

## Backend Banter Podcast

We created a [new trailer](https://www.youtube.com/watch?v=PclSNl1JRpI) for the podcast. You know, so you can share it with your friends.

This month's episodes include:

* [#024 - Behind HTMX: Carson Gross on the re-Rise of Hypermedia](https://www.backendbanter.fm/episodes/024-behind-htmx-carson-gross-on-the-re-rise-of-hypermedia)
* [#023 - Has Web Development Regressed? A Conversation with Wes Bos](https://www.backendbanter.fm/episodes/023-has-web-development-regressed-a-conversation-with-wes-bos)
* [#022 - Job Hunting as a Self-Taught Programmer with Don the Developer](https://www.backendbanter.fm/episodes/021-job-hunting-as-a-self-taught-programmer-with-don-the-developer)
* [#021 - TypeScript vs Elixir: An FP Showdown with Theo Browne](https://www.backendbanter.fm/episodes/021-typescript-vs-elixir-an-fp-showdown-with-theo-browne)

By the way, this show is NOT free. The cost is a podcast rating or a YouTube subscription. I can't verify that you've done your part, but we have an honor system here. If you have enjoyed more than one episode, do your part. I appreciate you.

## The cream of the crop

### [(Podcast) Lukas Fittl on Postgres Performance](https://www.se-radio.net/2023/09/se-radio-583-lukas-fittl-on-postgres-performance/)

by Software Engineering Radio

We've been using Postgres at Boot.dev since the beginning. I'm always interested to hear about the intricacies of database performance optimization. Usually as backend developers we don't need to be overly concerned with DB speed, we can just slap an index on a column and move on. But sometimes that's not nearly enough, and this episode goes deep on exactly when it's not.

### [(Podcast) Exploring the New Features of Python 3.12](https://realpython.com/podcasts/rpp/175/)

by The Real Python Podcast

Every new minor version of Python brings interesting new features to the language. You wouldn't want to be working without F-strings would you? Python has made giant leaps over the years, and this episode does a great job of covering all the stuff we need to know about the new 3.12 release.

### [(Article) Oh-Auth - Abusing OAuth to take over millions of accounts](https://salt.security/blog/oh-auth-abusing-oauth-to-take-over-millions-of-accounts)

by Aviad Carmel

OAuth is kinda everywhere. Here on Boot.dev we do sign in with Google, and Sign in with GitHub. OAuth offers a standard protocol for user authorization and authentication, and while its design is inherently secure, integration with web platforms can introduce vulnerabilities. This article goes over some of the, erm, implementation problems that can arise. Thar be foot guns.
