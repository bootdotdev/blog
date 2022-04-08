---
title: "Intro to the One-Time Pad Cipher"
author: Lane Wagner
date: "2021-06-28"
categories: 
  - "cryptography"
images:
  - /img/800/eyeball-art.webp
---

In [cryptography](/cryptography/what-is-cryptography/), the one-time pad, or OTP is a way of encrypting information so securely that it's impossible to be cracked. That said, OTP has a major drawback in that it requires both parties to have access to the _same_ key before a message is encrypted.

## How the one-time pad cipher works

When using the one-time pad, a message and a secret key are required to start. Each bit of the original message, assuming we can use binary data, is encrypted by using an `XOR` operation on it and the corresponding bit from the secret key.

### Refresher on XOR

XOR, or “exclusive or” is a binary operator that works with binary data. It returns `true` if both of its inputs are opposites (one false and one true), otherwise, it returns `false`.

```
true XOR false = true
false XOR true = true
true XOR true = false
false XOR false = false
```

Check out my other article, [why exclusive or is important in cryptography](/cryptography/why-xor-in-cryptography/), if you want more information.

### One-time pad step-by-step

So, for example, if we start with the message "hello word" and the key "I not know", first we'd covert the text to binary data.

```
hello world = 01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01100100
I not know = 01001001 00100000 01101110 01101111 01110100 00100000 01101011 01101110 01101111 01110111
```

Next, we'll perform the `XOR` operation on all the data.

```
01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01100100

XOR

01001001 00100000 01101110 01101111 01110100 00100000 01101011 01101110 01101111 01110111

=

00100001 01000101 00000010 00000011 00011011 00000000 00011100 00000001 00011101 00010011
```

The resulting binary data is now the "cipher text". In order to convert it back, all we need to do is `XOR` the ciphertext with the key and we'll get the original message back.

```
00100001 01000101 00000010 00000011 00011011 00000000 00011100 00000001 00011101 00010011

XOR

01001001 00100000 01101110 01101111 01110100 00100000 01101011 01101110 01101111 01110111

=

01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01100100
```

Convert the result back to text and we have the original message decrypted.

```
01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01100100

=

hello world
```

## Perfect secrecy in the one-time pad

A cipher is said to have [perfect security](https://en.wikipedia.org/wiki/Information-theoretic_security#Security_levels) if an attacker who has access to only the ciphertext can infer absolutely nothing of interest about the plaintext. The one-time pad _does_ have perfect security. That said, it only has perfect security if the following conditions can be met:

1. The key must be _at least_ as long as the plaintext
2. The key must _never be reused_
3. The key must be kept completely secret to the outside world yet shared by both parties
4. The key must have a uniform distribution that is independent of the plaintext

The [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is a great example of a cipher that is _not_ perfectly secure _or_ practically secure. As we demonstrated earlier, when given access to the ciphertext of a Caesar cipher, an attacker can see the positions and patterns of characters in the plaintext.

## Issues using the one-time pad in production

Most production ciphers are **not** perfectly secure, but are "close enough". In short, trade-offs are made that add to the _practical_ security of a system while sacrificing the perfect _theoretical_ security of the cipher itself.

In accordance with the requirements outlined above, it's really hard to implement a secure one-time pad in a real-world system. Let's look at the first requirement, that the key needs to be at least as long as the plaintext it encrypts. This means that if I want to encrypt the contents of my computer's hard drive, I need a key that's _hundreds of gigabytes_ in length. There's no way I'll remember that key, let alone be able to write it down.

The second requirement, that the key can't be reused, is a huge pain! This means memorizing keys is out of the question because I always need a new one. Not only that, but whatever security vulnerabilities are introduced by needing to communicate a shared key to my intended recipient will be repeated each time a new message is sent.

Lastly, the last requirement, that it must be kept secret yet somehow communicated to the intended recipient, is a **tall** order. In fact, all symmetric encryption algorithms suffer from this problem. As a result, if you need to communicate with another entity you probably need to use a separate [asymmetric encryption](/cryptography/very-basic-intro-to-pgp-gpg/) scheme.

## Example of the one-time pad code in Go

```go
func encrypt(plaintext, key []byte) []byte {
	final := []byte{}
	for i := range plaintext {
		final = append(final, plaintext[i]^key[i])
	}
	return final
}

func decrypt(ciphertext, key []byte) []byte {
	final := []byte{}
	for i := range ciphertext {
		final = append(final, ciphertext[i]^key[i])
	}
	return final
}
```
