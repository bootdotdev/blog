---
title: "For Loops in Go"
author: Lane Wagner
date: "2021-04-10"
lastmod: "2022-10-12"
categories: 
  - "golang"
images:
  - /img/800/gopher-on-a-loopy.png.webp
---

For loops are a programmer's best friend! They allow us execute blocks of code repeatedly and iterate over collections of items. In Go, there are several different ways to write one.

## #1 The standard 3-component loop

```go
// prints numbers 0 -> 99
for i := 0; i < 100; i++ {
    fmt.Println(i)
}
```

The 3 components of a for loop in Go are:

* The init statement, `i := 0`
* The condition, `i < 100`
* The post statement, `i++`

Here's how the Go compiler executes for-loops:

1. The `init` statement declares variables which are then available to the scope of the loop's body.
2. The `condition` is computed. If it evaluates to `true` then the body runs, otherwise the loop is complete.
3. The `post` statement runs.
4. Back to step #2

> Observe: Go's loop syntax looks similar to that of C, Java, or JavaScript. The biggest difference is the simple lack of parentheses surrounding the components. 

## #2 For-range loop

I've found that I'm rarely using Go's standard loop syntax, because I'm usually looping over a collection of values. If you need to iterate over a `map`, `slice`, `channel`, or `string`, Go makes it easy with the `range` keyword.

### Range over a slice in Go

```go
fruits := []string{"apple", "banana", "pear"}
for i, fruit := range fruits {
    fmt.Println(i, s)
}

// prints:
// 0 apple
// 1 banana
// 2 pear
```

### Range over a map in Go

```go
ages := map[string]int{
    "lane":    26,
    "preston": 28,
    "rory":    21,
}
for name, age := range ages {
    fmt.Println(name, age)
}

// prints:
// lane 26
// preston 28
// rory 21
```

### Range over a channel in Go

```go
ch := make(chan int)
go func() {
    for i := 0; i < 3; i++ {
        ch <- i
    }
    close(ch)
}()

// loop ends when channel is close
for value := range ch {
    fmt.Println(value)
}
fmt.Println("channel closed")

// prints:
// 0
// 1
// 2
// channel closed
```

### Range over a string in Go

```go
name := "lane"
for i, char := range name {
     // cast the rune to a string for printing 
     fmt.Println(i, string(char))
}

// prints
// 0 l
// 1 a
// 2 n
// 3 e
```

## #3 While loop in Golang

*While loops don't exist in Go!* However, by modifying a for loop we can get the same functionality.

```go
sum := 1
for sum < 10 {
    sum += sum
}
fmt.Println(sum)
```

In other words, a `for` loop in Go without an `init` or `post` statement is equivalent to a `while` loop in other languages.

## #4 Optional components loop

Building on the idea of a flexible for-loop, we can omit the `init` or `post` statements of the three-component loop as we please.

```go
i := 0
for ; sum < 1000; i++ {
    sum += i
}

for i := 0; sum < 1000; {
    sum += i
    i++
}
```

This can be a useful pattern when you want something like a [do-while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while), or an [immediate first tick from a ticker.](/golang/range-over-ticker-in-go-with-immediate-first-tick/)

## #5 Infinite loop

Infinite loops are useful when you have a worker or process that need to run forever, like a [web crawler](https://boot.dev/build/link-analyzer).

```go
sum := 0
for {
    sum++ // repeated forever
}
// never reached, loops continues on forever
```

## #6 Break from a loop

Breaking early from a loop can be useful, especially in an infinite loop. The `break` keyword will exit the loop immediately.

```go
sum := 0
for {
    sum++
    if sum >= 1000 {
        break
    }
}
fmt.Println(sum)

// prints:
// 1000
```

## #7 Continue (skip to the next iteration) in a loop

It can be useful to skip to the next iteration of a loop early. I do this all the time to create [guard clauses](/clean-code/guard-clauses/) within a loop.

```go
for i := 0; i < 10; i++{
    if i % 2 == 0 {
        continue
    }
    fmt.Println(i, "is odd")
}

// prints
// 1 is odd
// 3 is odd
// 5 is odd
// 7 is odd
// 9 is odd
```
