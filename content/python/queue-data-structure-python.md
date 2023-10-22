---
title: "Queue Data Structure in Python: Ordering at Its Best"
author: Lane Wagner
date: "2023-10-22"
categories:
  - "python"
  - "computer-science"
images:
  - /img/800/queue_of_swords.png.webp
---

A **queue** is an efficient collection of ordered items. New items can be added to one side, and removed from the other side.

![Queue Image](/img/800/queueclass.png.webp)

A queue is like a line at the grocery store; the first person to get in line will be the first to be checked out. The fundamental principle behind a queue is `FIFO` (first in, first out), meaning the first element added to the queue will be the first one to get removed (as opposed to a [stack](/python/stack-data-structure-python/), which is `LIFO`).

Queues are commonly used in computer science for algorithms, data buffer handling, and in everyday applications where tasks or data are lined up in order.

{{< bdyoutube CH6yLUtMZ28 >}}

## Basic Queue Operations:

* **Enqueue**: `queue.push(item)` - Adds an item to the back of the queue
* **Dequeue**: `queue.pop()` - Removes the front item from the queue
* **Front**: `queue.peek()` - Returns the front item without removing it
* **Size**: `queue.size()` - Returns the number of items in the queue

## Real-life scenarios for using a queue:

Take, for instance, a printer queue. If multiple documents are sent to the printer at nearly the same time, they're lined up in the order they were received. As each document finishes printing, the next in line starts. A queue-based data structure is perfect for this use case.

## Two Approaches to Implementing a Queue:

### 1. **List-Based Queue**

In Python, lists are versatile data structures, and they can be easily adapted to implement a queue. Here's a simple list-based queue:

```python
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
```

With this structure, enqueuing an item inserts it at the beginning, and dequeuing fetches from the end, ensuring a FIFO order. While this implementation is nice and *simple*, it's not the most efficient. 

The trouble is that every time an item is enqueued, all the other elements in the list must be shifted one position to the right. This pesky line right here is causing all the trouble:

```py
self.items.insert(0, item)
```

Under the hood, this isn't just adding an item to the front of the lift, it's actually iterating over every single item in the list and moving it one position to the right. That gets really slow when the list gets big. In Big-O notation, it's an `O(n)` operation, while all the other operations are `O(1)`: constant time.

### 2. **Linked List-Based Queue**

The trouble with the list based implementation is that no matter how you design it, either the enqueue or the dequeue operation will be slow: `O(n)`. At some point, you'll need to shift all the elements in the list to the right or left.

If we use a linked list instead of a normal list, we can avoid this problem completely. With a linked list, we can enqueue and dequeue in `O(1)` time. Here's a simple linked list-based queue:

```python
class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

While both implementations effectively model the queue behavior, the linked list approach generally provides better performance for enqueuing since it avoids the potential overhead of shifting elements in a list.

However, when considering which implementation to use, it's essential to factor in the specific requirements and constraints of the problem at hand.
