---
title: "Splitting a String into a Slice in Golang"
author: Lane Wagner
date: "2021-04-15"
categories: 
  - "golang"
images:
  - /img/800/splitting-a-lemon.jpeg
---

I can't begin to tell you how often I split strings in Go. More often than not I'm just parsing a comma-separated list from an environment variable, and Go's standard library gives us some great tools for that kind of manipulation.

## Split by commas or other delimiters

### strings.Split()

Go's rich standard library makes it easy to split a string into a slice. 99% of the time you need to split strings in Go, you'll want the [strings](https://golang.org/pkg/strings) package's [strings.Split() function](https://golang.org/pkg/strings/#Split).

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fruitsString := "apple,banana,orange,pear"
    fruits := strings.Split(fruitsString, ",")
    fmt.Println(fruits)
    // prints ["apple", "banana", "orange", "pear"]
}
```

The `Split` function takes a string and a delimiter as parameters and returns a slice of strings where each substring was formally separated by the given delimiter.

### strings.SplitN()

The `strings.SplitN()` function takes three arguments: the string to be split, a separator, and the number of resulting strings in the slice.

To be honest, I don't use this function very often, but it could be useful in niche conditions. For example, if you are working on a large document and are only interested in the first part of the text.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fruitsString := "apple.banana.orange.pear"
    fruits := strings.SplitN(fruitsString, ".", 3)
    fmt.Println(fruits)
    // prints ["apple", "banana", "orange.pear"]
}
```

## Split by delimiters and retain the delimiters

### strings.SplitAfter()

Similar to `Split()`, the `SplitAfter()` function splits the original string but leaves the delimiters at the end of each substring.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fruitsString := "apple.banana.orange.pear"
    fruits := strings.SplitAfter(fruitsString, ".")
    fmt.Println(fruits)
    // prints ["apple.", "banana.", "orange.", "pear"]
}
```

### strings.SplitAfterN()

`SplitAfterN` does the same thing as `SplitAfter` except it only splits the first `N` substrings. Everything else is retained in the final substring.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fruitsString := "apple.banana.orange.pear"
    fruits := strings.SplitAfterN(fruitsString, ".", 2)
    fmt.Println(fruits)
    // prints ["apple.", "banana.orange.pear"]
}
```

{{< cta1 >}}

## Split by whitespace and newlines

The strings package can do more than just separate a string based on a provided delimiter. The [strings.Fields() function](https://golang.org/pkg/strings/#Fields) separates a string **on all kinds of whitespace** and excludes them from the final result. This is useful if you don't care about the type of whitespace, e.g. tabs, spaces, and newlines all count as spaces.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Printf("Fields are: %q", strings.Fields(`apple
     banana orange
     pear
     `))
    // prints ["apple", "banana", "orange", "pear"]
}
```

## Split using a regex

Regular expressions are a popular way to manipulate strings, and Go's built-in regex engine can help us out. We don't even need to use the `strings` package here, instead, we'll use the [regexp package](https://golang.org/pkg/regexp/).

```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    s := regexp.MustCompile("[0-9]").Split("apple1banana2orange3pear", -1)
    fmt.Println(s)
    // prints ["apple", "banana", "orange", "pear"]
}
```

{{< cta2 >}}

## Gotcha - Strings in Go are special

If you work with a lot of strings, you should know that [Go handles strings differently](https://blog.golang.org/strings) than other languages like Java, C, and Python. Strings in Go are read-only slices of bytes, and those bytes are arbitrary-they can be anything. Strings in Go are not required to contain Unicode text, UTF-8 text, or any other encoding format.
