---
title: "The Proper Use of Pointers in Go (Golang)"
author: Lane Wagner
date: "2019-09-25"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/photo-1497005367839-6e852de72767.webp
---

Go has become increasingly popular in recent years, especially in my local area. It has been consistently displacing other backend languages like Ruby, Python, C# and Java. Go is wanted for its simplicity, explicitness, speed, and low memory consumption.

Many developers that are new to the language, or new to a language that can handle memory directly using pointers end up misusing those pointers.

## What Is a Pointer?

A pointer is a variable that stores the address of a value, rather than the value itself. If you think of a computer's memory (RAM) as a JSON object, a pointer would be like the key, and a normal variable would be the value.

```json
{
  "pointer": "variableValue"
}
```

Lets see one in action:

```go
package main

import "fmt"

func main() {
	// create a normal string variable
	name := "original"
	// pass in a pointer to the string variable using '&'
	setName(&name, "boot.dev")
	fmt.Println(name)
}

func setName(ptr *string, newName string) {
	// dereference the pointer so we can modify the value
	// and set the value to "boot.dev"
	*ptr = newName
}
```

This prints:

```
boot.dev
```

As you can see, because we have a pointer to the address of the variable_,_ we can modify its value, even within the scope of another function. If the value were not a pointer, this would not work:

```go
package main

import "fmt"

func main() {
	name := "original"
	setNameBroken(name, "boot.dev")
	fmt.Println(name)
}

func setNameBroken(ptr string, newName string) {
	ptr = newName
}
```

prints:

```
original
```

Pointers can be useful, but in the same way that they are useful, they can be dangerous. For example, if we dereference a pointer that has no value, the program will panic. For this reason we always check if an error value is nil before trying to print it.

## Syntax

**1\. Creating a pointer: &**

```go
newString := ""
newStringPointer := &newString
```

If you print that pointer you will see a memory address.

```go
package main

import "fmt"

func main() {
	newString := ""
	newStringPointer := &newString
	fmt.Println(newStringPointer)
}
```

prints: 0xc00000e1e0

Which is the memory address of that variable in your machine.

**2\. Describing a pointer: \***

In a function signature or type definition, the \* is used to designate that a value is a pointer.

```go
func passPointer(pointer *string) {
}
```

**3\. Dereferencing a pointer: \***

It can be slightly confusing, but the \* is used to describe a pointer and it is also used as an operator to dereference a pointer.

```go
func derefPointer(pointer *string) {
	newStringVariable := *pointer
        // newStringVariable is just a normal string
}
```

## When Should I Use a Pointer?

There are probably many nuanced cases for when a pointer is a good idea, but I would guess that 95% of the time when you use a pointer, it should be for one the following reasons:

**1\. A function that mutates one of its parameters**

When I call a function that takes a pointer as an argument, I expect that my variable will be mutated. If you aren't mutating the variable in your function, then you probably shouldn't be using a pointer.

**2\. Better Performance**

If you have a string that contains an entire novel in memory it gets really expensive to copy that variable each time it is passed to a new function. It may be worthwhile to pass a pointer instead, which will save CPU and memory. This comes at the cost of readability however, so only make this optimization if you must.

**3\. Need a Nil Value Option**

Sometimes a function needs to know what something's value is, as well as if it exists or not. I usually use this when [decoding JSON](/golang/json-golang/) to know if a field exists or not. For example, if a JSON object is:

```
{ "name": "boot.dev" } ----> *name: "boot.dev"
```

```
{ "name": "" } ----------> *name: ""
```

```
{} ----------------------> *name: nil
```

These are some rules of thumb for when to use pointers in your code. If you are unsure, and a normal value will work just fine, I would advise avoiding the pointer. Pointers are useful tools but can lead to nasty bugs or unreadable code quite easily.
