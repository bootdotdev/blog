---
title: "Your Code isn't Correct"
date: "2021-11-29"
categories: 
  - "clean-code"
tags: 
  - "mailing-list"
  - "sharing"
---

There is a common trap that we fall into as developers, and it is believing that because some code "worked" that the code was written "correctly". In reality, for most technical problems, a good developer can likely point out several different solutions. Any of those solutions might be perfectly reasonable, while none of them is the single "correct way".

## Different solutions optimize for for different things

You can only optimize for a few things at once, and there are always tradeoffs. Bloated memory consumption often makes way for faster computation speed. Simple syntax often leads to a lack of control or configurability. Different solutions to the same problem often optimize for slightly different things. I'm personally a fan of [optimizing for simplicity first](https://qvault.io/clean-code/optimize-for-simplicity-first/), but "simple" means different things to different people.

In some cases, short and concise variable names might be simple. In some cases, a longer name with 4 or 5 words might be simpler.

Firestore as a storage engine might be simple because it's "basically just persisted JSON", but leads to data duplication. It might make reading data simple, but adds complexity at "create", "delete" and "update" time.

Vanilla JavaScript is "simpler" than a giant React framework at first. Once your app grows so large that you begin rewriting reactive libraries into your own code, React would likely be "simpler".

In short, when you're reviewing someone else's code, and it looks different from how you would have done it, try to see if they're making improvements in areas where your solution wouldn't have. Just because your solution does one thing "better", doesn't mean it's better overall.

## Your code can always be better

I _really_ don't agree with the conclusion of this somewhat popular meme, and I cringe a bit when I see newer developers sharing it.

![](images/hqdefault.jpg)

If you need to maintain your code into the future, as most of us do, please revisit it and update it! Tech debt is real debt.

- Keep dependencies up to date
- Refactor API contracts to keep them sensical as business rules change
- Upgrade to newer infrastructure and technologies as it makes sense to do so
- Keep your team knowledgeable on the older parts of the system, legacy code can be scary

## Just because code can be better, doesn't mean it's a priority

There is some truth to the "1st rule of programming" meme though, don't get me wrong. There are cases where you don't want to waste precious time updating or refactoring code. For example:

- You just need a prototype because product market fit hasn't been found yet
- You know whatever code you wrote won't be needed for long because a more robust solution is being purchased or built
- You just need a proof of concept
- The client is unwilling to pay for maintenance (in a service-based business)

Be smart. Your solution isn't perfect, and that's okay. Continue to iterate and everything will be fine.
