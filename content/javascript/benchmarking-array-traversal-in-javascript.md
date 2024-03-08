---
title: "Which Method of Iteration in JavaScript is Fastest?"
author: Lane Wagner
date: "2019-11-08"
categories: 
  - "javascript"
images:
  - /img/800/ruinreborn_fantasy_horse_fantasy_rider_fantsy_horse_rider_gallp_25c1675d-fc0d-413d-8fab-9fc5138f7e41.png
---

There are many ways to traverse an array in Javascript. In this benchmark, we will look at five different ways and the pros and cons of each. Keep in mind that these benchmarks were run in a Chrome browser on Codepen.io. Results will vary by browser/interpreter.

For a working example of these benchmarks, take a look at this [codepen](https://codepen.io/lane-c-wagner/pen/GRRGryr). All benchmarks we ran on an array of 1,000,000,000 items.

## 1st: Vanilla JS - Backwards

```js
for (let i = arr.length-1; i>=0; i--){}
```

~ 30 milliseconds

Going **backwards is faster** than going forward! At each iteration the loop checks against a constant 0 zero value instead of calling the array's `.length` property. I highly recommend NOT putting this optimization into practice however, it's weird and results in hard to understand code.

## 2nd: Vanilla JS - Forwards

```js
for (let i = 0; i< arr.length; i++){}
```

~39 milliseconds

## 3rd: ES6 forEach()

```js
arr.forEach(function(element) {});
```

~180 milliseconds

Slow but with a more convenient syntax, nothing surprising here.

## 4th: jQuery Each

```js
$.each(arr, function( index, value ) {});
```

~225 milliseconds

Eeeeeew... jQuery. Convenient if you live in 2010. Very Slow.

## Wildcard: For..Of ES6

```js
for (const item of arr){}
```

First and second time running: 153 Milliseconds

Third+ times running : ~18 milliseconds

This is weird, and I'm not sure how to explain it. Maybe someone smarter than me can tweet me the answer [@wagslane](https://twitter.com/wagslane) . The first two times running this after a fresh browser load are quite slow, but then it gets blazingly fast. I'm assuming there are some es6 optimizations under the hood that kick in.
