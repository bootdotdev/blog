---
title: "Converting an Array to a JSON Object in JavaScript"
author: Lane Wagner
date: "2020-12-21"
lastmod: "2022-10-01"
categories: 
  - "javascript"
images:
  - /img/800/mechanical-beast.png.webp
---

JSON, or "JavaScript Object Notation", is a highly popular data exchange format that's widely used in web development. In this post, we'll explore several simple methods for converting a JavaScript array into JSON data. Plus, we'll discuss the benefits of using JSON and how it can help improve your web development projects.

If you're interested in learning more about JSON and HTTP, check out my ["Learn HTTP" course on Boot.dev](https://boot.dev/courses/learn-http) for an in-depth look at these powerful technologies.

## JS Array to JSON using JSON.stringify()

```js
const jsonString = JSON.stringify([1, 2, 3, 4, 5]);
```

The [JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) method converts a JavaScript object, array, or value to a JSON string. If you so choose, you can then send that JSON string to a backend server using the Fetch API or another communication library.

```js
const resp = await fetch('https://example.com', {
  method: 'POST',
  mode: 'cors',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify([1, 2, 3, 4, 5])
});
```

Because an array structure at the top level is valid JSON, if you're just worried about *validity*, then you don't even need to do any transformations. To prepare your array so that you can make a [fetch request](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) with it, it's as simple as using the `JSON.stringify()` method as we saw above.

If you want to convert back to an in-memory array, you can use [JSON.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) on the string.

```js
const arr = JSON.parse("[1, 2, 3]")
// arr is an array
// [1, 2, 3]
```

If you're looking to enhance your JavaScript skills, check out my [full JS course on Boot.dev](https://boot.dev/courses/learn-javascript)!

## Array to JSON with indexes as keys

If you don't want the direct string representation of a JSON array, you might want an object where the keys are the *indexes* of the array.

```js
["apple", "orange", "banana"]

// becomes

{
  "0": "apple",
  "1": "orange",
  "2": "banana"
}
```

To get a JSON object from an array with index keys you can use the [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) method in conjunction with `JSON.stringify`.

```js
const array = ["apple", "orange", "banana"]
const jsonString = JSON.stringify(Object.assign({}, array))
// jsonString becomes
// {"0":"apple","1":"orange","2":"banana"} 
```

## Convert each item in an array into JSON

If for some insane reason you need to stringify all the items in an array, but not the array as a whole, the [.map()](/javascript/javascript-map-function/) function is useful.

```js
const arr = [1, 2, 3]

const jsonStrings = arr.map(item => JSON.stringify(item))

const backToNumbers = jsonStrings.map((s) => JSON.parse(s))
```

## When dealing with an API, should you use objects or arrays?

If you're writing client-side code you probably won't get to decide. The API (back end) system that you're working with will probably have documentation that will specify the shape of the data it expects.

In general, I would say it's much more likely that an API will expect a top-level object for the request body, and if arrays of data are required they'll be a nested value within that top-level object.

For example, if I was writing an API that wanted a list of usernames, I'd probably accept the following JSON object:

```json
{
  "usernames": ["bill", "bob", "karen", "sue"]
}
```

Instead of a "naked" array, which is technically valid JSON:

```json
["bill", "bob", "karen", "sue"]
```

The reason that I generally prefer top-level objects is that I can add additional fields to the object in the future, without requiring large changes to the code. I also like it because it "self-documents" in a way. When you look at the first request body you can tell it's an array of usernames, in the second example, those strings could be anything.
