---
title: "(Very) Basic Intro To White-Box Cryptography"
author: Lane Wagner
date: "2020-04-27"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/White_Box_Crypto.webp
---

White-box cryptography combines methods of encryption and obfuscation to embed secret keys within application code. The goal is to combine code and keys in such a way that the two are indistinguishable to an attacker, and the new "white-box" program can be safely run in an insecure environment.

## What Does "White-Box" Mean?

In penetration testing, white-box testing is where the testers (or attackers) have access to the source code and internal workings of the system.

White-box cryptography is appropriately named because attackers have access to the compiled code where the keys exist. The difficult problem that it aims to solve is how to keep those keys safe while using them in execution.

## Kerckhoffs's Principle

[Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) revolutionized the way we think about [cryptography](/cryptography/what-is-cryptography/). It states that we should allow the attacker to know everything about a crypto implementation, except the key. If a cryptosystem can stand up to that level of scrutiny it will be the better for it.

White-box crypto takes this a bit further. That is, we technically give the attacker access to the key, we just hide/encrypt it well enough that they can't find it.

## How Does It Work?

To secure a program using white-box cryptography, we assume the attacker has complete access to the system. This includes:

- Access to executable binary
- Access to execution memory
- CPU call intercepts

To successfully hide the keys given this scenario, according to [Brecht Wyseur](https://www.esat.kuleuven.be/cosic/publications/thesis-152.pdf), we can take the following steps assuming we are trying to white-box a block cipher:

1. **Partial Evaluation**: When performing an operation, we alter the operation based on the key. For example, in the [substitution phase of a block cipher](/cryptography/aes-256-cipher/), we would change the [lookup table](https://en.wikipedia.org/wiki/S-box) to be dependent on the key. Note that if someone were to see this table, they could derive the key (solved in step 3)
2. **Tabularizing**: Transform all other operations to also use lookup tables. This is possible because lookup tables can describe any function.
3. **Randomization and Delinearization**: We create an encoded chain of lookup tables that has the same functionality as the original chain, but hides the key. Now, using this new chain, we have an obfuscated algorithm. For reading on the details of this operation, see [here](https://www.esat.kuleuven.be/cosic/publications/thesis-152.pdf#page=74).

## Is White-Box Secure In Practice?

Well, it depends. Security through obscurity is a well-known bad-practice in the cryptography industry, but there is an argument to be made that white-box crypto is more than just obfuscation. A recent [2018 paper](https://eprint.iacr.org/2018/098.pdf) on cracking white-box may be insightful.

White box practices have certainly been used, but not many time-tested open-source solutions currently exist. That said, you may be interested in one of the larger (still small) repositories on GitHub which white-boxes AES in C++: [https://github.com/ph4r05/Whitebox-crypto-AES](https://github.com/ph4r05/Whitebox-crypto-AES)

Intertrust recently claimed to launch the first [enterprise-ready solution](https://www.businesswire.com/news/home/20200224005912/en/Intertrust-Launches-Enterprise-Ready-White-Box-Cryptography-Solution-Web). Reading more on that may give some insight.

Hopefully this gives you a basic understanding of the purpose of white-box crypto, and even a spoiler of how it works from a 1,000 foot level.

Brecht Wyseur's [Thesis on White-Box Crypto](https://www.esat.kuleuven.be/cosic/publications/thesis-152.pdf)
