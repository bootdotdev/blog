---
title: "Why We Force You to Learn Multiple Programming Languages"
author: Lane Wagner
date: "2022-06-13"
categories: 
  - "education"
images:
  - /img/800/photo-1533709475520-a0745bba78bf.avif.webp
---

I've been building [Boot.dev](https://boot.dev) as a side-project for the last couple of years, and have recently had many new students ask the same question:

> "Why does your computer science curriculum require me to learn more than one programming language?"

It seems that a good number of students join the platform with the opinion that they would rather "fully master a single language" than "split their efforts". While I plan to explain this better in the app itself moving forward, I wanted to write get this blog post out to provide an in-depth explanation of why we have you learn several languages over the course of our [CS program](https://boot.dev/tracks/computer-science).

## First, some background on Boot.dev

So that you can understand where I'm coming from, let me explain what Boot.dev is, and what its goals are as an educational platform.

Boot.dev is a batteries-included computer science curriculum in the browser. We have some [strong opinions](/about) about the best way to learn to code. For example:

* We teach computer science and software engineering concepts first. Specific technologies are just a mechanism by which we teach the concepts.
* We are fully hands-on
* We have guided courses and unguided projects
* We teach modern technologies and languages
* We have a linear curriculum so students don't have to worry about what they should be learning next
* We gamify the experience as much as possible to keep students motivated

{{< cta1 >}}

## So why can't the whole curriculum be taught in a single language?

If you look at the [full CS curriculum we have planned in our public roadmap on Github](https://github.com/bootdotdev/curriculum), you'll see that it's basically impossible. There are certain concepts that are so tightly coupled to specific technologies that it makes no sense to try to teach them all the same way. Let's look at a few trivial examples.

* It's hard to really teach databases without SQL
* It's hard to teach functional programming without a purely functional language
* It's hard to teach OOP without an object oriented language
* It's hard to teach hardware interfaces without an assembler
* It's hard to teach typing without a strongly typed language
* It's hard to teach web without JavaScript
* It's hard to teach ML without Python

In short, we have 2 competing goals:

* We want to teach all the concepts using as few technologies as possible
* We want to teach all the concepts using technologies that teach the concept best

## So how many languages are you going to teach me?

Over the course of my traditional CS degree at university, I used 12+ programming languages. I think that's too many. I don't want to teach languages for the sake of teaching them. It's really an optimization problem where we want to introduce as few languages as possible, while effectively teaching every concept we want to teach. I'm confident that the full curriculum for [Boot.dev](https://boot.dev) will only require the use of about 6 languages in total, and that the majority of the program can just use JavaScript, Python, and Go.

{{< cta2 >}}

## Learning multiple languages removes your tunnel-vision

There is an additional benefit to learning a few different programming languages that we haven't talked about yet. By exposing you to different languages, you will begin to see some of the benefits, drawbacks, similarities, and differences between the various approaches to programming.

If you only ever write one programming language, it's easy to assume a certain way of doing things is the "best way", the "right way", or maybe even the "only way".

For example, JavaScript and Go have wildly different approaches to error flow:

```javascript
// JavaScript
try {
  doSomethingDangerous()
} catch (err){
  console.log(err)
}
```

```go
// Go
err := doSomethingDangerous()
if err != nil {
  fmt.Println(err)
}
```

By familiarizing you with several languages, I firmly believe you will have a deeper understanding of each technology, and when you might want to use different tools.

## Will I be a jack-of-all-trades, master of none?

Personally, I don't think so. I really do think that if you were to focus on only a single programming language from the start of your learning journey up until your first coding job, you would actually be in worse shape than if you'd spent some time broadening your horizons.

Some people assume that "learning to code" is about "learning a programming language". They think that if you learn Python, and then want to learn JavaScript, you'll be starting over from 0. **That couldn't be further from the truth.**

Learning your second programming language will take 1/5th of the time that it took to learn your first, because ~80% of the concepts you learned will apply to both languages. Once you've used 3 or 4 different coding languages, you can look at code in almost any language and understand what it says. You might find yourself needing to look up syntax occasionally, *but everyone does that anyways*.

![meme](/img/800/fd066e1554c9a78bc499d06840e7dd02.png.webp)

## Well, could you at least reduce the number of general-purpose languages?

If you've browsed [the curriculum](https://github.com/bootdotdev/curriculum), you may have noticed that we've settled on 3 languages to teach the majority of the content:

* JavaScript
* Python
* Go

We're going to try to use these 3 languages for *as much as we possibly can*, only mixing in other technologies as required by the subject matter. For example, using SQL when we're talking about relational databases.

Let me explain why we chose these three in particular.

### Why JavaScript?

You can't really get away from JavaScript these days. It's hard to [learn about backend programming](/backend/become-backend-developer/) (which is what most of our students are interested in) without first understanding *why* a backend exists. A backend only exists to power a front-end, so it makes sense that we would need to teach you a few front-end basics first. If you're going to build a front-end on the web, it almost certainly will use JavaScript, so our hand is forced on this one.

### Why Python?

Python gets out of your way, syntactically speaking. Algorithms and data structures are concepts that students often find more difficult to master, so it made sense to us to choose a language that would allow our students to focus as much as possible on the logic. Python also reads like English in many ways, which again makes it easier to see what an algorithm in Python is doing at a glance. Additionally, we have AI and ML content towards the end of the curriculum, so it's a two-birds-on-stone situation where we can revisit Python at that point without our students needing to learn an additional language.

### Why Go?

Our CS degree has an emphasis on backend programming, and I've personally had tremendous success with Go as a backend language.Go will make it easier to teach things like concurrency, compilers, and distributed systems than some of the other choices I've thought about. I do think we might eventually have a Rust course that goes to an even lower level in terms of manual memory management, but I haven't decided on that yet.

## Questions? Comments? Concerns?

The best way to reach me directly is by joining the [Boot.dev Discord server](https://discord.gg/EEkFwbv). You can also @ me on [Twitter](https://twitter.com/wagslane). Let me know what you think of our approach!
