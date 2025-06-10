---
title: "How to Properly Use Defer in Golang"
author: lane
date: "2021-06-01"
categories: 
  - "golang"
images:
  - img/800/ruinreborn_fantasy_art_simple_background_character_holding_up_e00cd330-8731-4171-b1aa-efe31ef057ac_2.png.webp
---

## What is the "defer" keyword in Go?

In the Go programming language, `defer` is a keyword that allows developers to delay the execution of a function until the current function returns. What throws some people off is that the deferred function's arguments are evaluated immediately, but the function itself doesn't fire until the wrapping function exits.

### Simple defer example - hello world

```go
func main() {
    defer fmt.Println("world") // deferred until main() exits
    fmt.Println("hello")
 }

// prints:
// hello
// world
```

## When would you want to defer something?

After programming in Go, it's really hard to remember how I dealt with closing connections or files in other languages. The `defer` statement is a very clean way to deal with any sort of "cleanup" that needs to happen in a function.

```go
resp, err := http.Get(url)
if err != nil{
    log.Println(err)
}
defer resp.Body.Close()
```

In Go's standard [http library](https://golang.org/pkg/net/http/), the documentation points out that HTTP responses must be closed by the client when it's finished. `The client must close the response body when finished with it`.

In the example above, you might be thinking, "I'll just close the response when I'm done with it, why should I `defer` it?". In my experience, the main reason to use `defer` is due to Go developers' liberal use of guard clauses. When a function has many exit points (places where it can `return` early), you don't want to prefix every return with a response closure. What if you miss one? Let's look at an example.

```go
func getUser() (User, error) {
    resp, err := http.Get("https://example.tld/users")
    if err != nil{
        return User{}, err
    }

    dat, err := io.ReadAll(resp.Body)
    if err != nil {
        resp.Body.Close()
        return err
    }

    user := User{}
    err = json.Unmarshal(dat, &user)
    resp.Body.Close()
    return user, err
}
```

Notice how `resp.Body.Close()` needs to be called in two places - at each potential exit point. With `defer`, we can simply our code.

```go
func getUser() (User, error) {
    resp, err := http.Get("https://example.tld/users")
    if err != nil{
        return User{}, err
    }
    defer resp.Body.Close()

    dat, err := io.ReadAll(resp.Body)
    if err != nil{
        return err
    }

    user := User{}
    err = json.Unmarshal(dat, &user)
    return user, err
}
```

## Defer, panic and recover - Why you shouldn't do it

I don't want to spend too much time on this, but some people have stumbled across Go's built-in `recover()` function and thought it might be a good idea to use `panic()` and `recover()` like `try` and `catch` in other languages.

### What is the recover() function in Go?

Simply put, _recover_ is a builtin function that regains control of a panicking goroutine. Recover is only used inside deferred functions. Calling `recover()` inside a deferred function stops the panicking sequence by and retrieves the error message passed to the `panic()` function call.

```go
func recoverWithMessage() {  
    if r := recover(); r!= nil {
        fmt.Println("recovered from", r)
    }
}

func fullName(firstName *string, lastName *string) string {  
    defer recoverWithMessage()
    if firstName == nil {
        panic("first name cannot be nil")
    }
    if lastName == nil {
        panic("last name cannot be nil")
    }
    return fmt.Sprintf("%s %s\n", *firstName, *lastName)
}

func main() {
    firstName := "Lane"
    lastName := "Wagner"
    fmt.Println(fullName(&firstName, &lastName))
    fmt.Println(fullName(nil, nil))
 }

// prints:
// Lane Wagner
// recovered from first name cannot be nil
```

The example above is a complicated and non-idiomatic way to handle runtime problems that would have been better dealt with by just passing `error` values. I understand that there are definitely edge-cases where use of `panic()` and `recover()` might make sense. That said, I've been writing Go professionally for about 5 years now and I've never felt a sufficient need, especially in application code. Do your best to refactor your project so you can just return `error`s like the good designers intended.

## When are function arguments evaluated?

Unlike other higher-order functions in Go, when you "pass" a function to the `defer` keyword, you pass an entire function call, not just the name of the function. This allows the function's arguments to be evaluated immediately. The `defer` keyword just ensures that the _body_ of the function won't run until the parent function returns.

```go
func main() {
    printMath(5, 6, multiply) // the "multiply" function is passed without arguments
}

// printMath does some math and prints the result
func printMath(x, y int, mathFunc func(int, int) int) {
    fmt.Println(mathFunc(x, y))
}

func multiply(x, y int) int {
    return x * y
}
```

The `defer` keyword on the other hand **does** take arguments.

```
defer fmt.Println(x + y)
```

`x+y` evaluates immediately, but doesn't print until `main()` exits.

## What happens with multiple defer statements?

Deferred function calls are pushed onto a stack data structure. When the parent function returns, all its deferred calls are executed in the reverse order that they were created.

```go
defer fmt.Println("third")
defer fmt.Println("second")
defer fmt.Println("first")

// prints:
// first
// second
// third
```
