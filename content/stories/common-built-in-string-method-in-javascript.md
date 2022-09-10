---
title: "Common Built-in String Methods in Javascript"
author: Femi Akinyemi
date: "2022-09-10"
images:
  - /img/800/common_built_in_head_image.png
dofollows:
  - "https://twitter.com/akinyemi_t"
categories:
  - "writing"
---


<!-- ## Introduction -->

### String

According to [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String),

> The **String** object is used to represent and manipulate a sequence of characters.

It would be impossible to write code without using a [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String). Strings are a part of every programmer's life.

For manipulating strings, JavaScript provides various functions and methods.

With these methods, developers can modify string values, determine character indexes, and change string cases. And so on.

This article will show some commonly used methods for manipulating strings in JavaScript:

## includes()

<code>includes()</code> method lets us determine whether or not a string includes another string.

### Syntax

```javascript
str.includes(searchString, position);
```

### Parameters

<code>searchString</code>
String to search within <code>str</code>. Regex cannot be used.

<code>position</code>
In the string, the location at which to begin searching for searchString. The default value is 0.

## Example

```javascript
const sentence = "The dog is mine";

const word = "dog";

console.log(
  `The word "${word}" ${
    sentence.includes(word) ? "is" : "is not"
  } in the sentence`
);
// expected output: "The word "dog" is in the sentence"
```

## charAt()

The <code>charAt()</code> method returns a character in a string at a specific index (position).
The first character has an index of 0 the second has an index of 1

### Syntax

```javascript
str.charAt(index);
```

## Example

```javascript
const sentence = "The house is mine";

const index = 4;

console.log(`The character at index ${index} is ${sentence.charAt(index)}`);
// expected output: "The character at index 4 is h"
```

## concat()

The <code>concat()</code> method combines strings (str1, str2, /_ …, _/ strN) into one. Upon concatenating the string arguments, it returns a new string.

### Syntax

```javascript
str.concat(str2);
str.concat(str2, str3);
str.concat(str2, str3, ... , strN);

```

## Example

```javascript
const str1 = "Text";
const str2 = "Book";

console.log(str1.concat(" ", str2));
// expected output: "Text Book"

console.log(str2.concat(", ", str1));
// expected output: "Text, Book"
```

## endsWith()

The <code>endsWith()</code> method returns true if a string ends with a specified string. Otherwise, it returns false.

### Syntax

```javascript
str.endsWith(searchvalue, length);
```

## Example

```javascript
const str1 = "Dogs are the best!";

console.log(str1.endsWith("best!"));
// expected output: true

console.log(str1.endsWith("best", 17));
// expected output: true

const str2 = "Are you ok?";

console.log(str2.endsWith("ok"));
// expected output: false
```

## indexOf()

The <code>indexOf()</code> method returns the position of the first occurrence of a value in a string.

If the value cannot be found, <code>indexOf()</code> returns -1.

It is important to note that <code>indexOf()</code> is case sensitive.

### Syntax

```javascript
str.indexOf(searchvalue, position);
```

### Parameters

<code>searchString</code>
Substring to search for.

<code>position</code>
In cases where <code>position</code> exceeds the length of the calling string, the method skips the calling string altogether. Methods treat <code>position</code> less than zero as if it were 0.

## Example

```javascript
const myString = "Hello World";
const myCapString = "Hello Nigeria";

console.log(`myString.indexOf("World") is ${myString.indexOf("World")}`);
// logs 6
console.log(`myCapString.indexOf("World") is ${myCapString.indexOf("World")}`);
// logs -1
```

## lastIndexOf()

In a string, <code>lastIndexOf()</code> returns the last occurrence (<code>position</code>) of a value.
A string is searched from the end to the beginning using the <code>lastIndexOf()</code> method.
<code>lastIndexOf()</code> method returns the index from the beginning (<code>position o</code>).

### Syntax

```javascript
str.indexOf(searchvalue, position);
```

### Parameters

<code>searchString</code>
Substring to search for.

<code>position</code>

As a default, <code>position</code> is defaulted to <code>+Infinity</code>, which is the index of the last instance of the specified substring.

## Example

```javascript
const paragraph = "In the end, we all felt like we ate too much.";

const searchTerm = "ate";

console.log(
  `The index of the first "${searchTerm}" from the end is ${paragraph.lastIndexOf(
    searchTerm
  )}`
);
// expected output: "The index of the first "ate" from the end is 32"
```

## repeat()


The <code>repeat()</code> method returns a new string containing the number of concatenated copies of the string that was passed in.

### Syntax

```javascript
str.repeat(count);
```

## Example

```javascript
const chorus = "until the night is over. ";

console.log(
  `Chorus lyrics for "I wanna be in your life until the night is over": ${chorus.repeat(
    7
  )}`
);

//Chorus lyrics for "I wanna be in your life until the night is over": until the night is over. until the night is over. until the night is over. until the night is over. until the night is over. until the night is over. until the night is over.
```

## replace()

<code>replace()</code> method searches for values in a string or regular expressions in a string.

The <code>replace()</code> method returns a newly created string with the replaced value(s).

<code>replace()</code> does not alter the original string.

### Syntax

```javascript
str.replace(pattern, replacement);
```

### Parameters

<code>pattern</code>
A regular expression is a typical example of a string or an object with the <code>Symbol.replace</code> method. Values without the <code>Symbol.replace</code> method will be converted to strings.

<code>replacement</code>

This can be a string or a function.

## Example

```javascript
const p = "The envelope is bad";

console.log(p.replace("is", "was"));
// The envelope was bad

const regex = /The/i;
console.log(p.replace(regex, "My"));
// My envelope is bad
```

## search()

The <code>search()</code> method searches for a word in the string and returns its index. If no match is found, it returns -1.

