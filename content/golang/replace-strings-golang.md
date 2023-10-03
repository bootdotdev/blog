---
title: "How Replace a String in Go - Top 5 Examples"
author: Lane Wagner
date: "2021-04-20"
lastmod: "2022-10-01"
categories: 
  - "golang"
images:
  - /img/800/prety-strings.png.webp
---

Go has a powerful standard library that makes string manipulation easy right out of the box. One of the functions I use most often is the [strings](https://golang.org/pkg/strings) package's [Replace()](https://golang.org/pkg/strings/#Replace) function. `strings.Replace()` returns a *copy* of its input string after replacing all instances of a given substring with a new one.

## How to use strings.Replace in Go

Function signature:

```go
func Replace(s, old, new string, n int) string
```

Example usage:

```go
strings.Replace("one one two two three", "one", "1", -1)
// 1 1 two two three
```

Notes about the function:

* `s` is the original string that contains the substrings to be replaced.
* `old` is the substring you want to be replaced.
* `new` is the substring that will be swapped out for `old`.
* `n` limits the number of replacements. If you want to replace them all, just set `n` to `-1`, or use the more explicit [ReplaceAll](https://golang.org/pkg/strings/#ReplaceAll) function.

## Example #1 - Replacing delimiters

Let's say you have some comma-separated values, CSVs. Perhaps you want to separate each word with a _space_ instead of a _comma_. This can be useful if you need to make your delimiters consistent so you can later [split the string into a slice](/golang/split-strings-golang/).

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Println(strings.Replace("apple,banana,orange,pear", ",", " ", -1))
    // prints "apple banana orange pear"
}
```

## Example #2 - Only replace some strings

It can be useful to only print the replace the first `n` instances of a word. For example, let's say we had some text containing dialogue, like in a movie script. If you want to change the delimiter between the speaker and there lines to be a dash instead of a colon, but _don't_ want to replace any colons in the dialogue, you can set `n=1`.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Println(strings.Replace("Lane: 'The box said price:1'", ":", " -", 1))
    // prints "Lane - 'The box said price:1'"
}
```

## Example #3 - Remove all instances of a string

Sometimes you just want to strip out specific characters. For example, you may want to remove all periods. To do so, you can simply replace all periods with an empty string.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Println(strings.Replace("123.456.789.0", ".", "", -1))
    // prints "1234567890"
}
```

## Example #4 - High-performance string replacement

If you need to perform the same replacements on many different documents, it can make sense to initialize a [Replacer](https://golang.org/pkg/strings/#Replacer), which is much faster that the `strings.Replace` function when used repeatedly. It's faster is because it builds a [trie structure](https://en.wikipedia.org/wiki/Trie) under the hood that it keeps in memory, and that structure can be used repeatedly.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    replacer := strings.NewReplacer(",", ":", "!", "?")
    fmt.Println(replacer.Replace("hello,there!good,reader!"))
    fmt.Println(replacer.Replace("glad,to!have,you!"))
    fmt.Println(replacer.Replace("bye,now!thank,you!"))
    // prints:
    // hello:there?good:reader?
    // glad:to?have:you?
    // bye:now?thank:you?
}
```

[NewReplacer()](https://golang.org/pkg/strings/#NewReplacer) takes a list of old-new string pairs, so you can use it to perform many different replacement operations.

```go
func NewReplacer(oldnew ...string) *Replacer
```

## Example #5 - Complicated Replacements with Regex

We're shifting packages entirely now, and will be using the standard library's [regexp](https://golang.org/pkg/regexp) package. This package exposes a [ReplaceAllString()](https://golang.org/pkg/regexp/#Regexp.ReplaceAllString) function that lets us do more complicated replacements using a standard regex. This may be useful if you need to do some dynamic replacements, or are fluent in regular expressions.

```go
func (re *Regexp) ReplaceAllString(src, repl string) string
```

```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    re := regexp.MustCompile(`r.t`)
    fmt.Println(re.ReplaceAllString("rat cat rot dog", "ram"))
    // prints "ram cat ram dog"

    re = regexp.MustCompile(`-.*-`)
    fmt.Println(re.ReplaceAllString("-rasjdkajnsdt-hello world", ""))
    // prints "hello world"
}
```
