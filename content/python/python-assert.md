---
title: "Python Assert Statement, How to Test a Condition"
author: Lane Wagner
date: "2021-12-13"
categories: 
  - "python"
images:
  - /img/yell.webp
---

In Python, an assertion is a statement that confirms something about the state of your program. For example, if you write a `createUser` function and you are sure that the user needs to be older than 18, you assert that the `age` field is greater than or equal to 18. You can think of an `assert` statement like a [unit test](/clean-code/writing-good-unit-tests-dont-mock-database-connections/) that is performed at runtime.

```py
def createUser(user):
  assert user.age >= 18
```

## tl;dr

- Assertions are simply boolean expressions that raise exceptions if their condition is `False`
- The `assert` statement is the built-in syntax for assertions in Python
- Developers often use `assert` to do type checking, and input/output validation for function signatures
- The `assert` statement is used for debugging purposes

## Anatomy of an assert statement in Python

Python has a built-in `assert` statement, and its syntax is as follows.

```py
assert condition [, error_message]
```

If the {condition} is false, an [AssertionError](https://docs.python.org/3/library/exceptions.html#AssertionError) is raised. If the optional second parameter, `error_message` was set, then that error message is used.

{{< cta1 >}}

## Catching an assertion error

You can catch an assertion error just like you would any other error in Python.

```py
age = 17
try:
    assert age >= 18, "too young!"
except Exception as e:
    print(e)
# prints: "too young!"
```

## Don't use the assert statement in production

The `assert` statement is a fantastic tool for debugging code and writing tests. You should probably **not** use an assert statement in a production environment. You should be checking your code for unexpected behavior _before_ you deploy it.

![](/img/test-in-production-meme.jpeg)

## Don't use parenthesis for the assert parameters

Do not use parentheses to call `assert` as if it were a normal function. Asser is a statement, not a function. When you call `assert(condition,message)`, you execute the `assert` statement with a tuple `(condition,message)` as the condition, and no actual message.
