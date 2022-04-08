---
title: "Sorting in Go - Don't Reinvent This Wheel"
author: Lane Wagner
date: "2020-05-27"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/eac4ebdf-829a-4d81-8f8b-4dc63a29b174.jpeg
---

Sorting is a common task in programming, and for that reason, most languages have a default sorting algorithm in their standard library. Go is one such language. Go has gone about providing sorting functionality in one of the most elegant ways possible, via an interface.

```go
type Interface interface {
    // Len is the number of elements in the collection.
    Len() int
    // Less reports whether the element with
    // index i should sort before the element with index j.
    Less(i, j int) bool
    // Swap swaps the elements with indexes i and j.
    Swap(i, j int)
}
```

Any type that satisfies this interface can be sorted using the standard library's [sort.Sort()](https://golang.org/pkg/sort/#Sort) function. There is rarely a reason to sort any other way because the sort function is O(n log(n)) in the worst case. You can take a look at the various algorithms that are used, depending on the data to be sorted, [here](https://golang.org/src/sort/sort.go).

## Sorting a Slice

The first thing to do, no matter what we are sorting is to create a custom type. A custom type will allow us to implement the _Len()_, _Less()_ and _Swap()_ methods on it.

```go
type mySlice []int
```

Then we implement the methods to fulfill the sort.Interface interface:

```go
func (ms mySlice) Len() int {
	return len(ms)
}

func (ms mySlice) Less(i, j int) bool {
	return ms[i] < ms[j]
}

func (ms mySlice) Swap(i, j int) {
	ms[i], ms[j] = ms[j], ms[i]
}
```

Let's test it out:

```go
package main

import (
	"fmt"
	"math/rand"
	"sort"
)

type mySlice []int

func (ms mySlice) Len() int {
	return len(ms)
}

func (ms mySlice) Less(i, j int) bool {
	return ms[i] < ms[j]
}

func (ms mySlice) Swap(i, j int) {
	ms[i], ms[j] = ms[j], ms[i]
}

func main() {
	ms := mySlice{}
	for i := 0; i < 10; i++ {
		ms = append(ms, rand.Intn(100))
	}
	fmt.Println("pre-sort:", ms)
	sort.Sort(ms)
	fmt.Println("post-sort:", ms)
}
```

prints:

```
pre-sort: [81 87 47 59 81 18 25 40 56 0]
post-sort: [0 18 25 40 47 56 59 81 81 87]
```

## Changing It Up

Rather than changing the way we call the sort function, if we want different behavior we just change the way we implement the interface. For example, if we want to sort greatest to least we just change the _Less()_ function:

```go
func (ms mySlice) Less(i, j int) bool {
	return ms[i] > ms[j]
}
```

which prints:

```
pre-sort: [81 87 47 59 81 18 25 40 56 0]
post-sort: [87 81 81 59 56 47 40 25 18 0]
```

## Other Types

Sorting integers is pretty boring. Besides, if we are just going to sort integers we can use the pre-defined [IntSlice](https://golang.org/pkg/sort/#IntSlice) type instead of coding it all again ourselves. Let's sort a slice of structs:

```go
type mtgCard struct {
	manaCost int
	name     string
}

type mtgCards []mtgCard
```

Now we implement the sorting:

```go
func (mCards mtgCards) Len() int {
	return len(mCards)
}

func (mCards mtgCards) Less(i, j int) bool {
	if mCards[i].manaCost < mCards[j].manaCost {
		return true
	} else if mCards[i].manaCost == mCards[j].manaCost {
		return mCards[i].name < mCards[j].name
	}
	return false
}

func (mCards mtgCards) Swap(i, j int) {
	mCards[i], mCards[j] = mCards[j], mCards[i]
}
```

The _Less()_ function we made will sort by manacost unless their is a tie, in which case it will sort by name. Let's test it out:

```go
func main() {
	mCards := mtgCards{
		{
			manaCost: 7,
			name:     "ajani",
		},
		{
			manaCost: 2,
			name:     "liliana",
		},
		{
			manaCost: 2,
			name:     "chandra",
		},
		{
			manaCost: 4,
			name:     "garruk",
		},
		{
			manaCost: 4,
			name:     "jace",
		},
		{
			manaCost: 5,
			name:     "bolas",
		},
	}

	fmt.Println("pre-sort:", mCards)
	sort.Sort(mCards)
	fmt.Println("post-sort:", mCards)
}
```

prints:

```
pre-sort: [{7 ajani} {2 liliana} {2 chandra} {4 garruk} {4 jace} {5 bolas}]
post-sort: [{2 chandra} {2 liliana} {4 garruk} {4 jace} {5 bolas} {7 ajani}]
```

## Don't Reinvent It

The standard library's sorting methods are powerful, don't code them yourself unless you have a very extreme use case. Take a look at some of the [other functionality](https://golang.org/pkg/sort/) provided by the sort package as well if you have time. Searching, stable sorting, and checking if a type is sorted are some pretty awesome features.
