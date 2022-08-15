---
title: "Concatenating with strings.Builder Quickly in Golang"
author: Lane Wagner
date: "2021-05-04"
categories: 
  - "golang"
images:
  - /img/800/knot-in-string-unsplash.jpeg
---

The Go standard library makes concatenating strings easy. Concatenation is just a fancy word for adding strings together to make a larger string. For example, if we concatenate `"hello"`, `" "` and `"world"` we'd get `"hello world"`.

The built-in [`fmt.Sprintf`](https://golang.org/pkg/fmt/#Sprintf) function takes a format and a variadic list of interfaces as input.

```go
func Sprintf(format string, a ...interface{}) string
```

The formatting option lets us template out how the final string will look, then we can add inputs that will be interpolated into the string.

```go
s := fmt.Sprintf("%v has been subscribed since %v.\n", user.Name, user.CreatedAt)
```

`%v` is a simple token that will be replaced by the default format of whatever the given arguments are. In our case, it was a `string` and a [time.Time](/golang/golang-date-time/). Check out the [documentation](https://golang.org/pkg/fmt) for all the formatting options.

## Efficient string concatenation

Go 1.10+ released the awesome [`strings.Builder`](https://golang.org/pkg/strings/#Builder) type, which lets us more efficiently build strings. Because it minimizes memory copying, `strings.Builder` is a high-performance option when it comes to doing bulk string concatenation.

### Quickly writing a user list - example

First, let's create an empty builder.

```go
var builder strings.Builder
```

Next, let's add a title string to our list.

```go
b.WriteString("user list\n")
```

Now we'll iterate from 0-9, and for each number write a line containing "`user #{i}`". Because `strings.Builder` implements the `io.Writer` [interface](/golang/golang-interfaces/), we can use the standard `fmt.Fprintf` function.

```go
for i := 0; i < 10; i++ {
    fmt.Fprintf(&b, "user #%d\n", i)
}
```

To actually print the full string we can use the `String()` method.

```go
fmt.Println(b.String())
```

Full code:

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    var b strings.Builder
    b.WriteString("user list\n")
    for i := 0; i < 10; i++ {
        fmt.Fprintf(&b, "user #%d\n", i)
    }
    fmt.Println(b.String())
}
```

## Preallocation for more speed

If you really want to speed up your string building, and you already know the size of your final string, you can use the builder's [`Grow()`](https://golang.org/pkg/strings/#Builder.Grow) method to preallocate the size of the buffer. This saves your code from needing to grow the memory dynamically.

```go
// Grow grows b's capacity, if necessary, to guarantee space for another n bytes.
// After Grow(n), at least n bytes can be written to b without another allocation.
// If n is negative, Grow panics.
func (b *Builder) Grow(n int)
```

So to preallocate for our example we could do the following.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    var b strings.Builder
    b.Grow(90) // we will be writing 90 bytes
    b.WriteString("user list\n")
    for i := 0; i < 10; i++ {
        fmt.Fprintf(&b, "user #%d\n", i)
    }
    fmt.Println(b.String())
}
```
