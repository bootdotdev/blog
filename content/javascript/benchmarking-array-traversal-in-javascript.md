---
title: "Benchmarking Array Traversal in Javascript - Going Backwards is Fastest"
date: "2019-11-08"
categories: 
  - "javascript"
tags: 
  - "sharing"
---

There are many ways to traverse an array in Javascript. In this benchmark, we will look at five different ways and the pros and cons of each. Keep in mind that these benchmarks were run in a Chrome browser on Codepen.io. Results will vary by browser/interpreter.

For a working example of these benchmarks, take a look at this [codepen](https://codepen.io/lane-c-wagner/pen/GRRGryr). All benchmarks we ran on an array of 1,000,000,000 items.

## 1st: Vanilla JS - Backwards

```
for (let i = arr.length-1; i>=0; i--){}
```

~ 30 milliseconds

Going **backwards is faster** than going forward! At each iteration the loop checks against a constant 0 zero value instead of calling the array's `.length` property. I highly recommend NOT putting this optimization into practice however, it's weird and results in hard to understand code.

## 2nd: Vanilla JS - Forwards

```
for (let i = 0; i< arr.length; i++){}
```

~39 milliseconds

## 3rd: ES6 forEach()

```
arr.forEach(function(element) {});
```

~180 milliseconds

Slow but with a more convenient syntax, nothing surprising here.

## 4th: jQuery Each

```
$.each(arr, function( index, value ) {});
```

~225 milliseconds

Eeeeeew... jQuery. Convenient if you live in 2010. Very Slow.

## Wildcard: For..Of ES6

```
for (const item of arr){}
```

First and second time running: 153 Milliseconds

Third+ times running : ~18 milliseconds

This is weird, and I'm not sure how to explain it. Maybe someone smarter than me can tweet me the answer [@wagslane](https://twitter.com/wagslane) . The first two times running this after a fresh browser load are quite slow, but then it gets blazingly fast. I'm assuming there are some es6 optimizations under the hood that kick in.

## Related JS Articles

- [How to Make a Custom Select Component in Vue.js](https://qvault.io/2019/09/09/how-to-make-a-custom-select-component-in-vue-js/)
- [How to Re-render a Vue Route When Path Parameters Change](https://qvault.io/2020/07/07/how-to-rerender-a-vue-route-when-path-parameters-change/)
- [Randomness and Entropy in Node and Electron](https://qvault.io/2019/07/03/randomness-and-entropy-in-node-and-electron/)
