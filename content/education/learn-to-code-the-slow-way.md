---
title: "Learn to Code the Slow Way"
author: Lane Wagner
date: "2023-09-10"
categories: 
  - "education"
images:
  - /img/800/shortcutwizard.png.webp
---

Ever since starting [Boot.dev](https://www.boot.dev), I've been flooded with what I call "quicksand questions". On the surface, a quicksand question *seems* like a good question. If you could answer it, it would catapult you from where you are (nightshift at the Wendy's drive-in) to where you want to be (telling friends that you work at Netflix btw).

Quicksand questions are all about finding shortcuts.

> I need a developer job in 3 months, what's the best way to do that?

> I see you've laid out 20 courses in your backend learning path, but, \*wink\* which ones can I skip?

## What's wrong with shortcuts?

Now, I want to be *clear*, there is *absolutely nothing wrong* with wanting to take a shorter path toward your career goal. Anything else would be insanity. If there was a pill to turn you into a senior developer overnight, I'd encourage you to pop that sucker.

In theory, educational min-maxing seems like a solid strategy, but in practice it just doesn't work.

Why? Because the destination is *unknown*.

Dijkstra's algorithm is great if you know where you're going. If you don't, you need something else.

## No one knows where they're going

The tech scene is a clusterf*ck of complexity. I learned like 10 different programming languages in college, and even 3 years into my degree, I still didn't know that I'd end up working as a backend engineer writing Go.

I interviewed for all sorts of nonsense, from embedded systems to frontend development. Yeah, turns out that my Prolog class didn't help much in my first interview, but you know what? It didn't *hurt*, and now when someone says "it's a declarative system" my facial expression doesn't betray ignorance.

![it's a declarative system](/img/800/its-declarative.png.webp)

If you knew *exactly* which concepts you'd need to master to pass your first interview, then you could might be able to find an effective shortcut. The trouble is, there is no *precise* subset of knowledge that will always be enough to pass every possible first interview.

* Every company has its own janky tech stack
* Every PM has their own version of "agile"
* Every hiring manager has their own 7-step interview process
* Every job requires different bits of arcane knowledge

You have *no idea* what you'll be doing day to day at your first job when you're starting to learn to code. I hear people say things like "I never even use my DSA skills at work", and upon further inspection, it turns out they're a WordPress "developer".

## So I shouldn't be interested in the shortest path?

You should, it's just not where you think you'll find it. The shortest path to a job as a programmer does *not* involve minimizing the amount of things you need to learn and build. That sort of thinking results in a much longer, more mentally exhausting journey. Something like this:

1. Jump directly into a web framework (probably Next.js since you're basic af)
2. Find you have a talent for building TODO apps
3. Realize you can't build "hello world" without a tutorial
4. Attempt to remedy that by doing more tutorials
5. Read on Twitter that ackshaully Rust is the best language
6. Admit defeat at the hands of the borrow checker
7. Repeat steps 1-4 `n` times, where `n` is a `d4_roll * your_stubbornness`

The shortest path (or at least short*er* path) usually looks like this:

1. Learn core programming/cs *concepts* in some language
2. Tentatively decide on the kind of programming you want to do (frontend, backend, mobile, etc)
3. Learn the fundamentals of that kind of programming in technologies well suited for it
4. Never stop learning and building while you search for a job

Don't get me wrong, this second path still isn't short. Programming isn't easy, sorry if you were told it was, but if you're willing to put in the effort you can avoid an aimless stroll through the 9th circle of tutorial hell.

## Don't be scared of work

Folks spend eons trying to find the shortest learning path, or trying to avoid learning things that "they'll never use again". They're fine wasting *months or years* learning absolutely nothing to avoid doing *any* unnecessary work. Why not bite the bullet and risk spending a few *days* learning something that's not directly applicable to the job you'll eventually land?

## Dogecoin to the mooon?

Let's be 100000000% honest. Some folks are looking for a good 'ol fasioned get rich quick scheme. After a few weeks of struggling with loops, they'll give up and purchase an AI-powered crypto trading bot on Fiverr. Don't be like those folks.

> Becoming a software engineer is NOT a "get-rich-quick" scheme. It's a "get-upper-middle-class-slow" scheme

The trick to "making it"? You have to actually get good.

So, instead of copy/pasting haphazardly from StackOverflow to "fix" the next error you encounter, take the extra minutes to figure out what it *means*. I can't begin tell you how many PRs I've reviewed that "fix" something, but are just a patch of a patch because the dev never grokked the underlying problem.

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

You want to have a bias toward becoming better, not reaching the end. There isn't an "end", there's just too much out there to learn. The scope of all of software engineering is larger than the scope of your last program's global namespace.

## It's not the advice you wanted

Getting fit, giving up addiction, building a business, and yes, getting your first dev job are all *hard*. Don't make it harder on yourself by wasting your time searching for shortcuts.

Learn evergreen foundational stuff, build projects that interest you, and you'll be amazed how far you can get in just a year or two of consistent effort.
