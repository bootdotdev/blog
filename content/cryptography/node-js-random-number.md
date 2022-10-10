---
title: "Secure Random Numbers in Node.js"
author: Lane Wagner
date: "2019-07-03"
lastmod: 2022-10-01"
categories: 
  - "cryptography"
  - "javascript"
  - "security"
images:
  - /img/800/6-dice-game-1024x350.webp
---

**Quick answer: use [crypto.randomBytes()](https://nodejs.org/api/crypto.html#crypto_crypto_randombytes_size_callback) for cryptographically secure randomness in Node.js.**

```js
const { randomBytes } = await import('node:crypto');

const buf = randomBytes(256);
console.log(`${buf.length} bytes of random data: ${buf.toString('hex')}`);
```

[crypto.randomBytes()](https://nodejs.org/api/crypto.html#crypto_crypto_randombytes_size_callback) is a *cryptographically secure* random number generator based on [openssl](https://wiki.openssl.org/index.php/Random_Numbers#Initialization). Depending on the operating system of the user, `randomBytes` will use `/dev/urandom` (Unix) or `CryptoGenRandom` (Windows).

While still pseudo-random sources, the important thing is that they are _not guessable_ by an attacker. In other words, after using `crypto.randomBytes()` to generate a secret key for [AES-256 encryption](/cryptography/aes-256-cipher/), no one will be able to guess the key.

## Randomness is a hard problem in Node.js

Randomness is a [hard problem for computers](/cryptography/what-is-entropy-in-cryptography/#computers-are-deterministic). Most functions that generate randomness in Node.js are *not* considered [cryptographically](/cryptography/what-is-cryptography/) secure. As a result, it's possible for attackers to take a good guess at which number will be generated. In the case of guessing a private key, insecure randomness can be actually be *catastrophic*.

## How to generate insecure random numbers

[Math.random()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) a JavaScript built-in function that returns a pseudo-random number between `0` and `1`. At first this sounds fairly pointless, but by always generating a number between `0` and `1`, the user of the function can scale that random result up to whatever size they need.

### Insecure example

Generate an insecure random number between `0` and `10` in Node.js:

```js
const betweenOneAndTen = Math.floor(Math.random() * 10)
```

### Insecure example #2

Generate an insecure random number between `10` and `100` in Node.js:

```js
const min = 10
const max = 100
const betweenOneAndTen = Math.floor(Math.random() * (max - min)) + min + 1
```

## Why is Math.Random() insecure?

Many non-secure sources of [entropy](/cryptography/what-is-entropy-in-cryptography/), like `Math.Random()`, do something similar to the following:

```js
function getRandom(timestamp, maxNumber){
  // Take the deterministic hash of the timestamp
  const hashedTime = sha256(timestamp)
  // Reduce the hash to within the range [0, maxNumber)
  return hashedTime % maxNumber
}
```

This function (while ignoring some implementation details of modulus math by such a large number) will return random numbers that are based on a timestamp input, which is called the *seed*. If I pass in different timestamps, the corresponding outputs would *appear* random. This is an example of a weak **pseudo-random** number generator.

A weak pseudo-random number generator works perfectly fine if you're trying to:

* Create sample data for an application
* Write a video game engine
* etc ...

However, weak pseudo-randomness can be *catastrophically dangerous* if you're trying to:

* Generate Bitcoin keys
* Generate passwords or salts
* etc ...

{{< cta1 >}}

## Should I always use crypto.randomBytes()?

No. There are dangers if you implement your random number generator on top of a low-level API like random bytes. Because it returns bytes and not numbers, it's up to you to convert the bytes into numbers. If you make a mistake, it can result in a vulnerability in your system.

In short, **use crypto.randomBytes()** whenever you need *raw bytes*. If you need a number within a range, for example, a random number between `0` and `9`, then use a non-biased function that uses `crypto.randomBytes()` as the *source* of entropy. For example: [node-random-number-csprng](https://github.com/joepie91/node-random-number-csprng)
