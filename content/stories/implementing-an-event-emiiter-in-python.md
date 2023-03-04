---
title: "Implementing an eventemitter class in python"
author: Youdiowei Eteimorde
date: "2023-03-03"
images:
  - /img/800/william-bout-7cdFZmLlWOM-unsplash.jpg.webp
dofollows:
  - "https://github.com/EteimZ"
  - "https://twitter.com/Eteims1"
  - "https://dev.to/eteimz"
  - "https://eteimz.github.io/"
categories:
  - "python"
  - "education"
---

When faced with the challenge of making decisions in programming, we often resort to using conditional statements such as if/else or switch statements to solve the problem. 
However, an alternative approach is to utilize events, which are a means of enabling communication between different software components.
Events are widely used in programming languages such as JavaScript, and its runtime environment Node.js, to facilitate various operations and functionalities. 

Node.js offers a module called [events](https://nodejs.org/api/events.html) that encompasses a collection of classes that are essential for working with events in Node.js. This module provides an interface for creating, emitting, and handling events in Node.js applications.

Unlike Node.js, the Python programming language does not include an events module in its standard library. However, various third-party libraries are available for this purpose. In this article, we will explore the concept of events and create a class that facilitates working with events in Python. The class will have an API based on the Node.js [EventEmitter](https://nodejs.org/api/events.html#class-eventemitter) class.

## The concept of event

Event is a critical element of the [event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture), 
which generally involves two types of entities: publishers and subscribers. 
The publisher is responsible for generating events and making them available to the subscribers, while the subscribers listen to events and execute actions in response to them.

When a publisher generates an event, it triggers a notification to all subscribed listeners.
Once the event has been triggered, each subscriber performs the relevant action based on the event information. 
This approach enables software components to communicate in a [loosely coupled](https://en.wikipedia.org/wiki/Loose_coupling) manner, promoting flexibility and scalability in software design.


## Python implementation

Now let's dive into the python implementation. First we define the `EventEmitter` class and it's method without implementation.

```python
class EventEmitter:

    def __init__(self):
        pass
    
    def on(self):
        raise NotImplementedError("method not implemented.")
    
    def emit(self):
        raise NotImplementedError("method not implemented.")
    
    def off(self):
        raise NotImplementedError("method not implemented.")
```

The `on` method of the class will be used to listen to events and register callbacks that will perform actions when the event has been triggered. 
Every registered callback is kept in a set that corresponds to a specific event. The `emit` method is used call every callback
in the set that corresponds to the triggered event. The `off` method is used to remove a specific callback from the set of callbacks of an event.

### `init` method

```python
from typing import Callable, Any
from collections import defaultdict

class EventEmitter:

    def __init__(self):
        self.events: dict[str, set] = defaultdict(set)
```

On initialization of the class, we have a default dictionary that uses the event name as the key and a [set](https://docs.python.org/3/library/functions.html#func-set) of callbacks as values.
We used a [default dictionary](https://docs.python.org/3/library/collections.html#collections.defaultdict) to prevent a [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) on the first addition to the dictionary.
We also imported all necessary [types](https://docs.python.org/3/library/typing.html) and defaultdict which isn't available globally.

### `on` method

```python
def on(self, event_name: str, callback: Callable[..., Any]) -> None:
    if not callable(callback):
        raise Exception("Callback should be a callable")
    self.events[event_name].add(callback)
```

The `on` method takes in the **event name** as a string and a callback of type [callable](https://docs.python.org/3/library/typing.html#typing.Callable). 
We have to ensure the user is truly providing a callable by using the [callable](https://docs.python.org/3/library/functions.html#callable) builtin function to check. 
If they are not we will raise an exception. Every subsequence call to the on method will just add more callbacks to the dictionary.

### `emit` method

```python
def emit(self, event_name: str, *arg):
    for func in self.events[event_name]:
        func(*arg)
```

The `emit` function uses a for loop to call every functions mapped to that particular event.

### `off` method

As for the `off` method we just have to check if the callback is in the set. If it is we remove it.

```python
def off(self, event_name, callback: Callable[..., Any]) -> None:
    if callback in self.events[event_name]:
        self.events[event_name].remove(callback)
```

Here's the complete code:

```python
from typing import Callable, Any
from collections import defaultdict


class EventEmitter:

    def __init__(self):
        # the events attribute maintains a list of events and their corresponding callbacks
        self.events: dict[str, set] = defaultdict(set)

    def on(self, event_name: str, callback: Callable[..., Any]) -> None:
        """
        Listen to event
        """

        # check if callback is a function

        if not callable(callback):
            raise Exception("Callback should be a callable")

        self.events[event_name].add(callback)

    def emit(self, event_name: str, *arg) -> None:
        """
        Trigger event
        """

        for func in self.events[event_name]:
                func(*arg)
    
    def off(self, event_name, callback: Callable[..., Any]) -> None:
        """
        Remove callback from event list
        """
        if callback in self.events[event_name]:
            self.events[event_name].remove(callback)

```

## Client code

Now let's write the client code that will make use of the `EventEmitter` class:

```python
e = EventEmitter() # create an instance of the class

# define callback functions
addition = lambda x, y : print(x + y)
substraction = lambda x, y : print(x - y)

e.on("add", addition) # register add event and place addition in its event list
e.on("add", print)    # place the print callback in add event list
e.on("sub", substraction) # register sub event and place substraction in its event list

e.off("add", print) # remove the print callback from the add event list
e.emit("add", 2, 3) # emit add event. result: 5
e.emit("sub", 5, 2) # emit sub event. result: 3
```

There we have it we have implemented the three major methods for working with events in python.
Obvisouly there is still much to be done to make it functional like its nodejs counter part.

Here are a few ideas:
- Study the node [EventEmitter](https://nodejs.org/api/events.html#class-eventemitter) api and implement other methods like [once](https://nodejs.org/api/events.html#emitteronceeventname-listener), [listenerCount](https://nodejs.org/api/events.html#emitterlistenercounteventname) and [setMaxListeners](https://nodejs.org/api/events.html#emittersetmaxlistenersn).
- Create a python package for it.
- Build a project utilizing the `EventEmitter` class.
