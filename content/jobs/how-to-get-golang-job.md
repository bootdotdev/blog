---
title: "How to Get a Job as a Golang Developer"
author: Natalie Schooner
date: "2023-03-17"
categories: 
  - "jobs"
  - "golang"
images:
  - /img/800/lane_gophers_in_a_job_interview_whisical_fantasy_setting_bb50879d-3834-4317-99bd-caab82f2daf0.png.webp
draft: true
---

Step 1: Learn Golang. Step 2: Apply for jobs. Step 3: Get accepted.

When I started researching this article, that was the first answer that came up on Reddit. It’s short and punchy, but it’s not very useful, is it? (The [second answer](https://www.reddit.com/r/golang/comments/i9ma30/how_to_find_a_job_as_a_go_developer/) was a joke that because "Go" only has two letters, some search bars don’t accept it since they need three or more characters to search.)

![search bar golang](/img/800/searchbar.png.webp)

Presumably, you’ve come to this article because you’re interested in the long version that has all the useful links, tips, tutorials, advice, and resources to help you get a job as a Golang developer.

I trawled Golang job postings and Reddit to bring you the very best and most complete solution. I’ll include a description of all the technology you should know, what you don’t need, and the best steps to apply that knowledge and get a job as a Golang engineer.

This is a long guide, so feel free to take this one step at a time, bookmark it, and return when you’re ready for the next section. Let’s dive in.

## What I assume you already have

Before we go any further, let’s establish that you’re here for the right reasons. Knowing Golang is great for your career – the [Golang salary](https://www.talent.com/salary?job=golang+developer#:~:text=The%20average%20golang%20developer%20salary%20in%20the%20USA%20is%20%24135%2C000,up%20to%20%24173%2C326%20per%20year.) for entry-level developers is $117k. There are tons of amazing remote Golang jobs.

But you shouldn’t be here just because you want a cushy position, or you think it’s easy to get a Golang developer job. You should be here because you think Go is a great language, backend development is cool, and you want to be the very best candidate for the role.

If you’re reading this article, you should have:

* Some Go proficiency.
* Interest in coding.
* A desire to learn your craft *in-depth*, without cutting corners.

> If you’re brand new to Go, I recommend you hop off this article and learn a little about it first. As part of our [backend-development career track](https://boot.dev/tracks/backend), we at Boot.dev offer a fantastic [Go intro course](https://boot.dev/learn/learn-golang) that will walk you through everything you need to know to get started with Go.

## What you don’t need

Let’s clear up some common misconceptions. If you’re looking to get a job with Go, you do not need:

* A computer science degree.
* 100% proficiency in Go.
* Deep knowledge of Go frameworks.

A computer science degree is a nice-to-have, but it’s expensive and time-consuming. Many jobs today don’t mind if you’re self-taught, as long as you have a portfolio of projects proving you have the skillset they need. **No degree, no problem**.

There’s also **no such thing as 100% proficiency** in any coding language, much less Golang. If you wait until you feel fully confident in your Go skills to apply for jobs, you’ll be trapped forever.

Instead, I recommend diving headfirst into coding. Have fun, don’t rush it, and don’t expect perfection from yourself. Build things and push yourself past your comfort zone, yes, but remember that

Finally, **you don’t need to know Go frameworks**, at least, not to start. There’s a real temptation to use frameworks as a shortcut. But if you start with frameworks, you’ll be left with:

> "An entire codebase, with mountains of dependencies, and you’ll understand how almost none of it works under the hood. When you encounter issues (and you will) you’ll be spending hours trying to work backward."
> 
> -- (Our founder, Lane, who has written a [few](/backend/dont-start-with-frameworks/) [articles](/backend/wrong-about-abstractions/) on the subject.)

## Step 1: Learn computer science fundamentals

Now let’s take a look at some things that you need to learn to get a job as a Golang developer. First on the list, master computer science fundamentals.

While realistically, you can get a job without a degree in CS, you still need the knowledge that comes with a computer science degree. (You’ll just get it in a fraction of the time and cost.)

Here are some fundamentals you should be deeply familiar with. And because we’re [big believers](/about/) in doing, not just reading, I’ll include a sample project you can run through to make sure you know your stuff in each section.

### Architecture

Go back to college, you need a degree in architecture before you can code in Golang!

Sorry, bad joke. I couldn’t stop myself. That being said, architecture in terms of backend development is not as dissimilar from physical architecture as you might assume. It’s about how you design a system with different components that can talk to each other and perform well.

An architect designing a building might use a steel frame to support the structure. That architect would consider how people will move through the building, and where the doors should go.

Similarly, when you think about architecture in the backend sense, you might decide that you need a microservices architecture to break the backend up into smaller, more manageable components. You might think about how data needs to come in and out of the backend, and build retrieval mechanisms based on that thinking.

I could quote you ten blogs and textbooks to read through to understand the vast world of "architecture," but like I said: boring. Instead, here’s [a good tutorial](https://www.velotio.com/engineering-blog/build-a-containerized-microservice-in-golang) to help you understand architecture by setting up a web app using microservices architecture.

Warning: it’s relatively advanced, so you may need to do deeper dives into any technologies you’re unfamiliar with. But when you finish, you’ll have a much better understanding of architecture.

### Object-oriented Programming

No, not [that OOP](https://www.youtube.com/watch?v=PUttqdr38t4).\[Lane, this is very well-known in my circle of the internet but idk if programmers will find it funny lol. Feel free to take it out if the reference doesn’t fit.\]

Object-oriented programming (OOP) is a computer programming model used in many languages, including Python. The idea is that "objects" can contain data and code.

Classes and objects are used to model real-world concepts and organize code. When you use OOP, you have simple, reusable pieces of code.

As a Golang developer, you should understand the key four OOP concepts: abstraction, encapsulation, inheritance, and polymorphism.

You will almost certainly be asked about this at interviews. Now, you can just memorize the definition of those concepts and rattle them off when prompted. That’ll at least show you prepared. But if you want to demonstrate real understanding, you’ll be better off if you actually understand them.

Go isn’t OOP per se, but there are times when it makes sense to force Go to behave like one. But for the sake of this section, I recommend learning about OOP using an OOP-native language like Python. We’ve got a [three-minute demo tutorial](https://boot.dev/learn/learn-object-oriented-programming) that will show you how to use OOP and how it works.

### Algorithms and data structures

Data structures are how you organize and store data in memory. An algorithm is just a good set of instructions to perform on that data. The two go hand in hand because you’ll almost always use them both together. For example, a sorting algorithm will need a data structure for the data to be stored. How well the algorithm performs depends on which data structure you choose.

Again, these are basics you can know in any language, so I recommend you use a tutorial [like this one](https://www.manning.com/liveproject/trees) to practice coding your algorithm and choosing data structures. We also have a [comprehensive algorithms course](https://boot.dev/learn/learn-algorithms) on Boot.dev that walks you through algorithms by actually building a demo product and an accompanying [data structures course](https://boot.dev/learn/learn-data-structures).

### Cryptography

It is a truth universally acknowledged, that a company in possession of a Golang developer job posting fortune, must be in want of ten other jobs, such as DevOps, InfoSec, and IT.

Paraphrasing Austen slightly, but chances are you already know that if you want to be a backend engineer, companies will expect you to wear several other hats. One of those is security. You should know all about encryption, password security, and ciphers.

Pro tip: make sure to fully spell out cryptography when you research it, or else you’ll just get a bunch of bitcoin.

Want to practice your cryptography skills? Again, we’ve got a [superb code-based tutorial](https://boot.dev/learn/learn-cryptography) on the subject. Aside from that, you could consider creating a simple cipher to encrypt and decrypt plaintext into and out of cyphertext. [Here’s](https://www.golangprograms.com/cryptography.html) a basic tutorial walking you through that project.

## Step 2. Master coding basics

Alongside knowing the fundamentals of computer science, you should also have some hands-on practice with coding. (And if you followed my advice, by the time you get to this section, you’ll have practiced coding in four separate projects.)

Here are the basic coding skills you should expect to have to get a job as a Golang developer. You may notice that all of these are code-agnostic – they’re true no matter if you’re coding in Python, Javascript, or Go.

### Write good, clean code

Is your code effective and efficient? Does it make sense to other people? Do you follow best practices?

The best way to do this is to solicit feedback and offer feedback. The process of editing and being edited on your code is the fastest way to improve. Post questions on StackOverflow, and look for questions you can answer. Buddy up with a friend to offer mutual peer editing.

### Debug

Every project you ever do will have bugs. It’s just a fact of life. Knowing how to debug is a critical coding basics step. Here are the three most important debugging subskills you should practice.

1.  Not blowing up. Errors and warnings can get very irritating, very quickly, especially if you’re under time pressure or stress. Cultivate a curiosity for finding out what’s wrong. Learn the most common errors and how to avoid them.
2.  Understanding the feedback. Most Go developers use a debugging tool like Delve or GDB. I also recommend learning how to use the print statement to debug. You can also learn to use the Log package to create custom logs for your code.
3.  Looking for help. Get used to browsing StackOverflow, Reddit, and Discord groups to look for bugs and how other people have solved them.

### Another coding language

Finally, if you want to get a job as a Golang developer, one of the most important coding basics to master is another language. I recommend Python, and ideally Javascript as well.

Not only does [knowing multiple languages make you more employable](/education/learn-multiple-programming-languages/), but it also makes you a better programmer. When you know how OOP works in Python, it’s easier to apply in Go, for example.

## Step 3. Learn backend tech and tool familiarity

So far, we’ve covered computer science fundamentals and coding basics. Those are useful for any Golang job title you might be applying for. Now let’s take a look at backend specifics, which will be more targeted towards becoming a Golang developer.

### APIs

As a Golang developer, you need to know RESTFul design principles, request and response handling, authentication and authorization mechanisms, and integrating third-party APIs.

Show off your mastery of this skill by building a cute finance API with [this tutorial](https://github.com/benfl3713/finance-api). In the end, you’ll have touched on:

* CRUD
* Authentication
* MongoDB (which we’ll get to in just a moment)
* Asp.net

### SQL and NoSQL databases

As a Go developer, you will build things that touch a lot of databases. Those might be SQL-friendly, like SQLite and MySQL. They might store data in a different format, like MongoDB, Redis, or PostgreSQL.

I cover both in my article on the [top backend technologies](/backend/top-backend-technologies/). To prove your mastery of these, I recommend building an app that uses a NoSQL database, and one that uses a SQL database. Read around your options and choose your database wisely. Be able to explain why.

### Kubernetes

Sometimes spelled "k8s." Not pronounced "kates," sadly. K8s is a popular orchestration platform that developers use to deploy and manage containerized applications at scale.

I hate jargon, so the translation of that is that people use Kubernetes to manage lots of containers simultaneously. Here "container" just means a lightweight version of a computer program that can run on different computers.

I love [this tutorial](https://blog.getambassador.io/go-kubernetes-rapidly-developing-golang-microservices-bfe36cfb5893) that walks you through how to set up a development environment for Kubernetes and make a change to a Golang microservice.

### Cloud environment

Go is amazing for building cloud-native applications. More and more companies nowadays are taking advantage of the benefits of cloud deployment and development (as I explored in my article on the [differences between DevOps engineers and Cloud engineers](/devops/devops-vs-cloud-engineers/), i.e. none).

Many job openings now mention that you should be familiar with AWS, GCP, and/or Azure. As of today, there are only Clouds owned by companies like Google, Amazon, and Microsoft. That’s good because it means those companies are invested in helping you learn how to use their tools. So you’ll often find great tutorials on company websites, like [this one](https://docs.oracle.com/en/cloud/paas/app-container-cloud/getting-started-go-accs/) from Oracle.

### Message queues

I covered this in more depth in my article about the [top backend technologies](/backend/top-backend-technologies/#top-four-message-queues), but basically, message queues are how you build async communication between services in a distributed system.

Here’s [a library](https://github.com/wagslane/go-rabbitmq) you can use to learn how to implement message queues in Golang using RabbitMQ, one of the more popular MQs at the moment.

## Step 4. Prove you have a can-do attitude

Once you’ve built a resume where every skill is easily demonstrated with a project on your portfolio, it’s time to cover the soft skills. I am firmly of the opinion that once you get your foot in the proverbial interview door, more jobs are lost by poor soft skills than by any gap on your resume.

To get a job as a Golang developer, you need to demonstrate the following "soft" skills:

* **Communication:** Can you talk to people? Can you explain complex topics simply to laypeople? Because you’ll be doing a lot of that in your job. The best way to prove this is by clearly and thoroughly explaining your thoughts as you do the whiteboard portion of your interview.
* **Problem-solving:** It’s on almost every single job posting for the very simple reason that as a Golang developer, people will be looking to you to fix a lot of problems, not just the ones in your specific purview.
* **Lateral thinking:** "Thinking outside the box" is harder to prove. I recommend you practice logic puzzles and riddles. This can be a lot of fun!
* **Code reviews:** Many companies will ask that you participate in these. Join coding communities and offer to buddy up with people to do this.
* **Big picture discussions:** Go back to those fundamentals. Are you able to contribute to a company’s overall strategy? Can you intelligently recommend different architectural structures? Do you have thoughts on cryptography? Most companies don’t want you to be a cog in the machine * they want people who have enough general knowledge in the field to spot bigger issues and know how to fix them, rather than just following instructions all the time.
* **Ability to interview well:** [Be humble and confident](/jobs/confidence-in-job-interviews/). That’s what it boils down to. It’s easier to do that if you know what you’re talking about, so I recommend doing as much interview question prep on websites like StrataScratch as you can. This will help you be more secure in your knowledge.

## Step 5. Portfolio and jobs

By now, you have general knowledge of the computer science fundamentals that underpin every Golang developer job. You have coding basics. You’ve proven competencies in key areas to get a Golang developer job. You’ve practiced interviews and you know you can smash it.

The final step is to build a portfolio and apply to jobs intelligently.

### Build your resume and portfolio

A resume is much more than a piece of paper. Once you’ve done all those projects I’ve listed above or some variation of them, it’s time to put together your resume and your portfolio.

You should carefully select the projects that work the best at showing off your skills. They should:

* Have well-written tests
* Have clean and well-organized codebases
* Detailed `README.md` files describing what they do, and how to use them
* Do something interesting. The more interesting your project, the more likely you are to pique the attention of a hiring manager

It’s also a good idea to [add libraries and packages](/jobs/libraries-and-packages-in-coding-portfolio) to your portfolio. This shows a deeper understanding of software engineering and architecture than most hiring managers are used to seeing.

### Apply intelligently

One of the main reasons you can’t get a job as a Golang developer? You’re using the spray and pray technique.

It’s much better to apply to one job every week and do a perfect job than applying to ten every week but half-assing it.

To apply intelligently, you should be:

* **Doing company research**. Stay up to date with company announcements, developments, new products, and press releases. This especially matters with companies using Golang.
* **Staying current with new tech**. Programming is a fast-moving field; Go is a new language that’s growing fast. You can impress hiring managers just by knowing more about the latest buzzword than your peers.
* **Practicing good network hygiene**. It’s a shame, but a lot of job success comes from who you know, not necessarily what you know. Join communities and learn how to make friends. See how you can give back * with code reviews, feedback, introductions, or debugging help. Then see if anyone can help you.

## How to get a job as a Golang developer: practice, apply, and get accepted.

I know I joked about it at the very start of this article, but that’s what all 2800 words of this advice boils down to.

Learning Golang goes way beyond memorizing frameworks and copy-pasting code, though. And it’s more than memorizing the four classes in OOP and different types of algorithms. You need to have a real understanding of these concepts, and you need to apply them to real-world projects, with real code.

And applying goes beyond hitting "easy apply" on every LinkedIn post you come across. The more time you take to do your research, practice and prove soft skills, and build a portfolio that proves you can do what you say you can, the better your chances will be.

Getting the job comes down to good interviewing practice and good networking. Immerse yourself in programming communities, develop a real joy and passion for learning new technologies, and have fun along the way. That’s the best way to get a job as a Golang developer.
