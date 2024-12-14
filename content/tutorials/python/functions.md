---
title: "Functions in Python"
author: lane
date: "2024-12-14"
categories:
  - "python"
images:
  - /img/800/functionsinpythonscreen.png.webp
imageAlts:
  - "computers and plants"
---

Functions in Python allow us to _reuse_ and _organize_ code. For example, say we have some code that calculates the area of a circle:

```py
radius = 5
area = 3.14 * radius * radius
```

That works! The problem is when we want to calculate the area of _other_ circles, each with its own radius. We _could_ just copy the code and change the variable names like this:

```py
radius = 5
area1 = 3.14 * radius * radius

radius2 = 7
area2 = 3.14 * radius2 * radius2
```

But we want to _reuse_ our code! Why would we want to redo our work? What if we wanted to calculate the area of thousands of circles??? **That's where functions help.**

_We're making all the static content from our Boot.dev courses available for free here on the blog. This one is the "Functions" chapter from [Learn to Code in Python](https://www.boot.dev/courses/learn-code-python). If you want to try the far more immersive version of the course, do check it out!_

Instead, we can define a new function called `area_of_circle` using the `def` keyword.

```py
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result
```

Let's break this `area_of_circle` function down:

- It takes one input (aka "parameter" or "argument") called `r`
- The body of the function is indented - this is the code that will run each time we use (aka "call") the function
- It `return`s a single value (the output of the function). In this case, it's the value stored in the `result` variable

