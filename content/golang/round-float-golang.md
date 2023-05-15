---
title: "How to Round a Float in Go"
author: Lane Wagner
date: "2022-11-13"
categories: 
  - "golang"
images:
  - /img/800/round-thing.png.webp
imageAlts:
  - "Generated with Stable Diffusion. Prompt: 'large round thing, dark, 4k, fantasy'"
---

## Round float and format to string

If you're rounding a floating point number in Go, it's most likely you want to format it in a string. Use the built-in [fmt.Sprintf()](https://pkg.go.dev/fmt#example-Sprintf) function.

```go
heightInMeters := 1.76234
msg := fmt.Sprintf("Your height is: %.3f", heightInMeters)
// msg = "Your height is: 1.762"
```

## Round float and store in a float

Use [math.Floor](https://pkg.go.dev/math#Floor), [math.Round](https://pkg.go.dev/math#Round) and [math.Ceil](https://pkg.go.dev/math#Ceil) from the standard [math](https://pkg.go.dev/math) package.

```go
heightInMeters := 1.76234
roundedDown := math.Floor(x*100)/100 // 1.0
roundedToNearest := math.Round(x*100)/100 // 2.0
roundedUp := math.Ceil(x*100)/100 // 2.0
```

## Round float and store in an int

To store the result as an `int`, use the same method as before and then cast the result.

```go
heightInMeters := 1.76234
roundedToNearest := int(math.Round(x*100)/100) // 2
```
