---
title: "???"
author: Lane Wagner
date: "2023-03-08"
categories: 
  - "devops"
  - "backend"
images:
  - /img/800/FusionDanceFinaleGotenTrunksBuuSaga.webp.webp
draft: true
---

Theo has this video on Kubernetes, currently titled ["You Don't Need Kubernetes"](https://www.youtube.com/watch?v=H5sPGruv2yc). Now, I'm a Kubernetes enjoyer, but I'm not here to argue that point. The part of the video I *do* want to discuss is unrelated to the title, it's where Theo draws the "Line of Primeagen":

![line of primeagen](/img/800/pointofprime.jpeg.webp)

He explains that some technologies trade scalability (performance, flexibility, whatever) for speed of development. Deploying Next.js using Vercel and Firebase is quick but it comes at a cost. As you scale up, either by adding users, or by adding more complex features, you'll need to do one of two things:

* Rewrite with something more flexible or performant
* Pay a *lot* of money to a third-party to handle your problems for you

So, the idea is that you should choose a fast-to-ship technology (any language with the word "script" in the name probably) so that:

* You can move faster
* You can hire cheaper

You should stick to that strategy until your scale hits the "Line of Primeagen". It represents the point where you're losing so much money due to slow code or third-party costs that it's worth it to do the hard things required to more efficiently "sacle" (whatever that means in your case).

You gotta hire a Rust Chad and kick those React Andys to the curb. Or something like that.

## What's wrong with this idea?

Well, nothing really. Theo's correct. If you're a founder, indiehacker, or engineer #1 at a startup, this is exactly how you should be thinking.

*...Granted, I can ship a Go app to Kubernetes faster than I can get eslint, tsc, and VSCode to all cooperate but I digress...*

The problem is that *you* aren't a founder, an indiehacker, or engineer #1 at a startup. 99% of my readers want to be a great engineer and earn a high salary as employee #2-10000 at a tech company. There's nothing wrong with that, but it means your decision-making will be different.

## What should *you* do?

When I look at that graph above, I think:

> "How can *I* be the one they throw money at to come in and do the hard things?"

In other words:

1. When you're making a business decision, it's generally good to pick the simplest, fastest, and cheapest option
2. When you're making a career decision, it can pay to be an expert in hard things

To be clear, that doesn't mean you need to 

## The intersection of hard and in-demand

Haskell is hard, but it's *really* niche. Jobs are pretty scarce.

JavaScript is easy (I'll die on this hill), but it's *everywhere*. Jobs are plentiful.

If you want to be expensive, like The Primeagen, you *should* learn Kubernetes. Or something. Kubernetes is just the example in the video, but there are tons of technologies and skills that, while hard, are also in high enough demand that companies pay a premium for that expertise.

![hard and in-demand](/img/800/difficultydemand.png.webp)

To be fair, Go isn't a hard language, but companies tend to use it to solve hard problems. Just look at Kubernetes, the King of distributed systems. It's written in Go.

People don't like to hear this, but *difficulty is a moat*. When something gets easy, it gets cheap. If you want to be paid a lot, you need to be **really good** at something that's both *in-demand* and *hard*. If it were easy, everyone would be doing it. That's why very few people actually made money dropshipping in 2015 or buying NFTs in 2017. 

It's also why I hate when coding Bootcamps talk about how easy it is to learn to code. It's not easy. At least, not if you're doing the interesting stuff that pays well.

To be clear, I don't believe in standing in the way of progress. I want coding and software engineering to get simpler, easier, and faster. The result of that, however, is that the winning strategy for software engineers is to continually specialize in hard and in-demand skillsets.
