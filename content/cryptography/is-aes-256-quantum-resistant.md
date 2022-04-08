---
title: "Is AES-256 Quantum Resistant?"
author: Lane Wagner
date: "2020-09-10"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/Copy-of-Pure-Functions-in-Go.webp
---

With quantum computers getting more powerful each year, many worry about the safety of modern encryption standards. As quantum computers improve in performance and the number of [qubits](https://en.wikipedia.org/wiki/Qubit) used for calculations increases, current cryptosystems are under threat. [AES-256](/cryptography/aes-256-cipher/) is one of the most powerful symmetric ciphers, but will it remain secure in a post-quantum world?

## What will break post-quantum?

Many asymmetric encryption algorithms have been mathematically proven to be broken by quantum computers using [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm). Shor's algorithm solves the following problem:

> Given an integer **N**, find its prime factors.

![number flow](/img/800/1_2wIjQH7NdYAmMI9nQa8BJw.png)

Because algorithms like RSA rely heavily on the fact that normal computers can't find prime factors quickly, they have remained secure for years. With quantum computers breaking that assumption, then it may be time to find new standards.

The following are examples of encryption that Shor's algorithm can break:

- [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Diffie Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [ECC](/cryptography/elliptic-curve-cryptography/)

{{< cta1 >}}

## Symmetric Encryption

Symmetric encryption, or more specifically AES-256, is believed to be quantum-resistant. That means that [quantum computers are not expected](https://en.wikipedia.org/wiki/Post-quantum_cryptography#Symmetric_key_quantum_resistance) to be able to reduce the attack time enough to be effective if the key sizes are large enough.

![symmetric kittens](/img/800/mddjVaf-1024x977.jpg)

[Symmetric Cats](https://i.imgur.com/mddjVaf.jpg)

[Grover's algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm) can reduce the brute force attack time to its square root. So for AES-128 the attack time becomes reduced to 2^64 (not very secure), while AES-256 becomes reduced to 2^128 which is still considered very secure.

## A Caveat

It is important to remember that [256-bit keys derived](/cryptography/key-derivation-functions/) from passwords actually can have less than 256-bits of entropy. If the owner of the key generated it from a weak password an attacker can try deriving keys from common passwords instead of trying random 256-bit numbers.

For example, instead of randomly trying

1. azpV4CYbAwQUP4BaJJJNDBxEUkghMF8x2Sd4Q7ihD04=
2. mtOXPNln432smP3pd3rVLw9rpGGkVsiqRhUFLXy/KBw=
3. ..

An attacker could try the following:

1. password123 --> 75K3eLr+dx6JJFuJ7LwIpEpOFmwGZZkRiB84PURz6U8=
2. password1234 --> uclQZA4bN0DpisuT5mnGV2b2Zw3RYJupH/QQUrpIxvM=
3. ...

If you are implementing AES in a cryptosystem in 2020 you should favor AES-256 over AES-128 for the quantum resistance and extra security that it offers.
