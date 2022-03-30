---
title: "Writing Bubble Sort in Go from Scratch"
author: Lane Wagner
date: "2021-06-08"
categories: 
  - "golang"
images:
  - /img/bubbles-in-water.webp
---

Bubble sort is named for the way elements "bubble up" to the top of the list. Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the [slice](https://qvault.io/golang/golang-make-maps-and-slices/) until the whole list is completely sorted.

## Full example of the bubble sort algorithm

```go
func bubbleSort(input []int) []int {
    swapped := true
    for swapped {
        swapped = false
        for i := 1; i < len(input); i++ {
            if input[i-1] > input[i] {
                input[i], input[i-1] = input[i-1], input[i]
                swapped = true
            }
        }
    }
    return input
}
```

## Using the algorithm in code

```go
func main() {
    unsorted := []int{10, 6, 2, 1, 5, 8, 3, 4, 7, 9}
    sorted := bubbleSort(unsortedInput)

    // sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
```

## Why use bubble sort?

Bubble sort is famous for how easy it is to write. It's one of the slowest sorting algorithms, but can be useful for a quick script or when the amount of data to be sorted is guaranteed to be small. If you need a sorting algorithm to use in a production system, I recommend [not reinventing the wheel and using the built-in sort.Sort method](https://qvault.io/golang/sorting-in-go-dont-reinvent-this-wheel/).

## Bubble sort Big-O complexity

While bubble sort is considered fast and easy to write, it's actually one of the slowest sorting algorithms out there. Because bubble sort needs to move through the entire list for each element in the list, which in code is a nested [for-loop](https://qvault.io/golang/golang-for-loop/), bubble sort has a complexity of `O(n^2)`.
