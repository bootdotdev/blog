---
title: "Make Maps and Slices in Golang - A Guide to Initialization"
author: Lane Wagner
date: "2020-06-29"
categories: 
  - "clean-code"
  - "golang"
---

There are quite a few ways to create new maps and slices in Go, for example, they can both be initialized using the `make()` function, the `new()` function, as literals, or by using the `var` keyword. With so many choices, which option is best? Or perhaps better asked, which one is best in your situation? Let's take a look.

## Slices

```go
var varStyle []string

literalStyle := []string{}

newStyle := new([]string)

makeStyle := make([]string, 0)
```

`var varStyle []string` is the idiomatic way to declare an _empty_ slice. The slice is actually `nil`, which means it will be `null` when [marshalled to JSON](https://qvault.io/golang/json-golang/) and will succeed nil checks.

`literalStyle := []string{}` should probably only be used when the literal is going to **start with values in it**, as in `literalStyle := []string{"cat", "dog", etc}`. Otherwise prefer `make()`

`newStyle := new([]string)` returns a pointer to the slice. Same as `ptrStyle := &[]string{}`. **Only use if you want a pointer.**

`makeStyle := make([]string, 0)` is the same as the literal style, but is preferred for idiomatic reasons when the **slice doesn't need non-zero starting values**. Make() allows the slice to be initialized with a starting length and capacity, which can have good performance implications in some circumstances:

**makeStyle := make(\[\]string, len, cap)**

## Maps

```go
var varStyle map[int]int

literalStyle = map[string]int{}

newStyle := new(map[string]int)

makeStyle := make(map[string]int)
```

`var varStyle map[int]int` creates a nil map. Writing (but not reading interestingly enough) will cause a panic. You probably don't want a nil map.

`literalStyle := map[string]int{}` using the literal syntax is just fine, though idiomatically it's probably best to use a make function. Developers are more used to seeing a make function and make offer some additional features.

`newStyle := new(map[string]int)` creates a pointer to a nil map... very often not what you want.

`makeStyle := make(map[string]int)` _This is probably what you want_! If you know your space requirements you can optimize for allocation by passing in a size:

```go
// Give me a map with room for 10 items before needing to allocate more space
makeStyle := make(map[string]int, 10)
```

Check out our [How To: Global Constant Maps and Slices](https://qvault.io/2019/10/21/how-to-global-constant-maps-and-slices-in-go/) article if you want to learn more about the proper use of maps and slices in Go.
