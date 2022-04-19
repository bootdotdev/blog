---
title: "Top 6 Golang Logging Best Practices"
author: Lane Wagner
date: "2020-01-07"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/photo-1457524461416-8796b6d23efb-e1589473495660.webp
---

Let's discuss a few rules of thumb for logging in Go, as well as some features you may not have heard of that can make debugging easier. Best practices for logging in Go are not so obvious and sometimes we need to look closer to see what is the best choice, considering the unique situation of error handling in Go.

1. Use Errors Where Appropriate, Not Strings
2. Wrap Errors
3. Use Formatters Like fmt.Errorf()
4. Format Structs Where Appropriate
5. Use the variadic forms of functions like fmt.Println()
6. Use the Built-in Log Package

## #1 - Use Errors Where Appropriate, Not Strings

Go has a built-in `error` type, which allows developers to easily differentiate errors from "normal" strings and check to make sure functions exit without a problem in a more explicit way. The `error` type is an [interface](/golang/golang-interfaces/) that simply requires the type in question to define an `Error()` function that prints itself as a string.

```go
type error interface {
    Error() string
}
```

**Never use a normal string where an error is appropriate!** When a string is returned from your function you imply to other developers that when the string isn't empty it's just "business as usual". The `error` type makes it clear that something is wrong when the error isn't `nil`.

For example, let's pretend we have a function that divides two numbers safely and returns a result.

```go
func divide(a, b float64) (float64, string) {
    if b == 0 {
        return 0.0, "can't divide by zero"
    }
    return a / b, ""
}
```

This will work perfectly. In fact, anywhere an error type works a string _could_ be used instead. However, if we're interested in writing code that other developers can more quickly understand and make contributions to, we should use an `error` type:

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0.0, errors.New("can't divide by zero")
    }
    return a / b, nil
}
```

## #2 - Wrap Errors

![Mummy Wrap Errors](/img/800/mummy_0.jpg)

Often times out of laziness we simply pass errors up a call chain. For example, let's look at this function that formats hours and minutes into a time message:

```go
func formatTimeWithMessage(hours, minutes int) (string, error) {
	formatted, err := formatTime(hours, minutes)
	if err != nil {
		return "", err
	}
	return "It is " + formatted + " o'clock", nil
}
```

The problem here is that the `formatTime` function can be called many other places within our application or library. If all we do is pass along the raw error, when the error is eventually printed, it gets really hard to tell where exactly the error originated from. Instead, let's do the following:

```go
func formatTimeWithMessage(hours, minutes int) (string, error) {
	formatted, err := formatTime(hours, minutes)
	if err != nil {
		return "", fmt.Errorf("formatTimeWithMessage: %v", err)
	}
	return "It is " + formatted + " o'clock", nil
}
```

Additionally, if you are working in Go 1.13 or later, then you can look into the more explicit [Unwrap](https://blog.golang.org/go1.13-errors#TOC_3.1.) method for error chains.

## #3 - Use Formatters Like fmt.Errorf()

`[fmt.Errorf()](https://golang.org/pkg/fmt/#Errorf)` is similar to `fmt.Printf()`, but returns an `error` instead of a `string`. You may have done this in the past:

```go
err := errors.New("Bad thing happened! " + oldErr.Error()) 
```

This can be accomplished more succinctly using fmt.Errorf():

```go
err := fmt.Errorf("Bad thing happened! %v", oldError) 
```

The difference in readability becomes even more obvious when the formatting in question is more complicated and includes more variables.

## #4 - Format Structs Where Appropriate

Printing structs can be quite ugly and unreadable. For example, the following code:

```go
func main() {
    make := "Toyota"
    myCar := Car{year:1996, make: &make}
    fmt.Println(myCar)
}
```

Will print something like:

```
{1996 0x40c138}
```

We likely want to get the value in the pointer, and we probably want to see the keys of the struct. So we can implement a default `String()` method on our struct. If we do so, then the Go compiler will use that method when printing.

```go
func (c Car)String() string{
    return fmt.Sprintf("{make:%s, year:%d}", *c.make, c.year)
}

func main() {
    make := "Toyota"
    myCar := Car{year:1996, make: &make}
    fmt.Println(myCar)
}
```

Which will print something like:

```
{make:Toyota, year:1996}
```

## #5 - Use the variadic forms of functions like fmt.Println()

In the past, I've often done the following when logging:

```go
fmt.Printf("%s beat %s in the game\n", playerOne, playerTwo)
```

Turns out, it is much easier to just use the `fmt.Println()` function's ability to add spacing:

```go
fmt.Println(playerOne, "beat", playerTwo, "in the game")
```

## #6 - Use the Built-in Log Package

It's often tempting to roll your own logging package, but I would advise that in most cases, the [standard log package](https://golang.org/pkg/log/) is _probably_ all you need. The standard library defines a type, [Logger](https://golang.org/pkg/log/#Logger), which you can use to customize your logging in an idiomatic way. If you don't want that much power and responsibility, you can do what I _usually_ do and use the standard [Print](https://golang.org/pkg/log/#Print) and [Fatal](https://golang.org/pkg/log/#Fatal) functions which just print to standard output along with a formatted date and time prefix.

## Best Practices

Glad you've made it this far! Learning to properly handle errors in Go is one of the things that sets advanced developers apart from newcomers. Striving to improve the readability and developer usability of your code will make you a better [computer scientist](/computer-science/comprehensive-guide-to-learn-computer-science-online/), and help you find more [worthwhile jobs](/computer-science/highest-paying-computer-science-jobs/) in the future.
