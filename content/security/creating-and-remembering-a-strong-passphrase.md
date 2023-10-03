---
title: "Creating and Remembering a Strong Passphrase"
author: Lane Wagner
date: "2019-08-03"
categories: 
  - "cryptography"
  - "security"
images:
  - /img/800/photo-1509822929063-6b6cfc9b42f2.jpeg
---

We all have hundreds of online accounts. Ideally, as many of those accounts as possible have unique passwords. Unique passwords however present a difficult problem.

**No one can remember hundreds of strong passwords.**

To fix this problem, we created password managers. Now, all of our passwords are neatly stored in one place, encrypted by one master password or passphrase. The problem with this of course is the master password or passphrase needs to be very secure.

Which should be used? A password or passphrase?

## Passphrases are Better Than Passwords

![password comic](/img/800/password_strength.png)

[XKCD](https://xkcd.com/936/)

This XKCD comic does a good job of explaining the difference between passwords and passphrases. A password is easier for a computer to guess (less entropy), and also is much harder to remember! There is NO REASON we should be using passwords. If you are an application developer, especially an app developer writing you backend in Go, take a look at [go-password-validator](https://github.com/lane-c-wagner/go-password-validator). It will give users full control so they can create strong passphrases.

## Entropy

You may have noticed in the comic that the example password has 28 bits of entropy while the passphrase has 44. Entropy just means the number of possibilities that an attacker would need to guess to crack a password or passphrase.

For example, imagine a password has 16 characters, and each character has 58 possibilities. This means that there are:

`58^16 = 16,400,152,899,115,243,850,138,976,256` possibilities.

If we take the base 2 logarithm of the number of possibilities then we arrive at how many bits of entropy the recovery code contains.

`log2(58^16) = 93.73` bits of entropy.

The chart below gives a rough idea of how long a given password or passphrase will take to crack based on how many bits of entropy it has and how many guesses per second the attacker can make (which depends on their hardware).

![password chart ](/img/800/rhdADIZYXJM2FxqNf6UOFqU5ar0VX3fayLFpKspN8uI.png)

[entropy chart](https://www.reddit.com/r/dataisbeautiful/comments/322lbk/time_required_to_bruteforce_crack_a_password/)

## How to Remember

Now that we've covered why and how a passphrase is safer than a password, let's look at how to create a memorable passphrase. The key to a memorable passphrase is imagery. The idea is to take 4 or 5 random words and use those words to create an image in your head. The more ridiculous the image, the easier it will be to remember.

The _correct horse battery staple_ from the above XKCD is a good example, but I'll give you another one. Let's pretend you are trying to remember:

_banana army acid nose spray_

I would probably imagine an army of bananas doing acid while being sprayed out of a giant nose. If I repeat "banana army acid nose spray" out loud a couple times while imagining this ridiculous scene, then I can memorize it in just a couple seconds.

Repeating it a couple times allows you to remember the exact order of the words, but picturing the image is what will cement ii in your mind for the long term.

I hope this helps you create secure pass-phrases! As always, stay safe online! It's a dangerous place.
