---
title: "You're Not Qualified to Have an Opinion on TDD"
author: Lane Wagner
date: "2021-11-29"
categories: 
  - "clean-code"
images:
  - /img/800/done.jpeg
draft: true
---

One of the marks of a good senior developer is that they have lots of interesting opinions. After years of working on different software projects, they'll be able to passionately explain why they think MongoDB is ass, paired programming is no fun, and the GitHub CLI changed their workflow.

The best opinions tend to carry quite a bit of nuance and the infamous "it depends" will rear its head if you keep digging. That said, I have anecdotally found 2 things to be true:

1. Senior developers without opinions tend to not be very good
2. Junior developers with many opinions tend to not get good quickly (and are annoying AF)

## Let the gatekeeping begin

As a new developer, its smart to consume developer content. It's more effective to spend time watching The Primeagen than to doom scroll your furry feed on TikTok. However, when you listen to Prime, Dax, TJ, or myself give opinions, you need to remember that they're *our* opinions, not *yours*.

Don't misunderstand: I publish my opinions to convince you to join my cult (Go is based) but taking my word at face value is a disservice to yourself. If you try to swallow and regurgitate another developer's opinions, not only will you stunt your learning, it will look bad in interviews and on the job. *It's obvious when your opinions haven't been forged in the fires of your own experience.*

## Context specific opinions

There are *many* of kinds of developers out there:

* Frontend
* Backend
* Mobile
* Embedded
* etc

But we don't just discriminate on tech stack! There are also many kinds of *companies*:

* Venture backed startups
* Indiehackers
* Established tech incumbents
* Non-tech companies with internal software
* Consultancies
* etc

No matter what advice you're hearing about technology, you need to remember that the speaker comes from a specific background. *Opposing hot takes* coming from people with *different backgrounds* can both be great takes.

* Know you need to scale compute across a cluster of machines? Kubernetes good.
* Building a portfolio site for your dog? Kubernetes bad.

![Kubernetes argument](/img/800/koobernetusmeme.png.webp)

* I work mostly on Backend HTTP servers in Go and think debuggers are a waste of time (the state of the program is easy to reproduce)
* John Carmack does a lot with game engines and loves debuggers (the state of the program is hard to reproduce)

* Theo works on a startup where product direction is constantly in flux and performance isn't the #1 problem. He likes TypeScript.
* The Primeagen works at Netflix btw and solves performance issues where product direction is relatively static. He likes Rust.

If you're a Xitter enjoyer like myself, you need to appreciate that the context is *never* contained in the tweet. You'll only start to understand the context surrounding a hot take if you're already familiar with the author.

The point? If you're new to coding, understand that this stuff is nuanced, but adding nuance to titles, thumbnails, and tweets *never* gets clicks.

## So what's this about TDD?

Test driven development is a somewhat controversial development methodology. Some developers love it, some hate it. MBA's always love it because it makes them feel secure and warm. TDD falls into the same category as a few other hot-button topics:

* Pair programming
* Agile & Scrum
* SOLID principles
* Micro-services vs Monoliths
* FP vs OOP
* NoSQL vs SQL
* etc

These are things that you'll hear about often, and most developers tend to form strong opinions about them. Here's my advice:

> If you haven't tried it in a real project (that you were paid for), keep your mind open

Listen to the opinions of others. Try to understand the reasoning behind the opinions. Try to think about the different situations where an opinion might make more or less sense. Then, when you have a chance, try it out for yourself.

Once you've done a thing, have a think about it. I love conducting interviews where the conversation turns into a discussion about the pros and cons of different technologies, architectures, and methodologies. It gives me a lot of insight into how a developer thinks about stuff. If you can't talk intelligently about a thing after doing it, you won't look like you understand it.

*PS: The only exception to all of this is scrum. **Scrum always sucks**, regardless of your company, religion, political beliefs or sexual orientation.*
