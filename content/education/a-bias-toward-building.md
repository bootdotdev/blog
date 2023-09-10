---
title: "A Bias for Learning"
author: Lane Wagner
date: "2023-09-09"
categories: 
  - "education"
images:
  - /img/800/pileofbooks.png.webp
draft: true
---

Ever since starting [Boot.dev](https://www.boot.dev), I get *a lot* of questions that I call "quicksand questions". On the surface, a quicksand question *seems* like a good question. If you had an answer to it, it would help you get from where you want (unemployable as a developer) to where you want to be (employed as a developer)!

These quicksand questions have something in common, they're all about finding shortcuts.

> I need a developer job in 3 months, what's the best way to do that?

> Hey I know you've laid out 20 courses here in the learning path, but, *wink wink*, which ones can I skip?

> I see you are teaching CS basics in Python, then teach backend development concepts in Go. Can I just skip the Python stuff?

I'll break down each of these questions in just a second, but first, let's talk about the underlying problem.

## What's wrong with shortcuts?

Now, I want to be *clear*, there is *abosultely nothing wrong* with wanting to take a shorter path to your career goal. Anything else would be insanity. If I could offer you a serum that upon injection would give you all the knowledge and experience you need to be a senior developer, you'd be *crazy* not to take it.

In fact, part of the reason I'm so passionate about Boot.dev is that I think CS degrees are fantastic in how deep they go on math, computer science, and programming theory. But I don't think it's the best route if you're in your late twenties or thirties and want to take a quicker path. Those acting and music electives aren't doing you any favors.

In short, shortcuts are good in a theoretical sense, but I've found in practice they don't work. Why? Because they're not really shortcuts.

## It's because tech is a messy clusterf*ck of complexity

Look, if you actually knew *exactly* which concepts you'd need to master to pass your first interviews, then you could take an effective shortcut. The trouble is, there is no *precise* subset of knowledge that will always be enough to pass those first interviews.

* Every company has unique needs
* Every hiring manager has different problems
* Every industry has different requirements
* Every geographic location has a different tech scene
* Every city has a different culture
* Every developer role uses different technologies

The list goes on and on. The point is, you have almost *no idea* what you'll be doing day to day at your first job when you're just starting to learn to code. I hear people say things like "I never even use my DSA skills at work", and upon further inspection, it turns out they're a WordPress "developer".

Budding backend developers shouldn't be taking advice from WordPress developers. They have different jobs to be done.

## So I shouldn't be looking for the shortest path?

You should, it's just not where you think you'll find it. The shortest path to a job as a programmer is *not* to try to minimize the amount of things you need to learn and build. That sort of thinking tends to result in a much longer, more mentally taxing journey. It usually looks like this:

1. Jump directly into a web framework
2. Find you have a talent for building Spotify clones
3. Realize you can't even build "hello world" without a tutorial
4. Attempt to remedy that by doing more tutorials
5. Read on Twitter that ackshaully Rust is the best language
6. Submit to defeat at the hands of the borrow checker
7. Repeat steps 1-4 `n` times, where `n` is a `D4 roll * your_stubbornness`

The shortest path (or at least short*er* path) usually looks like this:

1. Learn core programming/cs *concepts* in some language
2. Tentatively decide on the kind of programming you want to do (frontend, backend, mobile, etc)
3. Learn the fundamentals of that kind of programming in technologies well suited to it
4. Build, build, learn, build, learn and build, etc

Don't get me wrong, this second path still isn't exactly short. Programming isn't easy. But, the difference is that you're not wandering aimlessly through the 9th circle of tutorial hell. You're building a foundation of knowledge and skills that are useful in almost any programming job.

## Don't be scared of doing some work

Folks spend eons trying to find the perfect learning path, or trying to avoid learning things that "they'll never use again". Instead of wasting a few days learning something that's not directly applicable to the job they'll eventually land, they waste *months or years* learning absolutely nothing because they're scared of doing *any* unnecessary work.

## Go just a bit deeper

When you encounter an error, instead of copy/pasting haphazardly from StackOverflow to "fix it", you take the extra minutes to figure out what it means. I can't begin tell you how many PRs I've reviewed that "fix" something, but are just a patch on a patch because the dev never understand the underlying problem.

For example, an ex-Java dev (it's always the Java dev) finds that *sometimes* this function panics:

```go
// sendEmail sends emails, but sometimes panics
func sendEmail(e *email) error {
  // ...
}
```

They go straight to Google and find that panicking in Go can be "solved" with a `recover`. So they open a pull request:

```go
func sendEmail(e *email) error {
  defer func() {
    if r := recover(); r != nil {
      log.Println("recovered from panic in sendEmail")
    }
  }()

  // ...
}
```

This kinda works? But a better developer would try to understand and fix the underlying problem in the code. They would add `nil` checks, or just stop using pointers altogether for this function... why should I need a pointer to send an email anyway?

```go
// now sendEmail never panics
func sendEmail(e email) error {
  // ...
}
```

Bias yourself toward learning new shit, not toward reaching the end. It doesn't work, there isn't an "end".

As an aside, in startups, Y Combinator looks for founders that have a "bias toward action". People that ship a ton of stuff, even if it's not perfect tend to do better.

In my experience, students that have a bias toward good old fashioned "gettin good" tend to do much better. I'm not kidding when I tell you that I will have someone pop into the Boot.dev discord in February, and ask:

> I need a developer job in 3 months, what's the best way to do that?

Then they disappear for months after being told "that's an unreasonable expectation to set for yourself, there's a lot of stuff to learn". Without fail, that *same person* shows up in November again:

> I REALLY need a developer job in 3 months, what's the best way to do that?

Clearly having made zero progress over the 9 month period. You can make a lotta of progress in 9 months if you spend your time learning and building instead of "networking" in twitter spaces and looking for shortcuts.

## Learning can be fun, but it's not a true game

When I was a guest on the Indiehackers podcast, I thought Channing Allan said it well:

> When you're out hiking, if someone offered you a helicopter ride to the top of the mountain, you would obviously turn it down. You're there for the journey. That's how you can know if something is really a game for you.
