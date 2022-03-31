---
title: "Top 8 Benefits of Functional Programming"
date: "2021-02-25"
categories: 
  - "clean-code"
author: Lane Wagner
images:
  - /img/calculus-on-a-chalkboard.webp
---

Functional programming is a way to writing code where programs are created strictly through functions. Functional programming has gained quite a bit of traction in recent years among the development community, mostly because of the benefits it provides.

Functional programming is a declarative way to write provably correct code. Function definitions are expressions that simply map inputs to outputs, rather than a sequence of statements that update the state of the application.

Let's jump right into the top 8 reasons you should look into a functional style of coding, or perhaps switching to a completely functional programming language.

## Functional Programming Benefits

- [Functional Programming Benefits](#functional-programming-benefits)
  - [1\. Pure functions are better than impure functions](#1-pure-functions-are-better-than-impure-functions)
  - [2\. Pure functions are easier to test](#2-pure-functions-are-easier-to-test)
  - [3\. Functional programming leads to fewer bugs](#3-functional-programming-leads-to-fewer-bugs)
  - [4\. Functional code tends to have its state isolated, making it easier to comprehend](#4-functional-code-tends-to-have-its-state-isolated-making-it-easier-to-comprehend)
  - [5\. Function signatures are more trusted](#5-function-signatures-are-more-trusted)
  - [6\. Concurrency is more easily kept safe](#6-concurrency-is-more-easily-kept-safe)
  - [7\. Recursion is simpler, though not necessarily easier to learn](#7-recursion-is-simpler-though-not-necessarily-easier-to-learn)
    - [Imperative power function](#imperative-power-function)
    - [Functional power function](#functional-power-function)
  - [8\. Immutable variables lead to fewer side-effects](#8-immutable-variables-lead-to-fewer-side-effects)
- [Which languages are purely functional programming languages?](#which-languages-are-purely-functional-programming-languages)

### 1\. Pure functions are better than impure functions

A [pure function](https://qvault.io/2020/09/07/how-to-make-pure-functions-in-go/) is a function that has both of the following properties:

- Its return value is the same for the same arguments (no variation with local static variables, non-local variables, mutable reference arguments, or input streams from I/O devices).
- Its evaluation has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or I/O streams).

Because pure functions ensure that the state of the outside program isn't altered, they are strictly better to write than impure functions where possible. In some cases an impure function is necessary however, for example, if you need to make a network call, interact with a database, or print data to the console.

### 2\. Pure functions are easier to test

![](/img/testing-in-bio-lab-300x204.jpeg)

Pure functions are very easy to test for a couple reasons:

- The outputs are always the same for any given inputs. This ensures determinism and predictability.
- Pure functions don't depend on any state apart from the inputs, so there should be no scaffolding necessary to write a good test suite.

Because testing is so important in programming, it's really nice when we make it easier to write tests because it encourages us to write more of them. By utilizing pure functions as much as possible, you'll notice your programs will have more robust test harnesses.

### 3\. Functional programming leads to fewer bugs

Debugging and writing code with fewer bugs becomes quite a bit easier with pure functions. Because each function is simply a mapping of inputs to outputs, a simple stack trace or print statement at each level will reveal with problem. With imperative paradigms, you could have shared or mutable state almost anywhere else in the codebase that's potentially causing the bug.

### 4\. Functional code tends to have its state isolated, making it easier to comprehend

Let's take a look at the [Elm architecture](https://guide.elm-lang.org/architecture/) as an example. Elm is a purely functional programming language used to render webpages on the front end of an application.

![](/img/elm-architecture-300x230.jpg)

The Elm code is purely functional. It takes "state" as an input and converts it into the HTML that will render on the page. Whenever the user interacts with the page, the state is updated _outside_ of the Elm code. That state is then fed back into the Elm code and a new HTML output is produced.

As you may have realized, the stateful part of the system is not purely functional, the good news is it's so simple that there are unlikely to be bugs there. The Elm code that does the bulk of the work is purely functional however, so all the benefits are reaped by the majority of the codebase.

### 5\. Function signatures are more trusted

Examine the following Go code:

```go
var radius = 2.0

func areaOfCircle() float64 {
    return 3.14 * radius * radius
}
```

Technically this code will work. As long as everywhere I calculate the area of a circle I first update the global `radius` variable I'll get the correct output. the problem is that examining the signature of the function doesn't give the whole story. A pure function will have a signature that tells you all you need to know about its usage.

```go
// we don't know which circle's area is being computed, there's no explicit input
func areaOfCircle() float64
```

We can fix the problem by making the function pure:

```go
func areaOfCircle(radius float64) float64 {
    return 3.14 * radius * radius
}
```

### 6\. Concurrency is more easily kept safe

Pure functions are definitionally thread-safe. Code is thread-safe when we can guarantee that no two concurrent processes will be trying to access the same data at the same time. This is called a race condition and is one of the hardest kinds of bugs to pin down. Because pure functions never share state with other sections of a program they can't have race conditions.

For example, take the code from above again.

```go
var radius = 2.0

func areaOfCircle() float64 {
    return 3.14 * radius * radius
}
```

If two separate threads ([goroutines](https://qvault.io/2020/05/11/concurrency-in-rust-can-it-stack-up-against-gos-goroutines/)) are accessing the `areaOfCircle` function at the same time and altering the value of `radius`, one process could easily overwrite the other's value of radius and one thread ends up with the output that was intended for the other thread.

### 7\. Recursion is simpler, though not necessarily easier to learn

If you've ever tried to write an interpreter for a programming language, you've realized that recursion is a fairly easy concept to implement, at least when compared to imperative ideas like for-loops. Recursion simply requires that functions are able to call themselves, the rest is up to the developer. For-loops require a bunch of custom code in the interpreter or compiler that does the initialization, checks the end condition, executes the body, then finally executes the update statement.

```go
for (initialization; condition; update) {
    // body of for loop, executed once per iteration
}
```

I'll readily admit that while recursion is simpler, it's often harder for new programmers to wrap their heads around. Take a look at the following examples of a `pow` function that computes the result of `x` raised to the `n` power.

#### Imperative power function

```js
function pow(x, n) {
    let res = 1;
    for (let i = 0; i < n; i++) {
        res *= x;
    }
    return res;
}
```

#### Functional power function

```js
function pow(x, n) {
    if (n === 1) {
        return x;
    }
    return x * pow(x, n - 1);
}
```

### 8\. Immutable variables lead to fewer side-effects

The data inside functional program's functions is immutable. We can always create new variables and data structures but we aren't allowed to modify the existing values.

If every value in a program is only assigned once, it's easy to read the code and determine what the value is at any given point. If instead the named values are allowed to be updated it can be quite a bit harder to see what's going on at different lines in the code. In short, immutability makes programs much simpler and improves developer speed.

With that in mind, there are instances where immutability is a bad idea. This is most prevalent when your application needs to be performant and is continuously updating a value. Imagine a video game where your character's size is constantly fluctuating. It would be quite a computational burden to deallocate the entire character and re-create them each time the size changes. In this situation, it's probably worth the trade-off to use mutable data.

## Which languages are purely functional programming languages?

The following languages support purely-functional styles. In other words, the language will enforce the rules of functional programming:

1. [Haskell](https://www.haskell.org/)
2. [Clojure](https://clojure.org/)
3. [Scala](https://www.scala-lang.org/)
4. [PureScript](https://www.purescript.org/)
5. [Elm](https://elm-lang.org/)

Additionally, most general-purpose programming languages like Go, JavaScript, and Python will allow you to write functional programs, but won't force you to do so.
