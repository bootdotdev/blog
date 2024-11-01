---
title: "Maybe You Do Need Kubernetes"
author: Lane Wagner
date: "2024-03-08"
categories:
  - "education"
images:
  - /img/800/buildingarobot.png.webp
---

Theo has this great video on Kubernetes, currently titled ["You Don't Need Kubernetes"](https://www.youtube.com/watch?v=H5sPGruv2yc). I'm a Kubernetes enjoyer (I even wrote a [course on it](https://www.boot.dev/courses/learn-kubernetes), but I'm not here to argue about that. The part of the video I _do_ want to discuss has nothing to do with k8s. It's where Theo draws the "Line of Primeagen".

He explains that some technologies trade scalability (performance, flexibility, whatever) for speed of development. Deploying Next.js using Vercel and Firebase is quick but it comes at a cost. As you scale up, either by adding users or by adding more complex features, you'll need to do one of two things:

- Rewrite with something more flexible or performant
- Pay a _lot_ of money to a third-party to handle your problems for you

So, the idea is that you should choose a fast-to-ship technology so that you can move faster and hire more cheaply.

_...I can ship a Go app to k8s faster than I can get eslint, tsc, and vsc-de to cooperate... but I digress..._

Then you stick with that strategy until you scale up to the "Line of Primeagen":

![line of primeagen](/img/800/pointofprime.jpeg.webp)

It represents the point where you're spending so much money due to slow code or third-party costs that it's worth it to do the hard things required to more efficiently "scale" (whatever that means in your case).

You gotta hire a Rust Chad and kick those React Andys to the curb. Or something.

## What's wrong with this idea?

Well, nothing really. Theo's correct. If you're a founder, indiehacker, or engineer #1 at a startup, this is exactly how you should be thinking.

The problem is that _you_ aren't a founder, an indiehacker, or engineer #1 at a startup. 99% of my readers want to be a great engineer and earn a high salary as employee #2-10000 at a tech company. There's nothing wrong with that, but it means you should think about this stuff differently.

## What should _you_ do?

When I look at that graph above, I think:

> "How can _I_ be the one they throw money at to come in and do the hard things?"

In other words:

- When you're making a _business_ decision, it's generally good to pick the simplest, fastest, and cheapest option
- When you're making a _career_ decision, it pays to be an expert in hard things

To be clear, I'm _not_ saying that you should solve simple problems in complicated ways just to inflate your market value. That can have the opposite effect. Bad engineers do that. I'd say:

> Gain the hard skills required to solve complex problems, but only deploy complex solutions when they're actually needed.

## Maybe you should learn Kubernetes

People don't like to hear this, but _difficulty is a moat_. When something gets easy, it gets cheap. If you want to be paid a lot, you need to be **really good** at something that's both _in-demand_ and _hard_. If it were easy, everyone would be doing it. That's why very few people actually made money dropshipping in 2015 or buying NFTs in 2017.

![making money agen](/img/800/makingmoneyagen.png.webp)

It's also why I hate when coding Bootcamps talk about how easy it is to learn to code. It's not easy. At least, not if you're doing the interesting stuff that pays well.

To be clear, I don't believe in standing in the way of progress. I want coding and software engineering to get simpler, easier, and faster. The result of that, however, is that the winning strategy for software engineers is to continually build expertise in in-demand, hard-to-learn stuff.

## So should I not learn Next.js?

I'm not trying to single out individual technologies (except for Java, don't do Java kids). I'm saying that you shouldn't be scared of the hard stuff. Don't jump from easy tutorial to easy tutorial. Once you've found your bearings in this whole coding thing, start tackling some harder problems. The work will pay off.
