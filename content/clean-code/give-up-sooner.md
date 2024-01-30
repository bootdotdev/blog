---
title: "Give Up Sooner"
author: Lane Wagner
date: "2024-01-28"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/goldencitysad.png.webp
---

As a developer, how many times each day do you look something up online? I'm not talking about a simple piece of syntax, I'm talking about the things that are a bit harder to find. For example:

* Is there a good way to compile C to WebAssembly and run it in a browser without needing to modify the code itself?
* Can the Stripe UI export promotion code redemptions as a CSV?
* Is there a *good* tool for hot module reloading in Go?
* Is it socially acceptable to go out in public in South Dakota with blue hair?

While working as a team lead a few years ago, I remember asking Jeffy, a developer on my team:

> "Is there a way to get [sqlc](https://sqlc.dev/) to use pointers for nullable columns instead of the sql.Null types?"

Jeffy went heads down for... much longer than I would have expected. After more than a full day of research, he came back with:

> "No, there isn't a way. I found something that seemed promising, but it doesn't work. I think we should fork the project and add it ourselves."

*Hol' up.* I've got some questions.

First, you're telling me that you found what we want in the API of a well-known open-source project, but it's broken and *no one else* knows that it's broken but you? You are confident there aren't any skill issues involved?

Second, you're telling me that your recommended course of action is for our team of four to fork a project with many thousands of lines of code and maintain our own version ad infinitum? All for a little quality of life improvement?

![type safe sql princess bride](/img/800/typesafesqlwestley.png.webp)

*No, Jeffy. No.*

## What was Jeffy's problem?

Counterintuitively, I believe Jeffy's problem was that he didn't know when to give up. I don't mean on the task as a whole, I mean on each individual path he was taking to find the answer. Here's a chart.

![Jeffy's Local Maximum](/img/800/jeffylocalmax.png.webp)

Jeffy was too attached to his initial searching methods. Maybe he was too attached to one page from the docs, to his initial search query, or to Google as a search mechanism altogether. Jeffy found a *local maximum* and became stuck. He should have bailed **so much sooner** and tried looking elsewhere.

If I don't find good evidence that the answer I'm looking for exists in the place I'm searching, I'm bailing pronto. That doesn't mean I'm 100% certain it doesn't exist, but you usually don't have to read an entire Stack Overflow thread to know whether or not it relates to your problem.

I'm honestly amazed at how some developers take so long to look stuff up. Now, in their defense, even if you're an efficient searcher, you can still get stuck in a "quagmire": a local maximum. If you're not careful, you can find yourself reading on and on about a topic that seems like *exactly* what you're looking for, only for it to skim over the details that you actually need. Bummer.

I'm a big [fan of using AI](/computer-science/ai-taking-programming-jobs/) as a replacement for some of my would-be Google searches, but Chat GPT is the *ultimate* quagmire, that is the ultimate local maximum. It's the worst kind of quagmire because at every step it will confidently reassure you that it does in fact know the answer. When you insist that it's wrong, it confidently continues to provide information that sounds correct, but isn't.

If you use Chat GPT for programming assistance, you *need* to develop a strong sense of when Chat GPT is making stuff up. In short, *you need to know when to bail.*

## RTFM

Sometimes we talk about "Googling things" as a skill unto itself, and it kind of is. But similar to Chat GPT, it's less about formulating the most pristine search query, and it's more about knowing when to give up on a goose chase.

* Does the SERP indicate that your original search query was a good one? No? Bail.
* Does the first page you visit have a directly relevant title or first paragraph? No? Bail.
* After spending another minute on the page are you still convinced the answer is somewhere below? No? Bail.
* Is it likely the answer can be found more easily in the docs, the user manual, or, *gasp*, the code itself? Yes? Bail.

Reading the manual, perusing the official docs, or digging through the source code usually takes longer than skimming an on-topic article or tutorial, but SEO-spammed articles often coalesce into an entire sea of local maxima. They tease you by scratching the surface of what you're looking for, but if your issue isn't the most common one, you can waste hours trudging through the garbage.

Sometimes, taking the [time to go deep](/education/learn-to-code-the-slow-way/) into the topic is the fastest (only?) way to find answers to the more esoteric questions.

## Back to Jeffy

I don't want to leave you hanging on this story. As it turned out, the documentation for SQLC was complete, but it was tricky to understand how to use pointers for nullable columns if you landed on the wrong page. There are a lot of configuration options for SQLC, and it's easy to get lost.

I just cloned the repo, grepped for "pointer", and found the code that parsed the configuration option. It was clear after just a few minutes of reading the source that we just needed to do three things:

1. Specify the `go_type` we want (e.g. "string" instead of `sql.NullString`)
2. Set `nullable: true`
3. Set `pointer: true`

Here's the code:

```yaml
overrides:
  - db_type: "text"
    nullable: true
    go_type:
      type: "string"
      pointer: true
```

Sometimes you gotta rtfm. Sometimes you gotta suck it up and grep the code.

*btw, [sqlc](https://sqlc.dev/) is awesome and if you like Go you should be aware of it.*
