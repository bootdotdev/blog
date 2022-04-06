---
title: "What Is Entropy In Cryptography?"
author: Lane Wagner
date: "2020-09-28"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/What-is-entropy.webp
---

If you're familiar with the [laws of thermodynamics](https://en.wikipedia.org/wiki/Laws_of_thermodynamics), you may recognize the second law as the one that deals with entropy. In the realm of physics, entropy represents the degree of disorder in a system. Because systems tend to degrade over time, thermodynamic energy becomes less available to do mechanical work. In cryptography, [entropy](https://en.wikipedia.org/wiki/Entropy_(computing)) has a distinct but similar meaning.

In [cryptography](/cryptography/what-is-cryptography/), entropy refers to the randomness collected by a system for use in algorithms that require random data. A lack of good entropy can leave a cryptosystem vulnerable and unable to encrypt data securely.

For example, the [boot.dev](https://boot.dev/) generates random coupon codes from time to time. If the coupon codes weren't generated with enough randomness, attackers could pre-compute the codes and steal all the gems!

## Computers are Deterministic

Deterministic machines are machines that do exactly what we tell them to do.

_Every._

_Single._

_Time._

> In mathematics, computer science, and physics, a **deterministic system** is a system in which no randomness is involved in the development of future states of the system. A deterministic model will thus always produce the same output from a given starting condition or initial state
> 
> [Wikipedia](https://en.wikipedia.org/wiki/Deterministic_system)

In order to coax a machine into doing something random, we have to introduce a source of seemingly random input from outside the machine. Typically operating systems are primarily responsible for supplying sources of entropy to programs.

### Linux - A Dive Into Randomness Source Code

The average Linux machine can generate secure random numbers. Because Linux is conveniently open-source, here is a link to [random.c](https://github.com/torvalds/linux/blob/master/drivers/char/random.c), a file responsible for a randomness driver. By taking a look at the comments at the top of the file, we learn:

We must try to  gather "environmental noise" from the computer's environment, which must be hard for outside attackers to observe, and use that to generate random numbers. In a Unix environment, this is best done from inside the kernel.  
  
Sources of randomness from the environment include inter-keyboard timings, inter-interrupt timings from some interrupts, and other events which are both (a) non-deterministic and (b) hard for an outside observer to measure.

When a user is clicking around or typing, those timings (along with other system timings), are used as inputs to a pool of randomness, an "entropy pool". Since these events could happen at any time, and it would be hard to predict when they will happen in advance.

![hot tub](/img/gross-jacuzzi-pool-water.jpg)

Entropy Pool, Probably

Again, from the comments:

When random bytes are desired, they are obtained by taking the SHA hash of the contents of the "entropy pool". 

To sum up, random data is added to an entropy pool constantly. This randomness is based on hard to predict events within the machine. When a user desires randomness, a [hash](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/) is taken of the entropy pool and the result is supplied to the user. When we call any secure randomness function on a Linux machine, we are likely using this driver or one very similar to it.

{{< cta1 >}}

## How Much Entropy?

A Linux machine that has sufficient entropy in its pool will usually contain 4096 bits of randomness. This is more than enough for several secure calculations to be performed. For perspective, a very strong private key typically contains 256 bits of entropy. If you want to see how much entropy your Linux machine currently has available, you can use the following command:

```
cat /proc/sys/kernel/random/entropy_avail
```
