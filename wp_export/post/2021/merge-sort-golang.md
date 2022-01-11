---
title: "Merge Sort in Golang with Examples"
date: "2021-06-10"
categories: 
  - "golang"
---

Merge sort is a recursive sorting algorithm and, luckily for us, it's quite a bit faster than [bubble sort](https://qvault.io/golang/bubble-sort-golang/). Merge sort is a [divide and conquer algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm).

### Divide

- Divide the input slice into two (equal) halves
- Recursively sort the two halves

### Conquer

- Merge the two halves to form a sorted array

![](images/merge_sort_gif.gif)

## Full example of the merge sort algorithm

Merge sort actually has two functions involved, the recursive `mergeSort` function, and the `merge` function.

Let's write the `mergeSort()` function first. It's a recursive function, which means it calls itself, and in this case, it actually calls itself _twice_. The point of the `mergeSort` function is to split the array into two roughly equal parts, call itself on those parts, then call `merge()` to fit those halves back together.

```
func mergeSort(items []int) []int {
    if len(items) < 2 {
        return items
    }
    first := mergeSort(items[:len(items)/2])
    second := mergeSort(items[len(items)/2:])
    return merge(first, second)
}
```

The `merge()` function is used for merging two sorted lists back into a single sorted list, its where the "magic" really happens. At the lowest level of recursion, the two "sorted" lists will each have a length of 1. Those single element lists will be merged into a sorted list of length two, and we can build of from there.

```
func merge(a []int, b []int) []int {
    final := []int{}
    i := 0
    j := 0
    for i < len(a) && j < len(b) {
        if a[i] < b[j] {
            final = append(final, a[i])
            i++
        } else {
            final = append(final, b[j])
            j++
        }
    }
    for ; i < len(a); i++ {
        final = append(final, a[i])
    }
    for ; j < len(b); j++ {
        final = append(final, b[j])
    }
    return final
}
```

## Using the algorithm in code

```
func main() {
    unsorted := []int{10, 6, 2, 1, 5, 8, 3, 4, 7, 9}
    sorted := mergeSort(unsortedInput)

    // sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
```

## Why use merge sort?

### Pros

- Fast. Merge sort is much faster than bubble sort, being `O(n*log(n))` instead of `O(n^2)`.
- Stable. Merge sort is also a [stable sort](https://en.wikipedia.org/wiki/Category:Stable_sorts) which means that values with duplicate keys in the original list will be in the same order in the sorted list.

### Cons

- Extra memory. Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires an extra array in memory to merge the sorted subarrays.
- Recursive: Merge sort requires many recursive function calls, and function calls can have significant resource overhead.

If you need a sorting algorithm to use in a production system, I recommend [not reinventing the wheel and using the built-in sort.Sort method](https://qvault.io/golang/sorting-in-go-dont-reinvent-this-wheel/).

## Merge sort Big-O complexity

Merge sort has a complexity of `O(n*log(n))`. Don't be fooled because there aren't an explicit number of for-loops to count in the code. In merge sort's case, the number of recursive function calls is important.
