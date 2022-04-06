---
title: "(Very) Basic Intro to PGP (GPG)"
author: Lane Wagner
date: "2020-07-27"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/photo-1477039181047-efb4357d01bd.webp
---

[PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy), or its open-source alternative, [GPG](https://en.wikipedia.org/wiki/GNU_Privacy_Guard), is a program used to encrypt data such that only an authorized party can decrypt it. In this introduction, we will cover its use-cases and a high-level overview of the algorithms involved.

Both programs (and others) adhere to the [OpenPGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP) protocol. Because it is an implementation agnostic protocol, people can use the software they are most comfortable with and still send secure messages to each other.

## Only Pretty Good?

The "pretty good" part of "Pretty Good Privacy" is a hilarious understatement. It uses secure building blocks and remains an extremely private (albeit not very user-friendly) protocol for secure communication.

{{< cta1 >}}

## Symmetric vs Asymmetric Encryption

Asymmetric algorithms allows users to communicate securely without sharing private keys. They are suitable for the encryption of messages meant to be sent over an untrusted medium like emails or text messages.

Symmetric algorithms are computationally fast. They are primarily used to encrypt data at rest, such as files on a hard drive.

![Asymmetric vs Symmetric encryption pgp](/img/Asymmetric-vs-Symmetric.png)

PGP is a hybrid cryptosystem, it takes advantage of certain benefits from symmetric and asymmetric systems. PGP uses asymmetric keys to encrypt symmetric keys, which are used to encrypt messages. This keeps PGP computationally efficient while also allowing users to own their own private keys.

## How Does It Work?

OpenPGP, the protocol to which PGP and GPG adhere, can really be looked at as a set of rules for _how_ we use _other_ encryption and authentication algorithms. There are four main components of a PGP system:

- Symmetric encryption
- Asymmetric encryption
- Hashing and [Digital Signatures](/cryptography/hmac-and-macs-in-jwts/)
- Compression

## Putting It All Together

Let's go through each step of how a PGP message exchange works:

1. Raw data is hashed and signed using the sender's asymmetric private key. This will allow the receiver to verify that the message is _from_ who they think it is.
2. The data is compressed in order to save space
3. A new random symmetric key is generated for this exchange
4. The random symmetric key is used to encrypt the compressed data
5. The symmetric key is encrypted using the receiver's asymmetric public key
6. The encrypted symmetric key and the encrypted data are sent to the receiver
7. The receiver uses their private key to decrypt the symmetric key
8. The receiver uses the symmetric key to decrypt the data
9. The data is decompressed
10. The receiver verifies the digital signature using the sender's public key

![PGP Step by Step flowchart](/img/Untitled-Project-792x1024.jpg)

That's it! If you have questions be sure to reach out on [Twitter](https://twitter.com/wagslane).

{{< cta2 >}}

## Which Algorithms are Used?

PGP defines in the official [RFC 4880](https://tools.ietf.org/html/rfc4880) which algorithms must and should be supported by PGP clients. Let's go over each one.

### Symmetric Encryption Algorithms:

> Implementations MUST implement [TripleDES](https://en.wikipedia.org/wiki/Triple_DES).
> 
> Implementations SHOULD implement [AES-128](/cryptography/aes-256-cipher/) and [CAST5](https://en.wikipedia.org/wiki/CAST-128).
> 
> Implementations that interoperate with PGP 2.6 or earlier need to support [IDEA](https://en.wikipedia.org/wiki/International_Data_Encryption_Algorithm), as that is the only symmetric cipher those versions use. Implementations MAY implement any other algorithm.
> 
> [https://tools.ietf.org/html/rfc4880#section-9.2](https://tools.ietf.org/html/rfc4880#section-9.2)

### Asymmetric Encryption Algorithms:

> Implementations MUST implement DS for signatures, and [Elgamal](https://en.wikipedia.org/wiki/ElGamal_encryption) for encryption.
> 
> Implementations SHOULD implement [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) keys.
> 
> RSA Encrypt-Only and RSA Sign-Only are deprecated and SHOULD NOT be generated but may be interpreted.
> 
> See section 13.8 for notes on [Elliptic Curve](/cryptography/elliptic-curve-cryptography/), ECDSA, Elgamal Encrypt or Sign, and X9.42.
> 
> _Implementations MAY implement any other algorithm._
> 
> [https://tools.ietf.org/html/rfc4880#section-9.1](https://tools.ietf.org/html/rfc4880#section-9.1)

### Digital Signature Algorithms:

> Implementations MUST implement [SHA-1](/cryptography/how-sha-2-works-step-by-step-sha-256/). Implementations MAY implement other algorithms. [MD5](/security/hash-functions/) is deprecated.
> 
> [https://tools.ietf.org/html/rfc4880#section-9.4](https://tools.ietf.org/html/rfc4880#section-9.4)

### Compression Algorithms:

> Implementations MUST implement uncompressed data. Implementations SHOULD implement [ZIP](https://en.wikipedia.org/wiki/Zip_(file_format)). Implementations MAY implement and other algorithms.
> 
> [https://tools.ietf.org/html/rfc4880#section-9.3](https://tools.ietf.org/html/rfc4880#section-9.3)
