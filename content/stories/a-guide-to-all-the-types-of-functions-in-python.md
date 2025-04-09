---
title: "All the Kinds of Functions in Python"
author: eteims
date: "2022-10-13"
images:
  - /img/800/ruinreborn_magical_rune_rune_carved_on_stone_fantasy_art_simp_c96b2dca-cbe3-44a7-9cd4-f2499ac36519_3.png.webp
categories:
  - "python"
---

Functions are one of the most versatile tools in any Python programmer's toolbox. They enable code reuse and provide a form of abstraction. Python offers many different types of functions. In this article, I will be discussing the different types of functions you will encounter as a Python developer.

## Impure Functions

```python
num = 0

def sq(x):
    global num
    num = x # side effect
    return x * x

sq_num = sq(2) # returns 4
print(num) # 2
print(sq_num) # 4
```

Impure functions are one of the most common type of function. they take an input either by value or reference and return a value. They are impure because they perform [side effects](<https://en.wikipedia.org/wiki/Side_effect_(computer_science)>).

In the example above, the function performs a side effect by altering the global variable `num`. This is a valid side effect, but you'll often also encounter "side effects" like HTTP requests, printing to the console or accessing a database.

Impure functions are useful but are often error-prone and hard to test due to their side effects.

## Pure functions

```python
def sq(x):
    return x * x

sq_num = sq(2) # returns 4
```

Pure functions are functions with no side effects. They are similar to [functions](<https://en.wikipedia.org/wiki/Function_(mathematics)>) in mathematics. They take in an input and produce an output without altering any external states.

It makes them easy to test and predictable. Pure functions are widely used in [functional programming](https://en.wikipedia.org/wiki/Functional_programming)

## Subroutine

```python
def sub(x):
    print(f"The square of {x} is {x * x}")

sub(2)
# The square of 2 is 4
```

A subroutine is a function that doesn't return a value. It performs a task, and that task can be an effect. It could take in a value in other to perform it's task. After execution, it gives control back to the caller.

## Coroutine

Coroutines are functions capable of multitasking cooperatively. A function working cooperatively can pause its execution and hand control off to another function when it is idle or performing a [blocking](<https://en.wikipedia.org/wiki/Blocking_(computing)>) task.

Coroutines are a form of [concurrency](<https://en.wikipedia.org/wiki/Concurrency_(computer_science)>). They are preferred to other concurrency models like [multithreading](<https://en.wikipedia.org/wiki/Multithreading_(computer_architecture)>). Thanks to the `async` and `await` keywords introduced in [PEP 492](https://peps.python.org/pep-0492/), they have become common and intuitive. Below is an example of coroutines in Python using the [asyncio](https://docs.python.org/3/library/asyncio.html) library.

```python
import asyncio
import time

async def chill(label: str, n: int):
    print(f"{label}: Chilling for {n} seconds")
    await asyncio.sleep(n)
    print(f"Done chilling for {label}")


async def main():
    task1 = asyncio.create_task(chill("A", 2))
    task2 = asyncio.create_task(chill("B", 5))
    task3 = asyncio.create_task(chill("C", 3))

    starttime = time.perf_counter()
    await task1
    await task2
    await task3
    endtime = time.perf_counter()
    print(f"Task finished in {endtime - starttime}")

asyncio.run(main())

""" Sample output:
A: Chilling for 2 seconds
B: Chilling for 5 seconds
C: Chilling for 3 seconds
Done chilling for A
Done chilling for C
Done chilling for B
Task finished in 5.004022927998449
"""
```

The coroutine `chill` is called three times, and each instance of it blocks for a certain period. When a particular coroutine starts blocking it passes control to another coroutine. The coroutines in the example above block for a total of 10 seconds but they perform their task in 5 seconds in real-time because they worked cooperatively at the same time.

## Generators

When regular functions are called they perform their task and return to their caller. If they are called again they start execution from the beginning and return to their caller again.

Generators are functions that can pause their execution after being called. If they are called again they resume from where they stopped previously.

```python
def infCount():
    """
    Infinite counter
    """
    i = 0
    while True:
        yield i
        i += 1

# Usage
inf = infCount()
next(inf) # 0
next(inf) # 1
next(inf) # 2
```

The code above implements an infinite counter using generators in Python. The built-in `next()` function is used to call a generator. After each call, it pauses its execution and resumes on the next call.

## Methods

An Object is a collection of related data and functions. Functions in an object are called **methods**. Rather than manipulating the data directly, methods are used. This is known as **Encapsulation**. The method definition is contained in the **class** of the object along with its related data. When an instance of the class has been created the method can be accessed via the syntax `instance-name.method-name`.

```python
class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return (self.x, self.y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        print(f"New positiom {self.x} and {self.y}")

p = Position(2,3)
p.pos() # (2, 3)
p.set_pos(4, 5) # New positiom 4 and 5
p.pos() # (4, 5)
```

The class above defines 3 methods. The `__init__()` method is the constructor, `pos()` returns a tuple of the object's position and `set_pos()` changes the object's position. `self.x` and `self.y` are member variables mutated by the various methods.

## Anonymous function

Anonymous functions are functions without an assigned name. They are used to perform one-off tasks. The code below is an example of and anonymous function in Python.

```python
lambda x: x * x
```

Anonymous functions are also called **lambda expressions**. The functions can then be saved in variables.

```python
sq = lambda x: x * x
sq(2) # returns 4
```

## Higher-Order Functions

Higher-order functions take in other functions as input or return other functions. Here's a list of popular higher-order functions:

- `map()`
- `filter()`
- `reduce()`

### map()

The `map()` higher-order function takes in an array and another function. It then applies the function across the array.

```python
data = map(lambda x: x*x, [1,2,3,4,5])
list(data) # [1, 4, 9, 16, 25]
```

The code above uses the `map` higher-order function in Python to square all the values in the array via an anonymous function.

The map function returns an iterator which needs to be converted to a list to get the new values.

### filter()

The `filter()` higher-order function takes in an array and another function,
which is called the **predicate**.
It selects the entries in the array that are true based on the predicate function.

```python
data = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])
list(data) # [2, 4, 6, 8, 10]
```

The filter function also returns an iterator.

### reduce()

The `reduce()` higher-order function reduces an array of values to a single value using another function called the **reducer**.

```python
from functools import reduce

reduce(lambda a, b: a + b, ["H", "E", "L", "L", "O"])
# "HELLO"
```

The `reduce` higher-order function needs to be imported from [functools](https://docs.python.org/3/library/functools.html).

## Closures

```python
def factory():
    num = 10
    def mult_by_10(inp):
        return num * inp
    return mult_by_10

clos = factory()
clos(2) # returns 20
```

A closure is a function capable of capturing variables from where it was created. They are functions with internal state. They are created by a **higher-order function**.

The example above has a higher-order function called `factory`. The function has a variable called `num`. Another function is defined within the factory function called `mult_by_10`.

The `factory` function returns the `mult_by_10` function which is the **closure**. When the returned function is called, it still has access to the `num` value.

## Recursive function

A recursive function is a function that can call itself. It has a base case,
which serves as it's termination point. Recursion is often an alternative to iteration.

```python
def nthSum(n):
    if n == 0: # Base case
        return 0
    else: # else case
        return n + nthSum(n - 1)

nthSum(5) # returns 15
```

`nthSum()` is a recursive function that calculates the sum of n natural numbers.

## Curried function

A curried function is a function whose inputs can be partially applied. Curried functions are a form of **closures**.

```python
def add(x):
    def add2(y):
        return x + y
    return add2

add10 = add(10)
add10(2) # returns 12
```

Through this partial application, new functions can be created.

```python
from functools import partial

def add(x, y):
    retrun x + y

add10 = partial(add, y=10)
add10(2) # returns 12
```

A non-curried function can be partially applied via the `partial` function from `functools`.

## Decorators

Decorators are functions which add extra functionality to previously existing functions. They are similar to closures but have a special syntax.

```python
def decor(func):
    def wrapp():
        print("############")
        func()
        print("############")
    return decor

@decor
def hello():
    print("Hello World!")

"""Sample Output

############
Hello world!
############

"""
```

The example above defines a decorator called `decor` which takes in a function `func` as a parameter. Another function called `wrapp` is defined within `decor`. The `wrapp` function serves as a wrapper to the `func` function.

The `decor` is then used to decorate the `hello` function. Decorators are just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar).

```python
decor(hello)

"""Sample Output

############
Hello world!
############

"""
```

Python offers a wide range of functions and techniques for creating functions. Knowing the different types of functions helps you write better code, and also understand other programmers' code.
