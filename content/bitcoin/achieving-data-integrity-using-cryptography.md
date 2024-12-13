---
title: "Achieving Data Integrity Using Cryptography"
author: lane
date: "2020-05-04"
categories:
  - "bitcoin"
  - "cryptography"
images:
  - /img/800/Data_Integrity.webp
---

Data integrity refers to the accuracy, legitimacy, and consistency of information in a system. When a message is sent, particularly using an untrusted medium, data integrity provides us with confidence that the message wasn't tampered with. For example, the SSL signature of [Boot.dev](https://blog.boot.dev) provides confidence that the webpage and data coming from our servers are coming from us and not the NSA.

## What Are the Potential Causes of Illegitimate Data?

Data integrity protects from a wide range of problems that involve data being mutated against the purposes of the system. Some potential problems include:

**Physical Accident** - Bits of data sent over an imperfect medium can become corrupted. For example, a wireless signal could be lost temporarily, or a wire could experience a noisy electrical signal.

**Digital Accident** - The software responsible for communicating the message could have bugs that unintentionally mutate a subset of messages.

**Malicious Actor** - A man-in-the-middle could be altering messages to confuse correspondents or learn valuable information.

## Solution - Checksum

A checksum solves all three of the potential data integrity problems listed above. A checksum is a [deterministic](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/) value derived from the message data and can be transmitted separately. This means the checksum for a given message will always be the same.

The receiver of a message can generate a checksum from the message, and if the generated checksum matches the one that was sent then the message couldn't have been tampered with.

It is important to note that if the medium over which the checksum was obtained is untrusted then a malicious actor _could_ alter the message and the checksum. It is common good practice to sign the checksum using a digital signature. The digital signature provides proof that the sender of the checksum is who they say they are.

## What Makes a Good Checksum?

There are many types of checksums, but the best checksums are typically [cryptographic hash functions](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/). Hash functions that have the following properties make great checksums for validating data integrity:

- **Deterministic** - The hash of the same message will always be the same, with no randomness
- **Fast** - Computing a checksum shouldn't use unnecessary resources (A [KDF](/cryptography/key-derivation-functions/) is an inefficient checksum)
- **Rare collisions** - The likelihood of two different messages creating the same checksum should be astronomically unlikely
- **Small** - The result of the hash (AKA the "digest") should be short - no need to waste a lot of data.

The [SHA-256](/cryptography/how-sha-2-works-step-by-step-sha-256/) hash function is often used to create checksum digests.

## Example - Validating a Real Checksum

A common use case for checksums is the verification of a download. In this example, we are going to download the Bitcoin Core node software and verify its integrity. For an updated version go [here](https://bitcoin.org/en/download) or just follow along to use version 0.19.1. I will assume you are on Mac OS, for a different OS follow the instructions on the [download page](https://bitcoin.org/en/download).

1. [Download the program](https://bitcoincore.org/bin/bitcoin-core-0.19.1/bitcoin-0.19.1-osx.dmg)
2. [Download the checksum](https://bitcoin.org/bin/bitcoin-core-0.19.1/SHA256SUMS.asc)
3. Open a terminal and go to the downloads folder:

```bash
cd ~/Downloads
```

Compute and print the checksum of the downloaded dmg file:

```bash
shasum -a 256 bitcoin-0.19.1-osx.dmg
```

Which should print:

> 206d8d92189d22e735393abebeb7a2e7237a119dd448b4a40df8c357da1287b2 bitcoin-0.19.1-osx.dmg

Then print the downloaded (expected) checksum:

```bash
cat SHA256SUMS.asc | grep bitcoin-0.19.1-osx.dmg
```

Which should match:

> 206d8d92189d22e735393abebeb7a2e7237a119dd448b4a40df8c357da1287b2 bitcoin-0.19.1-osx.dmg

If they match, congratulations! Your download has been verified. No man in the middle altered the program that you downloaded.

Again, keep in mind that to verify that the checksum you were provided wasn't tampered with, you would need also to verify the [GPG signature](https://www.gnupg.org/gph/en/manual/x135.html).
