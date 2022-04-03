---
title: "Shamir's Secret Sharing Step-By-Step"
author: Lane Wagner
date: "2020-08-18"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/library-scaled.webp
---

_Adi Shamir's Secret Sharing_ is a [cryptographic algorithm](https://qvault.io/cryptography/what-is-cryptography/) that allows distinct parties to jointly share ownership of a single secret by holding _shares_. The original secret can only be reconstructed by using a minimum number of shares, which allows different parties to cooperate without the need to fully trust one another.

## Example Problem

To illustrate, let's imagine that a family of four all share a single Bitcoin wallet. This Bitcoin wallet contains a single private key that all members of the family co-own. Because there is a single key, any of the family members can use that key to spend all of the Bitcoins.

The family has a problem: If they each keep a copy, then only one of their copies needs to be compromised to have all the coins stolen. If only one of them keeps the key, then that person may lose it or decide to double-cross the other family members.

Luckily, one of the family members is also a cryptographer. Instead of naively sharing the original key, they use SSS ([Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing)). The family creates four shares and sets a threshold of three, with the Bitcoin key as the original secret. Now, their plan has the following properties:

- They have not stored the bitcoin key in a single place which makes it harder to steal
- Members of the family need to cooperate to spend the Bitcoin, one family member can't betray the others
- If a family member dies or loses their share, the other three members can still reconstruct the key

{{< cta1 >}}

## Understanding the Threshold

Every Shamir sharing scheme has a total number of shares and a threshold. The **threshold is the number of shares required** to reconstruct the original secret. For example, with five shares and a threshold of three, you only need three of the five shares to calculate the original secret.

## The Math - Lines

One of the fundamental mathematical properties used in Shamir's secret sharing is the fact that it takes _k_ points to define a polynomial of degree _k_ \- 1. For example:

- Only one line can be drawn between two points
- Only one possible parabola crosses through the same three points
- Only one cubic curve passes through the same four points
- An infinite number of lines can be drawn through the same point
- An infinite number of parabolas can be drawn through the same two points

## The Math - Walkthrough

Let us construct a scheme to share our secret 1954 (_S)_ with 4 (_n)_ shares and a threshold of 3 (_k)_.

First, we randomly choose _k_ - 1 positive integers, so in our case, 2 positive integers. We randomly choose 43 and 12.

Then, we build a polynomial of the form

```
y = a0 + a1*x + a2*x^2
```

Where a0 is the secret, and a1 and a2 are our randomly chosen integers. We are left with:

```
y = 1954 + 43x + 12x^2
```

Then, we use this formula to create 4 points (shares) that we give to each participant.

### Share 1

(x, y) where x = 1

y = 1954 + 43\*1 + 12\*1^2 = 2009

(1, 2009)

### Share 2

(x, y) where x = 2

y = 1954 + 43\*2 + 12\*2^2 = 2088

(2, 2088)

### Share 3

(x, y) where x = 3

y = 1954 + 43\*3 + 12\*3^2 = 2191

(3, 2191)

### Share 4

(x, y) where x = 4

y = 1954 + 43\*4 + 12\*4^2 = 2318

(4, 2318)

## Reconstruction

Each participant in our scheme now owns one `(x,y)` point, which is a single share. Remember that we set our threshold to 3 and that 3 points define a parabola (polynomial of degree 2) perfectly. That means that if we use three points, we can draw a parabola and calculate a0 (the secret). Let's assume we have control of shares 1, 2, and 4.

### Step 1 - Plot the points (shares) that we control

![shamirs secret sharing no line](/img/shamirs-secret-sharing-no-line-1024x498.jpg)

### Step 2 - Draw the corresponding parabola

![shamirs secret sharing](/img/shamirs-secret-sharing-1024x540.jpg)

### Step 3 - Find the point where `x=0`. It's `y` value is the secret

![shamirs secret sharing shares](/img/shamirs-secret-sharing-shares-1024x555.jpg)

In our case, the secret is `1954`.

{{< cta2 >}}

## It's not actually that simple. We need finite fields.

While the example we worked through above is great for demonstration purposes, it actually isn't very secure. For each share that an attacker obtains, they actually are gaining more and more information about the secret. While two points don't perfectly describe a parabola, they still leak critical information _about_ the parabola.

The solution lies in [finite field arithmetic](https://en.wikipedia.org/wiki/Finite_field_arithmetic). By plotting the function on a finite field of sufficient size, the graph of the polynomial becomes disjointed and scattered, which means the attacker is unable to make educated guesses about the pathing of the underlying function.

## Adi Shamir

Adi Shamir is an Israeli cryptographer famous for Shamir's Secret Sharing, but he is also a co-inventor of the widely used RSA algorithm that the vast majority of the internet is built upon. Shamir was born in Tel Aviv and earned an undergraduate degree [](https://en.wikipedia.org/wiki/Bachelor_of_Science)in math from the university there. Later he obtained his master's and Ph.D. degrees in Computer Science from the Weizmann Institute in 1975 and 1977 respectively.

![](/img/440px-Adi_Shamir_Royal_Society-200x300.jpg)
