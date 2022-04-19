---
title: "Removing Duplicates From a List in Python"
author: Lane Wagner
date: "2021-12-09"
categories: 
  - "python"
images:
  - /img/800/list.webp
---

Let's go over a few idiomatic ways to remove duplicates from lists in Python.

## Method #1 - Create a new list (simplest)

This is the easiest algorithm to code, but because it requires creating a new list, also requires more memory and is a bit slower.

```py
def remove_duplicates(original):
  deduped = []
  for item in original:
    if item not in deduped:
      deduped.append(item)
  return deduped
```

We take advantage of Python's [in keyword](https://www.w3schools.com/python/ref_keyword_in.asp) here, only adding each item to the final list if it isn't already present.

## Method #2 - Create a new list with syntactic sugar (less code, harder to understand)

```py
def remove_duplicates(original):
  deduped = []
  [deduped.append(item) for item in original if item not in deduped]
  return deduped
```

This is the same exact code from a performance standpoint but only uses one line. If you're into [code golf](https://code.golf/), then this might be your solution.

{{< cta1 >}}

## Method #3 - Use the built-in "set" data structure (fast, loses order)

A `[set()](https://www.w3schools.com/python/python_sets.asp)` is a group of values that doesn't contain any duplicates. By casting a list into a set and back, you remove all duplicates. The main drawback here is that you'll lose your ordering.

```py
def remove_duplicates(original):
  return list(set(original))
```

This method will be faster in most circumstances than the previous two because each transfer is `O(n)` in [big-o notation](https://boot.dev/course/884342fc-5469-47b4-8125-8bfc897428a8/67214b76-2e4b-4fc1-9610-2cf8c7c1c3a2/02e0d979-6758-493f-bf4f-bf7256fa7174/) terms. A group of two `O(n)` operations is faster than one `O(n^2)` operation. As a bonus, it even uses less code.

## Method #4 - Use an ordered dictionary (fast, maintains order)

By using the [collections](https://docs.python.org/3/library/collections.html) libraries' [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) type, we can maintain the ordering of the list while maintaining the same Big-O that we had with a `set()`.

```py
from collections import OrderedDict

def remove_duplicates(original):
  return list(OrderedDict.fromkeys(original))
```
