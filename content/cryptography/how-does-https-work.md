---
title: "How does HTTPS encryption work?"
author: Lane Wagner
date: "2023-01-26"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/https-lock.png.webp
imgAlts:
  - "HTTPS lock icon made with Midjourney"
---


Hypertext Transfer Protocol *Secure* or [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/https) is an extension of the [HTTP protocol](http://boot.dev/learn/learn-http). HTTPS secures the data transfer between client and server by [encrypting](https://developer.mozilla.org/en-US/docs/Glossary/Encryption) all of the information communicated.

HTTPS allows a client to safely share sensitive information with a server through an HTTP request. HTTPS is critically important when it comes to sending sensitive data such as credit card information, passwords, or bank account numbers.

## How does HTTPs work? (video)

{{< bdyoutube 0kwLpf6ms94 >}}

### Too long, didn't watch

In short, HTTPs works like this:

1. The client contacts server and requests a secure connection
2. The server sends the client its [public key](https://en.wikipedia.org/wiki/Public-key_cryptography)
3. The client and the server use asymmetric encryption (like [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))) to negotiate a shared private key
4. The shared private key is used by the client to encrypt the HTTP request (using [symmetric encryption](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) like [AES](https://blog.boot.dev/cryptography/aes-256-cipher/))
5. The server uses the shared private key to decrypt the HTTP request
6. The server uses the shared private key to send the client an encrypted response
7. The client uses the shared private key to decrypt the response

## HTTPS is just HTTP with extra security

![HTTPS](https://i.imgur.com/iOkQUdG.png)

HTTPS requires that the client use [SSL](https://developer.mozilla.org/en-US/docs/Glossary/SSL) or [TLS](https://developer.mozilla.org/en-US/docs/Glossary/TLS) to protect requests and traffic by encrypting the information in the request.

## When should I use HTTPs?

While HTTPs is only *critically* important when it comes to sensitive data, it's a good idea to just use HTTPS for *all* of your web traffic. If you browse to a website that doesn't use HTTPs, your browser will actually give you an ugly little warning to let you know that the site is not as secure as it should be.

![no http browser](/img/800/no-https.png.webp)

*If you develop websites, use HTTPs.*

## Careful! HTTPS is not necessarily private

Just because a website uses HTTPS doesn't mean that your communication with them is *private*.

### HTTPS keeps your messages private, but not your identity

It's important to note that while HTTPS encrypts *what you are saying*, it doesn't necessarily protect *who you are*. Tools like [VPNs (virtual private networks)](https://nordvpn.com/what-is-a-vpn/) are needed for remaining anonymous online.

If you use a VPN, the company that runs the VPN is responsible for keeping your identity private. There is another option for privacy called a [TOR](https://www.torproject.org/) network, which is a network of computers that are all connected to each other. The TOR network, which you you can use via a Tor browser, is designed to keep your identity *anonymous*, but it effectively adds another layer of privacy. You can use a VPN *and* a Tor browser if you're really concerned about your privacy.

In short, HTTPs keeps your messages private, but not your identity or the identity of the server you're communicating with. VPNs and TOR networks can help with that.

### HTTPS ensures that you're talking to the right person (or server)

In addition to encrypting the information within a request, HTTPS uses [digital signatures](https://en.wikipedia.org/wiki/Digital_signature) to prove that you're communicating with the server that you think you are. If a hacker were to intercept an HTTPS request by tapping into a network cable, they wouldn't be able to successfully pretend they are your bank's web server.
