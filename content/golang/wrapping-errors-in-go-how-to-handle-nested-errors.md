---
title: "Wrapping Errors in Go - How to Handle Nested Errors"
author: Lane Wagner
date: "2020-03-09"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/photo-1495863367063-b9ac3e6394f7.webp
---

Errors in Go are a hot topic. Many newcomers to the language immediately level their first criticism, _"errors in go are clunky! Let me just use try/catch!"_ This criticism is well-meaning but misguided.

The paradigm of errors as a type, rather than something to be thrown and cause panics, allows for more control of how to handle "bad" state. It also forces developers to think about errors at every step.

> What will go wrong here? How should I handle it?

There are plenty of articles that discuss the pros/cons of error handling in Go. I want to talk specifically about how the clunky (albeit better) handling of errors in Go can lead to a common problem: nested errors.

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

_isInRange()_ is a simple function that checks if a number is between two other predefined numbers, and returns a formatted error message in case the number is out of range.

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

As you can see, _getNumberFromStdIn()_ calls _isInRange()_. The problem with the above code is that if an error happens within _getNumberFromStdIn()_ and subsequently is logged to the console, it is almost impossible to tell where the error came from.

For example, if isInRange's error is logged to the console during execution:

```
isInRange: 3 must be between 5 and 10
```

Where did this come from? We know that _isInRange()_ created the error, but we don't know where _isInRange()_ was called. Was _isInRange()_ called by _getNumberFromStdIn()_? Or somewhere else? Perhaps we grep through our codebase and see that _isInRange()_ is called hundreds of times! Now our task to find the root of the error becomes much more difficult than it needs to be.

## Solution: Wrap The Errors

```go
func getNumberFromStdIn() (int, error) {
	reader := bufio.NewReader(os.Stdin)
	text, _, err := reader.ReadLine()

	const fName = "getNumberFromStdIn"
	if err != nil {
		return 0, fmt.Errorf("%v: %v", fName, err)
	}
	i, err := strconv.Atoi(string(text))
	if err != nil {
		return 0, fmt.Errorf("%v: %v", fName, err)
	}
	err = isInRange(i)
	if err != nil {
		return 0, fmt.Errorf("%v: %v", fName, err)
	}
	return i, nil
}
```

Now, when isInRange() is called in this specific location, we get a formatted message:

```
getNumberFromStdIn: isInRange: 3 must be between 5 and 10
```

By wrapping errors and building well-formatted error messages, we can keep better track of where errors are happening.

## Should I Always Wrap Errors?

Nope. Like all rules-of-thumb, there are exceptions.

For example, if I'm writing a package that exposes the function _getNumberFromStdIn()_ then my users (programmers using my package) don't need to know that _atoi()_ failed, they just need to know that _getNumberFromStdIn()_ failed. I don't need to wrap any errors. In fact, I can probably ignore the underlying error and create my own message from scratch.

If it is glaringly obvious where an error comes from, there is also less reason to wrap it. Wrapping an error, in theory, should never hurt, but it can be unnecessary work. Look at everything on a case-by-case basis.
