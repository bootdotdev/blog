---
title: "How to Create Constant Maps, Slices, & Arrays in Golang"
author: Lane Wagner
date: "2019-10-21"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/Constant-Maps-and-Slices-1.webp
---

For the most part, I've found that Go developers are pretty good at using global constants for configuration rather than global variables.

However, a problem arises when we want a constant version of some of the more complex types. The Go compiler does not allow us to [create array, map, or slice](/golang/golang-make-maps-and-slices/) constants. After realizing this, many developers decide to use a dangerous global variable.

In this article, we will explore some alternative options to effectively make constant maps, slices, and arrays, albeit with some trade-offs.

## Spoiler - TL;DR

If you're looking for a quick answer: Go doesn't support `const` arrays.

It also doesn't support constant maps, slices, or other complex types. From the official [specification](https://golang.org/ref/spec#Constants):

> There are _boolean constants_, _rune constants_, _integer constants_, _floating-point constants_, _complex constants_, and _string constants_. Rune, integer, floating-point, and complex constants are collectively called _numeric constants_.

The solution, which I explain in more detail later, is to use initialization functions. While of course the variables once created are still changeable, at least you can always get a new copy with the guarantee that it has the correct values.

### Example of const array in Go

```go
func getArray() [5]int {
    return [5]int{10, 20, 30, 40, 50} 
}
```

### Example of const slice in Go

```go
func getSlice() []string {
    return []string{"hello", "world"}
}
```

### Example of const map in Go

```go
func getMap() map[string]int {
    return map[string]int{
        "truck": 5,
        "car": 7,
    }
}
```

With the quick answer out of the way, let's explore why this is a good solution in many cases.

## A Brief Refresher on Globals and Constants

```go
package foo

// this is a global constant
const safeRateLimit = 10

// this is a global variable
var dangerousRateLimit = 10
```

When setting configuration globals, which should be read-only, there's **no good reason to use a global variable**. By using a variable instead of a constant you:

- Open up the potential for bugs when you or someone else accidentally mutates the value
- Confuse future developers who assume the value is _supposed_ to change

Most people already know this about global variables thankfully, and switching global variables to global constants is a fairly straightforward task.

{{< cta1 >}}

## What If I Want A Global Array, Map, or Slice?

![global slice](/img/800/Screen-Shot-2019-10-21-at-7.50.41-AM.png)

Let's assume the following situation:

We have a program that needs two sets of configurations. The configurations are:

- A list of supported social media networks
- A rate limit for making API calls to the networks (we assume they all have the same rate limit)

Now that we know a bit about the configurations we make the following decisions:

- Because these configurations will not change based on the environment the program is running in, we elect to set the values in code rather than using environment variables
- Since they are needed in many places in the app, we choose to scope them globally, instead of passing them into 20+ functions
- Because they should not change during the execution of the program, we decide to make them constant

We then write the following code:

```go
package main

const rateLimit = 10

const supportedNetworks = []string{"facebook", "twitter", "instagram"}
```

Much to our surprise, when we try to compile this code we get the following error:

const initializer \[\]string literal is not a constant

[Unlike constants in JavaScript](/clean-code/constants-in-go-vs-javascript-and-when-to-use-them/), Go doesn't allow complex types like slices, maps, or arrays to be constant! Our first instinct may be to lazily switch it to a variable, and add a comment:

```go
package main

const rateLimit = 10

// this is meant to be constant! Please don't mutate it!
var supportedNetworks = []string{"facebook", "twitter", "instagram"}
```

Whenever we find ourselves leaving comments like this, we should be aware we are doing something **wrong**.

## The Better Solution for Constants in Go

It's much better to use an initializer function (not to be confused with Go's conventional [init()](https://golang.org/doc/effective_go#init) function). An initializer function is a function that simply declares something and returns it. Like I explained above in the tl;dr a good solution to our problem would be as follows:

```go
package main

const rateLimit = 10

func getSupportedNetworks() []string {
	return []string{"facebook", "twitter", "instagram"}
}
```

Now, anywhere in the program, we can use the result of `getSupportedNetworks()` and we know that there is no way we can get a mutated value.

Obviously one of the biggest downsides to this approach is that to get a new copy of the configuration you're literally creating a new copy and making a function call. In the vast majority of cases this should be fine - if it's truly just a configuration you probably won't need to be accessing it all the time. That said, if you're rapidly making new copies it could become a performance issue.

## Good Practices

Being able to keep access to maps and slices that are effectively constant can make your code easier to read, and more importantly, much less error-prone. One of the most sought-after traits of a [computer scientist](/computer-science/comprehensive-guide-to-learn-computer-science-online/) for [high-end coding jobs](/computer-science/highest-paying-computer-science-jobs/) is the ability to read, write, and refactor code so that it's more maintainable and easier to understand.
