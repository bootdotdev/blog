---
title: "Guard Clauses - How to Clean up Conditionals"
author: Lane Wagner
date: "2020-09-06"
categories: 
  - "clean-code"
images:
  - /img/800/Guard-Clauses.webp
---

One of the first concepts [new developers](https://blog.boot.dev/) learn is the if/else statement. If/else statements are the most common way to execute conditional logic. However, complex and nested if/else statements can quickly become a cognitive burden and compromise the readability of a program.

## Guard Clauses

Guard Clauses leverage the ability to return early from a function (or continue through a loop) to make nested conditionals one-dimensional. Instead of using if/else chains, we just return early from the function at the end of each conditional block.

```go
func divide(dividend, divisor int) (int, error) {
	if divisor == 0 {
		return 0, errors.New("Can't divide by zero")
	}
	return dividend/divisor, nil
}
```

Error handling in Go naturally encourages developers to make use of guard clauses. When I started writing more JavaScript, I was disappointed to see how many nested conditionals existed in the code I was working on.

Let's take a look at an exaggerated example of nested conditional logic:

```js
function getInsuranceAmount(status) {
  let amount;
  if (!status.hasInsurance()){
    amount = 1;
  } else {
    if (status.isTotaled()){
      amount = 10000;
    } else {
      if (status.isDented()){
        amount = 160;
        if (status.isBigDent()){
          amount = 270;
        }
      } else {
        amount = 0
      }
    }
  }
  return amount;
}
```

Could be written with guard clauses instead:

```js
function getInsuranceAmount(status) {
  if (!status.hasInsurance()){
    return 1;
  }
  if (status.isTotaled()){
    return 10000;
  }
  if (!status.isDented()){
    return 0;
  }
  if (status.isBigDent()){
    return 270;
  }
  return 160;
}
```

The example above is **much** easier to read and understand. When writing code, it's important to try to reduce the cognitive load on the reader by reducing the number of entities they need to think about at any given time.

In the first example, if the developer is trying to figure out when **270** is returned, they need to think about each branch in the logic tree and try to remember which cases matter and which cases don't. With the one-dimensional structure offered by guard clauses, it's as simple as stepping through each case in order.