It is important to note that <code>search()</code> is case sensitive.

### Syntax

```javascript
str.search(searchValue);
```

## Example

```javascript
let text = "Mr. Ben has a blue car";
let position = text.search("Ben");

console.log(position);

// logs 4
```

## slice()

The <code>slice()</code> method returns a new string containing a section of a string without altering the original string.

### Syntax

```javascript
str.slice(indexStart);
str.slice(indexStart, indexEnd);
```

### Parameters

<code>indexStart</code>
This is the index of the first character to include in the returned substring.

<code>indexEnd</code>
This is the index of the first character to exclude in the returned substring.

## Example

```javascript
let str = "Welcome to Nigeria";

console.log(str.slice(11));
// expected result: "Nigeria"

console.log(str.slice(8, 11));

// expected result: "to"
```

## split()

The <code>split()</code> method creates an ordered list of substrings from a string. A string will be split into many parts
according to the seperator specified, and each element is returned as an array.

### Syntax

```javascript
str.split();
str.split(separator);
str.split(separator, limit);
```

### Parameters

<code>separator Optional </code>
This pattern describes where each split should occur.

<code>limit Optional</code>
A non-negative integer specifying the maximum number of substrings to include in the array.

## Example

```javascript
let str = "Nigeria is an African country";

let words = str.split(" ");
console.log(words);

// expected result : [ 'Nigeria', 'is', 'an', 'African', 'country' ]

let chars = str.split("");
console.log(chars[0]);

// expected result "N"

let strCopy = str.split();
console.log(strCopy);
//expected result : [ 'Nigeria is an African country' ]
```

## startsWith()

The <code>startsWith()</code> method determines whether a string begins with the characters of a specified string, returning true or false.

### Syntax

```javascript
str.startsWith(searchString);
str.startsWith(searchString, position);
```

### Parameters

<code>searchString</code>
The characters to be searched for at the beginning of this string. It cannot be a regex.

<code>position Optional</code>

A position at which <code>searchString</code> should be found (the index of <code>searchString</code>'s first character). The default value is 0.

## Example

```javascript
const str1 = "Yesterday was my birthday";

console.log(str1.startsWith("Y"));
// expected output: true

console.log(str1.startsWith("Yes", 3));
// expected output: false
```

## substring()

The <code>substring()</code> method returns the part of the string between the start and end indexes or to the end.

### Syntax

```javascript
str.slice(indexStart);
str.slice(indexStart, indexEnd);
```

### Parameters

<code>indexStart</code>

This index represents the first character in the returned substring.

<code>indexEnd</code>
This is the index of the first character to exclude in the returned substring.

## Example

```javascript
const str = "Breakfast";

console.log(str.substring(1, 3));
// expected output: "re"

console.log(str.substring(5));
// expected output: "fast"
```

## toLocaleLowerCase()

It converts a string to lowercase letters according to the current locale.

Browser language settings determine the locale.

<code>toLocaleLowerCase()</code> does not change the original string

Except for locales (such as Turkish) that conflict with regular Unicode case mappings, <code>toLocaleLowerCase()</code> returns the same result as <code>toLowerCase()</code>

### Syntax

```javascript
str.toLocaleLowerCase();
str.toLocaleLowerCase(locales);
```

### Parameters

<code>locales optional </code>
An array of strings containing BCP 47 language tags.

## Example

```javascript
let text = "Hello Nigeria!";
let result = text.toLocaleLowerCase();
console.log(result); // Expected: hello nigeria!
```

## toLocaleUpperCase()

It converts a string to uppercase letters according to the current locale.

Browser language settings determine the locale.

<code>toLocaleUpperCase()</code> does not change the original string

Except for locales (such as Turkish) that conflict with regular Unicode case mappings, <code>toLocaleUpperCase()</code> returns the same result as <code>toUpperCase()</code>

### Parameters

<code>locales optional </code>
An array of strings containing BCP 47 language tags.

## Example

```javascript
let text = "Hello Nigeria!";
let result = text.toLocaleUpperCase();
console.log(result); // Expected: HELLO NIGERIA!
```

## toString()

<code>toString </code> method returns a string as a string.
<code>toString </code> method does not change the original string.
The <code>toString </code> method converts a string object to a string.

### Syntax

```javascript
str.toString();
```

## Example

```javascript
let text = "Hello Nigeria!";
let result = text.toString();

console.log(result); // Hello Nigeria
```

## trim()

The <code>trim()</code> method removes the whitespace from both ends of a string and returns a new one.

### Syntax

```javascript
str.trim();
```

## Example

```javascript
const greeting = "   Hello Nigeria!   ";

console.log(greeting);
// expected output: "   Hello Nigeria!   ";

console.log(greeting.trim());
// expected output: "Hello Nigeria!";
```

## valueOf()

The <code>valueOf()</code> method returns a primitive value for a String.

### Syntax

```javascript
str.valueOf();
```

## Example

```javascript
let text = "Hello Nigeria!";
let result = text.valueOf();

console.log(result); // Hello Nigeria!
```

This concludes the list of commonly used methods in JavaScript. I hope you can use some of these for your projects.

Please, let me know what you think in the comment section.

Thanks for Reading 🌟🎉

I'd love to connect with you on <a href="https://twitter.com/akinyemi_t">Twitter</a>

On to another blog, some other day, till then Femi👋.

## Useful Resources

- [String mdn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)

- [JavaScript String Reference](https://www.w3schools.com/jsref/jsref_obj_string.asp)

- [How to Manipulate Strings in JavaScript Like a Professional Developer](https://medium.com/geekculture/how-to-manipulate-strings-in-javascript-like-a-professional-developer-6bec15b08cba)
