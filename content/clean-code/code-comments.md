---
title: "Best Practices for Commenting Code"
author: Lane Wagner
date: "2020-10-29"
lastmod: "2022-04-19"
categories: 
  - "clean-code"
images:
  - /img/800/comment.webp
---

I often hear that we need more and better comments in the code we write. In my experience, we frequently need *better* comments, we rarely need *more*, and we sometimes need *less*. Before you crucify me for my sacrilege, let me explain by giving you some of the "rules of thumb" I use for deciding when I should add a comment to my code.

## First, do no harm. If a comment is incorrect or outdated, update it or remove it

Incorrect documentation is **worse** than no documentation.

When reading code, developers typically take the path of least resistance when trying to understand how it works. When provided a function with a comment, most developers will read the comment instead of reading the code itself, especially if the function is long and complex. Let's take a look at this trivial example of a small function:

```go
// replace changes all the commas in the text to colons
func replace(s string) string {
	strings.Replace(s, ",", " ", -1)
}
```

When another developer decides to use this function, they expect that commas will be replaced by *colons*. As this code clearly shows, however, the commas will be replaced by *spaces*. Because of the incorrect comment, a reader will likely take any of the following actions:

* Assume the comment describes the expected behavior and potentially introduce a new bug
* Assume the code describes the expected behavior and potentially leave an existing bug
* Assume the comment describes what the code *actually* does, and use the function in new places, introducing more bugs.

The best solution with a small function like this would probably be to give the function a [more descriptive name](/clean-code/naming-variables) and delete the comment entirely.

```go
func replaceCommasWithSpaces(s string) string {
	strings.Replace(s, ",", " ", -1)
}
```

It's worth pointing out that the function name and the behavior could conflict as well, but at least now we only have 2 things to keep in sync:

* The behavior
* The function name

Instead of trying to keep 3 things in sync:

* The behavior
* The function name
* The comment

We also have the added benefit of re-emphasizing the expected behavior to readers of the code that calls this function, rather than just the readers of the function definition.

## Avoid redundant comments. Strive for a single source of truth

When a comment describes something that can easily be read in code, it runs the risk of being redundant. Redundancy in documentation is generally bad, especially if the code in question is updated frequently. With duplicate documentation, you run the risk of two different parts of the documentation disagreeing with each other. At that point, your reader will not only be confused but will be forced to go to the absolute source of truth, the code, to see what's going on.

Comments and documentation should, to some extent, follow the DRY principle (don't repeat yourself). If the code *clearly* states what is happening, why add a comment? If the expected behavior changes then *two* things need to be updated instead of one!

If your code doesn't clearly state what is happening, your first instinct should be to make the code more readable. If the nature of the code is complex, or if you don't have time due to business constraints to do some [refactoring](/clean-code/spend-time-refactoring/), then there is nothing wrong with adding explanatory comments.

{{< cta1 >}}

## Comments should explain "why" not "how"

Comments and documentation that explain *why* something is happening are *extremely* important. As we've talked about so far, comments that explain *how* the code works are often redundant and unnecessary. For example,

```go
func cleanInput(input string){
	input = strings.ReplaceAll(input, "^", "-")
	input = strings.ReplaceAll(input, "?", "_")
	...
}
```

It is clear by reading the code that all instances of carets and question marks are being replaced by dashes and underscores... but it's not clear *why* would we want to replace them.

```go
func cleanInput(input string){
	// clean input so that it can be used in a regex
	input = strings.ReplaceAll(input, "^", "-")
	input = strings.ReplaceAll(input, "?", "_")
	...
}
```

A comment that explains that carets and question marks are removed for later use in a regex is an example of a good comment because it's often impossible to express the "why" in code.

## Always write comments at API boundaries

As we try to weigh the necessity of adding a comment to code, we should take into account that up until this point we've mostly been talking about comments for **internal maintainers** of the code base. The best practices change drastically when we write comments for external *users* of our code. A good example of this would be `godoc` comments on the exported functions of a package.

When writing a package or library, we don't want the users of our code (the developers running `go get` or `npm install`) to have to worry about the internal implementation details. Good abstractions are black boxes. The Go standard library has great examples of this:

```go
// IndexRune returns the index of the first instance of the Unicode code point
// r, or -1 if rune is not present in s.
// If r is utf8.RuneError, it returns the first instance of any
// invalid UTF-8 byte sequence.
func IndexRune(s string, r rune) int {
	switch {
	case 0 <= r && r < utf8.RuneSelf:
		return IndexByte(s, byte(r))
	case r == utf8.RuneError:
		for i, r := range s {
			if r == utf8.RuneError {
				return i
			}
		}
		return -1
	case !utf8.ValidRune(r):
		return -1
	default:
		return Index(s, string(r))
	}
}
```

Hopefully, these rules of thumb help when you are trying to clean up your code and write better comments!
