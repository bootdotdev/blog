---
title: "Basic Intro to Key Derivation Functions"
author: lane
date: "2019-12-30"
categories:
  - "cryptography"
  - "security"
images:
  - /img/800/photo-1553386323-60698d6f7325.webp
---

A Key Derivation Function, or KDF, is a [cryptographic algorithm](/cryptography/what-is-cryptography/) that derives one or more secret keys from a secret value. If you've ever needed to store a password in a database or create a private key from a password, you may have used a KDF. Some examples of popular KDFs are [Argon2](https://en.wikipedia.org/wiki/Argon2), [Scrypt](/cryptography/very-basic-intro-to-the-scrypt-hash/), and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2).

## Are KDFs Just Hash Functions?

No, but there is overlap. To understand KDFs, let's first go through a quick refresher on [hash functions.](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/)

Some hash functions for example:

- [SHA-256](/cryptography/how-sha-2-works-step-by-step-sha-256/)
- MD5

A hash function takes an input and creates an output. In most password hashing scenarios it looks something like this:

```
sha256("password123") -> ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

The function must have the following properties:

- It scrambles data deterministically (Same input, same output)
- No matter the input, the output of a hash function always has the same size
- It cannot retrieve the input from the output (one-way function)

## So What's the Difference?

There are different types of KDFs. Some are based on stream or block ciphers, but in this article, we will focus on the most common type, hash-based key derivation functions.

As it turns out, all hash-based KDFs are secure hash functions, but not all hash functions are hashed-based KDFs.

![kdf vs hash ](/img/800/Capture-1.png)

In addition to the properties of a hash function, KDFs can serve the following purposes:

- Key Stretching
- Key Whitening
- Key Separation
- Key Strengthening

Let's look at each case separately, with the following definition of our general KDF in mind:

```
derivedKey = keyDerivationFunction(originalKey, salt, difficulty)
```

**Salt** is random data used to protect against pre-computation attacks or rainbow tables.

**Difficulty** can be used to make the KDF slower via intense computation, memory, or parallelism requirements. This protects against brute force attacks because it will take an attacker longer per guess.

## Key Stretching

Key stretching is the most common use case for the average developer. The idea is to take a key with low entropy (security or randomness) and stretch it into a longer key that is more secure. Passwords are undoubtedly a great example. For example, many websites use Bcrypt to stretch keys:

```
passwordForDB = bcrypt(password, salt, difficulty)
```

## Key Separation

KDFs allow child keys to be created from a master key. This can be used in applications like Bitcoin where child keys can control sections of a wallet. However, only the master has full control. This is done through the use of different salts. For example:

```
childOne = kdf(masterKey, saltOne, difficulty)
childTwo = kdf(masterKey, saltTwo, difficulty)
childThree = kdf(masterKey, saltThree, difficulty)
```

## Key Strengthening

Strengthing extends a key with a random salt, but then [deletes the salt](https://en.wikipedia.org/wiki/Key_derivation_function) so it can't be used again. This makes the resulting key stronger without adding significant vulnerabilities to the system.

## Should I Use KDFs?

Yes. Most often when storing passwords in databases, but also if any of these other use cases fall into the domain of your code. Tweet me if you have comments or questions. To read more check out the [HKDF paper](https://eprint.iacr.org/2010/264).
