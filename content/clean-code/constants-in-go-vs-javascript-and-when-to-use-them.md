---
title: "The Nuances of Constants in Go; Go Isn't JavaScript"
author: Lane Wagner
date: "2020-10-22"
categories: 
  - "clean-code"
  - "golang"
  - "javascript"
images:
  - /img/800/The-Nuances-of-Constants-in-Go-Go-Isnt-JavaScript.webp
---

Constants can be confusing and easy to misuse in Go if you are coming from an untyped language. Let's take a look at some of the nuanced details of how they work in Go. It's probably unsurprising, but Go's constants are almost nothing like JavaScript's bastardized version of the concept.

## Go vs JavaScript

Many programming languages support constants, often denoted by the keyword `const`.

Go and JavaScript both declare new constants in the same way:

```
const frameRate = 60
```

### Constants in Go

- Must be able to be assigned at compile time. The value of a `const` can't be the result of a runtime calculation
- Run faster because the compiler can make specific optimizations
- Cannot change. The compiler will not allow them to be re-assigned
- Only work with some types. [Arrays, Slices, Maps, Structs, etc... can't be made constant (or can they?)](/golang/golang-constant-maps-slices/)
- Are not normal Go types unless explicitly assigned as such

### Constants in JavaScript

- Can't be reassigned, but _can_ change. JavaScript's constants are extremely misleading. the `const` keyword does NOT define a constant value. It defines a constant _reference_ to a value.
- If the constant is a type that has inner workings that change, like an array or object then the inner references can be changed.
- Can be assigned using calculated values at runtime, but can't be re-assigned.

The takeaway if you are coming from JavaScript is that Go's constants are just _different_. They deal with compile-time values, not immutable naming.

In Go, constants provide _complete safety_ in regard to the value they hold. They cannot be computed (making them used less often), but are guaranteed to always reference the same value.

In JavaScript, all a `const` does is ensure that the same [name](/clean-code/naming-variables) can't be changed to reference a different variable in the same scope.

## Go's Constants Must Be Assigned At Compile Time

Constants in Go must be assigned _before_ the program runs. All constants are computed and saved when the program compiles using `go build`. Constants can rely on the value of other constants, but not on runtime calculations. For example:

```go
const seconds = 120
const minutes = seconds / 60
```

Works because both values can be known _before_ the program runs. The following will not work:

```go
func addMinutes(minutes int) {
	const more = minutes + 60
	return more
}
```

This won't work because `more` relies on a runtime variable, `minutes`. Keep in mind that this would work in JavaScript because the only rule with constants in javascript is that they can't be reassigned.

## Constants Are Faster

The Go compiler doesn't need to worry about a `const` changing its value, so it can swap every instance of the `const` with an unchanging number. This makes constants slightly faster.

## Numeric Constants are Just Numbers

Numeric constants can be much [larger and have much greater precision](https://blog.golang.org/constants#TOC_8.) than normal variables because they have [arbitrary-precision](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#:~:text=In%20computer%20science%2C%20arbitrary%2Dprecision,memory%20of%20the%20host%20system.). When numeric constants are assigned to a variable they must be able to fit the size of the type they are being assigned to. Take a look at the following examples:

```go
const large = 1e10000
const E = 2.71828182845904523536028747135266249775724709369995957496696763
```

The `large` number can't be printed, but we can still use it in a calculation:

```go
fmt.Println(large) // won't compile

small := (large / 1e9999) // works as expected
fmt.Println(small) // prints 10
```

High-precision floating point numbers like E can still be used but the high precision is lost when assigned to a `float64` or `float32`.

```go
e := math.E
fmt.Println(e)
// prints 2.718281828459045
```

{{< cta1 >}}

{{< cta2 >}}

## Should You Use Constants?

Yes. Constants are safer.

Use constants _wherever possible._ Why would you want to be able to accidentally mutate a value that you know should never change? Let the compiler save you from yourself, and use constants as much as possible.

You may be familiar with the idea that global variables in programming are a bad idea. Variables should typically belong to the smallest scope possible.

Constants in Go don't apply to the global variable rule, there is _nothing wrong_ with declaring global constants. Granted, if the constant is only used in one place, it may make sense to declare it there. The point however remains: **it isn't dangerous to declare constants globally**.

## Declare Multiple Constants as a Block

```go
const (
	pi = 3.14
	timeout = 120 * time.Second
	maxGoroutines = 20
)
```

## Only Some Types Can Be Constant

Numeric, boolean, and string types can all be made constant. This includes things like runes, floats, integers, and even custom types that are based on valid underlying types. For example:

```go
type myString string

const lane myString = "wagslane"
```

Other types like arrays, slices, and maps can not be declared as constant. This makes sense because those types are essentially just pointers, which are addresses of mutable data. However, I have written [another article on the elegant ways to get "effectively constant" slices and maps in Go](/golang/golang-constant-maps-slices/).

By contrast, in JavaScript, _anything_ can be made constant. JavaScript arrays can be declared as constant, but it doesn't stop the programmer from mutating the elements of the array! The only safety JavaScript's `const` provides is that the variable can't be explicitly reassigned.

{{< cta3 >}}

## Constants Are Untyped By Default

In Go, variables can have their typed inferred:

```go
thisIsAString := "@wagslane"
```

Constants, on the other hand, get an untyped flag

```go
const unTypedString = "@wagslane"
```

An untyped string behaves [mostly like a string](https://blog.golang.org/constants#TOC_4.). That is, it's a string type, but doesn't have a Go value of type **string**. To give it the official Go type of string, it must be declared:

```go
const typedString string = "@wagslane"
```
