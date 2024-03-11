---
title: "Cryptography Trends And News Going Into 2020"
author: Lane Wagner
date: "2020-01-03"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/cryptography_trends_and_news.webp
---

## Quantum Computing

Quantum computing may not be coming quite as fast as some in the field had certainly feared (or perhaps hoped). Google did, however, solve an impressive problem this year.

They published a paper in [Nature](https://www.nature.com/articles/s41586-019-1666-5). It stated that their quantum processor solved a problem that, in contrast, a digital computer would take 10,000 years to solve. The problem that was solved deals with generating certifiably random numbers. Their processor, 'Sycamore', uses 53 qubits, which corresponds to a search space of 1016.

## [Lattice-Based Cryptography](/cryptography/very-basic-intro-to-lattices-in-cryptography/)

Lattice-based Cryptography (LBC) is one of our best bets for secure "Post Quantum Cryptography". Therefore, almost half of the second round of [NIST's PQC contest](https://csrc.nist.gov/CSRC/media/Presentations/Round-2-of-the-NIST-PQC-Competition-What-was-NIST/images-media/pqcrypto-may2019-moody.pdf) is based on lattice math.

Lattice crypto is often based on the [shortest vector problem](https://en.wikipedia.org/wiki/Lattice_problem). A problem where, given a basis of a [vector space](https://en.wikipedia.org/wiki/Vector_space) and a [norm](https://en.wikipedia.org/wiki/Norm_(mathematics)), the goal is to find the shortest non-zero vector.

In addition, Matthew Dozer has a great introductory video:

{{< youtube 37Ri1jpl5p8 >}}

[Lattice-Based Crypto for IOT (Khalid, McCarthy, O'Neill)](https://eprint.iacr.org/2019/681.pdf)

[Lattice Based Cryptography - Wikipedia](https://en.wikipedia.org/wiki/Lattice-based_cryptography)

## Bitcoin - Schnorr Signatures

![bitcoin logo](/img/800/5a521fa72f93c7a8d5137fcf.png)

Instead of the current [ECDSA](/cryptography/elliptic-curve-cryptography/) implementation, Bitcoin might be switching to [Schnorr signatures](https://en.bitcoin.it/wiki/Schnorr) to get more efficiency when signing transactions. Instead of signing each transaction separately, with Schnorr, we can generate a single signature to validate many transactions at once. This allows Bitcoin to scale by requiring less data to be broadcast on the network when grouping transactions.

## More Rigorous Testing of Hash Functions

Also, Nicky Mouha [published a paper](https://eprint.iacr.org/2019/1421.pdf) exposing a vulnerability in Apple's CoreCrypto Library. This affects 11 out of 12 implemented hashes. However, MD2 is the only function to remain secure. As a result, a new test is founded which can help detect similar problems moving forward.

[Read more on NIST's testing here](https://www.nist.gov/publications/extending-nists-cavp-testing-cryptographic-hash-function-implementations)
