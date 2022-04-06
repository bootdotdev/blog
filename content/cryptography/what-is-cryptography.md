---
title: "What is Cryptography? A Complete Overview"
author: Lane Wagner
date: "2021-09-08"
categories: 
  - "cryptography"
images:
  - /img/What-is-cryptography-guide-min.webp
---

## What is cryptography?

Simply put, Cryptography provides a method for secure communication. It stops unauthorized parties, commonly referred to as adversaries or hackers, from gaining access to the secret messages communicated between authorized parties. The method that cryptography provides is called _encryption_.

Encryption transforms a key and input, the _plaintext_, into an encrypted output, the _ciphertext_. Encryption algorithms are only considered secure if attackers cannot determine any properties of the plaintext or the key when presented with only the ciphertext. An attacker should not be able to find out _anything_ about a key, even if they have many plaintext/ciphertext combinations that use that key.

A real-world example would be credit card information that you use for purchases on Amazon or other e-commerce sites. The code in your web browser encrypts the plaintext, your card number, into ciphertext, which to someone without the keys would look like illegible, random text. However, once your card number reaches its intended recipient, the online store, their software would decrypt it back into plaintext so they can charge you for your purchase.

{{< cta1 >}}

## Principles of cryptography

The core principles of modern-day cryptography include:

- Confidentiality
- Integrity
- Non-repudiation
- Authentication

Let's go over each one by one.

### Confidentiality

Data Confidentiality ensures that the data is limited to those who are authorized to view it. The data should only be visible to those who possess some critical information, like the decryption key, for example.

### Integrity

[Data integrity](/bitcoin/achieving-data-integrity-using-cryptography/) refers to the accuracy, legitimacy, and consistency of information in a system. When a message is sent, particularly using an untrusted medium like the internet, data integrity ensures us that a message wasn’t tampered with or accidentally altered.

Let's use the example of military orders. We're at war and an army general needs to send an order of retreat to his troops across the sea. Without a guarantee of data integrity, a hacker could intercept the message, change the order, and send it on its way. The army might receive an order to advance and walk right into a trap the general knew about.

### Non-repudiation

Non-Repudiation assures that no one can deny the validity of the data in question, and is actually a legal term used in cyber security. Non-Repudiation is typically accomplished by the use of a service that provides proof of the origin and integrity of the information. It makes it nearly impossible to successfully deny who or where a message came from.

Non-repudiation is similar to data integrity, but it has more to do with knowing _who_ sent the information, and less with whether or not it was _changed_ along the way. In the military example from above, even if we could guarantee that the retreat order was never tampered with, non-repudiation would be a way to ensure it was the general who gave the order in the first place, and not some enemy spy.

### Authentication

There are two kinds of authentication typically used in cryptography.

