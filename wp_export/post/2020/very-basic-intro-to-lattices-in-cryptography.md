---
title: "(Very) Basic Intro to Lattices in Cryptography"
date: "2020-08-21"
categories: 
  - "cryptography"
  - "security"
---

Lattice-based cryptography, an important contender in the race for quantum-safe encryption, describes constructions of cryptographic primitives that involve mathematical lattices. Lattices, as they relate to crypto, have been coming into the spotlight recently. In January 2019, Many of the semifinalists in the [NIST post-quantum-cryptography competition](https://www.nist.gov/news-events/news/2019/01/nist-reveals-26-algorithms-advancing-post-quantum-crypto-semifinals) were based on lattices. Lattice-based cryptography has promising aspects that give us hope for cryptographic security in a post-quantum world.

## What is a Lattice?

According to [Wikipedia](https://en.wikipedia.org/wiki/Lattice-based_cryptography), a lattice is the set of all integer linear combinations of basis vectors:

```
b1,...,bn E R^n
```

i.e.

```
L = { ∑ ai * bi : ai E Z }
```

More simply put, a lattice is defined by basis vectors, which are only able to be scaled by integers... yay no fractions!

For example, let's create a lattice of all the integers in a two-dimensional plane:

![two dimensional lattice](images/Capture-1024x740.png)

The definition of our lattice contains only 2 basis vectors,

v1 = (0,1)

v2 = (1,0)

![lattice with two vectors](images/Capture2-1-1024x740.png)

Our lattice is the set of **all** values that can be reached by any combination and scale of our basis vectors. For example, the point (2,0) is in our lattice because it can be reached by 2\*v1

![lattice with combination of vectors](images/Capture3-1-1024x740.png)

Similarly, we could create an entirely new lattice by changing our basis vectors to

v1 = (0,3)

v2 = (3,0)

![lattice with change of basic vectors](images/Capture5-1-1024x583.png)

As you can see, now the intermediary points (0,1) and (0,1) **no longer exist** in our lattice. There is no way to scale v1 (0,3) and v2 (3,0) to reach those points without using fractional scalars. With lattices, we can only scale by whole integers.

## How Does This Help With Crypto?

[Cryptographic algorithms](https://qvault.io/cryptography/what-is-cryptography/) are typically based on mathematical problems that are easy to verify the answer of, but hard to calculate.

For example, RSA is based on prime factorization. If I told you to find prime factors of _27,919,645,564,169,759_, that would be hard. However, if I told you that 48,554,491 and 575,016,749 _are_ prime factors, all you have to do is multiply them together in order to verify my answer.

RSA works great with classical computers. There are [no known solutions to find prime factors](https://crypto.stackexchange.com/questions/10590/what-makes-rsa-secure-by-using-prime-numbers) of a number reliably in less than exponential time.

In the quantum world, things don't look so peachy. [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm) on quantum computers can crack RSA in less than exponential time. For this reason, we need quantum-safe algorithms. Many believe that lattice math could be an answer.

## Shortest Vector Problem

![shortest vector problem](images/220px-SVP.svg_.png)

[The shortest vector problem (SVP)](https://en.wikipedia.org/wiki/Lattice_problem#Shortest_vector_problem_(SVP)) is one of the fundamentals problems presented by lattices that allow them to be useful in cryptography.

Simply put, the goal of SVP is for the attacker to find the shortest vector from the origin (above in red) when given the basis of a lattice (above in blue). A zero vector doesn't work as an answer, we consider it trivial.

How is it solved?

Like RSA with classical computers, it is hard to find the shortest vector of a large lattice, especially if it exists in many dimensions. One such slow solution for approximating the shortest vector is [Babai](https://en.wikipedia.org/wiki/L%C3%A1szl%C3%B3_Babai)'s algorithm, or [Nearest Plane Algorithm](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/cvp.pdf), which you can read about in the links provided.

## Related Articles

- [(Very) Basic Intro to Hash Functions (SHA-256, MD-5, etc)](https://qvault.io/2020/01/01/very-basic-intro-to-hash-functions-sha-256-md-5-etc/)
- [(Very) Basic Intro To Elliptic Curve Cryptography](https://qvault.io/2019/12/31/very-basic-intro-to-elliptic-curve-cryptography/)
- [(Very) Basic Intro to Key Derivation Functions (Argon2, Scrypt, etc)](https://qvault.io/2019/12/30/very-basic-intro-to-key-derivation-functions-argon2-scrypt-etc/)
