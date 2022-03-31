---
title: "How and Why to Write Enums in Go"
author: Lane Wagner
date: "2021-04-19"
categories: 
  - "golang"
images:
  - /img/list-with-pencil-and-paper.webp
---

An enum (short for enumerator), is a set of named constant values. An enum is a powerful tool that allows developers to create complex sets of constants that have useful names and yet simple and unique values.

## Example of an idiomatic enum

Within a constant declaration, the [iota](https://golang.org/ref/spec#Iota) keyword creates enums as successive untyped integer constants.

```go
type BodyPart int

const (
    Head BodyPart = iota // Head = 0
    Shoulder             // Shoulder = 1
    Knee                 // Knee = 2
    Toe                  // Toe = 3
)
```

## Why should you use enums?

Let's look at some questions you may have about enums. At first, enums may not seem useful, but I can assure you they are.

### And if you want an integer constant, can't you just use a normal `const`? E.g. `const head = 0`?

Yes, you _could_ do that, but enums are powerful by how they group _sets_ of constants together and guarantee _unique_ values. By using an enum, you're ensured by the compiler that none of the constants in your group, e.g. `Head`, `Shoulder`, `Knee`, and `Toe`, have the same value.

### Why not just use strings for unique values? For example, `const Head = "head"` and `const Shoulder = "shoulder"`?

Besides the overlapping answer of the compiler not guaranteeing uniqueness, a string takes much more memory and can lead to performance issues under constrained circumstances. If you have a group of 4, 10, or even 100 unique values, do you really need to store an entire `string`? An `int` will take up less room in your program's memory.

It's not just about the space though, especially with how powerful modern hardware is. Let's say you had some configuration variables such as the following.

```go
const (
    statusSuccess = iota
    statusFailed
    statusPending
    statusComplete
)
```

Pretend you need to change the name of `statusFailed` to `statusCancelled`, perhaps to become consistent with the rest of the codebase. If you had previously used the value `failed` instead of an enum, and now that value is strewn all across various databases, it becomes _really_ hard to change it. If you had just used an `enum`, you can [change the name](https://qvault.io/clean-code/naming-variables/) without touching the value and your code remains clean.

## How to create an enum starting from 1

Sometimes, if you're a masochist, or perhaps a Lua developer, you'll want your list of enums to start with a value of `1` instead of the default `0`, you can do that easily in Go.

```go
const (
    Head = iota + 1  // 1
    Shoulder            // 2
    Knee                 // 3
    Toe                   // 4
)
```

## Create an enums with multipliers

The `iota` keyword simply represents an incrementing integer constant that's one number larger each time it's used within the same `const` block. You can use it to do whatever math you like.

```go
const (
    Head = iota + 1        // 0 + 1 = 1
    Shoulder = iota + 2  // 1 + 2 = 3
    Knee = iota * 10      // 2 * 10 = 20
    Toe = iota * 100      // 3 * 100 = 300
)
```

With that in mind, remember that just because you _can_ doesn't mean you _should_.

## Using enums that skip values

If you want to skip a value just use the `_` character like you do to ignore return variables.

```go
const (
    Head = iota // Head = 0
    _
    Knee // Knee = 2
    Toe // Toe = 3
)
```

## String Enums in Go

Go doesn't have any built-in `string` functionality for enums, but it's pretty easy to implement a `String()` method. By using a `String()` method instead of setting the constants themselves as string types, you can get the same benefits of an enum with the "printability" of a string.

```go
type BodyPart int

const (
    Head BodyPart = iota // Head = 0
    Shoulder // Shoulder = 1
    Knee // Knee = 2
    Toe // Toe = 3
)

func (bp BodyPart) String() string {
    return []string{"Head", "Shoulder", "Knee", "Toe"}[bp]]
}
```

There are some "gotchas" to this approach, however, so be careful. If the number of declarations in your `const` block is different than the number of entries in the "[constant slice](https://qvault.io/golang/golang-constant-maps-slices/)" created by your `String()` method, the compiler won't alert you to the potential "out of bounds" error. Also, if you ever update the name of one of the constants don't forget to update its corresponding string in the list.
