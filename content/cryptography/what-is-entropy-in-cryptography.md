---
title: "What Is Entropy In Cryptography?"
author: Lane Wagner
date: "2020-09-28"
lastmod: "2022-07-19"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/What-is-entropy.webp
---

If you're familiar with the [laws of thermodynamics](https://en.wikipedia.org/wiki/Laws_of_thermodynamics), you may recognize the second law as the one that deals with entropy. In the realm of physics, entropy represents the degree of disorder in a system. Because systems tend to degrade over time, thermodynamic energy becomes less available to do mechanical work.

However, in [cryptography](/cryptography/what-is-cryptography/), [entropy](https://en.wikipedia.org/wiki/Entropy_(computing)) has a slightly different meaning. It refers to the randomness collected by a system for use in algorithms that require random seeds. A lack of good entropy can leave a crypto system vulnerable and unable to encrypt data securely.

For example, the [Boot.dev](https://www.boot.dev/) checkout system needs to generate random coupon codes from time to time. If the coupon codes weren't generated with enough randomness, attackers could pre-compute the codes and steal access to the courses!

## Computers are deterministic

Deterministic machines are machines that do exactly what we tell them to do.

Every.

Single.

Time.

> In mathematics, computer science, and physics, a **deterministic system** is a system in which no randomness is involved in the development of future states of the system. A deterministic model will thus always produce the same output from a given starting condition or initial state
> 
> [Wikipedia](https://en.wikipedia.org/wiki/Deterministic_system)

To coax a machine into doing something random, we actually have to introduce a source of seemingly random input from outside the machine. Typically operating systems are primarily responsible for supplying sources of entropy to programs.

{{< youtube abI_sTj4mrY >}}

### An example - How does the Linux kernel produce randomness for applications?

A typical Linux machine can generate secure random numbers. Because Linux is conveniently open-source, I can provide you a link to [random.c](https://github.com/torvalds/linux/blob/a24d22b225ce158651378869a6b88105c4bdb887/drivers/char/random.c), a file responsible for randomness in the Linux kernel. By taking a look at the comments at the top of the file, we learn:

> We must try to  gather "environmental noise" from the computer's environment, which must be hard for outside attackers to observe, and use that to generate random numbers. In a Unix environment, this is best done from inside the kernel.
> 
> Sources of randomness from the environment include inter-keyboard timings, inter-interrupt timings from some interrupts, and other events which are both (a) non-deterministic and (b) hard for an outside observer to measure.
> 
> When a user is clicking around or typing, those timings (along with other system timings), are used as inputs to a pool of randomness, an "entropy pool". Since these events could happen at any time, and it would be hard to predict when they will happen in advance.

![hot tub](/img/800/gross-jacuzzi-pool-water.jpg)

^ The entropy pool, probably ^

Again, from the comments:

> When random bytes are desired, they are obtained by taking the SHA hash of the contents of the "entropy pool". 

To sum up, random data is added to an entropy pool **constantly**. This randomness is based on "hard to predict" events within the machine. When a user desires randomness, a [hash](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/) is taken of the entropy pool and the result is supplied to the user. When we call any secure randomness function on a Linux machine, we are likely using this driver or one very similar to it.

## How much entropy is needed for a computer?

A Linux machine that has sufficient entropy in its pool will usually contain `4096` bits of randomness. This is more than enough for several secure calculations to be performed. For perspective, a very strong private key typically contains `256` bits of entropy. If you want to see how much entropy your Linux machine currently has available, you can use the following command:

```
cat /proc/sys/kernel/random/entropy_avail
```
