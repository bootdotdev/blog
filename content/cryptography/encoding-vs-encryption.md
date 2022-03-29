---
title: "Encoding vs Encryption - They Aren't the Same"
date: "2019-08-14"
categories: 
  - "cryptography"
  - "security"
---

While encryption does _involve_ various methods of encoding data, the two are absolutely not interchangeable. In fact, if you get them mixed up it can result in serious data breaches and security vulnerabilities.

[Encryption](https://en.wikipedia.org/wiki/Encryption) is a specific subset of encoding where the encoded messages can only be accessed by authorized parties (the ones holding the decryption keys).

[Encoding](https://qvault.io/2020/11/03/base64-vs-base58-encoding/) is simply a way of representing data in a specific format. For example, raw binary data can be encoded and decoded using the ASCII format as shown in the table below.

![encoding chart ](/img/asciifull.gif)

In the context of programming and cybersecurity, encoding offers **absolutely no security**. Sometimes formats like JWTs or Base64 outputs can confuse entry-level programmers because they appear encrypted when in reality **they aren't!** An attacker can easily figure out the protocol used to encode the data and reverse it. For example, in the case of ASCII encoding it's as simple as looking up each bytecode in the table above.

Encoding formats are only useful because they give computers and humans protocols to view and process raw binary data in a meaningful way.

To illustrate this point, try the following tools to see how easy it is to decode messages that are just encoded (not encrypted):

- [https://jwt.io/](https://jwt.io/)
- [https://www.base64encode.org](https://www.base64encode.org/)

![navajo code comic](/img/code_talkers.png)

[https://xkcd.com/2](https://xkcd.com/257/)[57/](https://xkcd.com/257/)

## Why you should ensure your encoded data is encrypted

At a job where I worked in the past, a developer before me built his own encoding scheme. It would take the raw binary data contained in a message and map specific bytes sequences to certain characters. It was totally made up, and the comment he left on the code was:

```
// Obfuscation technique. Base53 encoding for security
```

While it may confuse an attacker for a couple of minutes, this obfuscation offers more potential bugs in terms of needless complexity than it does security benefits. With free and easy to use encryption libraries available in all major programming languages, there is no excuse to try to bake your own these days.

[Elliptic curve cryptography](https://qvault.io/2020/07/21/very-basic-intro-to-elliptic-curve-cryptography/), RSA, [AES-256](https://qvault.io/2020/01/02/very-basic-intro-to-aes-256-cipher/), or another secure algorithm should have been used in the situation above. Ironically, it also probably would have taken less time to implement.

Security can be hard. However, take the time to use best-practices. It will save you so much time and headaches in the long run. Good luck, and stay safe out there!

## Related Articles

  - [Rust vs Go - Which Is More Popular?](https://qvault.io/2020/05/06/rust-vs-go-which-is-more-popular/)  
  - [Thinking about Recursion: How to Recursively Traverse JSON Objects and the Filesystem](https://qvault.io/2019/09/22/thinking-about-recursion-how-to-recursively-traverse-json-objects-and-the-filesystem/)   
  - [How to Make a Custom Select Component in Vue.js](https://qvault.io/2019/09/09/how-to-make-a-custom-select-component-in-vue-js/)
