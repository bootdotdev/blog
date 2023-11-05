---
title: "Understanding Stacks: Python Implementation of a Core Data Structure"
author: Lane Wagner
date: "2023-10-06"
categories: 
  - "python"
  - "computer-science"
images:
  - /img/800/stackofrocksfantasygame.png.webp
---

A **stack** is an abstract data type that serves as a collection of elements. The name "stack" originates from the analogy of items physically stacked on top of each other. Just like a stack of plates at a buffet, plates can be added, removed, and viewed from the top. However, plates further down are not immediately accessible.

![Stack Image](/img/800/stackclass.png.webp)

A stack operates on a `LIFO` (last in, first out) principle. This means that the most recently added item will be the first to be removed (as opposed to a [queue](/python/queue-data-structure-python/), which is `FIFO`).

{{< bdyoutube SD45xbKReT4 >}}

### Basic Stack Operations:

* **Push**: `stack.push(item)` - Adds a new item on top of the stack
* **Pop**: `stack.pop()` - Removes the top item from the stack
* **Peek**: `stack.peek()` - Returns the top item without removing it
* **Size**: `stack.size()` - Returns the number of items in the stack

### When might you use a stack?

Let's take the and example from the world of game development.

When designing a weapon system in a video game, especially for weapons with magazines like a repeater crossbow, a stack can be an ideal choice for the underlying data structure. A magazine that holds arrows, for instance, would benefit from the LIFO principle: the last arrow loaded is the first one fired.

Here's the code:

```python
class Magazine:
    def __init__(self):
        self.arrows = []

    def push(self, arrow):
        self.arrows.append(arrow)

    def pop(self):
        if not self.arrows:
            return None
        return self.arrows.pop()

    def peek(self):
        if not self.arrows:
            return None
        return self.arrows[-1]

    def size(self):
        return len(self.arrows)
```

You could then use the `Magazine` class:

```python
magazine = Magazine()
magazine.push("Arrow 1")
magazine.push("Arrow 2")
magazine.push("Arrow 3")

print(magazine.peek()) # Arrow 3

print(magazine.pop()) # Arrow 3
print(magazine.pop()) # Arrow 2
print(magazine.pop()) # Arrow 1
```

## Are stacks fast?

Stacks are fast. All operations are `O(1)`, which means they take the same amount of time regardless of the size of the stack. Stack of 10 items? Stack of 10,000 items? It doesn't matter, pushing and popping will be *blazingly* fast.

Think about it: you can only add or remove from the top of the stack. You *never* have to iterate through the entire stack to find an item.

Now, to be fair, if for some reason you know that an item exists in a Stack, you can `pop()` until you find it. This would be `O(n)`, but if that's a use case for you, you should probably be using a different data structure.

## The Origin of "Stack Overflow"

While many developers are familiar with the website [Stack Overflow](https://stackoverflow.com/), not everyone knows the term's origin. A programming language, such as Python, uses a stack data structure to manage function calls and their scope. 

Consider this simple program:

```python
def function_one():
    function_two()
    function_two()

def function_two():
    function_three()
    function_three()

def function_three():
    print("function three")

function_one()
```

Here, each function call is represented by a [call frame](https://en.wikipedia.org/wiki/Call_stack) in memory. When a function is invoked, a new frame is pushed onto the runtime stack. When the function completes its execution, its frame is popped off the stack.

### The Dreaded Stack Overflow

A "stack overflow" refers to an error that occurs when the stack exceeds its capacity. The limit of this capacity varies based on numerous factors like the programming language and available memory. If a program surpasses this limit, the stack overflows, which often results in the program crashing. Python, however, takes measures to prevent the interpreter stack from growing excessively large, thereby averting a stack overflow. Instead, a runtime exception is raised.
