---
title: "Hashing Passwords - Python Cryptography Examples"
author: Lane Wagner
date: "2020-01-29"
categories: 
  - "cryptography"
  - "python"
  - "security"
images:
  - /img/800/python.jpeg
---

Building a from-scratch server or using a lightweight framework is empowering. With that power comes responsibility, specifically the responsibility to securely store user's passwords.

Not understanding the security implications of password storage can lead to devastating breaches and leaks. If you are building an application and need to store user credentials, learn about hash functions.

## Can I Store Passwords In Plain Text?

To demonstrate the potential dangers, let us assume we DON'T hash passwords on a fake example website, _LoveMatchingToday_. Inevitably when a hacker or disgruntled employee obtains access to _LoveMatchingToday's_ database, they will download all the usernames and passwords:

> user.one@gmail.com - somePa$$wordHere

> user.two@hotmail.com - otherPlainTextPass

Now the attacker can go to other websites, and because a majority of people reuse passwords on different websites, they can hack other systems.

{{< cta1 >}}

## Solution - Hashing

A [hash function](/cryptography/very-basic-intro-to-hash-functions-sha-256-md-5-etc/) (or more specifically in our case, a [key derivation function](/cryptography/key-derivation-functions/)) deterministically creates a strong key from a password. Because hashes are one-way, the attacker can't re-create the plaintext password from the hash. Now the attacker would find something like this in the database:

> user.one@gmail.com - cab864878af008fbc550087940ffacdb79a7f82201725e3350e25d6cfbdd4255

> user.two@hotmail.com - 42a7fd2b639d18b3aba5db8504d4530f1f1ab58ab9615414b7629d6ec5c157b8

They won't be able to use the hash to log in on other systems because they don't have access to the original password.

In Python, [Bcrypt](/cryptography/bcrypt-step-by-step/) is a strong key derivation function that can be used in production systems:

```
import bcrypt
bcrypt.hashpw('userPlainTextPassword'.encode(), bcrypt.gensalt())
```

## Rainbow Tables and Salts

You may have wondered in the above code snippet what the _gensalt()_ function does. If we were to hash passwords without salts, an attacker could do a [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table) attack in order to find the original plain text.

> A salt is a random string of data hashed alongside a password to keep the hash result unique. **Salts should be recreated** each time a new password is saved, and the salt is stored alongside the hashed result so that it can be used again for comparison. **Libraries like bcrypt are smart enough to store the salt IN the resulting string** so that developers don't need to do the extra work.

For example, let's say that _LoveMatchingToday_ wisened up and started hashing passwords, but didn't include unique salts. An attacker could have a precomputed table of hashes:

> aab864878af008fbc550087940ffacdb79a7f82201725e3350e25d6cfbdd425f = password123

> afg3683232297323f2f0087940ffacdb79a7f8284723732350e25d6cfbdd4cccc = shadowTheHedgehog1234

They could then check each hash they find and see if a hash matches an entry in their table. If so, they can effectively "reverse" the hash and learn the original plaintext.

For this reason, we need to salt passwords. Luckily Bcrypt handles salting automagically. For the sake of learning, however, let's assume they didn't. If they didn't, our pseudocode would look something like this:

```py
# Save new password
salt = creatRandomSalt()
hashedPassword = hash(newPassword.concat(salt))
database.save(hashedPassword, salt)

# Check password
hashedPassword, salt = database.GetUserCredentals()
passwordInput = userInput
if hash(passwordInput.concat(salt)) == hashedPassword:
  login()
else:
  failure()
```

However, since Bcrypt stores the salt automatically with the hashed result in the "{salt}{hashed}" format, we can just use the following code:

```py
import bcrypt

# password = userInput
hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
# save "hashAndSalt" in data base

# To check:
# password = userInput
valid = bcrypt.checkpw(password.encode(), hashAndSalt)
```
