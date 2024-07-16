---
title: "Top 20 Entry-Level JavaScript Interview Questions"
author: Jamie Dunmore
date: "2021-07-29"
categories: 
  - "javascript"
  - "jobs"
images:
  - /img/800/JavaScript-Interview-Questions.webp
---

Versatile, powerful and ever-present, JavaScript is the world's most used programming language (for eight years and counting!) and shows no signs of slowing down. Check out these 20 practice interview questions for JavaScript! If you're on the job-hunt for an entry-level position, read on.

94.5% of web pages use JavaScript, it's one of the 10 most-loved programming languages, and with median salaries of [$112,000](https://insights.stackoverflow.com/survey/2020#technology-what-languages-are-associated-with-the-highest-salaries-worldwide-united-states) in the US, JavaScript offers a way to fast-track your way to higher earnings if you're thinking of switching careers.

You've mastered the basics -- perhaps by taking our [Intro to JavaScript course](https://boot.dev/courses/learn-javascript) -- and tried your hand at some simpler JavaScript projects or challenges. But are you ready for an entry-level junior dev role writing JavaScript?

To help you find out, here's a selection of 20 basic JavaScript interview questions you may be asked a variation of on the way to securing your first job.

**Quick note:** These tests help you discover any knowledge gaps you may have so you can fortify your skills and flourish when faced with real-life JavaScript interview questions in the future. So, don't be put off if the answers don't come to you instantly -- going back and refreshing any areas you aren't 100% comfortable means you're one step closer to mastering JavaScript!

## 1 -- What are the JavaScript data types?

**Answer:**

1. Number
2. String
3. Boolean
4. Object
5. Symbol
6. Undefined
7. Null

## 2 -- What are the differences between global and local variables? And how can having too many global variables negatively affect your code?

**Answer:**

Global variables have no scope and are accessible globally — they're fully available and accessible throughout your code.

However, global variables can also be more difficult to debug as coupling occurs between the many global variables, making bugs more likely, as well as more difficult to find and debug. There can also be conflicts between variable names in the local and global scope.

## 3 -- What are the differences between the `=`, `==`, and `===` operators?

**Answer:**

The `=` operator is for saying a variable is equal to something when declaring it, such as a string or a number:

```js
let fifty = 50

let greeting = "Hey there!"
```

The `==` abstract equality operator checks for equality only in value, and is a less strict evaluator than the `===` operator. The `==` operator converts the variable values to the same type before comparing them — also known as type coercion.

Therefore, even if two different variables are named, such as the number `2` and string`'2'`, as variables are converted to the same value before comparing them, this will still evaluate to true:

```js
console.log('2' == 2)
// true

console.log(0 == false)
// true
```

The `===` strict equality operator does not use any form of type coercion, and to evaluate as `true` both the type and the value must be the same:

```js
console.log('2' === 2)
// false

console.log(2 === 2)
// true

console.log(0 === false)
// false
```

## 4 -- How would you use escape characters to correctly log quotes in a string? For example, "Him & I are "good" friends."

**Answer:**

```js
console.log("Him & I are \"good\" friends.")
```

The `\` character is used before the double quotes to be able to use these in the string.

## 5 -- Explain the `.pop()` and `.push()` methods using the following array:

```js
let bootdotdev = ["the", "best", "coding", "courses", "ever", "like", "totally"];
```

1. What would happen if you used `bootdotdev.pop()`
2. What would happen if you used `bootdotdev.push("definitely", "start", "it")`

**Answers:**

The `.pop()` method removes the last element in the array and returns it. In the array above, `bootdotdev.pop()` would return `"totally"`.

The `.push()` method instead adds any included elements to the end of the array, and returns the new length of that array. In the array above, pushing:

```js
bootdotdev.push("definitely", "start", "it")
```

would return the length `10` , and if you `console.log(bootdotdev)` you would get:

```js
["the","best","coding","courses","ever","like","totally","definitely","start","it"]
```

## 6 -- What are higher order functions, and what are their benefits?

**Answer:**

Higher-order functions are functions that either accept or return another function — by taking them as an argument, or by returning them. They allow for common patterns that support the `.map`, `.sort` or `.filter` functions, for example.

Take a look at how the map function accepts a function as a parameter and applies it to the given array.

```js
const primes = [3, 5, 7, 11];

// pass a function to map
const doubledPrimes = primes.map(x => x * 2);

console.log(doubledPrimes);
// expected output: Array [6, 10, 14, 22]
```

## 7 -- Write a loop that prints every number divisible by 3 from 1-200:

**Answer:**

```js
for (let i = 1; i < 201; i++) {
  if (i % 3 === 0) {
    console.log(i)
  }
}
```

## 8 -- Name all JavaScript's Boolean logical operators:

**Answer:**

The AND `&&` operator, the NOT `!` operator, and the OR `||` operator.

The `&&` AND operator requires both operands to be true to evaluate to true. For example:

```js
if (age >= 21 && drinksConsumed <= 10) { 
     console.log('You can drink here.')
}
```

The `||` OR operator requires one of the operands to be true to evaluate to true. For example:

```js
if (age >= 12 || height >= 150) { 
     console.log('You can ride the rollercoaster.') 
}
```

The `!` NOT operator evaluates to true if the two operands are not equal. For example:

```
x = 7;
y = 5;

