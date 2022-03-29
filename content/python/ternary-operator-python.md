---
title: "How to Use the Ternary Operator in Python"
author: Lane Wagner
date: "2021-12-09"
categories: 
  - "python"
---

Developers love concise code that's easy to read. A ternary operator in Python is a piece of syntax that lets you perform a small if/else statement in a single line. Let's take a look at a few examples.

## Selecting the larger number with a ternary

```py
bob_height = 6
jill_height = 7
larger_height = bob_height if bob_height > jill_height else jill_height
```

You'll notice that a ternary in Python actually looks a lot like a normal if/else statement, just jammed into one line. That's basically what it is, except it also returns a value.

Contrast that syntax with JavaScript's ternary, which feels a little different.

```js
const largerHeight = bobHeight > jillHeight ? bobHeight : jillHeight;
```

Structure of a ternary in Python

Now that you've seen an example, it's important to understand what's going on.

```
[on_true] if [expression] else [on_false] 
```

`on_true` is returned if the `expression` is truthy, while `on_false` is returned if `expression` is falsy.

## Nested ternary in Python

First of all, I need to get this off my chest: please don't nest your ternaries! It's confusing and hard to read. That said, here's how you would do it.

```py
my_account = 100
wifes_account = 200

print("We have the same" if my_account == wifes_account else "I have more" if my_account > wifes_account else "Wife has more")
```

## Should you use ternaries in Python?

Generally speaking, yes. Ternaries are fantastic little bits of syntactic sugar that make code more concise and readable when used sparingly. You should probably never nest ternaries, or try to use them with anything more than a simple assignment operation. By trying to use ternaries too often, your code becomes very hard for others (or yourself) to understand later.
