---
title: "Best Practices for Commenting Code"
author: Lane Wagner
date: "2020-10-29"
categories: 
  - "clean-code"
tags: 
  - "sharing"
---

I often hear that we need more and better comments in the code we write. In my experience, we often need _better_ comments, we rarely need more, and often we need _less_. Before you crucify me for my sacrilege, let me explain.

## #1 - Incorrect Comments

Incorrect documentation is worse than no documentation, and redundant documentation is worthless. Let's remove the chaff. Developers typically (and rightly) take the path of least resistance when trying to figure out what a piece of code is doing. When provided a function with a comment, many developers will read the comment instead of reading the code itself, especially if the function is long and complex. Let's take a look at this trivial example:

```go
// replace changes all the commas in the text to colons
func replace(s string) string {
	strings.Replace(s, ",", " ", -1)
}
```

When another developer decides to use this function, they expect that commas will be replaced by colons. As this code clearly shows, however, the commas will be replaced by _spaces_. Because of the incorrect comment, a reader may take the comment at its word and introduce a bug, they may "fix" the comment and leave an existing bug, or they may "fix" the code and introduce a new bug. The point is, a bug is very likely to be produced if the reader isn't careful.

The solution would be to give the function a [more descriptive name](https://qvault.io/clean-code/naming-variables/) and delete the comment entirely.

```go
func replaceCommasWithSpaces(s string) string {
	strings.Replace(s, ",", " ", -1)
}
```

## #2 - Redundant Comments

It would have been strictly better to omit the comment in the example above entirely. The developer would have been forced to go to the single source of truth (the code) and would have interpreted the meaning correctly.

Comments and documentation should, to some extent, follow the DRY principle (don't repeat yourself). If the code _clearly_ states what is happening, why add a comment? If functionality changes then _two_ things need to be updated! If the code doesn't clearly state what is happening, then a developer's first instinct should be to make the code more readable, not to add a comment.

Redundancy is also quite simply a waste of time. Developers remain best-utilized writing code, architecting systems, and creating tests. We should only write documentation when absolutely necessary.

## #3 - Comments for the Outside World - AKA Documentation

As we try to weigh the necessity of adding a comment to code, we need to take into account that it's _more_ likely that a comment is needed if it exists at an architectural boundary. For example, when writing a package or library we don't want the users (other developers) of our code to have to worry about the internal workings. The function and class names along will well-written comments (or API docs as the case may be) should be all they need to understand how to use our APIs. The Go standard library has great examples of this:

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

## #4 - Comments Should Explain 'Why' not 'How'

Comments and documents that explain _why_ something is happening are quite important and don't apply to any of the previous criticisms I've made of comments. Comments that explain _how_ the code works are often redundant and lazy. For example,

```go
func cleanInput(input string){
	input = strings.ReplaceAll(input, "^", "-")
	input = strings.ReplaceAll(input, "?", "_")
	...
}
```

Here it is clear by reading the code that all instances of carets and question marks are being replaced by dashes and underscores... but why?

```go
func cleanInput(input string){
	// clean input so that it can be used in a regex
	input = strings.ReplaceAll(input, "^", "-")
	input = strings.ReplaceAll(input, "?", "_")
	...
}
```

A comment that explains that carets and question marks are removed for later use in a regex is an example of a good comment because it's often hard to express the "why" in code.

Hopefully, these rules of thumb help when you are trying to clean up your code and write better comments!
