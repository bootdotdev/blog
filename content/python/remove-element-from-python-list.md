---
title: "Complete Guide to Removing Elements From Lists in Python"
author: lane
date: "2021-12-09"
categories:
  - "python"
images:
  - /img/800/ruinreborn_fantasy_art_simple_background_fire_and_ice_snake_e_e4f734ba-e6ff-4247-8c0f-482ebbedc611_2.png.webp
---

While lists aren't the most efficient [data structure](https://www.boot.dev/courses/learn-data-structures-python) if you'll be doing lots of deleting from the middle, there are definitely good ways to accomplish the task. The built-in [`remove()`](https://python-reference.readthedocs.io/en/latest/docs/list/remove.html) method should be your first option. Let's go over some examples.

## Remove element in Python list by value

```py
primes = [2, 3, 5, 5, 7, 11]

primes.remove(5)

print(primes)
# [2, 3, 5, 7, 11]

primes.remove(5)
# [2, 3, 7, 11]

primes.remove(5)
# careful, this will throw an error
# ValueError: list.remove(x): x not in list
```

If you want to safely remove items, and you aren't sure if they exist in the list or not, you can either catch the error:

```py
try:
	primes.remove(5)
except Exception as e:
	print("not in list")
```

Or, you can check for existence first:

```py
if 5 in primes:
	primes.remove(5)
```

## Remove an element in Python list by index

The `del` statement is a built-in keyword that allows you to remove items from lists. The simplest example deletes the item at a given index.

```py
primes = [2, 3, 5, 5, 7, 11]

# delete the second item
del primes[1]

print(primes)
# [2, 5, 5, 7, 11]
```

Again, you need to be careful. If the index doesn't exist an error will be raised.

```
primes = [2, 3, 5, 5, 7, 11]

# delete the eleventh item
del primes[10]
```

`IndexError: list assignment index out of range`

```py
if len(primes) >= 10:
	del primes[10]
```

## Remove multiple of items from a python list

```py
primes = [2, 3, 5, 5, 7, 11]

# deleting items from 2nd to 4th
del primes[1:4]

print(primes)
# [2, 7, 11]
```

## Remove item by index and return it

The `.pop()` method removes an item from a list by index and returns that item.

```py
primes = [2, 3, 5, 7]

# pop the second element
popped = primes.pop(1)

print("popped:", popped)
# 3

print("list:", primes)
# [2, 5, 7]
```

If you don't pass an index parameter to `pop()` it will default to `-1` and remove the last element from the list. Just like the other methods, if you pass in a number too large, you'll get the following error.

`IndexError: pop index out of range`
