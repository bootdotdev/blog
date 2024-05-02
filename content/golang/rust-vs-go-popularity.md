---
title: "Rust vs Go - Which Is More Popular?"
author: Lane Wagner
date: "2020-05-06"
categories: 
  - "golang"
  - "rust"
images:
  - /img/800/Rust_Vs._Go.webp
---

Go and Rust are two of the hottest compiled programming languages, but which is more popular, Go or Rust?. I develop in Go full-time and love it, and I'm learning more about Rust recently - it's an exciting language. Let's explore some differences between the two and look at which is growing faster in the popularity polls.

## Popularity Stats

According to the StackOverflow [2019 surveys](https://insights.stackoverflow.com/survey/2019#technology-_-programming-scripting-and-markup-languages), Go is ahead in the polls when it comes to programming and markup languages.

![](/img/800/Screen-Shot-2020-05-05-at-8.07.37-PM-815x1024.png)

However, compare that to the previous year:

![](/img/800/Screen-Shot-2020-05-05-at-8.15.06-PM-880x1024.png)

Rust **wasn't even on the chart** just one year before.

Go did grow by an impressive 1.6%, but it would seem Rust might be growing even faster as a percentage over time.

Some more supporting evidence for the hypothesis that Rust is growing faster is another poll - [the most loved languages survey](https://insights.stackoverflow.com/survey/2019#technology-_-most-loved-dreaded-and-wanted-languages):

![](/img/800/Screen-Shot-2020-05-05-at-8.18.40-PM-747x1024.png)

Rust is a clear leader here, but Go isn't far behind. There is a lot of hype around Rust right now, for good reason.

Let's take a look at the most dreaded languages:

![](/img/800/Screen-Shot-2020-05-05-at-8.19.08-PM-725x1024.png)

No one dreads Rust. I suspect that a contributing factor is that Rust isn't used much yet. That said, the data indicates that Rust is currently more loved and less dreaded. Hard to argue with that.

Go actually makes the most dreaded chart, but close to the bottom. I suspect most of the hate is salty Java devs that have been forced to move to Go and give up their precious objects. They had to give up generics as well up until now, but we'll have [generics in Go](/golang/how-to-use-golangs-generics/) in 1.18.

## So Which Is Better?

I don't think one is strictly better than the other, and a lot comes down to preference. Let's examine the claims made by the maintainers:

![](/img/800/Golang-1024x578.png)

> Go is an open-source programming language that makes it easy to build simple, reliable, and efficient software.
> 
> [golang.org](https://golang.org/)

![](/img/800/rust-social.jpg)

> A language empowering everyone to build reliable and efficient software.
> 
> [rust-lang.org](https://www.rust-lang.org/)

Based on their official headlines it would seem they are in direct competition. The key difference is that Go also aims to be **simple**. Rust makes no such claim.

Here are my current fast and loose opinions on the strengths and weaknesses of each:


<div class="tablewrap">

|                          |     |      |
| ------------------------ | --- | ---- |
|                          | Go  | Rust |
| Speed                    | ✅✅  | ✅✅✅  |
| Memory Safe              | ✅✅✅ | ✅✅✅  |
| Simple                   | ✅✅✅ | ✅    |
| Standard Library         | ✅✅✅ | ✅✅   |
| Memory Optimized         | ✅✅  | ✅✅✅  |
| Support/Community        | ✅✅  | ✅    |
| Concurrency (Simplicity) | ✅✅✅ | ✅    |

</div>

Lane's Sloppy Rust vs Go Comparison

I think **Go will likely be the go-to for performant backend systems**. Go's rich standard library and easy concurrency makes standing up HTTP servers or other networked services simple and easy. Go is also faster, safer, and less memory intensive than most of the legacy competition. For example, Go is less memory intensive than Java and C#, faster than Python and Ruby, and safer than C++.

Rust seems like it may steal some of the spotlights from Go in **deeper backend processes** that need to get every ounce of efficiency that they can from the hardware. In microservices and polyglot architectures, it makes sense to mix and match technologies behind the scenes a bit.

Even more important than web programming for Rust, I see it being used for more **systems-level applications**. Rust could easily steal some business from C and C++ for uses in embedded devices, command-line utilities, and so forth.
