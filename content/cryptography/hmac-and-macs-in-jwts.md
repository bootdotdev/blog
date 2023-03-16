---
title: "HMAC and MACs - The Inner Workings of JWTs"
author: Lane Wagner
date: "2020-08-05"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/cybersecurity-speakers.webp
lastmod: "2023-01-17"
---

HMACs and MACs are authentication codes and are often the backbone of JWT authentication systems. A Message Authentication Code (MAC) is a string of bits that depends on a secret key and is sent with a message to prove the message wasn't tampered with. HMACs are a more strict version of MACs that offer additional security benefits.

## MAC - [Message Authentication Code](https://en.wikipedia.org/wiki/Message_authentication_code)

MACs are exactly what they sound like; small codes that allow receivers of messages to know who the sender was (authentication). A MAC code is calculated by using a message and a secret key as inputs. Anyone who has a copy of that secret key can then verify that that code and message were created by someone with the same key.

![MAC diagram](/img/800/Screen-Shot-2019-12-12-at-7.49.24-AM.png)

One way this is accomplished is by using a [hash function,](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/) for instance, [SHA-256](/cryptography/how-sha-2-works-step-by-step-sha-256/). Simply put, a hash function takes an input and then returns an output, where:

- The output is very unlikely to be the same for different inputs
- The output is always the same for the same inputs
- The output is not predictable - changing the input even slightly results in a seemingly random and large change to the output

Given this, a naive example of MAC generation by the sender could be:

```
message = 'my message here'
macCode = sha256('thisIsASecretKey1234' + message)
// send macCode and message
```

Then the verification by the receiver would be:

```
// receive macCode and message
if (macCode == sha256('thisIsASecretKey1234' + message)){
  // verified!
}
```

Note that MACs don't _necessarily_ need to use a hash function, but a hash _can_ be used as the "signing" mechanism.

{{< cta1 >}}

## HMAC - [Hash-Based Message Authentication Code](https://en.wikipedia.org/wiki/HMAC)

An HMAC is a kind of MAC. All HMACs are MACs but not all MACs are HMACs. The main difference is that an HMAC uses two rounds of hashing instead of one (or none). Each round of hashing uses a section of the secret key. As a naive example:

```
sha256('thisIsASe' + sha256('cretKey1234' + 'my message here'))
```

Which is a simplified version of the function given in [RFC-2104](https://tools.ietf.org/html/rfc2104).

Why use HMAC? Why do we need to hash twice?

With many hash functions, it's possible to change the message (without knowing the key) and obtain another valid MAC. We call this a [length extension attack](https://en.wikipedia.org/wiki/Length_extension_attack). No known extension attacks are known against the current HMAC specification.

## HMACs with JWTs

If you've ever implemented [JWTs](https://en.wikipedia.org/wiki/JSON_Web_Token) for authentication schemes within a web app, then you know that JWTs are wonderful for keeping track of who is who. A JWT (when using HMAC as the signing scheme) is basically just an HMAC message where the message data is a JSON object.

The interesting thing about the JWT system is that the sender and the receiver of the JWT are typically the same entity, that is, the webserver. Look at the following example:

1. User gives the server an username and password
2. Server verifies the username and password are correct
3. Server generates a JWT using HMAC:

```
hmacCode = sha256('thisIsASe' + sha256('cretKey1234' + '{"userID":"11be9160-2243-4449-934b-e8245fe2feb0"}'))
```

4. The server responds with the following (decoded) JWT:

```
header.{"userID":"e7a6e5b4-dbaa-4503-bd25-8ebfc3a54448"}.hmacCode
```

5. User decides to update his/her profile picture by sending the following request:

```
PUT /users/profile_picture
Authentication: Bearer {"userID":"e7a6e5b4-dbaa-4503-bd25-8ebfc3a54448"}.hmacCode

{"new_picture_url": "http://linktopicture.com/mypic"}
```

1. The server parses the JWT. The JWT says the user is the user with ID `e7a6e5b4-dbaa-4503-bd25-8ebfc3a54448`.
2. The server verifies that the user really is Lane by validating the HMAC code. Only someone with access to the secret key `thisIsASecretKey1234` could have made the HMAC code that corresponds to the `e7a6e5b4-dbaa-4503-bd25-8ebfc3a54448` JWT.
3. If verification is successful, then the server updates Lane's profile picture.

![JWT lifecycle](/img/800/hi42b4G.png.webp)

If you feel that I missed anything important, or have any questions, feel free to contact me!
