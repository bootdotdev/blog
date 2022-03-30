---
title: "Building a Linked List in Python with Examples"
author: Lane Wagner
date: "2021-01-11"
categories: 
  - "computer-science"
  - "python"
images:
  - /img/list.jpeg
---

A linked list is a linear data structure where elements are not stored next to each other in memory. The elements in a linked list are linked using pointers or references. Linked lists are an ordered collection of objects, similar to a normal list. Linked lists stand apart from lists in how they store elements in memory. While regular lists like arrays and slices use a contiguous memory block to store references to their data, linked lists store _references_, aka _pointers_ as part of each element.

![array vs linked list](/img/difference-between-arrays-and-linked-list-1024x431.jpg)

[source](https://www.faceprep.in/data-structures/linked-list-vs-array/)

A normal list is just a pointer to the first element in the list, and a specific item can be retrieved by providing a memory offset.

A linked list is also just a pointer to the first element in the list, but memory offsets won't do us any good. We need to examine the first element's `next` pointer to see where the next item is, then we can navigate to it. From there, we can find the next item and so on down the list.

## Python singly linked list example

### Node Class

First, we'll build a `Node` class. The `LinkedList` class we eventually build will be a list of `Node`s.

```py
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
```

Each node has a `val` data member (the information it stores) and a `next` data member. The `next` data member just points to the next `Node` in the list if there is one, otherwise it's `None`

### Linked List Constructor

```py
class LinkedList:
    def __init__(self):
        self.head = None
```

The constructor is easy - just initialize an empty `head` pointer. This indicates we now have an empty list.

### Iterating over the list

Let's make it easy to iterate over each item in the list using python's `for _ in _` syntax.

```py
def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
```

By implementing Python's `__iter__` method, we can now use iteration syntax. For example, `for item in linked_list:`.

### Adding to the linked list

Let's create a way to add items to the tail of the list, the `add_to_tail` method. It takes a node as input, iterates over the entire list, then adds the given node to the end.

```py
def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)
```

### Removing from the linked list

There are other ways to remove items from the list, but for now, and as an example, let's write a `remove from head` method.

```py
def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
```

`remove_from_head` removes and returns the first item from the list, assuming one exists.

### Printing the linked list

Last but not least, we can implement Python's `__repr__()` method so that we can call `print()` directly on a list and control what it printed. Here's a representation I like:

```
def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
```

This method will print each node's value in order, with arrows in between. For example, `hello -> this -> is -> my -> list`.

### Using the linked list

```py
linked_list = LinkedList()
linked_list.add_to_tail(Node('john'))
linked_list.add_to_tail(Node('sally'))
linked_list.add_to_tail(Node('jimmy'))
print("ll:", linked_list)
first = linked_list.remove_from_head()
print("removed:", first)
print("ll:", linked_list)
```

## Practical Applications of a Linked List

Linked lists are immensely valuable in computer science because they uniquely allow us to add and remove elements anywhere in the list quickly, with a Big-O complexity of just `O(1)`.

### Big-O complexity of a linked list

| Operation | Big-O Complexity |
| --------- | ---------------- |
| Insert    | O(1)             |
| Delete    | O(1)             |
| Index     | O(n)             |

Because of the fast operations, linked lists are used practically in many different scenarios, including:

- Stacks
- Queues
- Hash maps, to prevent collisions
- Undo/Redo operations (stack)
- Appending a song to a playlist
- To keep items in the same place in memory for performance reasons

## Full Linked List Code Sample

```py
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
```
