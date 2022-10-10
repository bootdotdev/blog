---
title: "How to Use the Ternary Operator in Python"
author: Lane Wagner
date: "2021-12-09"
lastmod: "2022-07-20"
categories: 
  - "python"
images:
  - /img/800/ternary.webp
---

Developers love concise code that's easy to read, and that's exactly what ternary operators are for. The ternary operator in Python lets you perform a small `if/else` statement in a **single line**. Let's take a look at a few examples.

## Example of selecting the larger number with a Pythonic ternary

```py
bob_height = 6
jill_height = 7
larger_height = bob_height if bob_height > jill_height else jill_height
# larger_height = 7
```

You'll notice that a ternary in Python actually looks a lot like a normal if/else statement, just jammed into one line. That's basically what it is, except it also returns a value.

Contrast that syntax with JavaScript's ternary, which feels a little different.

```js
const largerHeight = bobHeight > jillHeight ? bobHeight : jillHeight;
```

## The formal structure of a ternary

Now that you've seen an example, it's important to understand what's going on. As you may have gathered from the name *ternary*, it takes 3 operands:

* true_val
* condition
* false_val

```
[true_val] if [condition] else [false_val]
```

`true_val` is returned if the `condition` is truthy, while `false_val` is returned if `condition` is falsy.

## Example of checking if a number is oven or odd with a ternary

```py
def is_even_message(num):
  return "Number is even!" if num%2 == 0 else "Number is odd!"

print(is_even_message(6))
# Number is even!

print(is_even_message(5))
# Number is odd!
```

{{< cta1 >}}

## Example of a nested ternary

First of all, I need to get this off my chest: *please don't nest your ternaries!* It's confusing and hard to read. That said, here's how you can do it if you really want to.

```py
my_account = 100
wifes_account = 200

print("We have the same" if my_account == wifes_account else "I have more" if my_account > wifes_account else "Wife has more")
```

## Should you use ternaries in the Python programming language?

Generally speaking, *yes*. Ternaries are fantastic little bits of syntactic sugar that make code more concise and readable when used sparingly. You should probably never nest ternaries, or try to use them with anything more than a simple assignment operation. By trying to use ternaries too often, your code becomes very hard for others (or yourself) to understand later.
