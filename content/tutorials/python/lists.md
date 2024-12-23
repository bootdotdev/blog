---
title: "Lists in Python"
author: lane
date: "2024-12-25"
categories:
  - "python"
images:
  - /img/800/wagslane_snakes_all_slithering_in_a_line__studio_ghibli_anime_92c11046-1c25-44da-a9df-550614ab5404_0.png.webp
imageAlts:
  - "snakes in a list (line)"
---

## Lists

A natural way to organize and store data is in a `List`. Some languages call them "arrays", but in Python, we just call them lists. Think of all the apps you use and how many of the items in the app are organized into lists.

For example:

- An X (formerly Twitter) feed is a list of posts
- An online store is a list of products
- The state of a chess game is a list of moves
- This list is a list of things that are lists

Lists in Python are declared using square brackets, with commas separating each item:

```py
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
```

Lists can contain items of any data type, in our example above we have a `List` of strings.

_We're making all the static content from our Boot.dev courses available for free here on the blog. This one is the "Lists" chapter from [Learn to Code in Python](https://www.boot.dev/courses/learn-code-python). If you want to try the far more interactive version of the course, do check it out!_

Sometimes when we're manually creating lists it can be hard to read if all the items are on the same line of code. We can declare the list using multiple lines if we want to:

```py
flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
]

player_ages = [
    23,
    18,
    31,
    42
]
```

Keep in mind this is just a styling change. The code will run correctly either way.

## Counting in Programming

In the world of programming, counting is a bit strange! We don't start counting at `1`, we start at `0` instead.

### Indexes

Each item in a list has an index that refers to its spot in the list.

Take the following list as an example:

```py
names = ["Bob", "Lane", "Alice", "Breanna"]
```

- Index 0: `Bob`
- Index 1: `Lane`
- Index 2: `Alice`
- Index 3: `Breanna`

## Indexing into Lists

Now that we know how to create new lists, we need to know how to access specific items in the list.

We access items in a list directly by using their _index_. Indexes start at 0 (the first item) and increment by one with each successive item. The syntax is as follows:

```py
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided
```

## List length

The length of a List can be calculated using the `len()` function.

```py
fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3
```

The length of the list is equal to the number of items present. Don't be fooled by the fact that the length is not equal to the index of the last element, in fact, it will always be one greater.

## List Updates

We can also change the item that exists at a given index. For example, we can change `Leather` to `Leather Armor` in the `inventory` list in the following way:

```py
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']
```

## Appending in Python

It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the `.append()` method:

```py
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']
```

## Pop Values

`.pop()` is the opposite of `.append()`. Pop removes the last element from a list and returns it for use. For example:

```py
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'
```

## Counting the items in a list

Remember that we can iterate over all the elements in a list using a [loop](/tutorials/python/loops). For example, the following code will print each item in the `sports` list.

```py
sports = ["soccer", "basketball", "baseball"]
for i in range(0, len(sports)):
    print(sports[i])
```

## No-index Syntax

In my opinion, Python has _the most elegant_ syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:

```py
trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple
```

`tree`, the variable declared using the `in` keyword, directly accesses the value in the list rather than the index of the value. If we don't need to update the item and only need to access its value then this is a more clean way to write the code.

## Find an item in a list

Practice the "no-index" or "no-range" syntax:

```py
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Prints:
# apple
# banana
# cherry
```

## Slicing lists

Python makes it easy to slice and dice lists to work only with the section you care about. One way to do this is to use the simple slicing operator, which is just a colon `:`.

With this operator, you can specify where to start and end the slice, and how to step through the original list. List slicing returns a _new list_ from the existing list.

The syntax is as follows:

```python
my_list[ start : stop : step ]
```

For example:

```python
scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]
```

The above reads as "give me a slice of the `scores` list from index 1, up to but not including 5, skipping every 2nd value. _All of the sections are optional_.

### Omitting sections

You can also omit various sections ("start", "stop", or "step"). For example, `numbers[:3]` means "get all items from the start up to (but not including) index 3". `numbers[3:]` means "get all items from index 3 to the end".

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]
```

### Using only the "step" section

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]
```

### Negative Indices

Negative indices count from the end of the list. For example, `numbers[-1]` gives the last item in the list, `numbers[-2]` gives the second last item, and so on.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]
```

## List Operations - Concatenate

Concatenating two lists (smushing them together) is easy in Python, just use the `+` operator.

```python
total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]
```

## List Operations - Contains

Checking whether a value exists in a list is also really easy in Python, just use the `in` keyword.

```python
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True
```

## List deletion

Python has a built-in keyword [del](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement) that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []
```

## First Element

To access the first element of a list, you simply refer to index `0`. This is because list indexing starts at `0` in Python.

```python
animals = ["cat", "dog", "bird"]
first_animal = animals[0]
print(first_animal)
# Output: cat
```

## **Example**: Reverse a List

Python provides a simple way to reverse the order of elements in a list. You can use slicing to reverse the list.

```python
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)
# Output: [5, 4, 3, 2, 1]
```

Alternatively, you can use the `reverse()` method, which reverses the list in place.

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
# Output: [5, 4, 3, 2, 1]
```

## **xample**: Filter Messages

When working with lists, you may need to filter out certain elements based on a condition. Python provides a powerful feature called list comprehension to achieve this.

```python
messages = ["Hello world", "Python is great", "Have a nice day"]
filtered_messages = [message for message in messages if "Python" in message]
print(filtered_messages)
# Output: ['Python is great']
```

In the example above, we created a new list `filtered_messages` containing only the messages that include the word "Python". List comprehensions allow for a concise and expressive way to filter lists.

Hope this helps, best of luck writing your lists in Python!
