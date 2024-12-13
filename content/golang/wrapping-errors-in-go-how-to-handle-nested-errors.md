---
title: "Wrapping Errors in Go - How to Handle Nested Errors"
author: lane
date: "2020-03-09"
lastmod: "2022-04-15"
categories:
  - "clean-code"
  - "golang"
images:
  - /img/800/Nested_Erros.webp
---

Errors in Go are a hot topic. Many newcomers to the language immediately level their first criticism, "errors in go are clunky! Let me just use try/catch!" This criticism is well-meaning but misguided.

The paradigm of errors as a _type_, rather than something to be _thrown_, simplifies error handling and brings it to the forefront. It also forces developers to think about errors at every step.

> What will go wrong here? How should I handle it?

There are plenty of articles that discuss the pros/cons of error handling in Go. I want to talk specifically about how the verbose (but better) handling of errors in Go can lead to a common problem: deeply nested errors.

## The Called Function

To demonstrate the problem of nested errors, let's take a look at the following function:

```go
func isInRange(i int) error {
	const min = 5
	const max = 10
	if i < 5 || i > 10 {
		return fmt.Errorf("isInRange: %v must be between %v and %v", i, min, max)
	}
	return nil
}
```

`isInRange()` is a simple function that checks if a number is between two other predefined numbers, and returns a formatted error message in case the number is out of range.

## The Calling Function

```go
func getNumberFromStdIn() (int, error) {
	reader := bufio.NewReader(os.Stdin)
	text, _, err := reader.ReadLine()
	if err != nil {
		return 0, err
	}
	i, err := strconv.Atoi(string(text))
	if err != nil {
		return 0, err
	}
	err = isInRange(i)
	if err != nil {
		return 0, err
	}
	return i, nil
}
```

As you can see, `getNumberFromStdIn()` calls `isInRange()`. The problem with the above code is that if an error happens within `getNumberFromStdIn()` and subsequently is logged to the console, it is almost impossible to tell where the error came from.

For example, if `isInRange`'s error is logged to the console during execution:

```
isInRange: 3 must be between 5 and 10
```

Where did this come from? We know that `isInRange()` created the error, but we don't know where `isInRange()` was called. Was `isInRange()` called by `getNumberFromStdIn()`? Or somewhere else? Perhaps we grep through our codebase and see that `isInRange()` is called hundreds of times! Now our task to find the root of the error becomes much more difficult than it needs to be.

## The solution? Wrap the errors with some context

The [fmt.Errorf()](https://pkg.go.dev/fmt#Errorf) function is a favorite of mine, I use it in most functions I write. It allows us to format error messages, and more importantly to wrap errors within each other, which has the nice benefit of our error messages looking more like stack traces.

```go
func getNumberFromStdIn() (int, error) {
	reader := bufio.NewReader(os.Stdin)
	text, _, err := reader.ReadLine()
	if err != nil {
		return 0, fmt.Errorf("reader.ReadLine: %w", err)
	}
	i, err := strconv.Atoi(string(text))
	if err != nil {
		return 0, fmt.Errorf("strconv.Atoi: %w", err)
	}
	err = isInRange(i)
	if err != nil {
		return 0, fmt.Errorf("isInRange: %w", err)
	}
	return i, nil
}

func runMainThread() error {
	i, err := getNumberFromStdIn()
	if err != nil{
		return fmt.Errorf("getNumberFromStdIn: %w", err)
	}
}
```

Now, when `isInRange()` is called in this specific location, we get a formatted message:

```
getNumberFromStdIn: isInRange: 3 must be between 5 and 10
```

By wrapping errors and building well-formatted error messages, we can keep better track of where errors are happening. I often just add the name of the function being called to my error messages, but we can make the message say whatever we want. For example, I'll often include parameter information in the error so I know which inputs caused the error.

## Why use %w?

For quite a while I was using `%v` as the interpolated value in the `fmt.Errorf` function, and for the most part it worked as intended. The problem with `%v` really only arises when it comes time to compare two errors using the [errors.Is](https://pkg.go.dev/errors#Is) function. For example. I'll often want to check if a error as an "end of file" error, so I'll use the following check:

```go
if errors.Is(err, io.EOF) {
	fmt.Println("Reading file finished...")
}
```

This code would fail the error check:

```go
func readFile() ([]byte, error){
	dat, err := readLine() // returns io.EOF error
	if err != nil{
		// %v ruins the wrap, and future
		// errors.Is checks will fail for type io.EOF
		return fmt.Errorf("readLine: %v", err)
	}
	return dat, nil
}

_, err = readFile()
if errors.Is(err, io.EOF) {
	// this will NOT execute
	fmt.Println("Reading file finished...")
}
```

Instead, we can preserve the error check by using `%w`:

```go
func readFile() ([]byte, error){
	dat, err := readLine() // returns io.EOF error
	if err != nil{
		return fmt.Errorf("readLine: %w", err)
	}
	return dat, nil
}

_, err = readFile()
if errors.Is(err, io.EOF) {
	// this will execute
	fmt.Println("Reading file finished...")
}
```

As far as I know, when working with errors it's _always better_ to use `%w` over `%v`.

## Manually unwrapping errors

To be honest, I've never felt the need to manually unwrap an error. That said, I'm sure there are cases where you would want to do so. The standard library provides [errors.Unwrap](https://pkg.go.dev/errors#Unwrap) to do just that.

```go
err1 := errors.New("no user id provided")
err2 := fmt.Errorf("error on cronos server: [%w]", err1)
fmt.Println(err2)
// prints: "error on cronos server: [no user id provided]"
fmt.Println(errors.Unwrap(err2))
// prints: "no user id provided"
```

As an example, I might wrap an error with some sensitive context that's useful to my internal team, but maybe we need to unwrap it before returning it over an HTTP API for security purposes.

## Should I always wrap errors?

Like all rules of thumb, there are exceptions.

For example, if I'm writing a package that exposes the function `getNumberFromStdIn()` then my users (programmers using my package) don't need to know that `atoi()` failed, they just need to know that `getNumberFromStdIn()` failed. I probably don't want to be exposing too much internal logic to my API users. I can probably ignore the underlying error and create my own message from scratch that's more helpful to the end user.

If it is glaringly obvious where an error comes from, there is also less reason to wrap it. Wrapping an error, in theory, should never hurt, but it _can_ be unnecessarily verbose and a lot of extra work. As always, look at everything on a case-by-case basis.
