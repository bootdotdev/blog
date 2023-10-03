---
title: "How to Use Golang's Generics [Updated since 1.18]"
author: Lane Wagner
date: "2021-12-06"
categories: 
  - "golang"
images:
  - /img/800/blob.webp
---

Generics in Go have been [released with Go 1.18](https://go.dev/blog/go1.18)! This is one of the most eagerly-awaited features since the release of the language. Many devs have gone so far as to say Go's previous lack of generic types made the language too painful to use at all. Let's dive into what generics are, why you might use them in your own projects, and how they work in Go.

## What is a generic type?

Put simply, generics allow programmers to write behavior where the type can be specified later because the type isn't immediately relevant. This is an amazing feature because it allows us to write abstract functions that drastically reduce code duplication. For example, the following generic function will split a slice in half, no matter what the types in the slice are.

```go
func splitAnySlice[T any](s []T) ([]T, []T) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

Think about it, to split a slice into two halves, we don't really care about whether it's a slice of integers or a slice of strings, the logic is the same.

For example, we could call it with the following code.

```go
func main() {
    firstInts, secondInts := splitAnySlice([]int{0, 1, 2, 3})
    fmt.Println(firstInts, secondInts)
    // prints [0 1] [2 3]

    firstStrings, secondStrings := splitAnySlice([]string{"zero", "one", "two", "three"})
    fmt.Println(firstStrings, secondStrings)
    // prints [zero one] [two three]
}
```

Generics are a feature of many popular strongly-typed programming languages due to their amazing ability to reduce duplicate code. In dynamically typed languages like JavaScript and Python, you wouldn't need generics, but in Go, it's an amazing addition to the language.

## Generics in Go, the tl;dr

I'll try to summarize the [specification](https://go.googlesource.com/proposal/+/refs/heads/master/design/43651-type-parameters.md) for generics in Go in a few bullet points.

- Functions and types can have an additional list of type parameters before their normal parameters, using square brackets to indicate the generic types used within the function body. These type parameters can be used like any other parameter in the rest of the definition and in the body of the text. For example,
    - `func splitAnySlice[T any](s []T) ([]T, []T)`
- The type parameters are defined using "constraints", which are interface types. Constraints define the required methods and allowed types for the type argument and describe the methods and operations available for the generic type.
- Type inference often allows type arguments to be omitted.
- A special built-in constraint called `any` behaves similarly to `interface{}`.
- A new package called `constraints` will exist in the standard library that will contain commonly used constraints.

## Why should I care about generics?

Go is an amazing language that places an emphasis on simplicity and backward compatibility. In other words, Go has _purposefully left out many features_ other languages boast about because it counterintuitively makes the language better (at least in some people's opinion, and for some use-cases). Go code in one codebase looks like Go code in another codebase. Generally speaking, there is "one way to do it".

According to [historical data from Go surveys](https://go.dev/blog/survey2020-results), Go's lack of generics has always been listed as one of the top three biggest issues with the language. At a certain point, the cons associated with the lack of a feature justify the added complexity to the language. The community and the core team deliberated about it for years, but support for generics is overwhelming at this point it seems.

In short, you should care about generics because they mean you don't have to write as much code, especially if you're in the business of writing packages and tooling. It can be frustrating to write utility functions without generics support. Think about common data structures like binary search trees and linked lists. Why would you want to rewrite them for every type they could possibly contain? `int`, `bool`, `float64`, and `string` aren't the end of the list, because you may want to store a custom `struct` type.

Generics will finally give Go developers an elegant way to write amazing utility packages.

## What is a constraint?

Sometimes you need the logic in your generic function to know a thing or two about the types in question. Constraints are [interfaces](/golang/golang-interfaces/) that allow you to write generics that only operate within the constraint of a given interface type. In the first example above, we used the `any` constraint, which is comparable to the empty `interface{}`, because it means the type in question could be anything.

### Any constraint

The `any` "constraint" works great if you're treating the value like a bucket of data, maybe you're moving it around, but you don't care at all about what's in the bucket.

According to [the propsal](https://go.googlesource.com/proposal/+/refs/heads/master/design/43651-type-parameters.md), the operations permitted for the `any` type are as follows.

- declare variables of those types
- assign other values of the same type to those variables
- pass those variables to functions or return them from functions
- take the address of those variables
- convert or assign values of those types to the type `interface{}`
- convert a value of type `T` to type `T` (permitted but useless)
- use a type assertion to convert an interface value to the type
- use the type as a case in a type switch
- define and use composite types that use those types, such as a slice of that type
- pass the type to some predeclared functions such as `new`

If you do need to know more about the generic types you're working on you can constrain them using interfaces. For example, maybe your function will work with any type that can represent itself as a string.

```go
type stringer interface {
    String() string
}

func concat[T stringer](vals []T) string {
    result := ""
    for _, val := range vals {
        result += val.String()
    }
    return result
}
```

### Comparable constraint

The `comparable` constraint is a predefined constraint as well, just like the `any` constraint. When using the comparable constraint instead of the `any` constraint, you can use the `!=` and `==` operators within your function logic.

```go
func indexOf[T comparable](s []T, x T) (int, error) {
    for i, v := range s {
        if v == x {
            return i, nil
        }
    }
    return 0, errors.New("not found")
}

func main() {
    i, err := indexOf([]string{"apple", "banana", "pear"}, "banana")
    fmt.Println(i, err)
    // prints 1 <nil>
}
```

## Custom constraints

### Parametric constraints

Your interface definitions, which can later be used as constraints can take their own type parameters.

```go
type vehicleUpgrader[C car, T truck] interface {
    Upgrade(C) T
}
```

### Type lists

From [the proposal](https://go.googlesource.com/proposal/+/refs/heads/master/design/43651-type-parameters.md#operations-based-on-type-sets), we can simply list a bunch of types to get a new interface/constraint.

```go
// Ordered is a type constraint that matches any ordered type.
// An ordered type is one that supports the <, <=, >, and >= operators.
type Ordered interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
        ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
        ~float32 | ~float64 |
        ~string
}
```

### Mixed

We can also mix up parameterized declarations and type lists to get new interfaces.

```go
type ComparableStringer interface {
    comparable
    String() string
}
```

### Self referential

```go
Cloneable interface {
    Clone() Cloneable
}
```

## Generic Types vs Generic Functions

So we know that we can write functions that use generic types, but what if we want to create a custom type that can contain generic types? For example, a slice of order-able objects. The new proposal makes this possible.

```go
type comparableSlice[T comparable] []T

