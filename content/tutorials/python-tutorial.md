---
title: "Learn Python: A Free Tutorial for Beginners"
author: Lane Wagner
date: "2023-03-30"
categories:
  - "tutorials"
  - "python"
images:
  - /img/800/snakesclassroom.png.webp
toc: true
---

Python is an unbelievably powerful programming language that is used by millions of developers in production systems around the world. It's easy to learn, free to use, and has a huge community of developers that are always willing to help.

If you're interested in [back-end web development](/backend/become-backend-developer/), data science, [data engineering](/backend/backend-engineer-vs-data-engineer/), or just want to automate some of your boring tasks, Python is a great place to start.

**Optional video walkthrough**:

_Try to build this project on your own!_ Use this video if you get stuck, or to compare your architecture and coding patterns to mine.

{{< bdyoutube 4M87qBgpafk >}}

## Would you rather learn by doing?

I've included all the static read-only material you'll need here in this tutorial, but if you would like a **more hands-on experience**, you can take the interactive version of this course, complete with coding challenges and projects on [Boot.dev here](https://boot.dev/courses/learn-python).

## Chapter 1: Introduction

![python](https://i.imgur.com/s2j2b4e.png)

Thousands of students start their coding journey right here with Python. We think it's the best programming language to get started with. Python is famous for being a simple language that's easy to read and write.

However, just because it's simple that doesn't mean it's not useful! Python is an _extremely_ popular language in the industry, and is well-known for:

- Backend web servers
- DevOps and cloud engineering
- Machine learning
- Scripting and automation
- etc...

On the other hand, it's not particularly well-known for front-end work. While it's _possible_ to do so, Python isn't typically used to build visual user interfaces.

### Setup a Local Development Environment

To get started with Python, you'll need to install the `python` command on your computer, and then install a text editor or IDE. If you're not already familiar with how to do that, I have a full step-by-step [project guide here](https://boot.dev/courses/build-local-dev-environment-python) that you can follow.

If you're able to edit and run Python code on your computer, you're ready to continue!

### What is "Code"?

Code is just a series of instructions that computers can follow. Computers obey each instruction, _one after another_.

Programs can be comprised of _many_ instructions. Like many. Like millions.

Addition is one of the most common instructions in coding.

### Printing numbers

`print()` can print text using quotes:

```py
print("some text here")
```

but it can also print numbers without quotes:

```py
print(1)
```

and you can do math directly inside the parentheses:

```py
print(1 + 2)
```

Try some of these code snippets in your editor! For example, you could create a file called `hello.py` and write the following code:

```py
print("Hello, world!")
print(1 + 2)
```

Then, run the file with `python hello.py` and see what happens.

### Multiple Instructions

Code runs in order, starting at the top of the program. For example:

```py
print("this prints first")
print("this prints second")
print("this prints last")
```

### Syntax Errors

[Syntax](<https://en.wikipedia.org/wiki/Syntax_(programming_languages)>) is jargon for "valid code that the computer can understand". For example,

```py
prnt("hello world")
```

is invalid [syntax](<https://en.wikipedia.org/wiki/Syntax_(programming_languages)>) because `prnt()` is not a valid function, "print" is spelled incorrectly. As a result, an error will be thrown and the code won't execute.

### Syntax varies from langauge to language

A coding language's syntax makes up the rules that define what properly structured expressions and statements look like in that language. For example, in Python, the following would be considered _correct_ syntax:

```py
print("hello world")
```

While in a different programming language, like Go, the correct syntax would be:

```go
fmt.Println("hello world")
```

Code can have many different problems that prevent it from working as intended. Some examples include:

- A bug in the logic. For example, a program that should add numbers multiplies them instead
- A problem with speed. A program that calculates how to play the perfect game of chess might never be able to finish because it requires too many calculations.
- A problem with syntax. This is the most common problem for new developers. Luckily the Python interpreter will try to give you a descriptive error message in the console to help you find the problem.

## Chapter 2: Variables

[Variables](https://www.cs.utah.edu/~germain/PPS/Topics/variables.html) are how we store data in our program. So far we've been directly printing data by passing it directly into the `print()` function.

Now we are going to learn to save the data in variables so we can use and change it before we need to print it.

A variable is a name that we define that will point to some data. For example, I could define a new variable called `my_height` and set its value to 100. I could also define a variable called `my_name` and set it equal to "Lane".

### Creating variables

To create a new variable in Python we use the following syntax:

```py
my_new_variable_two = 2
this_can_be_called_anything = 3
```

### Variables Vary

Variables are called "variables" because they can hold any value and that value can change (it varies).

For example, the following will print `20`:

```py
acceleration = 10
acceleration = 20
print(acceleration)
```

The line `acceleration = 20` _reassigns_ the value of `acceleration` to 20. It _overwrites_ whatever was being held in the `acceleration` variable before.

### Let's do some math

Now that we know how to store and change the value of variables let's do some math!

Here are some examples of common mathematical operators in Python syntax.

```py
sum = a + b
difference = a - b
product = a * b
quotient = a / b
```

### Comments

Comments don't run like code, they are _ignored_ by the computer. Comments are useful for adding reminders or explaining what a piece of code does in plain English.

#### Single line comment

```py
# speed is a variable describing how fast your player moves
speed = 2
```

#### Multi-line comments (aka docstrings)

You can use triple quotes to start and end multi-line comments as well:

```python
"""
    the code found below
    will print 'Hello, World!' to the console
"""
print('Hello, World!')
```

This is useful if you don't want to add the `#` to the start of each line when writing paragraphs of comments.

### Variable Names

Variable names can't have spaces, they're continuous strings of characters.

In Python you should use "[snake_case](/clean-code/casings-in-coding/)" when creating variable names - it's become the "rule of thumb" for the language. By way of comparison, "camel case" is where the beginning of each new word except the first is capitalized.

#### No casing (pure insanity)

```py
somevariablehere = 10
```

#### Camel Case

```py
someVariableHere = 10
```

#### Snake Case

```py
some_variable_here = 10
```

### Basic Variable Types

In Python there are several basic data types.

#### String Type

"Strings" are raw text in coding speak. They are called "strings" because they are a list of characters strung together. Strings are declared in Python by using single quotes or double quotes. That said, for consistency's sake, we prefer double quotes.

```py
name_with_single_quotes = 'boot.dev'
name_with_double_quotes = "boot.dev"
```

#### Numeric Types

Numbers aren't surrounded by quotes when created, but they can have decimals and negative signs.

#### Integers are numbers without a decimal

```py
x = 5
y = -5
```

#### A "Float" is a number with a decimal

```py
x = 5.2
y = -5.2
```

#### Boolean Type

A "Boolean" (or "bool") is a type that can only have one of two values: `True` or `False`. As you may have heard computers really only use 1's and 0's. These 1's and 0's are just `Boolean` values.

```
0 = False
1 = True
```

```py
is_tall = True
```

### NoneType Variables

Not all variables have a value. We can declare an "empty" variable by setting it to `None`.

```py
empty = None
```

The value of `empty` in this instance is `None` until we use the assignment operator, `=`, to give it a value.

#### None is NOT a specific string

Note that the `None` type is _not_ the same as a string with a value of "None":

```py
my_none = None # this is a None-type
my_none = "None" # this is a string
```

### Dynamic Typing

Python is [dynamically typed](https://en.wikipedia.org/wiki/Type_system#Static_and_dynamic_type_checking_in_practice). All this means is that a variable can store any type, and that type can change.

For example, if I make a number variable, I can later change that variable to a string:

This is valid:

```py
speed = 5
speed = "five"
```

#### Just because you can doesn't mean you should!

In almost all circumstances, it's a _bad idea_ to change the type of a variable. The "proper" thing to do is to just create a new one. For example:

```py
speed = 5
speed_description = "five"
```

#### What if it weren't dynamically typed?

Statically typed languages like Go (which you'll learn in a later course) are statically typed instead of dynamically typed. In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash the program.

If Python were statically-typed, the first example from before would crash on the second line, `speed = "five"`. The computer would give an error along the lines of `you can't assign a string value ("five") to a number variable (speed)`

{{< bdyoutube GqXpFycPWLE >}}

### Math With Strings

Most of the math operators we went over earlier don't work with strings, aside from the `+` addition operator. When working with strings the `+` operator performs a "concatenation".

"Concatenation" is a fancy word that means the joining of two strings.

```py
first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
```

`full_name` now holds the value "Lane Wagner".

Notice the extra space at the end of `"Lane "` in the `first_name` variable. That extra space is there to separate the words in the final result: `"Lane Wagner"`.

### Multi-Variable Declaration

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

## Chapter 2: Computing Basics

### Python Numbers

In Python, numbers without a decimal part are called `Integers` - just like they are in mathematics.

Integers are simply whole numbers, positive or negative. For example, `3` and `-3` are both examples of integers.

Arithmetic can be performed as you might expect:

#### Addition

```python
2 + 1
# 3
```

#### Subtraction

```python
2 - 1
# 1
```

#### Multiplication

```python
2 * 2
# 4
```

#### Division

```python
3 / 2
# 1.5 (a float)
```

This one is actually a bit different - division on two integers will actually produce a `float`. A float is, as you may have guessed, the number type that allows for decimal values.

### Integers

In Python, numbers without a decimal part are called `Integers`. Contrast this to JavaScript where all numbers are just a `Number` type.

Integers are simply whole numbers, positive or negative. For example, `3` and `-3` are both examples of integers.

### Floats

A float is, as you may have guessed, the number type that allows for decimal values.

```py
my_int = 5
my_float = 5.5
```

### Floor division

Python has great out-of-the-box support for mathematical operations. This, among other reasons, is why it has had such success in artificial intelligence, machine learning, and data science applications.

Floor division is like normal division except the result is [floored](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) afterward, which means the remainder is _removed_. As you would expect, this means the result is an `integer` instead of a `float`.

```python
7 // 3
# 2 (an integer)
```

{{< bdyoutube fmM07zqoT5c >}}

### Exponents

Python has built-in support for exponents - something most languages require a `math` library for.

```python
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9
```

{{< bdyoutube sP8yhvtvipo >}}

### Changing In Place

It's fairly common to want to change the value of a variable based on its current value.

```py
player_score = 4
player_score = player_score + 1
# player_score now equals 5
```

```py
player_score = 4
player_score = player_score - 1
# player_score now equals 3
```

Don't let the fact that the expression `player_score = player_score - 1` is not a valid mathematical expression be confusing. _It doesn't matter_, it _is valid code_. It's valid because the way the expression should be read in English is:

> Assign to player_score the old value of player_score minus 1

### Plus Equals

Python makes reassignment easy when doing math. In JavaScript or Go you might be familiar with the `++` syntax for incrementing a number variable. In Python, we use the `+=` operator instead.

```python
star_rating = 4
star_rating += 1
# star_rating is now 5
```

### Scientific Notation

As we covered earlier, a `float` is a positive or negative number **with a fractional part**.

You can add the letter `e` or `E` followed by a positive or negative integer to specify that you're using [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation).

```python
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071
```

If you're not familiar with scientific notation, it's a way of expressing numbers that are too large or too small to conveniently write normally.

In a nutshell, the number following the `e` specifies how many places to move the decimal to the right for a positive number, or to the left for a negative number.

### Underscores for readability

Python also allows you to represent large numbers in the decimal format using underscores instead of commas to make it easier to read.

```py
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```

### Logical Operators

You're probably familiar with the logical operators `AND` and `OR`.

Logical operators deal with [boolean values](https://en.wikipedia.org/wiki/Boolean_data_type), `True` and `False`.

The logical `AND` operator requires that _both_ inputs are `True` to return `True`. The logical `OR` operator only requires that _at least one_ input is `True` to return `True`.

For example:

```
True AND True = True
True AND False = False
False AND False = False

True OR True = True
True OR False = True
False OR False = False
```

#### Python Syntax

```python
print(True and True)
# prints True

print(True or False)
# prints True
```

#### Nesting with parentheses

We can nest logical expressions using parentheses.

```py
print((True or False) and False)
```

First, we evaluate the expression in the parentheses, `(True or False)`. It evaluates to `True`:

```py
print(True and False)
```

`True and False` evaluates to `False`:

```py
print(False)
```

So, `print((True or False) and False)` prints "False" to the console.

### Binary Numbers

Binary numbers are just "base 2" numbers. They work the same way as "normal" base 10 numbers, but with 2 symbols instead of 10.

Each `1` in a binary number represents a greater multiple of 2. In a 4-digit number, that means you have the eight's place, the four's place, the two's place, and the one's place. Similar to how in decimal you would have the thousandth's place, the hundredth's place, the ten's place, and the one's place.

- `0001` = 1
- `0010` = 2
- `0011` = 3
- `0100` = 4
- `0101` = 5
- `0110` = 6
- `0111` = 7
- `1000` = 8

![binary](https://www.wikihow.com/images/4/47/B2d.gif)

{{< bdyoutube M3VLyEDPDR8 >}}

### Bitwise "&" Operator

Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value. For example, say you had the numbers `5` and `7` represented in [binary](https://en.wikipedia.org/wiki/Binary_code). You could perform a bitwise `AND` operation and the result would be `5`.

```
0101 = 5
&
0111 = 7
=
0101 = 5
```

A `1` in binary is the same as `True`, while `0` is `False`. So really a bitwise operation is just a bunch of logical operations that are completed in tandem.

`&` is the bitwise `AND` operator in Python. `5 & 7 = 5`, while `5 & 2 = 0`.

```
0101 = 5
&
0010 = 2
=
0000 = 0
```

### Binary notation

When writing a number in binary, the prefix `0b` is used to indicate that what follows is a binary number.

- `0b0101` is 5
- `0b0111` is 7

### Example: Guild Permissions

It's common practice in backend development to store user permissions as binary values. Think about it, if I have `4` different permissions a user can have, then I can store that as a 4-digit binary number, and if a certain bit is present, I know the permission is enabled.

Let's pretend we have 4 permissions:

- `can_create_guild` - Leftmost bit
- `can_review_guild` - Second to left bit
- `can_delete_guild` - Second to right bit
- `can_edit_guild` - Rightmost bit

Which are represented by `0b0000`. For example, if a user only has the `can_create_guild` permission, their binary permissions would be `0b1000`. A user with `can_review_guild` and `can_edit_guild` would be `0b0101`.

To check for, say, the `can_review_guild` permission, we can perform a bitwise `AND` operation on the user's permissions and the enabled `can_review_guild` bit (`0b0100`). If the result is `0b0100` again, we know they have that specific permission!

### Bitwise "|" Operator

As you may have guessed, the bitwise "or" operator is similar to the bitwise "and" operator in that it works on binary rather than boolean values. However, the bitwise "or" operator "ORs" the bits together. Here's an example:

- `0101` is 5
- `0111` is 7

```
0101
|
0111
=
0111
```

A `1` in binary is the same as `True`, while `0` is `False`. So a bitwise operation is just a bunch of logical operations that are completed in tandem. When two binary numbers are "OR'ed" together, the result has a `1` in any place where _either_ of the input numbers has a `1` in that place.

`|` is the bitwise `OR` operator in Python. `5 | 7 = 7` and `5 | 2 = 7` as well!

```
0101 = 5
|
0010 = 2
=
0111 = 7
```

### Not

We skipped a very important logical operator - `not`. The `not` operator reverses the result. It returns `False` if the input was `True` and vice-versa.

```python
print(not True)
# Prints: False

print(not False)
# Prints: True
```

## Chapter 3: Comparisons

### Comparison Operators

When coding it's necessary to be able to compare two values. `Boolean logic` is the name for these kinds of comparison operations that always result in `True` or `False`.

The operators:

- `<` "less than"
- `>` "greater than"
- `<=` "less than or equal to"
- `>=` "greater than or equal to"
- `==` "equal to"
- `!=` "not equal to"

For example:

```py
5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True
```

{{< bdyoutube QZdCkBWsC-4 >}}

### Evaluations

When a comparison happens, the result of the comparison is just a boolean value, it's either `True` or `False`.

Take the following two examples:

```py
is_bigger = 5 > 4
```

```py
is_bigger = True
```

In both of the above cases, we're creating a `Boolean` variable called `is_bigger` with a value of `True`.

Since `5 > 4`, `is_bigger` is always assigned the value of `True`.

### Why would I use the comparison if I can just set it to "True"?

You wouldn't in _this_ case. However, let's imagine that instead of hard-coding the numbers `5` and `4`, we had some _dynamic_ variables that we don't know the values of. For example, perhaps you're making a video game and need to keep track of player scores.

To calculate who wins, you would need to write something like:

```py
# player_one_points and player_two_points are defined and change somewhere else in the game's code
player_one_wins = player_one_points > player_two_points
print(player_one_wins)

# prints "True" when player one is winning, otherwise prints "False"
```

### Increment / Decrement

If we're changing a number and simply want to increment (add to) or decrement (subtract from) there are special operators for that.

```py
shield_armor = 4
shield_armor += 1
# shield_armor now equals 5
shield_armor += 2
# shield_armor now equals 7
```

```py
shield_armor = 4
shield_armor -= 1
# shield_armor now equals 3
shield_armor -= 2
# shield_armor now equals 1
```

Notice that `shield_armor+=1` is just short-hand for `shield_armor = shield_armor + 1`

### If Statements

It's often useful to only execute code if a certain condition is met:

```py
if CONDITION:
  # do some stuff here
```

for example:

```py
if bob_score > bill_score:
  print("Bob Wins!")
```

### If-Else

An `if` statement can be followed by zero or more `elif` (which stands for "else if") statements, which can be followed by zero or one `else` statement. For example:

```py
if score > high_Score:
    print('High score beat!')
elif score > second_highest_score:
    print('You got second place!')
elif score > third_highest_score:
    print('You got third place!')
else:
    print('Better luck next time')
```

First the `if` statement is evaluated. If it is `True` then the if statement's body is executed and all the other `else`s are ignored.

If the first `if` is false then the next `elif` is evaluated. Likewise, if it is `True` then its body is executed and the rest are ignored.

If none of the `if` statements evaluate to `True` then the final `else` statement will be the only body executed.

### If-Else Rules

- You can't have an `elif` or an `else` without an `if`
- You _can_ have an `else` without an `elif`

## Chapter 5: Loops

Loops are a programmer's best friend. Loops allow us to do the same operation multiple times without having to write it explicitly each time.

For example, let's pretend I want to print the numbers 0-9.

I could do this:

```py
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

Even so, it would save me a lot of time typing to use a _loop_. Especially if I wanted to do the same thing _one thousand_ or _one million_ times.

A _"for loop"_ in Python is written like this:

```py
for i in range(0, 10):
    print(i)
```

In English, the code says:

1. Start with `i` equals `0`. (`i in range(0`)
2. If `i` is not less than 10 (`range(0, 10)`), exit the loop.
3. Print `i` to the console. (`print(i)`)
4. Add `1` to `i`. (`range` defaults to incrementing by 1)
5. Go back to step `2`

The result is that the numbers `0-9` are logged to the console in order.

### Whitespace matters in Python!

The body of a for-loop _must_ be indented, otherwise you'll get a syntax error.

### Example

This code print the numbers 0-9 to the console.

```py
for i in range(0, 10):
    print(i)
```

### Range Continued

The `range()` function we've been using in our `for` loops actually has an optional 3rd parameter: the "step".

```py
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8
```

The "step" parameter determines how much to increment `i` by in each iteration of the loop. You can even go backwards:

```py
for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1
```

### F-strings in Python

You can create a string with dynamic values by using `f-strings` in Python. It's a beautiful syntax that I wish more programming languages used.

```py
num_bananas = 10
print(f"You have {num_bananas} bananas")
# You have 10 bananas
```

The opening quotes need to be proceeded by an `f`, then any variables within curly brackets have their values interpolated into the string.

## Chapter 6: Lists

A natural way to organize and store data is in the form of a `List`. Some languages call them "arrays", but in Python we just call them lists. Think of all the apps you use and how many of the items in the app are organized into lists.

For example:

- A twitter feed is a list of posts
- An online store is a list of products
- The state of a chess game is a list of moves
- This list is a list of things that are lists

Lists in Python are declared using square brackets, with commas separating each item:

```py
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
```

Arrays can contain items of any data type, in our example above we have a `List` of strings.

### Vertical syntax

Sometimes when we're manually creating lists it can be hard to read if all the items are on the same line of code. We can declare the array using multiple lines if we want to:

```py
flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
]
```

Keep in mind this is just a styling change. The code will run correctly either way.

### Counting in Programming

In the world of programming, counting is a bit strange!

We don't start counting at `1`, we start at `0` instead.

### Indexes

Each item in an array has an index that refers to its spot in the array.

Take the following array as an example:

```py
names = ["Bob", "Lane", "Alice", "Breanna"]
```

- Index 0: `Bob`
- Index 1: `Lane`
- Index 2: `Alice`
- Index 3: `Breanna`

### Indexing into Lists

Now that we know how to create new lists, we need to know how to access specific items in the list.

We access items in a list directly by using their _index_. Indexes start at 0 (the first item) and increment by one with each successive item. The syntax is as follows:

```py
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided
```

### List length

The length of a List can be calculated using the `len()` function. Again, we'll cover functions in detail later, but this is the syntax:

```py
fruits = ["apple", "banana", "pear"]
length = len(fruits)
# Prints: 3
```

The length of the list is equal to the number of items present. Don't be fooled by the fact that the length is not equal to the index of the last element, in fact it will always be one greater.

### List Updates

We can also change the item that exists at a given index. For example, we can change `Leather` to `Leather Armor` in the `inventory` array in the following way:

```py
inventory = ["Leather", "Healing Potion", "Iron Ore"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Healing Potion', 'Iron Ore']
```

### Appending in Python

It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the `.append()` method:

```py
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']
```

### Pop Values

`.pop()` is the opposite of `.append()`. Pop removes the last element from the array and returns it for use. For example:

```py
vegetables = ["broccoli", "cabbage", "kale", "tomato"];
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'
```

### Counting the items in a list

Remember that we can iterate (count) over all the items in an array using a loop. For example, the following code will print each item in the `sports` array.

```py
for i in range(0, len(sports)):
    print(sports[i])
```

### No-index Syntax

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

`tree`, the variable declared using the `in` keyword, directly accesses the value in the array rather than the index of the value. If we don't need to update the item, and only need to access its value then this is a more clean way to write the code.

### Find an item in a list

Example of "no-index" or "no-range" syntax:

```py
for fruit in fruits:
    print(fruit)
```

### Modulo operator in Python

#### The modulo operator can be used to find a remainder:

For example, `7` [modulo](https://en.wikipedia.org/wiki/Modulo_operation) `2` would be `1`, because 2 can be multiplied evenly into 7 at most 3 times:

`2 * 3 = 6`

Then there is 1 _remaining_ to get from `6` to `7`.

`7 - 6 = 1`

The d operator is the percent sign: `%`. It's important to recognize modulo is _not_ a percentage though! That's just the symbol we're using.

```py
remainder = 8 % 3
# remainder = 2
```

An odd number is a number that when divided by `2`, the remainder is _not_ `0`.

### Slicing lists

Python makes it easy to slice and dice lists to work only with the section you care about. One way to do this is to use the simple slicing operator, which is just a colon `:`.

With this operator, you can specify where to start and end the slice, and how to step through the original. List slicing returns a _new list_ from the existing list.

The syntax is as follows:

```python
Lst[ Initial : End : IndexJump ]
```

```python
scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]
```

The above reads as "give me a slice of the `scores` list from index 1, up to but not including 5, skipping every 2nd value. _All of the sections are optional_.

```python
scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5])
# Prints [70, 30, 20, 90]
```

```python
scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:])
# Prints [70, 30, 20, 90, 10, 50]
```

### List Operations - Concatenate

Concatenating two lists (smushing them together) is really easy in Python, just use the `+` operator.

```python
all = [1, 2, 3] + [4, 5, 6]
print(all)
# Prints: [1, 2, 3, 4, 5, 6]
```

### List Operations - Contains

Checking whether a value exists in a list is also really easy in Python, just use the `in` keyword.

```python
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True
```

### Tip: Quotes within quotes

To use quotes within quotes, they either need to be [escaped](https://stackoverflow.com/questions/10646142/what-does-it-mean-to-escape-a-string) or you need to use the _other_ kind of quotes. Because we usually use double quotes, we can nest strings with single quotes:

```py
f"banana is in fruits list: {'banana' in fruits}"
```

### List deletion

Python has a built-in keyword `del` that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete items from 2nd to 3rd
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

### Tuples

[Tuples](https://python-reference.readthedocs.io/en/latest/docs/tuple/) are collections of data that are ordered and unchangeable. You can think of a tuple as a `List` with a fixed size. Tuples are created with round brackets:

```python
my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True
```

While it's typically considered bad practice to store items of different types in a List it's not a problem with Tuples. Because they have a fixed size, it's easy to keep track of which indexes store which types of data.

Tuples are often used to store very small groups (like 2 or 3 items) of data. For example, you might use a tuple to store a dog's name and age.

```py
dog = ("Fido", 4)
```

Because Tuples hold their data, multiple tuples can be stored within a list. Similar to storing other data in lists, each tuple within the list is separated by a comma.

```python
my_tuples = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]
print(my_tuples[0][0])
# this is the first tuple in the list
```

## Chapter 7: Functions

Functions allow us to _reuse_ and _organize_ code. For example, let's pretend we need to calculate the area of a circle. We can use the formula `area = pi * r^2`, or in code:

```py
r = 5
area = 3.14 * r * r
```

This works great! The problem arises when multiple places in our code need to get the area of a circle

```py
r = 5
area1 = 3.14 * r * r

r2 = 7
area2 = 3.14 * r2 * r2

r3 = 11
area3 = 3.14 * r3 * r3
```

We want to use the same code, why repeat the work?

Let's declare a new function `area_of_circle()`. Notice that the `def` keyword is written before the function name, and tells the computer that we're declaring, or defining, a new function.

```py
def area_of_circle(r):
    return 3.14 * r * r
```

The `area_of_circle` function takes one input (which can also be called a parameter or argument), and returns a single output. We give our function the radius of a circle and we get back the area of that circle!

To use or "[call](https://en.wikibooks.org/wiki/Python_Programming/Functions#Function_Calls)" the function we can pass in any number as the input, and capture the output into a new variable:

```py
radius = 5
area = area_of_circle(radius)
```

Let's talk through this code example step by step.

1. The `radius` variable is created with a value of `5`.
2. The `area_of_circle` function is called with a single argument: `radius`
3. The `area_of_circle` function is executed, with `r` being equal to `5`
4. The result of `3.14 * r * r` is returned from `area_of_circle`, which happens to be `78.75`
5. `area_of_circle(radius)` resolves to the returned value of `78.75`
6. The `area` variable is created with a value of `78.75`

### Multiple Parameters

Functions can have multiple parameters, or inputs:

```py
def subtract(a, b):
    return a - b
```

### Where to Declare Functions

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

Lines of code execute in _order from top to bottom_, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after the definition.

The `main()` function is a convention used in many programming languages to specify the entrypoint of an application. By defining a single `main` function, and only calling `main()` at the end of the entire program we ensure that all of our function are defined before they're called.

### Order of functions

All functions _must_ be defined before they're used.

You might think this would make structuring Python code difficult because the order in which the functions are declared can quickly become so dependent on each other that writing anything becomes impossible.

As it turns out, most Python developers solve this problem by simply defining all the functions first, then finally calling the entrypoint function _last_. If you do that, then the order that the functions are declared in _doesn't matter_. The entrypoint function is usually called "main".

```python
def main():
    func2()

def func2():
    func3()

def func3():
    print("I'm function 3")

main() # entrypoint
```

### Scope

Scope refers to _where_ a variable or function name is available to be used. For example, when we create variables in a function (by giving names to our parameters for example), that data is _not_ available outside of that function.

For example:

```py
def subtract(x, y)
    return x - y
result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"
```

When the `subtract` function is called, we assign the variable `x` to 5, but `x` only exists in the code _within_ the `subtract` function. If we try to print `x` outside of that function then we won't get a result, in fact we'll get a big fat error.

{{< bdyoutube CKv_WHCcR-w >}}

### Global Scope

So far we've been working in the global scope. That means that when we define a variable or a function, that name is accessible in _every other place_ in our program, even within other functions.

For example:

```py
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius
```

Because `pi` was declared in the parent "global" scope, it is usable within the `get_area_of_circle()` function.

### Infinity

The built-in `float()` function can be used to create a [numeric floating point value](https://www.geeksforgeeks.org/python-float-type-and-its-methods/) that represents the negative infinity value. I've added it for you as a starting point.

```py
negative_infinity = float('-inf')
positive_infinity = float('inf')
```

### None Return

When no return value is specified in a function, (for example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value) it will return `None`. The following code snippets all return exactly the same thing:

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

### Parameters vs arguments

Parameters are the names used for inputs when _defining_ a function. Arguments are the names of the inputs supplied when a function is _called_.

To reiterate, arguments are the actual values that go into the function, say `42.0`, `"the dark knight"`, or `True`. Parameters are the names we use in the function definition to refer to those values, which at the time of writing the function, could be anything.

That said, it is important to understand that this is all semantics, and frankly developers are really lazy with these definitions. You'll often hear the words arguments and parameters used interchangeably.

```py
# a and b are parameters
def add(a, b)
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)
```

### Multiple return values

In Python, we can return more than one value from a function. All we need to do is separate each value by a comma.

```python
# returns email, age, and status of the user
def get_user():
    return "name@domain.com", 21, "active"

email, age, status = get_user()
print(email, age, status)
# Prints: "name@domain.com 21 active"
```

```python
def get_user():
    return "name@domain.com", 21, "active"

# this works, and by convention you should NOT use the underscore variable later
email, _, _ = get_user()
print(email)
# Prints: "name@domain.com"
print(_)
# Prints: "active"
```

### Default values for function arguments

Python has a way to specify a default value for function arguments. This can be convenient if a function has arguments that are essentially "optional", and you as the function creator want to use a specific default value in case the caller doesn't provide one

A default value is created by using the assignment (`=`) operator in the function signature.

```py
def get_greeting(email, name="there"):
    return f"Hello {name}, welcome! You've registered your email: {email}"
```

```py
msg = get_greeting("lane@example.com", "Lane")
# Hello Lane, welcome! You've registered your email: lane@example.com
```

```py
msg = get_greeting("lane@example.com")
# Hello there, welcome! You've registered your email: lane@example.com
```

If the second parameter is omitted, the default `"there"` value will be used in its place. As you may have guessed, for this structure to work, optional arguments that have defaults specified come _after_ all the required arguments.

## Chapter 8: Dictionaries

Dictionaries in Python are used to store data values in `key` -> `value` pairs. Dictionaries are a great way to store groups of information.

```python
car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}
```

### Duplicate keys

Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the associated value will simply be overwritten.

### Accessing Dictionary Values

Dictionary elements must be accessible somehow in code, otherwise they wouldn't be very useful.

A value is retrieved from a dictionary by specifying its corresponding key in square brackets. The syntax looks similar to indexing into a list.

```python
car = {
    'make': 'tesla',
    'model': '3'
}
print(car['make'])
# Prints: tesla
```

### Setting Dictionary Values

You don't need to create a dictionary with values already inside. It is common to create a blank dictionary then populate it later using dynamic values. The syntax is the same as getting data out of a key, just use the assignment operator (`=`) to give that key a value.

```python
names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names_arr = name.split()

    # here we update the dictionary
    names_dict[names_arr[0]] = names_arr[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}
```

### Updating Dictionary Values

If you try to set the value of a key that already exists, you'll end up just updating the value of that key.

```python
names = ["jack bronson", "james mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names_arr = name.split()

    # we're always setting the "jack" key
    names_dict["jack"] = names_arr[1]

print(names_dict)
# Prints: {'jack': 'denver'}
```

### Deleting Dictionary Values

You can delete existing keys using the `del` keyword.

```python
names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['joe']

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}
```

### Deleting keys that don't exist

Notice that if you try to delete a key that doesn't exist, you'll get an _error_.

```python
names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['unknown']
# ERROR HERE, key doesn't exist
```

### Checking for existence

If you're unsure whether or not a key exists in a dictionary, use the `in` keyword.

```python
cars = {
    'ford': 'f150',
    'tesla': '3'
}

print('ford' in cars)
# Prints: True

print('gmc' in cars)
# Prints: False
```

### Iterating over a dictionary in Python

```python
fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny
```

### Ordered or Unordered?

As of Python version `3.7`, dictionaries are _ordered_. In Python `3.6` and earlier, dictionaries were _unordered_.

Because dictionaries are ordered, the items have a defined order, and that order will _not_ change.

Unordered means that the items used to _not_ have a defined order, so you couldn't refer to an item by using an index.

\*\*The takeaway is that if you're on Python `3.7` or later, you'll be able to iterate over dictionaries in the same order every time.

## Chapter 9: Sets

Sets are _like_ Lists, but they are _unordered_ and they guarantee uniqueness. There can be no two of the same value in a set.

```python
fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}
```

### Adding values to a set

```python
fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}
```

### Empty set

Because the `{}` syntax creates an empty dictionary, to create an empty set, just use the `set()` function.

```python
fruits = set()
fruits.add('pear')
print(fruits)
# Prints: {'pear'}
```

### Iterate over values in a set (order is not guaranteed)

```python
fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
```

### Removing values from a set

```python
fruits = {'apple', 'banana', 'grape'}
fruits.remove('apple')
print(fruits)
# Prints: {'banana', 'grape'}
```

## Chapter 10: Errors

You've probably encountered some errors in your code from time to time if you've gotten this far in the course. In Python, there are two main kinds of distinguishable errors.

- syntax errors
- exceptions

### Syntax errors

You probably know what these are by now. A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.

```py
this is not valid code, so it will error
```

If I try to run that sentence as if it were valid code I'll get a syntax error:

```
this is not valid code, so it will error
      ^
SyntaxError: invalid syntax
```

### Exceptions

Even if your code has the right syntax however, it may still cause an error when an attempt is made to execute it. Errors detected during execution are called "exceptions" and can be handled gracefully by your code. You can even raise your own exceptions when bad things happen in your code.

Python uses a try-except pattern for handling errors.

```python
try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"
```

The `try` block is executed until an exception is raised or it completes, whichever happens first. In this case, a "divide by zero" error is raised because division by zero is impossible. The `except` block is only executed if an exception is raised in the `try` block. It then exposes the exception as data (`e` in our case) so that the program can handle the exception gracefully without crashing.

### Raising your own exceptions

Errors are _not_ something to be scared of. Every program that runs in production is expected to manage errors on a constant basis. Our job as developers is to handle the errors gracefully and in a way that aligns with our user's expectations.

#### Errors are NOT bugs

{{< bdyoutube k23hjyvvhcA >}}

When something in our own code happens that we don't expect, we should raise our own exceptions. For example, if someone passes some bad inputs to a function we write, we should not be afraid to raise an exception to let them know they did something wrong.

An _error_ or _exception_ is raised when something bad happens, but as long as our code handles it as users expect it to, it's _not_ a bug. A bug is when code behaves in ways our users don't expect it to.

For example, if a player tries to forge an iron sword out of bronze metal, we might raise an exception and display an error message to the player. However, that's the expected behavior of the game, so it's not a bug. If a player can forge the iron sword out of bronze, that may be considered a bug because that's against the rules of the game.

```python
raise Exception("something bad happened")
```

Software applications aren't perfect, and user input and network connectivity are far from predictable. Despite intensive debugging and unit testing, applications will still have failure cases.

Loss of network connectivity, missing database rows, out of memory issues, and unexpected user inputs can all prevent an application from performing "normally". It is your job to catch and handle any and all exceptions gracefully so that your app keeps working. When you are able to detect that something is amiss, you should be raising the errors yourself, in addition to the "default" exceptions that the Python interpreter will raise.

```python
raise Exception("something bad happened")
```

#Different types of exceptions

We haven't covered classes and objects yet, which is what an `Exception` really is at its core. We'll go more into that in the object-oriented programming course that we have lined up for you next.

For now, what is important to understand is that there are different types of exceptions and that we can differentiate between them in our code.

### More syntax for errors

```python
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception:
    print("unknown exception")

try:
    nums = [0, 1]
    print(nums[2])
except ZeroDivisionError:
    print("0 division")
except Exception:
    print("unknown exception")
```

Which will print:

```
0 division
unknown exception
```

## Chapter 11: Python Facts

### The Zen of Python

Tim Peters, a long time Pythonista describes the guiding principles of Python in his famous short piece, [The Zen of Python](https://www.python.org/dev/peps/pep-0020/).

> Beautiful is better than ugly.
>
> Explicit is better than implicit.
>
> Simple is better than complex.
>
> Complex is better than complicated.
>
> Flat is better than nested.
>
> Sparse is better than dense.
>
> Readability counts.
>
> Special cases aren't special enough to break the rules.
>
> Although practicality beats purity.
>
> Errors should never pass silently.
>
> Unless explicitly silenced.
>
> In the face of ambiguity, refuse the temptation to guess.
>
> There should be one-- and preferably only one --obvious way to do it.
>
> Although that way may not be obvious at first unless you're Dutch.
>
> Now is better than never.
>
> Although never is often better than _right_ now.
>
> If the implementation is hard to explain, it's a bad idea.
>
> If the implementation is easy to explain, it may be a good idea.
>
> Namespaces are one honking great idea -- let's do more of those!

### Why Python?

Here are some reasons we think Python is a future-proof choice for developers:

- Easy to read and write - Python reads like plain English. Due to its simple syntax, it's a great choice for implementing advanced concepts like AI. This is arguably Python's _best feature_.
- Popular - According to the Stack Overflow Developer Survey, [Python is the 4th most popular](https://insights.stackoverflow.com/survey/2020#most-popular-technologies) coding language in 2020.
- Free - Python, like many languages nowadays, is developed under an open-source license. It's free to install, use, and distribute.
- Portable - Python written for one platform will work on any other platform.
- Interpreted - Code can be executed as soon as it's written. Because it doesn't need to take a long time to compile like Java, C++, or Rust, releasing code to production is typically faster.

### Why not Python?

Python might not be the best choice for a project if:

- The code needs to run fast. Python code executes very slowly, which is why performance critical applications like PC games aren't written in Python.
- The codebase will become large and complex. Due to its dynamic type system, Python code can be harder to keep clean of bugs.
- The application needs to be distributed directly to non-technical users. They would have to install Python in order to run your code, which would be a huge inconvenience.

### Python 2 vs Python 3

One thing that's important to keep in mind as you continue your Python journey is that the Python ecosystem suffers from split personality syndrome. Python 3 was released on December 3rd, 2008, but over a decade later the web is still full of Python 2 dependencies, scripts and tutorials.

In this course, **we used Python 3** - just like any good citizen should these days.

One of the most obvious breaking changes between Python 2 and 3 is the syntax for printing text to the console.

#### Python 2

```python
print "hello world"
```

#### Python 3

```python
print("hello world")
```

## Congratulations on making it to the end!

If you're interested in doing the interactive coding assignments and quizzes for this course you can check out the [Learn Python course over on Boot.dev](https://boot.dev/courses/learn-python).

That course is a part of my full [back-end developer career path](https://boot.dev/tracks/backend), made up of other courses and projects if you're interested in checking those out.