!(x == y) // evaluates to true
```

## 9 -- How do `break` and `continue` statements differ and where would you use each?

**Answer:**

`Break` statements cause the code to exit a loop immediately.

```js
for (let i = 0; i < 100; i++) {
  if (i === 10) { break; } // this ends the loop early (at 10 instead of 100)
  console.log('the current number is: ' + i)
}
```

`Continue` statements immediately jump to the next iteration of the loop.

```js
for (let i = 0; i < 100; i++) {
  if (i%2 === 0) { continue; } // skips even numbers
  console.log('The number is odd');
}
```

## **10 -- What is JSON? And how would you convert JSON strings into objects, or convert an object into a JSON string?**

**Answer:**

JSON, or JavaScript Object Notation, is used to send and convert plain text into JavaScript objects, and they are written in exactly the same way. JSON is often used to display data on a web page after being read from a web server.

It's used to send data between computers, but can also be used by any programming language — it isn't limited to JavaScript. The text-only format makes it easy to send between computers.

To convert a JSON string into a JavaScript object, use this function:

```js
JSON.parse()
```

To convert an object into a JSON string, use this function:

```js
JSON.stringify()
```

## 11 -- What are the `.slice()` and `.splice()` methods, and how do they differently affect arrays?

**Answer:**

`.slice()` doesn't modify the original array, and returns the elements from the array, minus the instructed elements to be sliced off based on the numbers instructed in the brackets.

If one parameter is written, this will be used as the start parameter, and if two parameters are written, the second element will be used as the end parameter.

```js
const reasonsToTryBootdotdev = ["free trial", "interactive", "browser based", "helpful community", "range of content"]; 

reasonsToTryBootdotdev.slice(2,4)
// ["browser based", "helpful community"]
```

The `.splice()` method instead modifies the original array. It returns the deleted elements as arrays, and is often use to insert or remove elements to or from an existing array.

```js
const reasonsToTryBootdotdev = ["free trial", "interactive", "browser based", "helpful community", "range of content"]; 
const removed = reasonsToTryBootdotdev.splice(2,4)
console.log(reasonsToTryBootdotdev)
// ["free trial","interactive"]

console.log(removed)
// ["browser based","helpful community","range of content"]
```

## 12 -- What are arrow functions and what benefits do they bring in your code?

**Answer:**

Arrow functions were introduced in ES6 and are a shorthand version of writing traditional functions. They save room and can make code more easily readable, are quicker to write, and can make coding more efficient. They also inherit the parent version of `this`.

```js
// pre-ES6 traditional way
function (height) {
  return height + 10;
}

// post-ES6 way with arrow functions
height => height + 10;
```

## 13 -- What is the `isNaN` function?

**Answer:**

The `isNaN` function determines whether a value is, or is not, a number (Not-a-Number). If the value is not a number, it will evaluate to `true`, and if the value is a number, it will evaluate to `false`.

## 14 -- What are the differences between undeclared and undefined variables?

**Answers:**

**Undeclared variable:** a variable that isn't declared as a variable using the `var` , `const` or `let` keywords.

**Undefined variable:** a variable that has been defined using one of the variable keywords, but hasn't been given a value.

## 15 -- How would you submit a form in JavaScript?

**Answer:**

```js
document.forms[0].submit()
```

This will submit the first form on the page (index `0`).

## 16 -- When are you most likely to use the `then` method?

**Answer:**

Promises, introduced in JavaScript ES6 in 2015, are an effective way to handle deferred and asynchronous computation.

The `then` method is used with Promises to execute based on whether the Promise has been fulfilled, or rejected. The Promise is originally substituted in for the eventual value after the deferred computation has finished, with the `then` method consisting of two callback functions for either the success or fail case within the Promise.

## 17 -- How would you write an object for a database containing the following person's details:

- Jamie, age 24, with green eyes and ID number 5000.

**Answer:**

```js
const person = {
   firstName: "Jamie",
   age: 24,
   eyeColor: "green",
   id: 5000
}
```

## 18 -- Name 3 JavaScript frameworks and give a short description of what they're used for:

**Answer:**

Could include:

- AngularJS
- React
- Vue.js
- Ember.js
- Express.js
- Meteor
- Polymer
- Mithril.js
- Svelte
- Backbone
- jQuery

## 19 -- Name the 6 screen objects and what they describe:

**Answer:**

- `AvailHeight` — returns the available height in the client's screen
- `AvailWidth` — returns the available width in the client's screen
- `ColorDepth` — the depth of images supported on the client's screen
- `PixelDepth` — the depth of pixels supported on the client's screen
- `Height` — the height of the screen
- `Width` — the width of the screen

## 20 -- What is the DOM? And what does it do?

**Answer:**

The Document Object Model represents HTML documents in a way JavaScript can interpret.

The DOM is an object-oriented view of the HTML web page document where each HTML attribute is an object within a hierachy consisting of element, attribute and body nodes that can then be accessed and modified or manipulated using functions.
