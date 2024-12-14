---
title: "Variables and Types in Python"
author: lane
date: "2024-12-13"
categories:
  - "python"
images:
  - /img/800/symbolsonboard.png.webp
imageAlts:
  - "math on chalkboard"
---

Variables are how we _store_ data as our program runs. You're probably already familiar with _printing_ data by passing it straight into `print()`:

```py
print("hello world")
# hello world

print(45)
# 45
```

Variables allow us to _save_ the data in variables so we can reuse it and change it _before_ printing it.

_We're making all the static content from our Boot.dev courses available for free here on the blog. This one is the "Variables" chapter from [Learn to Code in Python](https://www.boot.dev/courses/learn-code-python). If you want to try the far more immersive version of the course, do check it out!_

## Creating Variables

A "variable" is just a name that we give to a value. For example, we can make a new variable named `my_height` and set its value to `100`:

```py
my_height = 100
```

Or we can define a variable called `my_name` and set it to the text string `"Lane"`:

```py
my_name = "Lane"
```

We have the freedom to choose any name for our variables, but they should be _descriptive_ and consist of a single "token", meaning continuous text with underscores separating the words.

## Using Variables

Once we have a variable, we can access its value by using its name. For example, this will print `100`:

```py
print(my_height)
```

And this will print `Lane`:

```py
print(my_name)
```

## Variables Vary

Variables are called "variables" because they can hold any value and that value can change (it varies).

For example, this code prints `20`:

```py
acceleration = 10
acceleration = 20
print(acceleration)
```

The line `acceleration = 20` _reassigns_ the value of `acceleration` to 20. It _overwrites_ whatever was being held in the `acceleration` variable before (10 in this case).

## Storing Results

Now that we know how to store and change the value of variables, let's do some math!

Here are some examples of common mathematical operators in Python syntax.

```py
summation = a + b  # Addition
difference = a - b # Subtraction
product = a * b    # Multiplication
quotient = a / b   # Division
```

Parentheses can be used to [order math operations](https://www.mathsisfun.com/operation-order-pemdas.html).

```py
avg = (a + b + c) / 3
```

## Negative Numbers

Negative numbers in Python work the way you probably expect. Just add a minus sign:

```py
my_negative_num = -1
```

## Comments

Comments don't do... anything. They are _ignored_ by the Python interpreter. That said, they're good for what the name implies: adding comments to your code in plain English (or whatever language you speak).

## Single line comment

A single `#` makes the rest of the line a comment:

```py
# speed describes how fast the player
# moves in meters per second
speed = 2
```

## Multi-line comments (aka docstrings)

You can use triple quotes to start and end multi-line comments as well:

```python
"""
    the code found below
    will print 'Hello, World!' to the console
"""
print("Hello, World!")
```

This is useful if you don't want to add the `#` to the start of each line when writing paragraphs of comments.

## Variable Names

Variable names can _not_ have spaces; they're continuous strings of characters.

The creator of the Python language himself, Guido van Rossum, implores us to use `snake_case` for variable names. What _is_ snake case? It's just a style for writing variable names. Here are some examples of different casing styles:

| Name        | Code             | Language(s) that recommend it |
| ----------- | ---------------- | ----------------------------- |
| Snake Case  | `my_hero_health` | Python, Ruby, Rust            |
| Camel Case  | `myHeroHealth`   | JavaScript, Java              |
| Pascal Case | `MyHeroHealth`   | C#, C++                       |
| No Casing   | `myherohealth`   | No one: don't do this         |

To be clear, your Python code will still _work_ with Camel Case or Pascal Case, but can we please just have nice things? We just want some consistency in our craft.

> If you won't use snake case for _you_, do it for _me_. I beg you.

## Basic Variable Types

Python has several basic data types.

### Strings

In programming, snippets of text are called "strings". They're lists of characters _strung_ together. We create strings by wrapping the text in single quotes or double quotes. That said, **double quotes are preferred**.

```py
name_with_single_quotes = 'boot.dev' # not so good
name_with_double_quotes = "boot.dev" # so good
```

### Numbers

Numbers are _not_ surrounded by quotes when they're declared.

**An integer is a number without a decimal part**:

```py
x = 5 # positive integer
y = -5 # negative integer
```

**A float is a number with a decimal part**:

```py
x = 5.2
y = -5.2
```

### Booleans

A "Boolean" (or "bool") is a type that can only have one of two values: `True` or `False`. As you may have heard, computers really only use 1's and 0's. These 1's and 0's are just `True/False` boolean values.

```py
is_tall = True
is_short = False
```

## F-strings in Python

Ever played Pokemon and chosen a funny name so that the in-game messages would come out funny?

In Python, we can create strings that contain dynamic values with the f-string syntax.

```py
num_bananas = 10
print(f"You have {num_bananas} bananas")
# You have 10 bananas
```

- Opening quotes must be preceded by an `f`.
- Variables within curly brackets have their values "interpolated" (injected) into the string.

## NoneType Variables

Not all variables have a value. We can make an "empty" variable by setting it to `None`. `None` is a special value in Python that represents the absence of a value. It is _not_ the same as zero, False, or an empty string.

```py
my_mental_acuity = None
```

The value of `my_mental_acuity` in this case is `None` until we use the assignment operator, `=`, to give it a value.

{{< bdyoutube pZoDH6aU7ws >}}

### None is _not_ a string

NoneType is _not_ the same as a string with a value of "None":

```py
my_none = None # this is a None-type
my_none = "None" # this is a string with the value "None"
```

So when would you _use_ it? One use case is to represent that a value hasn't been determined yet, for example, an uncaptured input. For example, maybe your program is waiting for a user to enter their name. You might start with a variable:

```py
username = None
```

Then later in the code, once the user has entered their name, you can assign it to the `username` variable:

```py
username = input("What's your name? ")
```

Remember, it's crucial to recognize that `None` is not the same as the string `"None"`. They look the same when printed to the console, but they are different data types. If you use `"None"` instead of `None`, you will end up with code that looks correct when it's _printed_ but fails the _tests_.

## Dynamic Typing

Python is dynamically typed, which means a variable can store any type, and that type can _change_.

For example, if I make a number variable, I can later change that variable to a string:

```py
speed = 5
speed = "five"
```

### But like, maybe don't

In almost all circumstances, it's a _bad idea_ to change the type of a variable. The "proper" thing to do is to just create a new one. For example:

```py
speed = 5
speed_description = "five"
```

### What is non-dynamic typing?

Languages that aren't dynamically typed are statically typed, such as Go. In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash the program.

If Python were statically typed, the first example from before would crash on the second line, `speed = "five"`. The computer would give an error along the lines of `you can't assign a string value ("five") to a number variable (speed)`.

## Math With Strings

When working with strings, the `+` operator performs a "concatenation", which is a fancy word that means "joining two strings". _Generally speaking, it's better to use string interpolation with `f-strings` over `+` concatenation_.

```py
first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"
```

`full_name` now holds the value "Lane Wagner".

Notice the extra space at the end of `"Lane "` in the `first_name` variable. That extra space is there to separate the words in the final result: `"Lane Wagner"`.

## Multi-Variable Declaration

We can save space when creating many new variables by declaring them on the same line:

```py
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
```

Which is the same as:

```py
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200
```

Any number of variables can be declared on the same line, and variables declared on the same line _should_ be related to one another in some way so that the code remains easy to understand.

We call code that's easy to understand "clean code".
