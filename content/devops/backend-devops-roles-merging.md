---
title: "Full-Stack Ops: Back-end and DevOps Roles are Merging"
author: Lane Wagner
date: "2022-10-10"
categories: 
  - "devops"
  - "backend"
images:
  - /img/800/FusionDanceFinaleGotenTrunksBuuSaga.webp.webp
---

## It's time for some speculation on my part

I believe that the job duties of "back-end" and "devops" engineers will coalesce to include almost everything that "the user doesn't see". There will still be room for specialization, but these roles will become less distinguishable overall.

First, let's talk about *why* I think this is happening, and then let's talk about what it means for us as back-end and devops engineers.

## The problem: Most companies need to ship simple features more quickly

The underlying idea behind this entire article is a simple one - most companies need to ship simple features more quickly. It's not particularly challenging to build simple features, the hard part in any product-driven company is finding out *which* features deserve to be shipped, and keeping the code in a place where features can be added quickly.

That said, there will always be hard problems to solve. As a company grows, problems that used to be simple, like an edit button, become *really really hard*, like an edit button *on Twitter*.

### Front-end engineers writing back-end code ship faster

One of the universal advantages of hiring "full stack" engineers is that it reduces the number of potential "blockers" involved in fixing a bug or adding a feature. The time to complete a task can more than double when more than a single person is required to work on it.

For example, a "full stack" engineer can pick up a task, add the required back-end code, add the required front-end code, and be done. However, if back-end and front-end engineers need to collaborate on a single ticket, everything is much more complicated. The back-end engineer deploys new code, writes documentation, then passes the ticket off to the front-end engineer. At that point, the front-end engineer takes some time to learn how the API works, and might even do some back-and-forth with the back-end dev before they get the front-end working.

### Back-end engineers who deploy infrastructure ship faster

Just as full-stack engineers improve efficiency in full-stack engineering tasks, back-end engineers that know how to deploy infrastructure increase the efficiency in back-end tasks. If a back-end engineer is working on a task that requires a new database, they would normally need to pass the task off to an ops team first, just like a front-end team would pass the need for new API endpoints to the back-end team. Instead, if the back-end engineer knows how to edit Terraform files, they can do it themselves, making everything move quite a bit faster.

However, as I pointed out above - this comes with a trade-off. Requiring your engineers to know and do *more* means that they won't necessarily be as good at any one thing. If you're familiar with the idea of a [T-Shaped developer](/about/#t-shaped-developers-are-the-most-successful), you're giving them a wider row but a more shallow column. That said, on small teams this is *usually* a good trade to make.

{{< cta1 >}}

## A caveat: The bigger the company, the more specialized the roles

Generally speaking, smaller companies need these jack-of-all-trades engineers that can do full-stack work and deploy their own code. These are people who can do many things well, but who aren't necessarily experts at any one thing. Large companies may still need jacks-of-all-trades, but they *also* need experts to solve the complex problems that only arise on the edge. 

Larger companies generally need a larger diversity of expertise to ensure that *someone* on the team can solve domain-specific problems as they arise.

**The trade-off is one of speed for expertise. More specialized teams can usually solve harder problems but do so more slowly.**

## What's changed: Companies can get away without specializing for longer

This large/small company need for specialization has always existed, but I think the line is moving. Companies are now able to grow larger than before on the backs of generalists, primarily because of all the tooling that exists.

* Node.js makes full-stack development easier.
* The cloud makes infrastructure easier to manage.
* Code written in modern languages like Go, TypeScript, and Rust is simpler to write and maintain.
* Services like Stripe, Twilio and Sendgrid allow you to outsource complex features you would have written from scratch.

{{< cta2 >}}

## So what should I do as an ops engineer?

In the [2022 stack overflow survey](https://survey.stackoverflow.co/2022/#developer-profile-developer-roles), only 10% of respondents claim to have devops responsibilities, down from 12% in 2020. The most interesting thing is that in the summary of the section, the survey creators say:

> Developers are wearing multiple hats. The majority of respondents said they considered themselves to be more than one type of developer - with DBAs, SREs, and Security professionals reporting the most variety. On average each of these roles reported being seven other developer types.

In other words, the people doing security, database work, telemetry, and monitoring also tend to be doing the most disparate activities. This makes a lot of sense to me. As monotonous IT tasks are getting automated away, it frees up these professionals to do more and more other kinds of interesting work. In some cases, they may simply start writing back-end code.

### My advice: Write more code

My advice here is simple - continue to specialize in the ops-related tasks that large companies will always need, but [start writing more code](/devops/devops-engineers-should-code/). I'm not saying that IT ops jobs are going away, I'm saying that **we'll continue to automate the boring stuff, so don't specialize in the boring stuff.**

Unless your company is in the business of infrastructure, I'd argue it's probably wise to outsource your infra to a cloud provider, and assuming you deploy on the cloud, a significant amount of your "IT Ops" work should be taken care of for you. The best part about using a cloud provider is that you can manage your infrastructure in code. **The buzzword is "GitOps", and I'm a fan.**

The best "DevOps" engineers in the industry write code and use source control. Automating and versioning infrastructure tasks in code means you don't need as many people SSH'ing onto servers to install dependencies and deploy new releases. It's faster to use code, and also less prone to human error. As a result, the company only needs a few people writing and maintaining automated systems. The majority of their engineers can then *use* those tools to *deploy their own code*.

The trend I'm seeing is that for small, simple web apps, the full-stack or back-end devs can just deploy on the cloud using some simple out-of-the-box configuration files. As the company grows, you'll likely need a more dedicated "devops" team, but if that team's any good, they'll just be hardening the deployment tooling so that the rest of the team can *do their own ops.* "Every back-end engineer an ops person", or something like that.

## So what should I do as a back-end engineer?

Get familiar with cloud technologies, and get familiar with the infrastructure you deploy on if you aren't already. If you like small companies and startups, this will be even more important. If you go to work at larger companies, you'll likely have most of the deploy tooling built for you, but it's still much better if you understand how it works.

You can hardly write great application code if you don't understand where and how it runs.

Good luck!
