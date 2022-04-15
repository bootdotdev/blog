---
title: "Best Practices for Interfaces in Go"
author: Lane Wagner
date: "2020-03-15"
categories: 
  - "golang"
images:
  - /img/800/block-interfaces.jpeg
---

Interfaces in Go allow us to treat different types as the same data type temporarily because both types implement the same _kind_ of behavior. They're central to a Go programmer's toolbelt and are often used improperly by new Go developers, which leads to unreadable and often buggy code.

## What is an interface in Golang?

In Go, an interface is a custom type that other types are able to _implement_, which gives Go developers a powerful way to use abstraction. Interfaces are named collections of method signatures, and when other types implement all the required methods, they implicitly implement the interface.

For example, errors in Go are interfaces, and the standard `error` interface is simple, all a type needs to do to be considered an `error` is define an `Error()` method that accepts no parameters and returns a `string`.

```go
type error interface {
    Error() string
}
```

The simplicity of the `error` interface makes [writing logging](/golang/golang-logging-best-practices/) and metrics implementations much easier. Let's define a struct that represents a network problem:

```go
type networkProblem struct {
	message string
	code    int
}
```

Then we can define an `Error()` method:

```go
func (np networkProblem) Error() string {
	return fmt.Sprintf("network error! message: %s, code: %v", np.message, np.code)
}
```

Now, we can use an instance of the `networkProblem` struct wherever an error is accepted.

```go
func handleErr(err error) {
	fmt.Println(err.Error())
}

np := networkProblem{
	message: "we received a problem",
	code:    404,
}

handleErr(np)

// prints "network error! message: we received a problem, code: 404"
```

{{< cta1 >}}

## Best practices for writing interfaces

Writing clean interfaces is **hard**. Frankly, anytime you're dealing with abstractions in code, the simple can become complex very quickly if you're not careful. Let's go over some rules of thumb for keeping interfaces clean.

1. [Keep interfaces small](#small)
2. [Interfaces should have no knowledge of satisfying types](#no-knowledge)
3. [Interfaces are not classes](#not-classes)

### 1. Keep Interfaces Small

If there is only one piece of advice that you take away from this article, make it this: **keep interfaces small!** Interfaces are meant to define the _minimal_ behavior necessary to accurately represent an idea or concept.

Here is an example from the standard [HTTP package](https://golang.org/pkg/net/http/#pkg-overview) of a larger interface that's a good example of defining minimal behavior:

```go
type File interface {
    io.Closer
    io.Reader
    io.Seeker
    Readdir(count int) ([]os.FileInfo, error)
    Stat() (os.FileInfo, error)
}
```

Any type that satisfies the interface's behaviors can be considered by the HTTP package as a _File_. This is convenient because the HTTP package doesn't need to know if it's dealing with a file on disk, a network buffer, or a simple `[]byte`.

### 2. Interfaces Should Have No Knowledge of Satisfying Types

An interface should define what is necessary for other types to classify as a member of that interface. They shouldn't be aware of any types that happen to satisfy the interface at design time.

For example, let's assume we are building an interface to describe the components necessary to define a car.

```go
type car interface {
	Color() string
	Speed() int
	IsFiretruck() bool
}
```

`Color()` and `Speed()` make perfect sense, they are methods confined to the scope of a car. `IsFiretruck()` is an anti-pattern. We are forcing all cars to declare whether or not they are firetrucks. In order for this pattern to make any amount of sense, we would need a whole list of possible subtypes. `IsPickup()`, `IsSedan()`, `IsTank()`... where does it end??

Instead, the developer should have relied on the native functionality of [type assertion](https://yourbasic.org/golang/type-assertion-switch/) to derive the underlying type when given an instance of the **car** interface. Or, if a sub-interface is needed, it can be defined as:

```go
type firetruck interface {
	car
	HoseLength() int
}
```

Which inherits the required methods from `car` and adds one additional required method to make the car a `firetruck`.

### 3. Interfaces Are Not Classes

- Interfaces are not classes, they are slimmer.
- Interfaces don't have constructors or deconstructors that require that data is created or destroyed.
- Interfaces aren't hierarchical by nature, though there is syntactic sugar to create interfaces that happen to be supersets of other interfaces.
- Interfaces define function signatures, but not underlying behavior. Making an interface often won't [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) up your code in regards to struct methods. For example, if five types satisfy the error interface, they all need their own version of the `Error()` function.

## Additional information about interfaces

### The empty interface

The empty interface doesn't specify any methods, and as such every type in Go implements the empty interface.

```go
interface{}
```

It's for this reason that developers sometimes use a `map[string]interface{}` to work with [arbitrary JSON data](/golang/json-golang/), although I recommend using [anonymous structs instead where possible](/golang/anonymous-structs-golang/).

### Zero value of an interface

Interfaces can be `nil`, in fact, it's their zero value. That's why when we check for errors in Go, we're always checking `if err != nil`, because `err` is an interface.

### Interfaces on pointers

It's a common "gotcha" in Go to implement a method on a pointer type and expect the underlying type to implement the interface, _it doesn't work like that_.

```go
type rectangle interface {
    height() int
    width() int
}

type square struct {
    length int
}

func (sq *square) width() int {
    return sq.length
}

func (sq *square) height() int {
    return sq.length
}
```

Though you may expect it to, in this example the `square` type does **not** implement the `rectangle` interface. The `*square` type **does**. If I wanted the `square` type to implement the `rectangle` interface I would just need to remove the pointer receivers.

```go
type rectangle interface {
    height() int
    width() int
}

type square struct {
    length int
}

func (sq square) width() int {
    return sq.length
}

func (sq square) height() int {
    return sq.length
}
```
