---
title: "BIP 32 Watch-Only Wallets"
author: Lane Wagner
date: "2019-07-25"
categories: 
  - "bitcoin"
  - "cryptography"
  - "security"
images:
  - /img/800/frozen.jpeg
---

[Bitcoin improvement proposal 32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) is, in my opinion, one of the most important BIPs we have. (Thanks [Peter Wuille](https://twitter.com/pwuille)!) BIP 32 gave us Hierarchical Deterministic Wallets, which grant the ability to create a tree of keys from a single seed.

In the early days of Bitcoin, each time a user wanted to receive new coins, their wallet would randomly generate a new Bitcoin private key, along with the associated public key and address. For example (and don't try to use these):

Private key: **L57hXXKTCRgJRytYMVbhaxnsKpWZdzPzReKUghiYY6D6aQqQrM39**

Address (public key hash): **1P3AzkwVv1jDJAhEBQby6873xwJvymzDRn**

Each user's wallet software contained lists of public and private key pairs. If the user's computer breaks or became stolen, you will lose all the private keys. The user had to be fairly tech-savvy to know how to export and encrypt their keys for safekeeping. Even so, each time they received coins to a new address, they needed to re-back up the new private key.

## HD wallets to the rescue

Following BIP 32, new wallets called HD wallets (Hierarchical Deterministic, not High Definition) made the backup process a lot easier and safer.

Instead of generating random private keys for each transaction, HD wallets generate one [seed](https://bitcoin.org/en/glossary/hd-wallet-seed) which is used to create a master private key. This master private key can be used to generate more "child" private keys for each transaction. Because the child keys are determined using the same pattern each time, the user doesn't need to back up all of their private keys, only the one seed:

**000102030405060708090a0b0c0d0e0f**

However, since most wallets have also adopted [BIP 39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) you may be more familiar with a 12 or twenty-four-word encoding of your seed (again don't use this example):

**bubble cat run happy tree bird snow flake person orange yellow mother**

Now, on a piece of paper or in a password manager like [Boot.dev](https://blog.boot.dev), users can back up their seed phrase. Then they know that all the Bitcoins that will ever be stored in their wallet are recoverable.

{{< cta1 >}}

## Watch only HD wallet

![eye picture](/img/800/icon95-20-512.png)

A watch-only HD wallet is the same as a normal HD wallet except that it can't spend coins, only store them. Watch-only wallets are perfect for users who want a wallet to receive new coins easily but don't want to spend regularly from that wallet, similar to a savings account.

The seed (and associated private keys) are stored offline or under heavy encryption, while the [extended public key](https://www.google.com/search?q=bitcoin+xpub&oq=bitcoin+xpub&aqs=chrome.0.0j69i60j0l4.2127j0j7&sourceid=chrome&ie=UTF-8) is used in the online watch-only wallet.

A full watch-only wallet is much better and safer than using the same address again and again. This is because [using new addresses enhances privacy](https://en.bitcoin.it/wiki/Address_reuse).

Thanks for reading, good luck, and stay safe being your own bank!
