---
title: "Loops in Python"
author: lane
date: "2024-12-23"
categories:
  - "python"
images:
  - /img/800/loopsinthesky.png.webp
imageAlts:
  - "loops in the sky"
---

If you're new to Python, or perhaps coding in general (welcome!), loops are what allow us to do the same thing over and over and over again, without having to re-type the same code each time. For example, let's pretend I want to print the numbers 0-9.

I _could_ do this:

```python
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
```

However, it would save me a lot of time typing to use a _loop_. Especially if I wanted to do the same thing _one thousand_ or _one million_ times.

A _"for loop"_ in Python is written like this:

```python
for i in range(0, 10):
    print(i)
```

`i` replaces the numbers `0` to `9`. In English, the code says:

1. Start with `i` equals `0`. (`i in range(0)`)
2. If `i` is not less than 10 (`range(0, 10)`), exit the loop. Else:
   1. Print `i` to the console. (`print(i)`)
   2. Add `1` to `i`. (`range` defaults to incrementing by 1)
   3. Go back to step `2`.

The result is that the numbers `0-9` are logged to the console in order.

_We're making all the static content from our Boot.dev courses available for free here on the blog. This one is the "Loops" chapter from [Learn to Code in Python](https://www.boot.dev/courses/learn-code-python). If you want to try the far more interactive version of the course, do check it out!_

**By the way, whitespace matters in Python!**

The body of a for-loop _must_ be indented; otherwise, you'll get a syntax error. Every line in the body of the loop must be indented in the same way - we use the "4 spaces" convention. Pressing the `<tab>` key should automatically insert 4 spaces.

## Range Continued

The `range()` [function](/tutorials/python/functions) we've been using in our `for` loops actually has an optional 3rd parameter: the "step".

```python
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8
```

The "step" parameter determines how much to add to `i` in each iteration of the loop. You can even go backwards:

```python
for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1
```

## Iterating over lists

While explictly looping from one number to another is _useful_, more often than not you'll probably want to iterate over all the elements in a [list](/tutorials/python/lists). In my opinion, Python has _the most elegant_ syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:

```py
trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple
```

`tree`, the [variable](/tutorials/python/variables) declared using the `in` keyword, directly accesses the value in the list rather than the index of the value. If we don't need to update the item and only need to access its value then this is a more clean way to write the code.

## While

Python has another type of loop, the `while` loop. It's a loop that continues `while` a condition remains `True`. The syntax is simple:

```python
while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)
```

The example above is hardcoded to continue forever, creating an infinite loop. Typically, a `while` loop's condition will have an explicit comparison that determines when the loop ends:

```python
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)
```

With loops, we can efficiently automate repetitive tasks, manage data sequences, and streamline complex processes in programming. Mastering loops empowers us to write cleaner, more efficient code, and to embrace the true power of programming automation.