func allEqual[T comparable](s comparableSlice[T]) bool {
    if len(s) == 0 {
        return true
    }
    last := s[0]
    for _, cur := range s[1:] {
        if cur != last {
            return false
        }
        last = cur
    }
    return true 
}

func main() {
    fmt.Println(allEqual([]int{4,6,2}))
    // false

    fmt.Println(allEqual([]int{1,1,1}))
    // true
}
```

## Get the zero value of a generic

The `var name T` syntax is a simple way to generate the zero value of a generic type in Go. This is especially useful considering idiomatic Go's consistent use of [guard clauses](/clean-code/guard-clauses/).

```go
func returnZero[T any](s ...T) T {
    var zero T
    return zero
}

func main() {
    fmt.Println(returnZero(5))
    // prints "0"
    fmt.Println(returnZero("string"))
    // prints ""
    fmt.Println(returnZero(true))
    // prints "false"
}
```

## Limitations of generics

### No switching on a generic's underlying type

```go
// DOES NOT WORK
func is64Bit[T Float](v T) T {
    switch (interface{})(v).(type) {
    case float32:
        return false
    case float64:
        return true
    }
}
```

The only way to get around this is to use an interface directly and perform a runtime type switch.

### No inheritence

If you were hoping generics would make Go an object-oriented language with full inheritance capabilities, then you'll be disappointed. While generics reduce code duplication, you still won't be able to subclass a hierarchy of types.

## Generics vs interfaces

Interfaces in Go are a form of generic programming in that they let us require disparate types to implement the same APIs. We then write functions that implement those interface types, and those functions will work for any type that implements those methods. Tada, we have a beautiful abstraction layer.

The problem with this approach in many cases is that it requires each type to rewrite its logic, even if the logic is identical. Generics in Go use interfaces as constraints because interfaces are already the perfect thing to enforce the requisite APIs, but generics add a new feature, type parameters, which can [DRY up our code](/clean-code/dry-code/).

## Generics vs code generation

Go programmers have had a history of using code generation, the toolchain even has [go generate](https://go.dev/blog/generate) built-in. In short, due to Go's lack of generics, many developers in the past used code generation to work around the problem. They would generate copies of nearly identical functions, where the only real differences were the parameter's types.

Now, with generics, we can stop generating so much code! Code generation will still have a place in solving other problems, but anywhere we need to write the same logic for multiple types we should just use generics. Generics are a much more elegant solution.

## Using generics now

You can play with generics today with Go 1.18! Make sure you just get your local toolchain updated to the latest version. You can get going immediately by playing around on [boot.dev's Golang playground](https://boot.dev/playground/go), it's running 1.18 at the time of writing.

## How do generics work under the hood?

Generics are really just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar), nothing fundamental about your code's runtime speed will be impacted much by using generics. Since the implementation isn't fully released yet, we don't quite know exactly what the performance impacts will be. That said, here are my guesses.

1. Compilation time will take longer by some (likely negligible) nonzero factor. It doesn't make sense to me that adding a new compile time feature would help the compiler run any faster.
2. The runtime of generics vs single-type functions (whether written by hand or generated by code) will be nearly identical.
3. Generics will generally outperform interfaces at runtime by some (likely negligible) nonzero factor. Interfaces seem likely to have some additional runtime overhead due to type assertions and such.

## Will the standard library use generics now?

For new functions, types, and methods the answer is yes. However, for existing APIs, the Go team seems to remain committed to not breaking backward compatibility, which is a great decision in my opinion. Russ Cox [opened a discussion](https://github.com/golang/go/discussions/48287) to talk about this issue and has a proposal to rewrite the types and functions that clearly would use generics if we wrote them today.

He suggests adopting an "Of" suffix for the updated functions. For example, [sync.Pool](https://pkg.go.dev/sync#Pool) becomes sync.PoolOf.

## Do generics change what is "idiomatic"?

Definitely. A trivial example is that it used to be wise to [use `float64` by default](/golang/default-native-types-golang/) if you need a numeric type. Now there are many cases where you can use some kind of numeric constraint and open your code up to more reuse.

I'm excited to see what new best practices emerge as generics make their way into production code and we all get to play around with them.
