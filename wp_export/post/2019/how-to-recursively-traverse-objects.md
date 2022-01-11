---
title: "How to Recursively Traverse JSON Objects"
date: "2019-09-22"
categories: 
  - "javascript"
---

I've found that it's pretty rare that I need recursion in application code, but every once in a while I need to write a function that operates on a tree of unknown depth, such as a JSON object, and that's often best solved recursively. Even though recursion is rare, it is important to recognize when a problem is best solved recursively so that we can implement a good solution when the time comes.

## What is Recursion?

Function recursion is a process in computer science that occurs when a function calls itself.

![man answering two phones](images/cut.jpg)

For example:

```
function printArrayRecursive(arr, i) {
  // base case, stop recurring
  if (i === arr.length){
    return;
  }
  console.log(arr[i])
  // call ourself with the next index
  recursive(arr, i+1)
}
```

In the code above, `printArrayRecursive` prints one element from the list, then calls itself again with the next index. Each successive call to itself prints the next element, and so on. The recursion continues until the **base case** is reached. In our example, the base case is when the index is equal to the array's length.

The same function looks quite a bit different in the **iterative** world, which you are probably more familiar with:

```
function printArrayIterative(arr){
  for (let i = 0; i < arr.length; i++){
    console.log(arr[i])
  }
}
```

In the case of simply printing the items of a list, the iterative approach is better for a number of reasons:

- Easier to read and understand
- Less memory utilization - _Recursive functions keep all calls on the stack until the base case is reached_
- Faster compute time - _Recursive functions come with the overhead of an entire function call for each step_
- If there is a bug in the recursion, the program is likely to enter an infinite loop

## Why Use Recursion?

Iterative programs can be written using recursion, and all recursive programs can be written using iteration. Both systems are, unless limited by the implementation, [Turing c](https://en.wikipedia.org/wiki/Turing_completeness)[omplete](https://en.wikipedia.org/wiki/Turing_completeness).

![mechanical turing machine ](images/mechanical-turing-machine-in-wood-vo8izckhif0mp4-shot0001_featured.png)

[mechanical turing machine](https://hackaday.com/2018/03/08/mechanical-wooden-turing-machine/)

The primary reason to choose recursion over iteration is **simplicity**.

Many years ago the majority of compilers and interpreters didn't support the syntax for iteration. **For-loops simply didn't exist**. This is primarily because it's much simpler to write an interpreter that can handle recursion than it is to write one that supports loops.

Even if a compiler supports loops, some problems are easier to solve with a recursive function. A good example is tree traversal. I often write recursive functions to find every property of any JSON object, or to search every file in a folder that may have an infinite number of nested subfolders.

## Examples

Recursively print all properties of a JSON object:

```
function printAllVals(obj) {
  for (let k in obj) {
    if (typeof obj[k] === "object") {
      printAllVals(obj[k])
    } else {
      // base case, stop recurring
      console.log(obj[k]);
    }
  }
}
```

Recursively print all the filenames of a folder, and its subfolders, and their subfolders, ad infinitum.

```
function printSubFiles(dir) {
  files = fs.readdirSync(dir);
  files.forEach(function (file) {
    absName = `${dir}/${file}`
    if (fs.statSync(absName).isDirectory()) {
      printSubFiles(absName)
    } else {
      // base case, stop recurring
      console.log(file)
    }
  });
};
```

When trying to figure out how to write a function recursively, think:

> _"What is my base case? What should stop the recursion from continuing?"_

Once that's hammered out, the rest of the function just needs to answer the questions,

> _"What do I want to do with my current value?"_

and

> _"How do I call myself to get to the next value?"_

Recursion is an important principle to understand for any programmer, and I hope this helps you be just a little better! If you're interested in learning more about recursion and functional programming principles, take a look at our [functional programming course.](https://qvault.io/intro-to-functional-programming/)

## Related Articles

- [How to Re-render a Vue Route When Path Parameters Change](https://qvault.io/2020/07/07/how-to-rerender-a-vue-route-when-path-parameters-change/)
- [How To Cache Images – React Native Expo (Managed)](https://qvault.io/2020/02/04/how-to-cache-images-react-native-expo-managed/)
- [JavaScript With Statement Explained – A Deep Dive](https://qvault.io/2020/01/15/javascript-with-statement-explained-a-deep-dive/)
- [Converting an Array to JSON Object in JavaScript](https://qvault.io/2020/12/21/converting-an-array-to-json-object-in-javascript/)
