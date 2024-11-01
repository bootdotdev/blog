---
title: "How to Create Constant Maps, Slices, & Arrays in Golang"
author: Lane Wagner
date: "2019-10-21"
lastmod: "2022-10-01"
categories:
  - "clean-code"
  - "golang"
images:
  - /img/800/howtocreatemaps.png.webp
imageAlts:
  - "Making maps, slices, and arrays in GoLang is as easy as making maps, slices, and arrays in GoLang"
---

**The quick answer is that Go does not support constant arrays, maps or slices.** However, there are some great workarounds.

For the most part, I've found that [developers learning Go](https://www.boot.dev/courses/learn-golang) for the first time are pretty good at using global _constants_ for configuration values rather than global _variables_. However, a problem arises when we want a constant version of some of the more complex types. The Go compiler does not allow us to [create array, map, or slice](/golang/golang-make-maps-and-slices/) constants. After realizing this, many developers decide to use a dangerous global variable.

In this article, we will explore some alternative options that allow us to make a _form_ of constant maps, slices, and arrays, albeit with some trade-offs. Please don't use global variables if you can avoid them!

## So if Go doesn't support these types of constants, what is the best alternative?

The solution is to use _initialization functions_. While slices, maps, and arrays once created are still able to be mutated, at least you can always get a new _copy_ by re-calling the initialization copy. The new copy is guaranteed to contain the original values.

### Example of const array in Go

```go
// An initialization function that creates
// and returns a new copy of an array
func getArray() [5]int {
    return [5]int{10, 20, 30, 40, 50}
}
```

```go
// A mutable array of size 3
var nums = [3]int {10, 20, 30}
```

```go
// A mutable array of size 3,
// but with syntactic sugar that relies on
// the compiler to compute the length
var nums = [...]int {10, 20, 30}
```

### Example of const slice in Go

```go
// An initialization function
// that creates a new slice of strings
func getSlice() []string {
    return []string{"hello", "world"}
}

// A mutable slice of strings
var msgs = []string{"hello", "world"}
```

### Example of const map in Go

```go
// An initialization function
// that creates a map
func getMap() map[string]int {
    return map[string]int{
        "truck": 5,
        "car": 7,
    }
}
```

With the quick answer out of the way, let's explore why initialization functions are our best bet.

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

## What happens if I try to use a constant array, map, or slice?

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

It's much better to use an initializer function as we talked about above (not to be confused with Go's conventional [init()](https://golang.org/doc/effective_go#init) function). An initializer function is a function that simply declares something and returns it. Like I explained above, a good solution to our problem would be as follows:

```go
package main

const rateLimit = 10

func getSupportedNetworks() []string {
	return []string{"facebook", "twitter", "instagram"}
}
```

Now, anywhere in the program, we can use the result of `getSupportedNetworks()` and we know that there is no way we can get a mutated value.

Obviously one of the biggest downsides to this approach is that to get a new copy of the configuration you're literally creating a new copy and making a function call. In the vast majority of cases, this should be fine - if it's truly just a configuration you probably won't need to be accessing it too often. That said, if you're rapidly making new copies constantly the extra memory overhead could become a performance issue.

## Good Practices

Being able to access to maps and slices that are _effectively_ constant makes your code easier to read, and more importantly, less error-prone. One of the most sought-after traits of a [computer scientist](/computer-science/comprehensive-guide-to-learn-computer-science-online/) for [high-end coding jobs](/computer-science/highest-paying-computer-science-jobs/) is the ability to read, write, and refactor code so that it's more maintainable and easier to understand.

## Are you _sure_ that Go doesn't support constant maps slices and arrays?

Yes. From the official [specification](https://golang.org/ref/spec#Constants):

> There are _boolean constants_, _rune constants_, _integer constants_, _floating-point constants_, _complex constants_, and _string constants_. Rune, integer, floating-point, and complex constants are collectively called _numeric constants_.
