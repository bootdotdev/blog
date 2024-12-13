---
title: "You're Not Qualified to Have an Opinion on TDD"
author: lane
date: "2023-11-07"
categories:
  - "clean-code"
images:
  - /img/800/wizardsfightingoversomething.png.webp
---

One of the marks of a good senior developer is that they have lots of interesting opinions. After years of working on different software projects, they'll be able to passionately explain why they think MongoDB is ass, paired programming is no fun, and the GitHub CLI changed their workflow.

I have anecdotally found 2 things to be true:

1. Senior developers without opinions tend to not be very good
2. Junior developers with many opinions tend to not get good quickly (and are annoying AF)

## Let the gatekeeping begin

As a new developer, it's smart to consume developer content. However, when you listen to Prime, Dax, Theo, or myself give opinions, you need to remember that they're _our_ opinions, not _yours_.

![i think this htmx meme](/img/800/ithinkthishtmx.png.webp)

Don't misunderstand: I publish my opinions to convince you to join my cult (Go is based) but taking my word at face value does a disservice to yourself. If you simply regurgitate another developer's opinions, not only will you stunt your learning, but it will look bad in interviews and on the job. _It's obvious when your opinions haven't been forged in the fires of your own experience._

## Context-specific opinions

There are _many_ kinds of developers out there:

- Frontend
- Backend
- Mobile
- Embedded
- etc

But we don't just discriminate on tech stack! There are also many kinds of _companies_:

- Venture backed startups
- Indiehackers
- Established tech incumbents
- Non-tech companies with internal software
- Consultancies
- etc

No matter what advice you're hearing about technology, you need to remember that the speaker comes from a specific background. _Opposing hot takes_ coming from people with _different backgrounds_ can both be great takes.

- Do you need to scale computing power across a cluster of machines? Kubernetes good.
- Are you building a personal site for your dog? Kubernetes bad.

- I work mostly on Backend HTTP servers in Go and think debuggers are a waste of time (the state of the program is easy to reproduce)
- John Carmack does a lot with game engines and loves debuggers (the state of the program is hard to reproduce)

- Theo works on a startup where product requirements are constantly in flux and performance isn't the #1 problem. He likes TypeScript.
- The Primeagen works at Netflix btw and works on performance issues where product direction is relatively static. He likes Rust.

Now, the best opinions tend to carry the infamous "it depends" as you keep digging for exactly this reason. However, if you're a Xitter enjoyer like myself, you need to appreciate that the context is _never_ contained in the tweet. You'll only begin to understand the context surrounding a hot take once you're familiar with the author.

The point? If you're new to coding, understand that this stuff is nuanced, but adding nuance to titles, thumbnails, and tweets _never_ gets clicks.

## So what's this about TDD?

Test-driven development is a somewhat controversial development methodology. Some developers love it, some hate it. MBA's _always_ love it because it makes them feel safe. TDD falls into the same category as a few other hot-button topics:

- Pair programming
- Agile & Scrum
- SOLID principles
- Micro-services vs Monoliths
- FP vs OOP
- NoSQL vs SQL
- etc

These are things that you'll hear about often, and most developers tend to form strong opinions about them. Here's my advice:

> If you haven't used it in a real project, don't hate it (yet)

That's why it's _literally impossible_ to hate Haskell. No one has tried it in production yet.

## Be a humble junior dev (I wasn't)

One of the biggest mistakes I made early was simply assuming I knew more than I did. I would push for refactors that made no sense to get away from technologies that I thought were "old" or "bad". I wanted to rewrite perfectly stable parts of the code because I thought the new hotness was more maintainable.

![rewrite in react](/img/800/rwwriteinreact.png.webp)

By all means, consume coding content online, but try to understand the reasoning behind the opinions you're hearing. Try to think about the context the speaker is coming from. Then, when you have a chance, try the thing out for yourself before making your own bold claims.

_PS: The only exception to all of this is scrum. **Scrum always sucks**, you can just trust me on that one. It sucks regardless of your company, religion, political beliefs or sexual orientation._

_PPS: If this is your first time hearing about Kubernetes and you want to learn, we have a [complete interactive course on k8s here](https://www.boot.dev/courses/learn-kubernetes) that you can check out_.
