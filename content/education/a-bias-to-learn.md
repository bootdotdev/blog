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

Ever since starting [Boot.dev](https://www.boot.dev), I've been flooded with what I call "quicksand questions". On the surface, a quicksand question *seems* like a good question. If you could answer it, it would catapult you from where you are (Wendy's drive-in) to where you want to be (telling Twitter you work at Netflix btw).

Quicksand questions have something in common, they're all about finding shortcuts.

> I need a developer job in 3 months, what's the best way to do that?

> Hey I know you've laid out 20 courses here in your backend learning path, but, *wink*, which ones can I skip?

> I see you teach cs basics in Python, then teach backend development in Go. Can I just skip the Python stuff?

## What's wrong with shortcuts?

Now, I want to be *clear*, there is *absolutely nothing wrong* with wanting to take a shorter path toward your career goal. Anything else would be insanity. If there was a pill to turn you into a senior developer overnight, I'd encourage you to pop that sucker.

In theory, career-path min-maxing seems like a solid strat, but in practice it just doesn't work.

Why? Because the destination is *unknown*.

Dijkstra's algorithm is great if you know where you're going. If you don't, you need something else.

## No one knows where they're going

The tech scene is a clusterf*ck of complexity. I learned like 10 different programming languages in college, and even after 3 years into my degree, I still didn't know that I'd end up working as a backend engineer writing Go. I interviewed for all sorts of nonsense, from embedded systems to frontend development.

If you knew *exactly* which concepts you'd need to master to pass your first interviews, then you could might be able to find an effective shortcut. The trouble is, there is no *precise* subset of knowledge that will always be enough to pass every possible first interview.

* Every company has its own janky tech stack
* Every PM has their own version of "agile"
* Every hiring manager has their own 7-step interview process
* Every developer role requires different types of arcane knowledge

The list goes on and on. The point is, you have *no idea* what you'll be doing day to day at your first job when you're just starting to learn to code. I hear people say things like "I never even use my DSA skills at work", and upon further inspection, it turns out they're a WordPress "developer".

## So I shouldn't be looking for the shortest path?

You should, it's just not where you think you'll find it. The shortest path to a job as a programmer does *not* involve minimizing the amount of things you need to learn and build. That sort of thinking results in a much longer, more mentally exhausting journey. That slog usually looks something like this:

1. Jump directly into a web framework (probably Next.js since you're basic af)
2. Find you have a talent for building todo apps
3. Realize you can't build "hello world" without a tutorial
4. Attempt to remedy that by doing more tutorials
5. Read on Twitter that ackshaully Rust is the best language
6. Admit defeat at the hands of the borrow checker
7. Repeat steps 1-4 `n` times, where `n` is a `d4_roll * your_stubbornness`

The shortest path (or at least short*er* path) usually looks like this:

1. Learn core programming/cs *concepts* in some language
2. Tentatively decide on the kind of programming you want to do (frontend, backend, mobile, etc)
3. Learn the fundamentals of that kind of programming in technologies well suited for it
4. Build, build, learn, build, learn and build, etc

Don't get me wrong, this second path still isn't short. Programming isn't easy, sorry if you were told it was. But, the difference with this second approach is that you're not wandering aimlessly through the 9th circle of tutorial hell. You're building a foundation of knowledge that remains useful in almost any programming job.

## It's really an attitude problem

The primary difference between the 2 paths I outlined is one of *mindset*.

The first has a bias toward reaching the end. It's about skipping steps and taking shortcuts. It's no different than a crypto bro's "get rich quick" attitude.

The second approach has a bias toward *learning and building*. When you encounter an error, instead of copy/pasting haphazardly from StackOverflow to "fix it", you take the extra minutes to figure out what it means. I can't begin tell you how many PRs I've reviewed that "fix" something, but are just a patch of a patch because the dev never grokked the underlying problem.

For example, an ex-Java dev (it's always a Java dev) finds that *sometimes* this function (in Go) panics:

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

This kinda works? But a better developer would try to understand and fix the underlying problem in the code. They would add `nil` checks, or just stop using pointers altogether for this function...

```go
// now sendEmail never panics
func sendEmail(e email) error {
  // ...
}
```

Bias yourself toward getting good, not reaching the end. There isn't an "end"!

## Biases can be helpful when the problem is vague

In startups, Y Combinator looks for founders that have a "bias toward action". People who ship a ton of stuff, even if it's not perfect tend to build more successful companies.

In my experience, students with a bias toward "gettin' good" tend to do better. It's not an infrequent occurrence that someone pops into the Boot.dev Discord and says:

> I need a developer job in 3 months, what's the best way to do that?

Then they disappear for months after being told "That is probably an unreasonable expectation to set for yourself". Without fail, that *same person* shows up in November again:

> I REALLY need a developer job in 3 months, what's the best way to do that?

Having clearly made **zero** progress over the 9-month period. You can make a *lot* of progress in 9 months if you spend your time learning and building instead of "networking" in Twitter spaces and DM'ing influencers for their secret shortcuts.

## It's not the advice you wanted

Getting fit, giving up addiction, building a business, and yes, getting your first job as a developer are all *hard*. Don't make it harder on yourself by wasting your time searching for shortcuts.

Learn evergreen concepts, build a lot of stuff, and you'll be amazed how far you can get in even just a year.
