---
title: "Converting an Array to JSON Object in JavaScript"
author: Lane Wagner
date: "2020-12-21"
categories: 
  - "javascript"
images:
  - /img/800/javascript-on-laptop.webp
---

JSON, or "JavaScript Object Notation", is an extremely popular data exchange format, especially in web development. Let's go over a few simple ways to convert an array to JSON data.

## Quick Answer - JS Array to JSON

Arrays are actually valid JSON! If you're just worried about _validity_, then you don't even need to do any transformations. To prepare your array so that you can make a [fetch request](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) with it, it's as simple as using the `JSON.stringify()` method.

```js
const resp = await fetch('https://example.com', {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify([1, 2, 3, 4, 5])
  });
```

The `JSON.stringify()` method converts a JavaScript object, array, or value to a JSON string that can be sent over the wire using the Fetch API (or another communication library).

## Weird Answer - Array to JSON with indexes as keys

If you don't want the direct string representation of a JSON array, you might want an object where the keys are the _indexes_ of the array.

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

## When should you use arrays vs objects?

If you're writing client-side code, it's likely that you won't get to decide. The API (back end) system that you're working with will probably have documentation that will specify the shape of the data it expects.

In general, I would say it's much more likely that an API will expect a top-level object for the request body, and if arrays of data are required they'll be a nested value within that top-level object.

For example, if I was writing an API that wanted a list of usernames, I'd probably accept the following JSON object:

```js
{
  "usernames": ["bill", "bob", "karen", "sue"]
}
```

Instead of a "naked" array, which is technically valid JSON:

```js
["bill", "bob", "karen", "sue"]
```

The reason that I generally prefer top-level objects is that I can add additional fields to the object in the future, without requiring large changes to the code. I also like it because it "self-documents" in a way. When you look at the first request body you can tell it's an array of usernames, in the second example, those strings could be anything.

And if this isn't making sense to you, you might want to check out our [computer science courses](https://boot.dev/courses/).