To ["call"](https://en.wikibooks.org/wiki/Python_Programming/Functions#Function_Calls) this function (fancy programmer speak for "use this function") we can pass in any number as the argument (in this case, `5`) for the parameter `r`, and capture the output into a new variable:

```py
area = area_of_circle(5)
print(area)
# 78.5
```

1. `5` goes in as the input `r`
2. The body of the function runs, which stores `78.5` in the `result` variable
3. The function returns the value `78.5`, which means the `area_of_circle(5)` expression evaluates to `78.5`
4. `78.5` is stored in the `area` variable and then printed

Because we've already _defined_ the function, now we can use it as many times as we want with different inputs!

```py
area = area_of_circle(6)
print(area)
# 113.04

area = area_of_circle(7)
print(area)
# 153.86
```

Functions are tricky! It takes a minute to get used to them, but after that they'll be second nature to you. You might find yourself slowing down a bit, and if you do, that's totally normal.

{{< bdyoutube Q5A9_UdFm5Q >}}

Let's break down this function line by line so you can understand every nook and cranny of it.

```py
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

radius = 5
area = area_of_circle(radius)
print(area)
# 78.5
```

Here's a chronological explanation of what happens when the above code is executed:

1. `def area_of_circle(r)`: The `area_of_circle` function is defined for later use, but _not_ called. It accepts a single input, the arbitrarily named `r`. The body of the function (`pi = 3.14`... etc) is ignored for now.
2. `radius = 5`: A new variable called `radius` is created and set to the value `5`.
3. `area_of_circle(radius)`: The `area_of_circle` function is called with `radius` (in this case 5) as the input. Finally, we jump back to the function definition.
4. `def area_of_circle(r)`: We will now start executing the body of the function, and `r` is set to `5`.
5. `pi = 3.14`: A new variable called `pi` is created with a value of `3.14`.
6. `result = pi * r * r`: Some simple math is evaluated (`3.14 * 5 * 5`) and stored in the `result` variable.
7. `return result`: The result variable is returned from the function as output.
8. `area = area_of_circle(radius)`: The returned value is stored in a new variable called `area` (in this case `78.5`).
9. `print(area)`: The value of `area` is printed to the console.

## Multiple Parameters

Functions can have multiple parameters ("parameter" being a fancy word for "input"). For example, this `subtract` function accepts 2 parameters: `a` and `b`.

```py
def subtract(a, b):
    result = a - b
    return result
```

The name of a parameter doesn't matter when it comes to which values will be assigned to which parameter. It's **position** that matters. The first parameter will become the first value that's passed in, the second parameter is the second value that's passed in, and so on. In this example, the `subtract` function is called with `a = 5` and `b = 3`:

```py
result = subtract(5, 3)
print(result)
# 2
```

Here's an example with four parameters:

```py
def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro
```

It can be called like this:

```py
my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)
# Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.
```

## Printing vs Returning

Some new developers get hung up on the difference between `print()` and `return`.

It can be particularly confusing when the test suite we provide simply prints the output of your functions to the console. It makes it _seem_ like `print()` and `return` are interchangeable, _but they are not_!

- `print()` is a function that:
  1. Prints a value to the console
  2. Does _not_ return a value
- `return` is a keyword that:
  1. Ends the current function's execution
  2. Provides a value (or values) back to the caller of the function
  3. Does _not_ print anything to the console (unless the return value is later `print()`ed)

### Printing to debug your code

Printing values and running your code is a great way to debug your code. You can see what values are stored in various variables, find your mistakes, and fix them. Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.

In the real world, it's rare to leave `print()` statements in your code when you're done debugging. Similarly, you need to remember to remove any `print()` statements from your code before submitting your work because it will interfere with the tests!

## Where to Declare Functions

You've probably noticed that a variable needs to be declared _before_ it's used. For example, the following doesn't work:

```py
print(my_name)
my_name = 'Lane Wagner'
```

It needs to be:

```py
my_name = 'Lane Wagner'
print(my_name)
```

Code executes in _order from top to bottom_, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until _after_ the definition.

## Order of functions

All functions _must_ be defined before they're used.

You might think this would make structuring Python code hard because the order of the functions needs to be _just right_. As it turns out, there's a simple trick that makes it super easy.

Most Python developers solve this problem by defining _all_ the functions in their program first, then they call an "entry point" function _last_. That way _all_ of the functions have been read by the Python interpreter before the first one is called.

Note: _conventionally this "entry point" function is usually called `main` to keep things simple and consistent_.

```python
def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint last
main()
```

## None Return

When no return value is specified in a function, it will automatically return `None`. For example, maybe it's a function that prints some text to the console but doesn't explicitly return a value. The following code snippets all return the same value, `None`:

```python
def my_func():
    print("I do nothing")
    return None
```

```python
def my_func():
    print("I do nothing")
    return
```

```python
def my_func():
    print("I do nothing")
```

## Multiple return values

A function can return more than one value by separating them with commas.

```python
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values
```

### Receiving multiple values

When calling a function that returns multiple values, you can assign them to multiple variables.

```py
dmg, mana = cast_iceblast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90
```

When `cast_iceblast` is called, it returns two values. The first value is assigned to `dmg`, and the second value is assigned to `mana`. Just like function inputs, it's the _order_ of the values that matters, not the variable names. We could just as easily call the variables `one` and `two`:

```py
one, two = cast_iceblast(5, 100)
print(f"Damage: {one}, Remaining Mana: {two}")
# Damage: 10, Remaining Mana: 90
```

That said, descriptive variable names make your code easy to understand, so use them!

### What happened to the variables?

The `damage` and `new_mana` variables from `cast_iceblast`'s function body only exist _inside_ of the function. They can't be used outside of the function. We'll explain that more later when we talk about scope.

## Parameters vs arguments

Parameters are the names used for inputs when _defining_ a function. Arguments are the values of the inputs supplied when a function is _called_.

To reiterate, **arguments are the actual values** that go into the function, such as `42.0`, `"the dark knight"`, or `True`. **Parameters are the names** we use in the function definition to refer to those values, which at the time of writing the function, can be whatever we like.

That said, this is all semantics, and frankly, developers are really lazy with these definitions. You'll often hear the words "arguments" and "parameters" used interchangeably.

```py
# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)
```

## Default values

In Python, you can specify a [default](https://docs.python.org/3/glossary.html#term-parameter) value for a function argument. It's nice for when a function has arguments that are "optional". You as the function definer can specify a specific default value in case the caller doesn't provide one.

A default value is created by using the assignment (`=`) operator in the function signature.

```py
def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)
```

```py
get_greeting("lane@example.com", "Lane")
# Hello Lane welcome! You've registered your email: lane@example.com
```

```py
get_greeting("lane@example.com")
# Hello there welcome! You've registered your email: lane@example.com
```

If the second parameter is omitted, the default `"there"` value will be used in its place. As you may have guessed, for this structure to work, optional arguments (the ones with defaults) must come _after_ all required arguments.
