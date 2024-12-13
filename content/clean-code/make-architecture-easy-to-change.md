---
title: "Your Architecture is Bad, So Make It Easy to Change"
author: lane
date: "2023-02-10"
categories:
  - "clean-code"
images:
  - /img/800/crumbling-building-greek.png.webp
---

Have you ever started a new software development job and thought:

> "Wow, what a beautifully architected system! I wouldn't change anything here."

Unless it's a brand-new project, I'm guessing not. Most of us are dreadfully aware of the dashes of technical debt we sprinkle into our codebases every day, all in the name of getting the job done.

Don't get me wrong, I'm a clean architecture _nerd_. I love talking about monoliths, microservices, containers, clusters, PaaS, caching, message queues, and everything else under the sun. I do everything I can to make sure that my code is easy to debug, easy to scale, and easy to add features to.

Here's the thing: _I also know that my architecture is terrible, and yours is too._

## Why is your architecture so bad?

Well, maybe it's not. Your architecture may be pretty good _at the moment_. You might be using a popular design pattern, you may have services that can scale up to handle 10x the load that you're currently seeing, and all the engineers on your team might understand the codebase.

Unfortunately, your architecture _is_ bad three years from now. It's bad when your team goes from 10 to 100 engineers. It's bad when your company pivots from a B2B SaaS product to a B2C mobile app. It's bad when you onboard a new enterprise client that requires you to store all their data in a different country.

Assuming you have good engineers, your architecture is probably bad due to _business_ decisions, not technical ones. It is often a _good_ business decision to accrue technical debt if the payoff is worth it, and a savvy engineer will know when to make that tradeoff.

## Is there no hope?

It's sometimes a good decision to take on technical debt, but we need to acknowledge that the debt must _eventually_ be paid back.

You _can_ know what a good architecture for your _current_ business needs is, so build that! There's no sense in planning for 1,000,000 users when you only have 500. Avoid planning too far ahead, but also understand that your future needs could be _wildly_ different from your current ones.

To put this idea simply:

> Build your systems for the present, but anticipate a very different future

## Wait for more information before locking in your architecture

The best architectural decision you can make is to often _not make one_. Here's an example. Let's pretend you're building a web app that displays temperature data from various weather sources. You're already using a PostgreSQL database for authentication and user information and need to decide where to store the weather data, but you know that your temperature aggregations queries won't scale well in a monolithic database like Postgres.

However, you only have a few data sources and a few users, so scalability isn't a problem. I'd argue that you should just shove that data in Postgres, with a loose plan to move to a more domain-specific solution later.

But wait!!! Here's where most engineers go wrong.

_You should be engineering around the fact that you don't like your current solution._

Instead of locking yourself into Postgres by using advanced Postgres features and implementing `JOIN`s to your other tables, try to keep your data as flat and as simple as you can. When you do inevitably need to move your data somewhere else, you can do so with minimal effort.

When you're building software for a fast-growing company, a "clean" architecture isn't an _optimized_ one, but a _modular_ one that can be changed easily.

## So I should just procrastinate?

It's not about procrastinating architectural decisions, it's about being able to make smarter decisions once the real data comes in. As an engineer, it's impossible to predict every pivot the business will make, every requirement a customer will have, and every technology that will be released in the future. Your goal is to engineer a system that does its job while delaying decisions you don't _need_ to make until you have more information.
