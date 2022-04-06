---
title: "How to Make Pure Functions in Golang"
author: Lane Wagner
date: "2020-09-07"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/Pure-Functions-in-Go.png
---

Pure functions are often hyped up in the JavaScript world, probably because of the abundance of stateful front end applications. While pure functions have their downsides (i.e. inconvenience, potentially large argument lists), they should be used as much as reasonably possible.

## What is a Pure Function?

According to [Wikipedia](https://en.wikipedia.org/wiki/Pure_function), a Pure function has the following properties:

1. Its return value is the always same for the same arguments
2. Its evaluation has no side effects (no mutation of data outside the function)

Which means that as a developer I know two important things:

1. When I call a pure function I will get the same result every time
2. After calling a pure function the rest of my program will be in the same state it was before calling it

Because of these properties, pure functions keep applications simple. As we know, simple applications tend to be faster, are easier to test and debug, and are less error prone in general.

{{< cta1 >}}

## Example in Go

Let's take a look at an example function. Using Go, we'll write a `countNamesInText` function that [splits a given string into words delimited by whitespace](/golang/split-strings-golang/#delimiters), then, counts all the words that match a name pulled from the database.

```go
totalCounted := map[string]int{}

func countNamesInText(text string) {
	total := 0
	name := getNameFromDatabase()
	for _, word := range strings.Split(text, " ") {
		if word == name {
			total++
		}
	}
	totalCounted[name] = total
}
```

This function is impure for a couple reasons. Let's examine each one.

### 1\. Program state is mutated by calling countNamesInText()

Instead of mutating a global variable as a means of "returning" data to the caller, we should return the data via a `return` statement:

```go
func countNamesInText(text string) int {
	totalCounted := 0
	name := getNameFromDatabase()
	for _, word := range strings.Split(text, " ") {
		if word == name {
			totalCounted++
		}
	}
	return totalCounted
}
```

Now `countNamesInText` is _more_ "pure" because it will not change the application's state, though you may have noticed that we still have another problem.

### 2\. Database Argument

`countNamesInText` is still impure because the "name" value, which affects the result of the function call, is retrieved from a database. In order for our function to be self-contained, that value should instead be passed as a parameter.

Currently, if we wrote the test:

```go
func TestCountNamesInText(t *testing.T) {
	actual := countNamesInText("this word here")
	if actual != 2{
		t.Errorf("want 2 got %v", actual)
	}
}
```

It wouldn't work consistently. If the database isn't set up, or if the database was tampered with, our tests will fail. That makes this a bad test, and we wrote the bad test because we have an impure function.

Let's purify a bit more:

```go
func countNamesInText(text, name string) int {
	totalCounted := 0
	for _, word := range strings.Split(text, " ") {
		if word == name {
			totalCounted++
		}
	}
	return totalCounted
}
```

Our function is pure, so we can write a good test:

```go
func TestCountNamesInText(t *testing.T) {
	actual := countNamesInText("this word here", "this")
	if actual != 1{
		t.Errorf("want 1 got %v", actual)
	}
}
```

This is what a call to the function in the application might look like:

```go
totalCounted := map[string]int{}
name := getNameFromDatabase()
totalCounted[name] = countNamesInText("some name in here", name)
```
