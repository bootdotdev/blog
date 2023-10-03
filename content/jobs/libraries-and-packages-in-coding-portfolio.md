---
title: "Add Libraries and Packages to Your Coding Portfolio"
author: Lane Wagner
date: "2022-11-13"
categories: 
  - "jobs"
images:
  - /img/800/library.png.webp
---

Building a job-ready portfolio of coding projects doesn't happen overnight, but if you're like most self-taught developers, you've likely built up a nice collection of todo apps, calculators, and other toy programs. Here's the thing, applications for end-users are great, but I'm here to convince you that adding a *library* to your portfolio will make you *much* more hireable.

A specific library that I wrote has helped me land jobs several times, but I'll talk about that more later.

## Wait, what's the difference between an application and a library?

Applications are normal programs. They start up and do some stuff. They have an entry point like a `main()` function. On the other hand, a library (aka package), consists of some code intended to be used in other programs. If you've ever used `go get`, `npm install`, or `pip install`, then you've included a 3rd party library in your code.

Here are some examples.

| Name                                                   | Type        |
| ------------------------------------------------------ | ----------- |
| [Docker](https://github.com/docker)                    | Application |
| [Kubernetes](https://github.com/kubernetes/kubernetes) | Application |
| [Discord](https://discord.com/)                        | Application |
| [go-rabbitmq](https://github.com/wagslane/go-rabbitmq) | Library     |
| [numpy](https://numpy.org/)                            | Library     |
| [lodash](https://www.npmjs.com/package/lodash)         | Library     |

## What is a "portfolio project" anyhow?

A portfolio project is just a project that you feel comfortable sharing with potential employers - both the finished product *and* the code. Its primary purpose is simply to assist you in your job search, it shows what you're capable of building, and frankly, a great portfolio can do a lot for your [confidence in interviews](/jobs/confidence-in-job-interviews/). Not every project you build while learning to code should necessarily be a "portfolio" project. You'll build plenty of projects just for the sake of learning, or for fun.

*Portfolio* projects require some additional work. I recommend picking just 2-3 projects that you'll actively showcase on a resume or GitHub profile page. You should hold these select projects to a higher standard. They should not only *work*, but also:

* Have well-written tests
* Have clean and well-organized codebases
* Detailed README.md files describing what they do, and how to use them
* Do something *interesting*. The more interesting your project, the more likely you are to pique the attention of a hiring manager

**I recommend making at least one of your portfolio projects a library, and at least one an application.**

I'd also recommend getting your [GitHub or GitLab profile in order](/jobs/build-github-profile/), after all, it's where your portfolio lives. It's okay to have more than just your 2-3 portfolio projects set as "public" on your GitHub, but you probably only want to pin your best work.

## Okay, what's so why should I create a library for my portfolio?

1. Designing a good library shows a deep understanding of software engineering and architecture
2. It's easier for an engineer to understand why a library is useful than a random app that may or may not be the target user of
3. It's easier for your project to gain some traction on GitHub as a library, which can act as social proof
4. Many entry-level developers aren't building libraries, so you'll stand out

Let's go over each point in a bit more detail.

### 1. A library demonstrates engineering and architectural skills

It's pretty easy to build a small app using *awful* coding and architectural practices. As long as it *works*, your users can't even tell the code is shitty right?

With libraries, you can't get away with it. Your users are developers, so if your library's exposed functions, classes, and types are poorly written, it's dreadfully obvious. Conversely, it's easy and fast for someone skimming your documentation to see if your library has a good API.

When managers are browsing your work, it's important that they can quickly tell that you've built something amazing, and packages can communicate that effectively.

### 2. A random hiring manager is more likely to be your "target user"

Building a cool app that people will use is *really hard*, and has very little to do with coding skills. However, it helps a lot in the hiring process if the people interviewing you think you've built some cool stuff.

When you build an application, you're typically building it for a specific kind of person. For example, tinder is built for (mostly) single people looking for relationships. People in happy, monogamous relationships are unlikely to care about Tinder.  

However, when you're building a library, even if your interviewer isn't exactly the user of your library (due to a coding language mismatch for example), they will likely understand and appreciate the technical problem your library solves. Applications solve all sorts of problems, from medical billing to boredom. Libraries truly just solve a single problem: technical complexity, and that's something every developer understands.

### 3. Libraries can gain traction more easily

While it's not necessary, it's a great [help to your job search](/jobs/reasons-you-cant-get-a-programming-job/) if one of your projects can get some "social proof" behind it. GitHub stars, blog posts referencing the tech, and external pull requests all quickly signal to a reader that this project is "legit".

Now, I'm not saying you should spend your valuable time marketing your portfolio project, but the added benefit of libraries over applications is that they tend to gain traction in developer circles more easily. If you build a library that solves a meaningful technical problem, even if it's a small one, then publish it on NPM or wherever is most appropriate for the language, you have a good chance of gaining a couple of users and fans.

### 4. Most developers aren't building libraries

When you're applying for your first developer job, your competing with many other new developers. Frankly, most of the candidates are doing the same old things, which makes it hard for the hiring team to find the best people. Anything you can do to stand out positively will help!

The fact that most developers don't even have a good portfolio of projects will already be a point in your favor. However, if on top of that you have a cool library with a simple API you'll be in a really good place.

## The libraries and packages that helped me get work

I've now written a couple of little packages that have helped me in my job search. While I don't mention all of them in every interview, at least one has come up in my last 3 interviews. Well, the last 3 interviews in which I ended up taking the job. Here they are, in descending order of precedence in my portfolio:

* [go-rabbitmq](https://github.com/wagslane/go-rabbitmq)
* [go-password-validator](https://github.com/wagslane/go-password-validator)
* [go-tinytime](https://github.com/wagslane/go-tinytime)

Good luck with your current and future job searches!
