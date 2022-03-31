---
title: "Should You Return Empty or Nil Slices in Go?"
author: Lane Wagner
date: "2020-09-03"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/slice.jpeg
---

In Go, we often need to return zero values. Idiomatic Go encourages the use of guard clauses, and [guard clauses](https://qvault.io/2019/08/16/guard-clauses-how-to-clean-up-conditionals/) necessitate the need to return early. When returning early with an error, by convention all other return values should be zero values. The confusion arises with data types like maps and slices. Should maps and slices be returned as a simple `nil` value, or should an empty but instantiated value be returned?

For example, should we use this syntax?

```go
func getItems(url string) ([]string, error) {
	data, err := makeRequest(url)
	if err != nil {
		return nil, err
	}
	items, err := unpack(data)
	if err != nil {
		return nil, err
	}
	return data, nil
}
```

Or perhaps this syntax?

```go
func getItems(url string) ([]string, error) {
	data, err := makeRequest(url)
	if err != nil {
		return []string{}, err
	}
	items, err := unpack(data)
	if err != nil {
		return []string{}, err
	}
	return data, nil
}
```

## The Differences

I ran a quick bit of code to show some of the differences between nil and empty slices:

```go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var nilSlice []string
	fmt.Println(nilSlice)                     // Output: []
	fmt.Println(len(nilSlice), cap(nilSlice)) // Output: 0 0
	fmt.Println(nilSlice == nil)              // Output: true
	dat, _ := json.Marshal(nilSlice)
	fmt.Println(string(dat)) // Output: null

	emptySlice := []string{}
	fmt.Println(emptySlice)                       // Output: []
	fmt.Println(len(emptySlice), cap(emptySlice)) // Output: 0 0
	fmt.Println(emptySlice == nil)                // Output: false
	dat, _ = json.Marshal(emptySlice)
	fmt.Println(string(dat)) // Output: []
}
```

As you can see there are some similarities between nil and empty slices:

- Both have zero length and cap
- Both print `[]`
- Both can be used the _same way_ in range loops and append functions (not shown here)

They differ in the following ways:

- Only a `nil` slice will succeed a nil check
- When [encoded as JSON](https://qvault.io/golang/json-golang/) using the standard library, the nil slice becomes `null` and the empty slice becomes `[]`

## Which Should I Do?

**Generally speaking, prefer nil**.

According to the [Go wiki](https://github.com/golang/go/wiki/CodeReviewComments#declaring-empty-slices), nil is the preferred style. When we just need to return an empty slice `nil` will work great in practically all cases. It's also easier to type `nil` than `[]string{}` or `make([]string, 0)` and typically gets syntax highlighted which makes it easier to read.
