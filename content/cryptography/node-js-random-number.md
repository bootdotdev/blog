---
title: "Secure Random Numbers in Node JS"
author: Lane Wagner
date: "2019-07-03"
categories: 
  - "cryptography"
  - "javascript"
  - "security"
images:
  - /img/6-dice-game-1024x350.webp
---

Randomness is a hard problem for computers. Most functions that generate randomness are **not** considered [cryptographically](https://qvault.io/cryptography/what-is-cryptography/) secure. What this means is that it's possible for attackers to take a good guess at what number a non-secure randomness generator generated. In the case of guessing a randomly generated private key, for example, this can be catastrophic.

## How to generate insecure random numbers

**`Math.random()`** is a built-in function in JavaScript that returns a floating-point, pseudo-random number in the range 0 to less than 1. By always generating a number between 0 and 1, you can scale the result up to whatever size you need.

### Example - Random number between 0 and 9

```
const betweenOneAndTen = Math.floor(Math.random() * 10)
```

### Example - Random number between 10 and 100

```
const min = 10
const max = 100
const betweenOneAndTen = Math.floor(Math.random() * (max - min)) + min + 1
```

## Why is Math.Random insecure?

Many non-secure randomness, or [entropy](https://qvault.io/cryptography/what-is-entropy-in-cryptography/), generators like `Math.Random()` do something similar to the following:

```
function getRandom(timestamp, maxNumber){
  // Take the deterministic hash of the timestamp
  const hashedTime = sha256(timestamp)
  // Reduce the hash to within the range [0, maxNumber)
  return hashedTime % maxNumber
}
```

This function (while ignoring some implementation details of modulus math by such a large number) will return random numbers that are based on the timestamp input, which is called the **seed**. If I pass in many different timestamps, the various outputs would **appear random**. This is an example of a weak **pseudo-random** number generator.

A weak pseudo-random number generator works perfectly fine if one is trying to:

- Create sample data for an application
- Write a video game engine
- etc ...

However, weak pseudo-randomness can be **catastrophically dangerous** if one is trying to:

- Generate Bitcoin keys
- Generate passwords or salts
- etc ...

## Use crypto.randomBytes() for cryptographically secure psuedo-randomness

Node's built-in `[crypto.randomBytes()](https://nodejs.org/api/crypto.html#crypto_crypto_randombytes_size_callback)` function is a cryptographically secure random number generator that is based on [openssl](https://wiki.openssl.org/index.php/Random_Numbers#Initialization). Depending on the operating system of the user, `randomBytes` will use `/dev/urandom` (Unix) or \`CryptoGenRandom (Windows).

While still pseudo-random sources, the important thing is that they are _not guessable_ by an attacker. In other words, after using `crypto.randomBytes()` to generate a secret key for [AES-256 encryption](https://qvault.io/cryptography/aes-256-cipher/), no one will be able to guess the key.

## Should I always use crypto.randomBytes()?

No. There are dangers if you implement your random number generator on top of a low-level API like random bytes. Because it returns bytes and not numbers, it's up to you to convert the bytes into numbers. If you make a mistake, it can result in a vulnerability in your system.

In short, **use crypto.randomBytes()** whenever you need _raw bytes_. If you need a _number_ within a range, for example, a random number between 0-9, then use a non-biased function that uses `crypto.randomBytes()` as the source of entropy. For example: [node-random-number-csprng](https://github.com/joepie91/node-random-number-csprng)
