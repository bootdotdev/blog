---
title: "Top 15 Golang Interview Questions [Updated 2022]"
author: Lane Wagner
date: "2020-08-31"
categories: 
  - "golang"
images:
  - /img/800/whiteboard.webp
---

Let's take a look at some good technical questions to be familiar with, whether you are the interviewer or the interviewee.

## 1. What's the difference between a goroutine and an operating system thread?

- Go provides built-in channels for goroutines to communicate safely between themselves.
- More goroutines can run on a typical system than system threads. For example, with Java, you can run many _thousands_ of threads. With Go, you can run many _millions_ of goroutines.
- Goroutines startup more quickly than operating system threads.
- Multiple Goroutines are multiplexed onto OS threads, rather than a 1:1 mapping.
- You can write massively concurrent servers without having to resort to event programming.
- Goroutines are not hardware-dependent like threads.
- Goroutines are more lightweight, largely due to [segmented stacks](https://blog.cloudflare.com/how-stacks-are-handled-in-go/#segmentedstacks) in memory

## 2. Can constants be computed in Go?

Constants can **not** be computed at runtime, their value must be known at compile time. That said, constants can be computed at compile-time, typically as a derivative of other constants. For example:

```go
const hours = 7643

const minutes = hours * 60
```

## 3. What does the Go ecosystem use for package and dependency management?

Until recently the GOPATH setup allowed developers to import packages as long as they were in the local Go workspace. As of Go ~1.13 it's recommended to use `go mod`. With `go mod`, source code isn't required to be a part of the `GOPATH` environment variable.

Go doesn't use a package manager like NPM or Cargo. The Go toolchain provides commands like `go get` for fetching external dependencies straight from their remote source control repositories, and `go mod` for managing the dependencies of a specific project.

## 4. How would you succinctly swap the values of two variables in Go?

```go
var1, var2 = var2, var1
```

## 5. Do you have any preferences for error-handling methodologies in Go?

Errors in Go are an interface type, where any type that implements the single `Error()` method can be considered an error:

```go
type error interface {
    Error() string
}
```

Whenever a function has a possibility to go wrong, like a network call or a type conversion, the function should return an error as its last return variable. The caller should check the error value, and any value other than `nil` is considered an error.

Idiomatic Go developers should prefer [guard clauses](/clean-code/guard-clauses/) over if-else chains, especially when handling errors. Errors should also be [wrapped in a meaningful way](/golang/wrapping-errors-in-go-how-to-handle-nested-errors/) as they are passed up the call stack if appropriate.

## 6. What is a pointer and when would you use it?

A [pointer](/golang/the-proper-use-of-pointers-in-go-golang/) holds the memory address of a value.

- `&` generates a pointer to its operand.
- `*` dereferences a pointer (exposes the underlying value).

Pointers can be used to:

- Allow a function to directly mutate a value that is passed to it
- To increase performance in edge cases. Sometimes passing a large struct of data results in inefficient copying of data
- To signify the lack of a value. For example, when [unmarshalling JSON data](/golang/json-golang/) into a struct it can be useful to know if a key was absent rather than it being present with the zero value.

## 7. Describe the difference between [sync.Mutex](https://golang.org/pkg/sync/#Mutex) and [sync.RWMutex](https://golang.org/pkg/sync/#RWMutex)

The normal mutex locks data so that only one goroutine can access it at a time.

A [RWMutex (read/write)](/golang/golang-mutex/) can lock data for "reading" and for "writing". When locked for reading, other readers can also lock and access data. When locked for writing no other goroutines, including other readers can access the data.

## 8. Consider the following code. What will be the value of s1?

```go
primes := [6]int{2, 3, 5, 7, 11, 13}
s1 := primes[1:4]
```

`s1` will be: `[3 5 7]`

When slicing an existing array or slice the first index is inclusive while the last index is exclusive. If an index is omitted on one side of the colon, then all values until the edge of the original slice are included in the result.

## 9. Are channels and maps safe for concurrent access?

Channels are safe for concurrent access, for this reason, they have blocking operations. Maps are unsafe for concurrent access and require a locking mechanism like a mutex to be safely used across goroutines.

## 10. How would you [sort](/golang/sorting-in-go-dont-reinvent-this-wheel/) a slice of custom structs?

I would build a new type that represents a slice of that struct type. For example:

```go
type fruitSlice[]fruit

type car struct {
	size int
	color string
}
```

Then I would fulfill the standard library's [sort.Interface](https://golang.org/pkg/sort/#Interface):

```go
type Interface interface {
    Len() int
    Less(i, j int) bool
    Swap(i, j int)
}
```

I would then be able to use the [sort.Sort](https://golang.org/pkg/sort/#Sort) function:

```
sort.Sort(fruitSlice(cars))
```

## 11. Does Go support generic programming?

Go doesn't currently support [generics](/golang/how-to-use-golangs-generics/), but [support is coming in 1.18](https://blog.golang.org/generics-proposal). Generics will allow us as developers to write code that operates on types without needing to re-implement the same function multiple times for all the different types.

For example, say you want to implement a Binary Tree in Go, that can store any type of item. This _should_ be easy because the binary tree shouldn't care about the types it stores, it never needs direct access to them. Currently, you only have two options: rewrite the tree for every type you want to support, or use an interface and cast the type every time you insert or remove something from the tree, neither of which are ideal solutions.

## 12. Is `ni`l only valid on pointer types?

Nope! `nil` is the zero value for pointers, interfaces, maps, slices, channels, and function types. `nil` represents an _uninitialized_ value.

## 13. Does Go provide support for OOP via classes?

No, Go isn't an object-oriented programming language. Interfaces are the way we handle most abstractions in Go, and it requires an entirely different way of thinking.

## 14. How do you export functions from a package?

Exported functions in Go just need to be capitalized to be exported.

```go
func DoWork(){
    // this function is usable outside this package
}

func doWork(){
    // this function is NOT usable outside this package
}
```

## 15. What do you like about Go?

Well, this one's up to you, but [I have a few things in mind](/golang/why-learn-golang/).

- Easy for beginners
- Modern language with simple syntax
- Ease of concurrency
- Great pay
- Built for the web
- Fast
- Memory efficient
