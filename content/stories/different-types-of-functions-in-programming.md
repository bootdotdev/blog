---
title: "Different types of functions in programming"
author: Eteims
date: "2022-10-09"
images:
  - /img/800/luca-bravo-XJXWbfSo2f0-unsplash.webp.webp
dofollows:
  - "https://github.com/EteimZ"
  - "https://twitter.com/Eteims1"
  - "https://dev.to/eteimz"
categories:
  - "computer-science"
  - "python"
  - "javascript"
---

Functions are one of the most versatile tools in any programmer's toolbox.
They enable us to easily reuse code without having to repeat ourselves.
Functions are also a form of abstraction, we call them without necessarily knowing how they were implemented.

One exciting thing about functions is they come in different shapes and sizes figuratively at least.
In this article I will be discussing the different types of functions you will encounter in the wild.

## Functions

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

This is the most common type of function, they take in an input either by value or reference and return a value. 
These functions can also perform side effects. 

In the example above the function performs a side effect by altering the global variable `num`.
In the real world, the side effect can be an HTTP request or even printing to the console.

Functions are very useful but they are very error-prone and hard to test due to their side effects.

## Pure functions

```python
def sq(x):
    return x * x

sq_num = sq(2) # returns 4
```

Pure functions are just like functions but they perform no side effects. They are similar to functions in mathematics, they take in an input and produce an output. Without altering any external states.

This makes them easy to test and predictable. Pure functions are widely used in functional programming.

## Subroutine

```python
def sub(x):
    print(f"The square of {x} is {x * x}")

sub(2)
# The square of 2 is 4
```

A subroutine is a function that doesn't return a value. 
They simply perform a task, and that task can be an effect. 
After execution, they give control back to the caller. 
They could take in a value in other to perform their task.

## Coroutine

Coroutines are functions capable of multitasking cooperatively. A function that is working cooperatively can pause its execution and hand control to another function when it is idle or performing a blocking task.

Coroutines are a form of concurrency and are preferred to other concurrency models like multithreading. 
Thanks to the `async` and `await` keywords introduced in modern programming languages, they have become very common and intuitive to use. 
Below is an example of coroutines in python using the `asyncio` framework.

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

The coroutine `chill` is called three times, and each instance of it blocks for a certain period. 
When a particular coroutine starts blocking it passes control to another coroutine. 
The coroutines in the example above block for 10 seconds in total but they perform their task in 5 seconds because they worked cooperatively.

## Generators

When regular functions get called they perform their task and return to their caller if they are called again they start execution from the beginning again and return to the caller again.

Generators are functions that can pause their execution after being called, if they are called again they resume from where they stopped previously.

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

The code above implements an infinite counter using generators in python. The `next` built-in function is used to call a generator. After each call, it pauses its execution and resumes on the next call.

Here's an example of generators in JavasScript:

```javascript
function* infCount() {
  let i = 0;
  while (true) {
    yield i;
    i += 1;
  }
}

let inf = infCount();
inf.next(); // { value: 0, done: false }
inf.next(); // { value: 1, done: false }
inf.next(); // { value: 2, done: false }
inf.next(); // { value: 3, done: false }
```

## Methods

An Object is a collection of related data and functions. Functions in an object are called **methods**. 
Rather than manipulating the data directly methods are used. This is known as Encapsulation. 
The method definition is contained in the **class** of the object along with its related data. 
When an instance of the class has been created the method can be accessed via the syntax `instance-name.method-name`.  

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

The class above defines three methods. 
The `__init__` method is the constructor method, `pos` returns a tuple of the object's position and `set_pos` changes the object's position. 
The data being manipulated by the method is the `self.x` and `self.y` properties.

## Anonymous function

Anonymous functions are functions without an assigned name. They are used to perform one off tasks. 
The code below is an example of anonymous functions in python.

```python
lambda x: x * x
```

Anonymous function in JavaScript:

```javascript
function (x){
    return x *x;
}
```

They can also be used as an expression, often known as **lambda expression** and assigned to variables.

```python
sq = lambda x: x * x
sq(2) # returns 4
```

Lambda expressions in JavaScript are known as **Arrow functions**:

```javascript
const sq = x => x * x;
```

## Higher-Order Functions

Higher-order functions are functions that take in other functions as input or return other functions. Here's a list of popular higher-order functions:

- `map`
- `filter`
- `reduce`

### map

The `map` function takes in an array and another function. It then applies the function across the array.

```python
map(lambda x: x*x, [1,2,3,4,5])
```

The code above uses the `map` higher-order function in python to square all the values in an array via an anonymous function.

### filter

The `filter` higher-order function takes in an array and another function,
which is called the **predicate**. 
It selects the entries in the array that are true based on the predicate function.

```javascript
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].filter((x) => x % 2 == 0);
// [ 2, 4, 6, 8, 10 ]
```

The code above uses JavaScript's `array.filter` method and an anonymous function to filter all the even numbers in the array.

### reduce

The `reduce` higher-order function reduces an array of values to a single value using another function called the **reducer**.

```javascript
["H", "E", "L", "L", "O"].reduce((a, b) => a + b);
// "HELLO"
```

The code above uses the `array.reduce` method in JavaScript and a reducer to reduce the value of an array of strings to a string.

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

A closure is a function capable of capturing variables from where it was created.
They are functions with internal states. They are created by a **higher-order function**.

The example above has a higher-order function called `factory`. 
The function has a variable called `num`. Another function is defined within the factory function called `mult_by_10`.

The `factory` function returns the `mult_by_10` function which is the **closure**.
When the returned function is called, it still has access to the `num` value.

## Recursive function

A recursive function is a function that can call itself. Recursive functions contain a base case, 
which serves as it's termination. It also needs one or more else cases.
The recursive function serves as an alternative to iteration.

```python
def nthSum(n):
    if n == 0: # Base case
        return 0
    else: # else case
        return n + nthSum(n - 1)

nthSum(5) # returns 15
```

A recusive function that calculates the sum of n natural numbers.

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

Through this partial application new functions can be created.

```javascript
const add = (x) => (y) => x + y;

const add10 = add(10);

add10(2); // returns 12
```

The example above creates a curried function via anonymous functions in JavaScript.