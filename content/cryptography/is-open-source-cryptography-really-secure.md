---
title: "Is Open-Source Cryptography Really Secure?"
author: Lane Wagner
date: "2020-01-30"
categories: 
  - "cryptography"
  - "open-source"
  - "security"
images:
  - /img/photo-1497285597995-6ed7de6bfebd.webp
---

The purpose of [cryptography](https://qvault.io/cryptography/what-is-cryptography/) is to keep information private, and the purpose of open-source is to make code public... So we shouldn't open-source our cryptography algorithms right?

I've been asked this several times by multiple people so I figured it is a subject worth addressing. Many developers seem to be under the impression that crypto and security systems (the application-specific implementation of cryptosystems) are more secure if their details are kept private.

**This can't be further from the truth**

According to [Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle), also known as Shannon's maxim:

_The enemy knows the system. One ought to design systems under the assumption that the enemy will immediately gain full familiarity with them._

In other words, attackers should be allowed to know our algorithms inside and out. The only secret we don't share with attackers should be the private keys used at runtime.

There are several reasons as to why this is a good rule to live by, let's examine each one.

## 1\. Obfuscation Isn't Encryption

If a developer is operating under the assumption that attackers won't know about the details of their code, they may be tempted to try to build in security that is dependent on that.

For example, they may [encode data in a confusing way instead of encrypting it](https://qvault.io/2019/08/14/stop-with-the-obfuscation-encoding-and-encryption-are-not-the-same/), assuming that the enemy will think it is encrypted, or not be able to guess HOW it was encoded.

**BAD.**

When something needs to be kept secret, always encrypt.

![Navajo code comic](/img/code_talkers.png)

## 2\. You Probably Suck

If you roll your own crypto, you are likely to overlook vulnerabilities that have been accounted for in open-source versions. By the way, I don't mean that you specifically suck at writing crypto, I mean that no one person (or organization) can reasonably be responsible for vetting all possible attack vectors. Open-source allows the worldwide developer community to help expose problems with the code.

![L is for loser](/img/loser.png)

Not only are you likely to have problems in underlying mathematics and algorithms, but it is likely that your application-level implementation will also have vulnerabilities. There are no industry standard best practices to follow for your custom algorithms.

## 3\. Get New Updates

By using popular crypto libraries that are regularly updated, your code won't be vulnerable to the recently discovered attacks on the algorithms you are using.

Take advantage of the community, and give back by contributing when you can!

Go: [https://golang.org/pkg/crypto/](https://golang.org/pkg/crypto/)

Node: [https://nodejs.org/api/crypto.html](https://nodejs.org/api/crypto.html)

Python: [https://pypi.org/project/cryptography/](https://pypi.org/project/cryptography/)
