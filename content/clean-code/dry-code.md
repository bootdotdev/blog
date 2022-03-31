---
title: "The Pros and Cons of DRY Code"
author: Lane Wagner
date: "2021-01-25"
categories: 
  - "clean-code"
images:
  - /img/desert.jpeg
---

Clean code is like clean garbage - it's only clean if it doesn't exist. In other words, the only clean code is [no code](https://github.com/kelseyhightower/nocode). Let's start with an acknowledgment that a perfectly clean (empty) codebase is useless, that is, without code, we can't provide value to our users. With that in mind, our pursuit of "clean code" will necessarily consist of tradeoffs. We'll trade usefulness for cleanliness, complexity for speed, ownership for ease of development, and abstractions for reusability.

DRY (don't repeat yourself) code is often held aloft as an ideal in the quest for clean code. Let's explore why I think DRY can be a good [heuristic](https://qvault.io/2020/11/30/examples-of-heuristics-in-computer-science/), but far from an absolute.

## What is DRY Code?

According to [Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself):

> **Don't repeat yourself** is a principle aimed at reducing repetition of software patterns, replacing it with abstractions or using data normalization to avoid redundancy. Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

While this definition is fairly exhaustive, what I've found people _usually_ mean when they say "DRY code" is that when you find yourself repeating pieces of logic you should instead create a reusable function, interface, class, etc, so that you only have to maintain one copy of it. For example, take the following API calls:

```javascript
export async function updateUserHandle(handle) {
  if (!isLoggedIn()){
    // redirect to login screen
    return;
  }
  let token = localStorage.getItem(jwtKey);
  let decodedToken = decodeJWT(token);
  const hoursDelta = 24;
  if (decodedToken.exp < (Date.now() + hoursDelta*60*60) / 1000){
    refreshToken();
  }
  return await fetch(`${domain}/v1/users/handle`, {
    method: 'PUT',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
      handle
    })
  });
}

export async function updateUserInterests(interestUUIDs) {
  if (!isLoggedIn()){
    // redirect to login screen
    return;
  }
  let token = localStorage.getItem(jwtKey);
  let decodedToken = decodeJWT(token);
  const hoursDelta = 24;
  if (decodedToken.exp < (Date.now() + hoursDelta*60*60) / 1000){
    refreshToken();
  }
  return await fetch(`${domain}/v1/users/interests`, {
    method: 'PUT',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
      interestUUIDs
    })
  });
}
```

You may have noticed, but the beginning of those two API calls are nearly identical - they handle some basic logic that checks to see if the user is properly authenticated and sends that authentication in the request. This might not be a big deal with just two API calls, but what if we have 30? Or maybe 1000? Instead, we can DRY up this code by writing a simple `fetchWithAuth` function that will centralize all the client's authentication logic in a single place:

```js
async function fetchWithAuth(url, params){
  if (!isLoggedIn()){
    // redirect to login screen
    return;
  }
  let token = localStorage.getItem(jwtKey);
  let decodedToken = decodeJWT(token);
  const hoursDelta = 24;
  if (decodedToken.exp < (Date.now() + hoursDelta*60*60) / 1000){
    refreshToken();
  }
  if (!params.headers){
    params.headers = {};
  }
  params.headers.Authorization = `Bearer ${token}`;
  return await fetch(url, params);
}

export async function updateUserHandle(handle) {
  return await fetchWithAuth(`${domain}/v1/users/handle`, {
    method: 'PUT',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      handle
    })
  });
}

export async function updateUserInterests(interestUUIDs) {
  return await fetchWithAuth(`${domain}/v1/users/interests`, {
    method: 'PUT',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      interestUUIDs
    })
  });
}
```

## Why wouldn't you DRY out your code?

Seems like a good idea to reduce code duplication right? Well, yes, in general it is. That said, let's look at some of the drawbacks that come along with too much centralization.

### 1\. Too many abstractions

Sometimes code is the same at a given point in time, but later on, it becomes distinct in some way. It's really hard to guarantee that duplicate blocks of code will remain perfect copies of each other forever. A hypothetical example of this would be if the Facebook and Instagram APIs had the exact same way to create a social post. Just because they're _coincidentally_ the same, probably doesn't mean that the logic should only be written once.

The solution is likely to remain disciplined about splitting out code that, while it may be similar now, is only _coincidentally_ similar. We should try to only merge code that's _fundamentally_ the same. A great example would be a math function like `log2`. That function should work for every case where you need to calculate a logarithm - each call is _fundamentally_ the same.

### 2\. External dependency creation

If two different projects share the same logic, it can often make sense to centralize it in a library package. While this is often a great idea, it can add overhead and can end up being more trouble than it's worth. For example, even if the abstraction makes sense, you're definitely adding at least the following complexity to the project:

- Management of the dependencies versions and running updates regularly
- Requires multi-project updates in order to get a new change to a specific dependent
- Often involves more remote infrastructure like NPM or PyPy
- Gets harder to make "breaking" changes to the libraries core functions - requires a higher standard of code quality and architecture

### 3\. Localization complexity

When debugging or reading code, it would be easiest if the flow of logic started at the top of a file and flowed in a linear path. For example:

```
START PROGRAM
INSTRUCTION 0
INSTRUCTION 1
INSTRUCTION 2
INSTRUCTION 3
END PROGRAM
```

Unfortunately, in useful programs, we need functions, classes, methods, type definitions, etc. that force us to read and write code in a non-linear way. The goal should be to keep everything as linear as possible and sacrifice linearity and simplicity for reusability and separation of concerns only as necessary. Every time we extract a chunk of code from a larger function into a smaller more encapsulated one, the code becomes just a little bit harder to follow.

With a highly compartmentalized project, when we see a function called `getUser`, if we want to _really_ know what's going on we have to peek into that function and remember our external context because we're now looking at an entirely different file. The cognitive burden becomes greater and greater the more definitions we need to jump through to grok a single logical pathway.

## Takeaways - Code smells and heuristics

Since no code is perfect, we need to make use of some heuristics (rules of thumb), to try to work towards a cleaner codebase.

### 1\. WET code, or the rule of three

WET is a better rule of thumb in my opinion than DRY.

WET stands for "write everything twice", and forces you to think a bit harder about whether or not a piece of logic _deserves_ an abstraction. The rule of three is an alternative that says you should wait until you've written something three times before breaking it out.

### 2\. Is it testable?

Most functions should be predictable and testable. They should behave like math functions or [pure functions](https://qvault.io/golang/pure-functions-in-golang/) - given a set of inputs you'll always receive the same outputs, and the state of the program isn't mutated. If the code you're thinking about condensing into a function can be a pure function, then it's likely a better idea than if it were an impure function.

Pure functions are easy to write good unit tests for - if your abstraction is easily testable it's more likely to be a good abstraction.

### 3\. Are there special cases or arguments only used by a fraction of callers?

Take a look at the following example:

```js
function getArea(height, width){
  return height * width
}
```

This is a great function! It's very simple, and obviously can be used to calculate the area of any shape. Here's a bad example:

```js
function getArea(height, width, isTriangle){
  if (isTriangle){
    return (height * width) / 2
  }
  return height * width
}
```

Special cases are bad news - I'm trying to be too abstract. Instead, I should just create two separate functions:

```js
function getTriangleArea(height, width){
  return (height * width) / 2
}

function getRectangleArea(height, width){
  return height * width
}
```

Have any more ideas for good rules of thumb? Let me know on [Twitter](https://twitter.com/wagslane)! I'd love to update and improve this article.
