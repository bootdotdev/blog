---
title: "JavaScript Map Function Explained - A Deep Dive"
author: lane
date: "2020-01-12"
categories: 
  - "javascript"
images:
  - /img/800/javascript-map-function-explained.webp
---

The built-in JavaScript `map` function returns a new array, where each element in the new array is the result of the corresponding element in the old array after being passed through a callback function. Later in the article, we'll do a deep dive into some more advanced concepts regarding the map function and its uses.

## Map Function Syntax

### Example Usage

```js
let newArray = oldArray.map(function callback(currentValue, index, array) {
    // return element for new_array
}, thisArg)
```

The Array object's built-in `map` method takes a function definition as its first parameter. The function whose definition we pass in will have 3 arguments available to it and will be called for each element in the original array. Each return value that the function creates will be the elements for the new array.

For instance, a simple example would look like:

```js
const oldArray = [1, 4, 9, 16];

function double(val, index, arr){
  return val * 2
}

const newArray = oldArray.map(double);

// newArray = [2, 8, 18, 32]
```

There is also an optional second parameter to the map function that we will go over later, a way to override `thi`s.

## Syntactic Sugar

In the above example, to double each value in the original array, we only used the `val` argument. It's _extremely_ common to only care about the `val` argument in the map function. When that's all we need we can simplify the syntax, and even throw in some es6 arrow functions:

```js
const oldArray = [1, 4, 9, 16];

const double = arr => arr * 2;

const newArray = oldArray.map(double);

// newArray = [2, 8, 18, 32]
```

By only specifying one argument in our function definition, the interpreter will only give our function the `val` parameter, which is okay if it's the only thing we care about.

We can also use an anonymous function, which means defining the function in the map's input instead of giving it a name. This keeps our code clean and readable (assuming we don't need to reuse the callback function elsewhere)

```js
const oldArray = [1, 4, 9, 16];

const newArray = oldArray.map(arr => arr * 2);

// newArray = [2, 8, 18, 32]
```

## Index Parameter

If you remember from earlier, the callback function definition has a second parameter, the index:

```js
function callback(currentValue, index, array)
```

By using the index parameter we can do some more interesting calculations based on the position in the array:

```js
const oldArray = [1, 4, 9, 16];

const newArray = oldArray.map((val, index) => {
  return val * index
});

// newArray = [0, 4, 18, 48]
```

## Array Parameter

The third and final parameter made available to our callback is a copy of the original array. This can be useful if we care about more than just the value or index that we are currently operating on. We can look forward or backward in the array and use other elements as part of our mapping:

```js
const oldArray = [16, 9, 4, 1];

const newArray = oldArray.map((val, index, arr) => {
  let nextItem = index + 1 < arr.length ? arr[index + 1] : 0
  return val - nextItem;
});

// newArray = [7, 5, 3, 1]
```

## Overriding 'This'

The map function has an often-overlooked optional second parameter. We can provide an object that will become 'this' within the scope of our callback.

```js
let newArray = oldArray.map(callbackFunction, thisArg)
```

For example, maybe we have a callback that is used in other places in our code, and we want to reuse it, but we just need to change the environment it operates in:

```js
const oldArray = [1, 4, 9, 16];

function ourFunc(val, index, arr){
  return val * this.windowSize
}

const newArray = oldArray.map(ourFunc, {windowSize: 10});

// newArray = [10, 40, 90, 169]
```

Now we can reuse that callback, but change its parameters by modifying 'this'.

## Using .map() in React

It's super common in React.js or Vue.js to need to render a list of data on a page, and the `.map()` method is a great way to do it. [This Scrimba post](https://scrimba.com/articles/react-list-array-with-map-function/) gives us a great example:

```jsx
const heroes = ["Superman", "Batman", "Wonder Woman"]

const Headings = () => {
  const headings = heroes.map((hero, index)=>
    <h1 key={index}>{hero}</h1>)
  return <header>{headings}</header>
}
```
