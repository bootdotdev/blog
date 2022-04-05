---
title: "Don't Go To Casting Hell - Use Default Native Types in Go"
author: Lane Wagner
date: "2020-05-21"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/hrll.webp
---

Go is strongly typed, and with that, we get many options for simple variable types like integers and floats. The problem arises when we have a _uint16_, and the function we are trying to pass it into takes an `int`. We find code riddled with `int(myUint16)` that can become slow and annoying to read. In other words, when Go developers stray from the "default" type for any given type family, the code can get messy quickly.

## Go's Basic Types

```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```

There are 5 different types that can represent an integer, 5 types for an unsigned integer, 2 for a float, and 2 for a complex number. While it's hard to defend the notion that the compiler itself has default types, the standard library certainly plays favorites.

For example, the [cmplx](https://golang.org/pkg/math/cmplx/) package which does math with complex numbers accepts and returns exclusively _complex128_.

With floats, the vast majority of the [math](https://golang.org/pkg/math/) package has function signatures using _float64_. In the same package ints are usually just the _int_ type, and unsigned integers are typically _uint32_.

These are what I've come to refer to as the "default native types":

```
bool

string

int

uint32

byte

rune

float64

complex128
```

{{< cta1 >}}

## Why Do We Care About Defaults?

There is a good reason that the majority of code uses these values. In all of the above cases, the choice of specific sub-types are based on range and precision. `int8` can store values between `-128` and `127`, while `int64` ranges from `-9,223,372,036,854,775,808` to `9,223,372,036,854,775,807. At the same time, int8` uses a single byte while `int64` uses 8x that.

The defaults above were chosen in the standard library (and by the vast majority of Gophers) because they are the common-sense, works-most-of-the-time, big-enough-range values. Exposing a [rounding function](https://golang.org/pkg/math/#Round) for _float32_ simply won't be as useful as _float64_. It can't be used by as many values.

```go
func Round(x float64) float64
```

If you have a float32 that you want to round, you first need to cast it:

```go
math.Round(float64(myFloat32))
```

This is not only slow but clunky to read. Type conversions take time. Memory must be allocated. My advice is to use the default type (_float64_ in the case of floats) in your applications unless you have a compelling reason not to.

## When Not To Use Default Types

Performance and Memory.

That's about it. The only reason to deviate from the defaults is to squeeze out every last bit of performance when you are writing an application that is resource-constrained. (Or, in the special case of uint64, you need an absurd range of unsigned integers).

For example, I probably wouldn't swap out a single _uint32_ for _uint8_, even if I was certain I would only need 8 bytes. However, If I have a slice of uints that can potentially hold thousands of values, I may see a significant memory savings by doing a few type conversions and using _uint8_.

A few good examples of this are the packages I maintain, [go-tinydate](https://github.com/lane-c-wagner/go-tinydate), and [go-tinytime](https://github.com/lane-c-wagner/go-tinytime). Usually, I encourage users NOT to use them, and to just use the [default time.Time](/golang/golang-date-time/). However, in my backend career, there have been applications that went from using 16GB of RAM down to less than 4GB by making the swap to TinyDate or TinyTime.

## Use Defaults

Make your life and the lives of your coworkers easy. Use the defaults unless you have a very compelling reason not to.