1. Integrity authentication like a [MAC or HMAC](/cryptography/hmac-and-macs-in-jwts/) ensures that data hasn't been tampered with.
2. Source authentication, like an [SSL certificate](https://en.wikipedia.org/wiki/Certificate_authority), can be used to verify the identity of who created the information. Every time you connect to a website over HTTPS, your browser ensures that you're connected to the site you think you are by checking the SSL certificate.

## Guidelines for cryptographers

[Never try to design your own cryptosystem. The best cryptographers in the world](/cryptography/is-open-source-cryptography-really-secure/) routinely design cryptosystems with serious security flaws. As it turns out, it's _really_ hard to build a secure system. There are just too many attack vectors to consider.

For a cryptosystem to be considered "secure enough" it needs to go through intense scrutiny by the security community. "Security through obscurity", or the fact that attackers may not have knowledge of your system, is something that should never be relied on. In fact, good systems do expose to attackers how they work. Only the private keys should be kept secret.

> _The enemy knows the system. One ought to design systems under the assumption that the enemy will immediately gain full familiarity with them._
> 
> According to [Kerckhoffs’s principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle)

Always take reasonable steps to protect any keys that your software systems use.

**Never** store encryption keys in plain text with the data they protect. That's the virtual equivalent of locking your front door and leaving the key on the frame. It's the first place an attacker will look.

Let's take a look at a few rules of thumb for securely storing keys.

1. **Protect your private keys with strong access control lists**, or ACLs. Follow the principle of least privilege, that is, only allow those you really need the keys to get access to them.
2. **Use a secure password or secret manager** to keep track of your keys. Good secret managers will encrypt your keys using a strong [key-derivation function](/cryptography/key-derivation-functions/) like [bcrypt](/cryptography/bcrypt-step-by-step/) or [scrypt](/cryptography/very-basic-intro-to-the-scrypt-hash/).
3. **In extreme cases, a hardware security module** is a physical device that can be used to store keys offline securely. Software applications can then access HSMs connected to the same machine. The HSM actualy performs decryption on the HSM itself, so the keys never leave the device.

Lastly, ensure you only use key strengths and operating modes that comply with the latest industry best practices. For example, AES-256 should typically be used over AES-128, if for no other reason than its larger key size provides more entropy when going up against a quantum algorithm.

For more information, read our post on [whether open-source cryptography really is secure](/cryptography/is-open-source-cryptography-really-secure/)

## What practical problems does cryptography solve?

A secure system provides the four principles of cryptography to systems in the real world. Confidentiality, integrity, authentication, and non-repudiation are necessary properties in modern software, and they wouldn't be possible without cryptography.

Software systems, especially those that exist on the web, often have many endpoints, clients, dependencies, networks, and servers. All the physical machines that are required to make your crossword app work need to communicate over networks that can not be trusted. Internet communication takes place over open, public networks that can be trivially compromised by external attackers.

There are two main types of attacks that exist on open networks:

- **In a passive attack**: the hacker listens to a network connection and reads sensitive information as it is transmitted.
- **In an active attack**: the attacker impersonates a client or server, intercepts communications intended for it in transit, and modifies the information before forwarding it to its original destination.

The confidentiality and integrity protection provided by cryptographic protocols such as SSL/TLS can protect communications from malicious eavesdropping and tampering. Authentication protection ensures that the data you receive really came from who you thought it came from. For example, are you sending your social security number to your bank, or to a Nigerian prince?

Cryptography isn't only useful for data in transit, it can also be used to protect data at rest. Data that is simply stored on a disk in a database can be encrypted to prevent future accesses from reading it. This kind of encryption happens when you lock your phone or computer and keeps your information safe if your devices are stolen.

{{< cta2 >}}

## Types of cryptography

There are three main types of cryptography:

1. Symmetric key encryption
2. Asymmetric key encryption
3. Hash functions

### Symmetric key cryptography

Symmetric encryption uses the **same key** for encryption and decryption. The sender and receiver of the message use a single shared key to encrypt and decrypt messages. Symmetric key systems are faster and simpler, but sharing keys is difficult. If you need to communicate over an insecure medium, how would you get the key to the recipient in the first place?

The answer is that for communication to another party, you'll probably want to use asymmetric encryption, which we'll cover shortly. Symmetric encryption excels when you're encrypting information at rest. For example, your password manager encrypts your passwords, but they aren't being sent to anyone. You only need one key, because you're the only one using it.

Common symmetric encryption algorithms include [AES](/cryptography/aes-256-cipher/) and [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard).

![symmetric encryption vs asymmetric encryption](/img/Symmetric-vs-Asymmetric-Cryptography-min-1024x1024.png)

### Asymmetric key cryptography

Asymmetric encryption uses **different keys** for encryption and decryption. A pair of keys that are cryptographically related are used to encrypt and decrypt information. A public key is used for encryption while its private key is used for decryption.

If I want to receive a message from my wife, I would send her my public key. The public key is just that, public. If someone intercepts the key, it's not a problem, they won't be able to use it to decrypt anything.

My wife would then use my public key to encrypt a message for me. Now, since I'm the only one that owns the corresponding private key, I'll be able to decrypt that message once I receive it.

Common asymmetric encryption algorithms [ECC](/cryptography/elliptic-curve-cryptography/) and [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

| Properties              | Symmetric                       | Asymmetric                                        |
| ----------------------- | ------------------------------- | ------------------------------------------------- |
| **Keys**                | A single key                    | A private and public key                          |
| **Speed**               | Faster, simple                  | Slower, more complex                              |
| **Use cases**           | Bulk encryption of data at rest | Encryption of data in transit between two parties |
| **Principles provided** | Confidentiality                 | Confidentiality, authentication, non-repudiation  |

### ****Hash Functions****

The third most common type of cryptography involves [hash functions](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/). No key is used in this algorithm. A fixed-length value is calculated from the plaintext, which makes it impossible for the contents of the plaintext to be recovered.

However, because the same plaintext will always hash to the same output, it can be used to, for example, compare passwords without ever storing them.

Popular hashing functions include [SHA-256](/cryptography/how-sha-2-works-step-by-step-sha-256/), [Bcrypt](/cryptography/bcrypt-step-by-step/), and [Scrypt](/cryptography/very-basic-intro-to-the-scrypt-hash/).

## Cryptology vs cryptography vs cryptanalysis

### Cryptology

Cryptology is the science of secret messages. Anything that has to do with making or breaking codes falls into cryptology’s domain. Cryptology can also be thought of as the study of encryption and decryption. In a nutshell, cryptography and cryptanalysis are the two branches under the umbrella of cryptology.

- Cryptography: Study of building secure cryptosystems.
- Cryptanalysis : Study of breaking cryptosystems.
- Cryptology: Study of both cryptography and cryptanalysis.

Cryptology is extremely heavy on mathematics, such as number theory and the application of formulas and algorithms. An interesting anecdote is that cryptology was the main field of study of the first computer scientists, including [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) himself.

### Cryptography

People often lazily use "cryptography" in place of the word "cryptology", but in reality, cryptography focuses only on building cryptosystems.

For example, the design of [AES-256](/cryptography/aes-256-cipher/), the system that allows us to encrypt the personal information on our phones and laptops, would have been primarily _cryptography_ work.

### Cryptanalysis

Cryptanalysis is the inverse of cryptography. It's the study of how to break secret codes, not make them. Having a solid understanding of cryptanalysis is fundamental in cryptography, however, as one must know their enemy.

Imagine that the FBI gets ahold of your personal mobile phone, and they want to snoop around to see what you've been up to. The methods they would employ to "crack" the code and decrypt the contents of your phone would be cryptanalysis techniques.

For more information, we have a full post on [cryptology vs cryptography](/cryptography/cryptology-vs-cryptography/)

## What is quantum computing, and will quantum computing break cryptography?

Where a classical bit holds a single binary value such as `0` or `1`, a [qubit](https://en.wikipedia.org/wiki/Qubit) can hold both values simultaneously. This means a single qubit can hold much more information than a classical bit, and all this is made possible by the phenomenon of [superposition](https://en.wikipedia.org/wiki/Quantum_superposition). This unique property allows them to process information in potentially logarithmic time, or in other words, exponentially faster than classical computers.

Many asymmetric encryption algorithms have been mathematically proven to be broken by quantum computers using [Shor’s algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm). Because algorithms like RSA rely heavily on the fact that normal computers can’t find prime factors quickly, they have remained secure for years. With quantum computers breaking that assumption, then it may be time to find new standards.

On the other hand, symmetric encryption, or more specifically [AES-256](/cryptography/aes-256-cipher/), is believed to be quantum-resistant. That means that [quantum computers are not expected](https://en.wikipedia.org/wiki/Post-quantum_cryptography#Symmetric_key_quantum_resistance) to be able to reduce the attack time enough to be effective if the key sizes are large enough.

For more information, read our post on [whether AES-256 is quantum resistant](/cryptography/is-aes-256-quantum-resistant/)

## How do Bitcoin, cryptocurrency and other blockchains utilize cryptography?

Bitcoin and other cryptocurrencies rely on cryptographic algorithms to function, hence the "crypto" in the name. Bitcoin uses two primary cryptographic methods. The first is asymmetric encryption. A bitcoin wallet is, at its core, a collection of private keys that can be used to sign transactions on the network. Bitcoin and other blockchain technologies utilize cryptographic signatures, which are a form of asymmetric encryption, to guarantee that when you send a Bitcoin to your friend, it was actually you that sent it.

The second is hashing. Bitcoin mining makes use of the SHA-256 algorithm to act as a proof-of-work on the network. Because the output of hash functions can't be easily guessed, the network can trust that an actor in the network has expended a good deal of energy computing the result of a calculation.

The reason we care that it took someone a lot of work to add a new block to the blockchain is to make it more secure. Every miner has to solve a difficult "hashing lottery" to add a new block, but if it were too easy, anyone could add new blocks quickly to rewrite the blockchain to their advantage. Proof-of-work consensus is what makes Bitcoin the most secure public network ever created in human history.

If you're interested in reading more in-depth about how Bitcoin works, you can do so on [bitcoin.org](https://en.bitcoin.it/wiki/Main_Page).

## History of cryptography - A timeline of important events

Cryptology is a _very_ young science. Although humans have had rudimentary forms of cryptography for thousands of years, the systematic study of cryptology as a science only began about a hundred years ago. The advent of computers made cryptography many orders of magnitude more complex than it had been previously.

- **1900 BC** - First evidence of altered symbols in text found in the [tomb of Khnumhotep](https://en.wikipedia.org/wiki/Khnumhotep_II) II in Egypt. The writings weren't meant to be secret, but are the first evidence we have of someone altering encoding symbols.
- **100 BC** - [Ceasar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). Julius Caesar was known to use a form of encryption to convey secret messages to his army generals posted on the war front. This substitution cipher, known as the Caesar cipher, is perhaps the most mentioned historic cipher (an algorithm used for encryption or decryption) in academic literature. It's a simple cipher where each character of the plain text is simply substituted by another character to form the ciphertext. For example, "a" becomes "d", "b" becomes "e", and so on.
- **500 AD** - [Vigenere's Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). Vigenere designed a cipher that is said to have been the first cipher to use a secret key.
- **1800** [Hebern Rotor Machine](https://en.wikipedia.org/wiki/Hebern_rotor_machine). In the early 1800s, when everything became electric, Hebern designed an electromechanical device that used a single rotor in which the secret key is embedded in a rotating disk. The key encoded a [substitution box](https://en.wikipedia.org/wiki/S-box) and each keystroke on the keyboard resulted in the output of ciphertext. Like the caesar and vigenere ciphers, Hebern's machine was broken by using letter frequencies.
- **1918** - [Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine). The Engima machine was invented by German engineer Arthur Scherbius at the end of World War I and was heavily used by German forces during World War II. The Enigma machine used 3 or more rotors that spin at different speeds as you type on the keyboard and output corresponding letters of the ciphertext. In the case of Enigma, the key was the initial setting of the rotors.
- **1943** Alan Turing and others on his team at Bletchley Park, complete the "Heath Robinson", a specialized machine for cipher-breaking. This team was also responsible for cracking the Enigma Machine during the second world war.
- **1948** – Claude Shannon [writes a paper](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) that is responsible for establishing our modern mathematical basis of information theory.
- **1970** - [Lucifer Cipher](https://en.wikipedia.org/wiki/Lucifer_(cipher)). In the early 1970s, a team from IBM designed a cipher called Lucifer. The Nation Bureau of Standards (now NIST) in the U.S. put out a request for proposals for a block cipher that would become a national standard. Lucifer was eventually accepted and became [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard) (Data Encryption Standard).
- **1977** - [RSA public key encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) invented by Ron Rivest, Adi Shamir and Leonard Adleman.
- **1991** - Phil Zimmermann releases [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy).
- **1994** - [Secure Sockets Layer (SSL)](https://en.wikipedia.org/wiki/Secure_Sockets_Layer) encryption protocol released by Netscape, which now secures the majority of the modern web.
- **1994** – [Peter Shor devises an algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm) which lets quantum computers determine the factorization of large integers quickly.
- **1997** - DES Broken by exhaustive search. In 1997 and the following years, DES was broken by an exhaustive search attack. The main problem with DES was the small size of the encryption key. As computing power increased, it became easy to brute force all the different combinations of the key to get a possible plaintext message.
- **2000** - [AES](/cryptography/aes-256-cipher/) accepted as DES replacement. In 1997, NIST again put out a request for proposal for a new block cipher. It received 50 submissions. In 2000, it accepted Rijndael, and christened it as AES or the Advanced Encryption Standard.
- **2004** - [MD5](https://en.wikipedia.org/wiki/MD5) shown to be vulnerable to collisions
- **2009** - [Bitcoin](https://bitcoin.org/en/) network launch

{{< cta3 >}}

## For further study

**For beginners:** If you've been inspired to learn cryptography as a beginner to coding and computer science, we have an entire computer science course curriculum to take you from complete beginner to graduate level. As cryptography is a more advanced topic, we suggest you start with our [Intro to Coding with JavaScript courses](https://boot.dev/course/2af5c197-21eb-48b4-bd90-b0d59adb311e/eca6fbac-01a2-4b03-9837-e2242d665e21/88898457-a74f-4dd7-97d3-f8a48d0a6beb).

**For experienced coders:** We recommend our [Practical Cryptography course](https://boot.dev/practical-cryptography-course/) which covers everything from the basics of encryption and brute force attacks to stream ciphers, block ciphers, and hash functions.
