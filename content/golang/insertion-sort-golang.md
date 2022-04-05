---
title: "How to Write Insertion Sort in Go"
author: Lane Wagner
date: "2021-06-14"
categories: 
  - "golang"
images:
  - /img/insert.webp
---

Insertion sort builds a final sorted list one item at a time. It's much less efficient on large lists than more advanced algorithms like quicksort or [merge sort](/golang/merge-sort-golang/). Insertion sort is a simple algorithm that works just like you would arrange playing cards in your hands. A slice is first split into sorted and unsorted sections, then values from the unsorted section are inserted into the correct position in the sorted section.

![](/img/insertionsort.gif)

## Full example of the insertion sort algorithm

```go
func insertionSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := i; j > 0 && arr[j-1] > arr[j]; j-- {
			arr[j], arr[j-1] = arr[j-1], arr[j]
		}
	}
	return arr
}
```

As you can see, the `insertionSort()` function starts by iterating over the entire slice in a nested for loop. The job of the inner for loop is to consume one value for each repetition, and grow the sorted output list, which are all the elements before index `i`. At each repetition, insertion sort removes one element from the input data, finds the location it belongs within the sorted first section, and inserts it there. It repeats until no input elements remain.

## Using insertion sort in code

```go
func main() {
    fmt.Println(insertionSort([]int{5,3,2,1,0,4))
    // prints
    // [0, 1, 2, 3, 4, 5]
}
```

{{< cta1 >}}

## Why use insertion sort?

Insertion sort has a Big O complexity of `O(n^2)`, because that is its worst-case complexity. The outer loop of insertion sort executes `n` times, while the inner loop depends on the input. In the worst case (a reverse sorted array) the inner loop executes `n` times as well. In the best case (a sorted array) the inner loop immediately breaks resulting in a total complexity of `O(n)`.

Like [bubble sort](/golang/bubble-sort-golang/), the algorithm is just too slow for general-purpose production use, but can be a great learning tool. Here are some additional properties of insertion sort.

- Simple implementation, easy to write
- Fast for very small data sets
- Faster than other simple sorting algorithms like Bubble Sort
- Adaptive: Faster for partially sorted data sets
- Stable: Does not change the relative order of elements with equal keys
- In-Place: Only requires a constant amount of memory
- Online: Can sort a list as it receives it

Some production sorting implementations use merge sort for very small inputs under a certain threshold (very small, like 10ish). Insertion sort is better for very small lists than some of the faster algorithms because:

- There is no recursion overhead
- Tiny memory footprint
- It's a stable sort as described above
