---
title: "Slow Is Smooth, Smooth Is Fast - 25% of Our Time Refactoring"
author: Lane Wagner
date: "2020-09-01"
categories: 
  - "clean-code"
tags: 
  - "sharing"
images:
  - /img/photo-1559041881-74dd9fd9b600.jpeg
---

My team has been spending less of our "free" time working on bugs and features from the backlog, and more time refactoring our code and tests. As a result, and perhaps somewhat counterintuitively, we've noticed a significant increase in our throughput of features and bug fixes.

As it turns out, it's easy to find bugs and add features to a well-written codebase that the entire team is familiar with. Go figure.

I've been paying attention to our throughput and efficiency as we've made a conscious effort to spend around 25% of our time refactoring, revisiting, and restyling existing code and tests. Let's go over some of the benefits we've seen since making the change.

## Context and Caveats

I've found that in articles like this it's important to give as much context to the situation as possible, as certain development methodologies may work better or worse in teams with a different size, tech stack, or development process. Here are some notable things about our situation:

- 4 engineers on my team, ~16 in the company
- Tech stack - Go, Postgres, ElasticSearch and RabbitMQ
- Microservices architecture on Kubernetes
- Kanban-style development process - [no scrum](https://qvault.io/misc/leave-scrum-to-rugby-i-like-getting-stuff-done/)
- Our team is responsible for ~15 repositories
- Each repo represents a small service in a data pipeline process that handles sorting and NLP of social media posts

![Go Kubernetes](/img/go_kubernetes-1024x592.png)

## Code Familiarity

With only four engineers on my team and ~15 repositories we're responsible for, it was hard for all four of us to be intimately familiar with all the code. When we needed a new microservice, one team member typically wrote the first iteration, and one other team member did a quick code review. The engineer who did the first iteration would then be primarily responsible for bug fixes and new features relating to that project.

By focusing more of our time on reviewing and refactoring existing code, it gave us a chance to hop into projects that we never would have had a reason to become familiar with before. Not only does getting more eyes on a project mean the overall code quality will likely go up, but it also means we aren't hosed if the original maintainer moves on to a new company.

## Slow to Fix Bugs

When you get deep into spaghetti code, it can be really hard to find bugs. In a messy codebase, sometimes fixing a bug can actually _add_ to the "uncleanliness" of the code. You may have to exacerbate or extend an already bad architectural pattern in order to get a bug fix in.

Ideally, you would do the refactoring _first_ and _then_ fix the bug (assuming the bug still exists after a good refactoring). Unfortunately, oftentimes there isn't enough time to refactor a project before fixing a critical bug. For this reason, we should **always be refactoring** so that bug fixes can happen quickly without having a negative impact on code quality.

## Slow to Add Features

I don't want to beat a dead horse, the reasoning here is largely the same as with bug fixes. Adding features to a messy codebase just makes it messier. It's like frosting a cake that's already been dropped on the ground. I guess the cake would taste better if you still felt inclined to eat it, but you've made the inevitable clean-up harder.

![Happy Birthday to the Ground](/img/happy_birthday_to_ground.gif)

## Try It Yourself

Since adding a consistent refactoring process to our team's routine, we've been able to put _more_ features through to production while spending _less_ time working on them. Let me know what you think and if you have a different experience.
