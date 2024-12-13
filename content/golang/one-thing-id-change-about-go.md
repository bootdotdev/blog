---
title: "The One Thing I'd Change About Go"
author: lane
date: "2023-08-12"
categories:
  - "golang"
images:
  - /img/800/wagslane_A_caveman_coder_etching_the_Go_Gopher_into_a_stone_tab_2a1df1e1-429d-429d-b122-e21f1f7a6a3a.png.webp
---

Go is built for grug brained programmers like me.

> grug brain developer not so smart, but grug brain developer program many long year and learn some things although mostly still confused
>
> apex predator of grug is complexity
>
> complexity bad
>
> say again:
>
> complexity _very_ bad
>
> _you_ say now:
>
> complexity _very, very_ bad
>
> given choice between complexity or one on one against t-rex, grug take t-rex: at least grug see t-rex
>
> -- [grugbrain.dev](https://grugbrain.dev/)

The Go team took _many years_ to add generics to the language. It was a good addition, and many argued that it was an _obvious_ decision that should have been made sooner.

I disagree.

The simple truth is that when you're building applications, especially back-end web applications or CLI apps (which is where Go shines as a language imo) you just don't need generics all that often. They're quite nice to have, but far from _necessary_.

Are you building a clever library using general-purpose data structures? Sure, generics make your life much easier. But let's be real, I'm over here parsing JSON and shoveling strings into databases. I don't need 3 layers of abstraction to get 'er done.

_Smol-brain code work gud for application layer._

## What else is Go good for?

Before I start shitting on my favorite language, let me point out some of the other reasons I love Go.

1. Grug-brained syntax (already mentioned)
2. Statically compiled binaries
3. A toolchain with built-in formatting, testing and dependency management
4. Dependency management built on Git repos (no npmjs.com or crates.io)
5. A standard library that cares about the web
6. Goroutines and channels (concurrency that doesn't suck)
7. Fast despite a garbage collector

## What would I change about Go?

Not a hard question. It's sum types! (Or enums, tagged unions, or whatever you want to call them).

Go currently has a shitty excuse for [enums](/golang/golang-enum/):

```go
type Color int

const (
		Red Color = iota
		Green
		Blue
)
```

They're pretty bad. Go's "enums" are verbose, error-prone, and don't ackshually enforce much of anything from a typing perspective. Let me show you what I mean.

### It's just an alias

```go
type Color int
```

This is a type _alias_. At the end of the day, the new `Color` type is just an `int`. It's not really a new _type_, it's just a new _name_ for an existing type. In this world, every integer on God's green Earth is a valid color.

That's crap.

If I wanted that I would just use an `int`.

I want to _restrict_ the set of valid colors to a specific _subset_ of colors, e.g. `Red`, `Green`, and `Blue`.

### iota

The `iota` keyword in Go is a special feature that allows you to define a sequence of constants that increment by `1`. Sound useful? _It's not._ It's just cryptic syntactic sugar.

A smol-brained developer like me might make a few constants like this:

```go
const (
		Red Color = 0
		Green Color = 1
		Blue Color = 2
)
```

But a big-brained developer might save a few characters by using `iota`:

```go
const (
		Red Color = iota
		Green
		Blue
)
```

Here's the kicker: the `iota` method uses the _same_ amount of lines of code, but now I need to count on my fingers and toes to figure out the actual _value_ of any of these constants.

```go
const (
		Red Color = iota
		Green
		Blue
		Grey
		Black
		White
		Yellow
		Orange
		Purple
		Pink
		Brown
		Chartreuse
		Mauve
)
```

_What's the value of `Mauve`?_

Additionally, there isn't even support to quickly marshal these integers into strings (e.g. for debugging) without writing mountains of boilerplate code.

Frankly I just pretend `iota` doesn't exist and instead define string constants like a peasant:

```go
type Color string

const (
		Red Color = "Red"
		Green Color = "Green"
		Blue Color = "Blue"
)
```

### Despite the verbosity, nothing is safe

Believe it or not, I can still do this in Go:

```go
type Color string

var carColor Color = "clearly not a color"
```

The compiler don't care. The `Color` type we made is just an alias for `string`. Any `string` is a valid `Color`. Sure, I defined some constants, `Red`, `Green`, and `Blue`, but they're just constants that I _hope_ and _pray_ and _beg_ my team to use.

I have no way to _enforce_ this stuff at compile time. So now my only choice is to write runtime checks everywhere I use the colors:

```go
switch color {
case Red:
		// do happy thing
case Green:
		// do other happy thing
case Blue:
		// do other other happy thing
default:
		return errors.New("wHY dIDn'T yOU uSe a vALID cOLoR???")
}
```

Eew, *run*time.

If there's one thing I hate more than indenting with spaces it's doing _literally anything_ at runtime.

### How to make Go better

I can't believe I'm using TypeScript as an example of a language that does something _well_, but here we are. In TypeScript, you can define a sum type like this:

```ts
type Color = "Red" | "Green" | "Blue";
```

![Shut up and take my money](/img/800/takemymoney.jpeg.webp)

Look at that. It's simple. It's elegant. It's _safe_.

Sum types provide _more_ type safety, _more_ expressiveness, are _easier_ to understand, all while being _less_ verbose. It's a win-win-win-win. If it weren't for Go's backward compatibility promise (which I love), I'd even rip out the stupid `iota` keyword in addition to adding sum types.

## 🚨🚨 BREAKING: TypeScript snatches defeat from the jaws of victory 🚨🚨

TypeScript did it. They have beautiful beautiful sum types. They're called _unions_ in TypeScript, but they're the same thing.

Then some galaxy-brained 10x developer decided it also needed an `enum` keyword so we'd have 2 ways to accomplish the same thing:

```ts
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT",
}
```

Write Go.

Be grug.

Pray for sum types.
