---
title: "Free Functional Programming Course Released - JavaScript and PureScript"
author: Lane Wagner
date: "2020-10-19"
categories: 
  - "javascript"
---

We just launched our new ["Intro to Functional Programming" course](https://boot.dev/intro-to-functional-programming/), and frankly, I'm a bit exhausted (more on that later). This course is an interactive code-in-the-browser course that teaches the basics of FP in JavaScript and PureScript.

In order to celebrate this launch, we will be offering the course for **free** on signup (using the 250 free signup gems) for the **entire month of October**! Even if you can't take the course this month, be sure to create an account and claim the offer :)

## What's In the Course?

There are 5 modules:

- Recursion
- Pure Functions
- Data Structures
- PureScript
- Higher Order Functions

The goal of the course is to cover the basics of FP in such a way that students can implement the concepts in any language, framework, or even just for theoretical practice. We go over functional versions of various algorithms and data structures, learn the difference between imperative and functional paradigms, and learn to curry functions using PureScript syntax.

The course has ~60 exercises currently, and like all of our courses, we will be adding to it and improving the quality regularly.

{{< cta1 >}}

## What the Hell is PureScript?

[PureScript](https://www.purescript.org/) is a strongly-typed purely functional programming language that compiles to JavaScript. PureScript has a very Haskell-like syntax and you can play around with it on our [PureScript playground here.](https://boot.dev/playground/purescript)

Example PureScript:

```purs
import Prelude
import Effect.Console (log)

greet :: String -> String
greet name = "Hello, " <> name <> "!"

main = log (greet "World")
```

I was originally intending this course to be written completely in JavaScript. The boot.dev platform already supported JavaScript and I thought I would be able to convey all of the basic FP concepts through JS, at least to a satisfactory degree.

_I was wrong._

There are so many concepts that are hard to understand in functional programming if the language allows you to circumvent each rule. For example, in JavaScript you can write an immutable stack by exposing some functions:

```js
function push(stack, s){
    newStack = []
    for (const item of stack){
        newStack.push(item)
    }
    newStack.push(s)
    return newStack
}

function pop(stack){
    newStack = []
    for (const item of stack){
        newStack.push(item)
    }
    newStack.pop()
    return newStack
}

function peek(stack){
  if (stack.length > 0){
      return stack[stack.length-1]
  }
  return null
}
```

The problem is there is nothing stopping another developer (or yourself) from "breaking the rules" and mutating the array later. That's why I decided to teach myself some PureScript and implement it as part of the program!

I still think JavaScript has a useful part to play in the course, however, especially with the popularity of FP in front-end code. For example, take a look at [Ramda](https://ramdajs.com/) and [React Hooks](https://reactjs.org/docs/hooks-intro.html).

Anyhow, be sure to [take a look at the course](https://boot.dev/) and as always let us know how we can improve!
