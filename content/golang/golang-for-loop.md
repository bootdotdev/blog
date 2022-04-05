---
title: "All the Ways to Write for Loops in Go"
author: Lane Wagner
date: "2021-04-10"
categories: 
  - "golang"
images:
  - /img/loop-architecture.webp
---

A for loop executes a block of code repeatedly, and in Golang, there are several different ways to write one.

## #1 The standard three-component loop

Go has fairly standard syntax for the three-component loop you're used to from C, Java, or JavaScript. The big difference is the lack of parentheses surrounding the components.

```go
for i := 0; i < 100; i++ {
    sum += i
}
```

The three components are:

- The init statement, `i := 0`
- The condition, `i < 100`
- The post statement, `i++`

The compiler executes the for-loop in the following manner:

1. The `init` statement executes and variables declared there are made available to the scope of the loop's body.
2. The condition is computed. If it evaluates to `true` then the body runs, otherwise the loop is complete.
3. The `post` statement runs.
4. Back to step #2

## #2 For-range loop

More often than not, you'll be looping over a collection of items like a `map`, `slice`, `channel`, or `string`. While you _can_ use a traditional three-component loop, Go makes it easier by providing the `range` keyword.

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

## #3 While loop

By using one component in a for-loop signature rather than three, we can effectively build a while-loop in Golang. There is no `while` keyword in Go.

```go
sum := 1
for sum < 10 {
    sum += sum
}
fmt.Println(sum)
```

{{< cta1 >}}

## #4 Optional components loop

Building on the idea of a flexible for-loop, we can omit the init or post statements of the three-component loop as we please.

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

This can be a useful pattern when you want something like a [do-while, or an immediate first tick from a ticker.](/golang/range-over-ticker-in-go-with-immediate-first-tick/)

## #5 Infinite loop

Infinite loops are useful within goroutines when you have a worker or process that should continue perpetually.

```go
sum := 0
for {
    sum++ // repeated forever
}
// never reached, loops continues on forever
```

{{< cta2 >}}

## #6 Break from a loop

Breaking early from a loop can be useful, especially in a forever loop. The `break` keyword will exit the loop immediately.

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

It can be useful to skip to the next iteration of a loop early. This can be a good pattern for [guard clauses](/clean-code/guard-clauses/) within a loop.

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
