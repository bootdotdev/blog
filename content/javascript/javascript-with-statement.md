---
title: "JavaScript With Statement Explained – A Deep Dive"
date: "2020-01-15"
categories: 
  - "javascript"
---

JavaScript's built-in `with` statement specifies the default object for the given property and gives us a shorthand for writing long object references. More precisely, it adds the given object to the head of the scope chain.

Note: Use of the _with_ statement is discouraged. It can lead to strange bugs. That said, it's important to understand how it works because it may exist in legacy code.

## With Function Syntax

### Usage

```
with (expression){
  statement
}
```

_expression_: An [expression](https://en.wikipedia.org/wiki/Expression_(computer_science)) that evaluates to an object that will become the default object inside its scope.

_statement_: Code that will run with the evaluated expression as the default object

## Example

```
let car = {color: 'red'}
with(car){
  console.log(color)
}

// prints 'red'
```

As you can see, the car object becomes the default object in the scope. The object's properties become available without using the dot (`.`) operator.

If the variable already exists in the parent scope, it will be overwritten:

```
let color = 'blue'
let car = {color: 'red'}
with(car){
  console.log(color)
}

// prints 'red'
```

## Why Shouldn't I Use 'With'?

![stop sign in bushes](/img/photo-1550770203-e14cc04c58fa-1024x680.jpeg)

> Using `with` is not recommended, and is forbidden in ECMAScript 5 [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions_and_function_scope/Strict_mode). The recommended alternative is to assign the object whose properties you want to access to a temporary variable.
> 
> [Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)

While using `with` can make long pieces of code easier to read due to the removal of long accessor paths, the danger of potential bugs due to ambiguity isn't worth the convenience.

```
with(car.make.model){
  let size = width * height * length;
}

// vs

let size = car.make.model.width * car.make.model.height * car.make.model.length;
```

There's an argument to be made that code will be smaller and easier to send to the browser by using 'with' statements. While true, the gains are negligible, especially when compared to what code minifiers do.

## Related Reading

- [JavaScript Map Function Explained - A Deep Dive](https://qvault.io/2020/01/12/javascript-map-function-explained-a-deep-dive/)
- [JavaScript vs Java – Differences, Similarities, and History](https://qvault.io/2020/01/14/javascript-vs-java-differences-similarities-and-history/)
- [Go’s WaitGroup – JavaScript’s PromiseAll??](https://qvault.io/2020/06/04/gos-waitgroup-javascripts-promiseall/)
