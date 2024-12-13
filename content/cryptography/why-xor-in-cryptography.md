---
title: "Why is Exclusive Or (XOR) Important in Cryptography?"
author: lane
date: "2020-01-18"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/why-is-exclusive-or-_xor_-important-in-cryptography.webp
---

If you are getting into [cryptography](/cryptography/what-is-cryptography/), or just trying to understand the fundamentals, you may have noticed that the `exclusive or` (XOR) operation is used quite often, especially in ciphers. XOR is a simple bitwise operation that allows cryptographers to create strong encryption systems, and consequently is a fundamental building block of practically all modern ciphers. Let's dive into the details and see what makes XOR so important.

## What is XOR?

XOR, or "exclusive or" operates on binary data. It returns true if both of its inputs are opposites (one false and one true), otherwise, it returns false. You may see the operator written this way: ⊕.

![XOR example](/img/800/Screenshot-from-2019-08-04-12-01-49.png)

For example, in Go, the code would be something like:

```
func exclusiveOr(a bool, b bool) bool {
	return a != b
}
```

## XOR Cipher - The Perfect Cipher

It is interesting to note that if:

1. The key is the same size as the message
2. The key is kept secret and generated truly randomly

Then the XOR cipher is certainly **impossible** to crack. This is known as a [one-time pad](https://en.wikipedia.org/wiki/One-time_pad). However, a simple XOR shouldn't be used in production due to the key length needing to be too long to be practical.

## Cipher Example

For instance, let's simply encrypt the word "hi"

1. First, convert "hi" to binary, here is a [free tool](https://www.rapidtables.com/convert/number/ascii-to-binary.html))

`01101000 01101001`

2. Next, create a random secret key that has the same length:

`01010010 01000101`

3. Then, create an encrypted message by XOR'ing the message and the key:

```
01101000 01101001 ("hi")
XOR
01010010 01000101 (secret key)
=
00111010 00101100 (encrypted message)
```

4. Finally, decrypt the message by XOR'ing the key with the encrypted message again:

```
00111010 00101100 (encrypted message)
XOR
01010010 01000101 (secret key)
=
01101000 01101001 ("hi")
```

## Why does it work?

XOR works as a cipher because it is its own inverse.

> 𝑎 = (𝑎 **⊕** 𝑏) **⊕** 𝑏

And, as we demonstrated in our example:

> _encrypted_ = _message_ **⊕** _key_  
> and  
> _message_ = _encrypted_ **⊕** _key_

## Is XOR used in production ciphers?

The simple XOR cipher isn't used in production because it is impractical to use keys that are the same length as the message body. However, the XOR is still extremely useful. In fact, it is used in almost all symmetric encryption algorithms. XOR is the primary operation in the ["add round key" step of AES-256](/cryptography/aes-256-cipher/). It is also used in the [DES cipher.](http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm)
