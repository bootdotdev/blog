---
title: "Programming types and (incorrect) mindsets"
author: Lane Wagner
date: "2023-05-08"
categories: 
  - "clean-code"
images:
  - /img/800/rubberduckfantasy.webp
---

DHH, the creator of Ruby on Rails, Hey, Basecamp, and a few other things, recently wrote an article titled "[Programming types and mindsets](https://world.hey.com/dhh/programming-types-and-mindsets-5b8490bc)", and I just *have* to chime in on this one.

I thought we'd moved past this by now. A decade or so ago, it seemed like there was healthy banter about the pros and cons of dynamically typed vs statically typed languages, and genuinely interesting discussions about the tradeoffs took place. My perception, and certainly my belief at present is this:

> There are effectively no good arguments for a dynamic type system

"Hmm..." you might say. "That's not a very balanced take Lane." Agreed. DHH might even say that I'm expressing "utter disbelief that the other side might hold a reasonable position".

I actually would *love* to hear some good reasons in support of the idea that dynamic typing helps *in any way*. Unfortunately, I don't see any concrete arguments in the original essay apart from statements like:

> It [dynamic typing] allows the poetic syntax that results in such beautiful code

To be fair, making arguments may not be the point of DHH's article in the first place. It seems to be more about his mindset of "to each their own, I like my dynamic typing."

## Steelmanning the dynamic typing argument

I've gone to external resources to try to find some arguments for dynamic typing. I've found a few, but I think they're generally bad arguments, or worse, they actually deal with something tangential to the type system itself. Let's jump in.

## Argument 1. Simpler syntax

> Dynamically typed languages often have simpler syntax and less boilerplate code

True. I choose to start developers with Python on [Boot.dev](https://boot.dev) because I think it has such a simple syntax that it makes for an amazing environment in which to learn programming.

But that's *despite* the dynamic typing, not *because* of it.

With languages that support type inference, 80% of the "boilerplate" code is just gone. In Python, we have:

```py
x = 1
```

and in Go, we have:

```go
x := 1
```

The difference is that in the Go version, if I later try to use `x` as a string, or I pass it into a function that expects a non-integer, I'll be warned *before* I run my code.

I think is an outdated argument, and it originates from back when good type inference wasn't as common.

Now, type inference does *not* eliminate the "boilerplate" syntax that is actually useful, namely, *function signatures*. For example, in Python, we have:

```py
def increment(x):
    return x + 1
```

and in Go, we have:

```go
func increment(x int) int {
    return x + 1
}
```

I'm sorry, but my take here is that if you're not interested in declaring to the world the expected inputs and outputs of your functions, *you're not interested in writing code that can be easily understood and maintained by humans*. In the dynamically typed world, the solution to this is to write more external documentation and add comments. I'd rather have my tooling be able to tell me what's going on from within my editor.

### Argument 2. Enhanced productivity

> Due to their flexibility and ease of use, dynamically typed languages can lead to increased productivity for certain tasks or projects, especially when rapid development or prototyping is crucial.

It's true that certain languages "get out of your way" and can make certain tasks a bit easier. I need to parse a CSV? I'm probably whipping out Python. But that's not *because* it's a dynamically typed language. It's because:

* The syntax reads like English
* It's interpreted and therefore has no compilation step
* It has an amazing wealth of libraries for those kinds of tasks

There's no *fundamental reason* that this syntax couldn't work with type safety:

```py
for car in cars:
    # use car here
```

Python has great enumeration syntax, and Python is dynamically typed, but those two things aren't strictly dependent on each other.

And to be honest, I do find myself writing more and more CLI "scripts" in Go these days because compile times are so short, and yet I still get the benefits of a statically typed language.

### Argument 3. Duck typing

> Dynamically typed languages often employ duck typing, which allows for more flexible and reusable code

What is duck typing? Well, it's the idea that if something *acts* like a duck, it *is* a duck.

```py
class Mallard():
    def quack(self):
        return "Quack!"

class RubberDuck():
    def quack(self):
        return "Squeak!"
```

Both `Mallard` and `RubberDuck` can now be treated as a "duck" because they can both `.quack()`

```py
def main():
    ducks = [Mallard(), RubberDuck()]
    for duck in ducks:
        print(duck.quack())
```

Yup. Duck typing is *awesome*. But this version of duck typing is just duck typing without any compile-time, or heck, even *tooling*-time support. If I throw a `Tire()` object into my list of `ducks`, I won't know that it doesn't `.quack()` until I run my code and watch it fail. In a statically typed language, I would have been warned *before* I ran my code because I'd be using interfaces to *ensure* that my types can `.quack()`.

### 4. Using the same variable for different types

> In dynamically typed languages, variables can hold values of different types at different times. This flexibility can be useful for certain programming tasks and patterns.

I have nothing to say here. This is just bad practice. In no world should you be changing the *type* of thing a variable holds. I can't think of a better way to write spaghetti code, and hopefully this doesn't need any further explanation.

## Is DHH just wrong?

About typing? I think so. Is he also smarter than me? Likely. Is he more experienced than me? Absolutely.

Here's the thing, I'm not saying Ruby and Python and JavaScript are unusable, or even that they're *worse* languages than all their statically typed counterparts. Every language I've used has things I like, and things I dislike. However, their dynamic nature is certainly a *flaw*, not a *feature*.

All this said, I agree with DHH's point here:

> That's not to say all matters of programming approaches boil down to equal but different mindsets. There are limits to this relativism. But dynamic vs static typing is certain within its confines. So too is functional vs object-oriented programming. Poles on both these axes have shown to deliver excellent software over the decades (and awful stuff too!).

In many, many, *many* cases, the answer truly is that "it depends". OOP vs functional? It depends. Monolith vs services? It depends. Synchronous HTTP call vs async events? It depends.

**Static vs dynamic typing? Almost certainly static.**
