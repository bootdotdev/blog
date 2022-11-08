---
title: "CI/CD Isn't Just About Efficiency"
author: Lane Wagner
date: "2022-09-26"
categories: 
  - "devops"
  - "backend"
images:
  - /img/800/8020.avif.webp
---

DevOps principles, and CI/CD specifically, are generally presented as a more efficient way to run a software development organization. While I hold the belief that CI/CD *is* more efficient and effective than manually testing and deploying code, I'd like to talk about something we don't bring up quite as often.

Put simply, CI/CD *makes us happy*.

## Developer happiness matters

There are great resources out there that demonstrate the practical benefits of CI/CD. Fewer bugs, faster features, tighter release schedules, etc. If you're interested in that data, I'd recommend the book "Accelerate", but let's forget about all of that for a moment.

Tech companies spend *a lot* of money to keep employees happy. Provided the budget exists, they set up ping-pong tables, buy soda machines, host meetups and hire baristas. All those perks are great, but if I'm ssh'ing onto a server multiple times each day to pull down new code and manually restart the back-end, I'm not a happy camper.

**Good engineers want to automate the boring stuff.**

## People don't quit bad jobs, they quit bad developer experiences

There's a saying:

> People don't quit bad jobs, they quit bad bosses

There's truth there of course, but I for one will quit a job, even if I *do* have a good boss if I *hate* the developer experience. Now, I'm also the kind of person that will go to great lengths to *upgrade* the developer experience before quitting, but sometimes there are simply too many roadblocks.

I *really* do not like doing manual tasks that can be easily automated. I do *not* like deploying code. I *do* like merging PRs. I do *not* like pulling down my coworker's 4-line PR so I can run `go test`. I *do* like seeing that the tests passed in the PR.

{{< cta1 >}}

## Is it worth it to set up automation?

One of my favorite comics about automation is this classic [XKCD](https://xkcd.com/1319/).

![xkcd automation](https://imgs.xkcd.com/comics/automation_2x.png)

However, there is a problematic assumption that some people make in regard to automation. I do *not* think this is the right equation:

```
should_automate = time_to_automate < time_for_task * num_tasks
```

The equation is far too practical. Humans are emotional creatures. I think there needs to me more leeway given to account for the fact that it's generally *more enjoyable* to write automation than to do a manual task over and over.

For completely selfish reasons, I would rather spend 8 hours writing a script to move some data into a database than spend 6 hours manually copying and pasting. One of the tasks is soul-sucking, finger-numbing, painfully *boring* work. The other will probably be a bit of fun.

Perhaps a good analogy is, "To earn $100, would you rather spend 4 hours shoveling rock or 6 hours playing videogames?" 

## The remaining manual tasks become more enjoyable

Imagine that a bug is reported, and you know *exactly* what the problem is. If you've got some nice automation pipelines set up, fixing the problem for your users is *almost* as easy as simply making the code change.

However, if you don't have any automation in place, it's an annoying pain in the ass. Changing the code still only takes 30 seconds, but you're now going to spend 15 minutes manually getting the new code running in production. You think, "Maybe this deployment can wait until the end of the day when we were going to deploy anyways."

I guess what I'm saying is that I'm *extraordinarily* lazy, and I'm aware of it. I keep myself motivated and effective by making sure I like my job as much as possible. Automation isn't just about being more effective in an absolute sense; though it *is* that as well. Automation is also about being more effective by making my job more enjoyable so that I'm more motivated to do it.

## What's your point?

I'm not going to automate everything - I haven't thrown efficiency to the wind. However, I bias toward automating because I'm not a machine, I'm human, and I enjoy it.
