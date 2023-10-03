---
title: "Are You a DevOps Engineer If You Aren't Writing Code?"
author: Lane Wagner
date: "2022-09-12"
categories: 
  - "devops"
  - "backend"
images:
  - /img/800/photo-1602992708529-c9fdb12905c9.avif.webp
---

"DevOps" is one of the most misunderstood terms in the software development industry. To be clear, I'm not the arbiter of truth when it comes to the definitions of words. That said, I'm here to say two things:

1. The pioneers of the DevOps movement had a specific meaning in mind when they coined the term, and that meaning is *mostly* misunderstood.
2. We've learned a lot about DevOps over the last 10 years. I use the term to describe what I believe are the *current* best practices in regard to the *original* meaning.

One of the things that bothers me the most about the "DevOps" industry is that middle management in so many companies seems to be incentivized to [rebrand their ops department](https://wagslane.dev/posts/no-one-does-devops/) to a "DevOps" department without introducing any positive change.

**DevOps is not just ops in the cloud.**

## A note on definitions

I enjoy a great conversation, and nothing kills good conversations like two people using the same word while meaning different things.

There is nothing magic about the word "DevOps" or any other word for that matter. If you want to tell me you have a different definition of the word, *that's fine*. It can be *confusing* depending on how different your definition is, but we can work with it. That said, it's *up to you* to be clear about what *you* mean when you talk about DevOps - especially if you're using an unusual definition of the term.

Following my advice, I'm going to define *a part* of what I believe "DevOps" to be. That is, that **good DevOps organizations have very few IT ops people that don't write code**.

* I interpret the "[DevOps Handbook](https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002)" and "[The Phoenix Project](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/1942788290/ref=sr_1_1?crid=JU3U3CV4OQDS&keywords=the+phoenix+project&qid=1662910991&s=books&sprefix=the+phoenix+projec%2Cstripbooks%2C120&sr=1-1)" (which are the books that started "DevOps") to support this idea.
* I also interpret much of the research over the last 10 years (including the data in the "[Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339/ref=sr_1_1?crid=1HX8YTKQW1PHN&keywords=accelerate+book&qid=1662911026&s=books&sprefix=accelerate+boo%2Cstripbooks%2C115&sr=1-1)" book) to support the idea that ops people who write code enable more effective organizations.

## What does the DevOps Handbook say?

Let's take a look at an excerpt from the "DevOps Handbook":

> Myth — DevOps Means Eliminating IT Operations, or "NoOps": Many misinterpret DevOps as the complete elimination of the IT Operations function. However, this is rarely the case. While the nature of IT Operations work may change, it remains as important as ever. IT Operations collaborates far earlier in the software life cycle with Development, who continues to work with IT Operations long after the code has been deployed into production.
> 
> Instead of IT Operations doing manual work that comes from work tickets, it enables developer productivity through APIs and self-serviced platforms that create environments, test and deploy code, monitor and display production telemetry, and so forth. By doing this, IT Operations become more like Development (as do QA and Infosec), engaged in product development, where the product is the platform that developers use to safely, quickly, and securely test, deploy, and run their IT services in production.

The most important point for our purposes is:

> IT Operations become more like Development ... where the product is the platform that developers use ... to run their services

In other words, if a "DevOps" team is to be a team at all, in my opinion, it should be the team responsible for building the tooling that enables developers to quickly test, deploy, and monitor their services *themselves*.

## Is there no place for IT Ops people anymore?

Yes, there absolutely is. There are plenty of organizations that need traditional IT operations engineers and have no real need for them to be writing custom code. I want to be clear, the vast majority of *my experience* is in the development of cloud-based web services. In that environment, I've found that "DevOps" engineers who can script, write automation, build APIs and use Git are more effective than those who can't.

However, I can trivially think of other industries where IT teams who don't code could be just as effective as those who can. For example, if you have teams of people working close to the hardware itself, it's less likely that they would need to write code. There's probably more than enough work to go around configuring hardware, setting up networks, etc.

With all that in mind, I think there are certain skills in this world that you *simply should pick up*, assuming you have the time and the resources.

1. Do you need to know how to code? Nope. Will it almost certainly make you a more effective "knowledge worker"? Yup.
2. Do you need to be a great writer? Nope. Will it almost certainly make you a better communicator? Yup.

I wouldn't say "everyone needs to learn to code". I *would* say, if coding interests you and you have some spare time, it's worth your while to pick it up.

## So should I learn to code as an ops person?

If you're a DevOps engineer that's uncomfortable with the idea of writing code, it's never to late to start. I've found that ops people make *great* developers for several reasons:

* They're familiar with command line tooling, telemetry, networking, etc
* They're familiar with technologies like databases, pubsub systems, load balancers, etc
* They understand the programs they'll be writing from the outside, now they just need to figure out the internals
* They're already used to banging their head against the keyboard trying to figure out why something is broken

Anyhow, not to plug my stuff too hard, but if you're interested in getting started with back-end coding, I've created [Boot.dev](https://boot.dev) to be a place for ops engineers to upskill in coding and computer science. Do check it out if you want to learn to write back-end code in Python, JavaScript and Go. That said, if Boot.dev is not your cup of tea, check out [FreeCodeCamp](https://www.freecodecamp.org/), [the Odin Project](https://www.theodinproject.com/), or any other good resources that work for your needs.

## So, are you a DevOps engineer if you aren't writing code?

Sure, you can be whatever you want. My intention isn't to gatekeep. I guess there are three things I care about.

1. I want to work in an organization that enables developers to test, deploy, and monitor their services easily and in an automated fashion.
2. I call the people that make that happen "DevOps" people.
3. You don't *have* to write code to achieve the goals of DevOps, but it's going to be a lot harder if you *can't*.

Best of luck!
