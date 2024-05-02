---
title: "AES-256 Cipher – Python Cryptography Examples"
author: Lane Wagner
date: "2020-02-06"
categories: 
  - "cryptography"
  - "python"
  - "security"
images:
  - /img/800/AES256 Python.webp
aliases:
  - /cryptography/aes-256-cipher-python-cryptography-examples/cryptography/very-basic-intro-to-the-scrypt-hash/
---

Want to encrypt text with a password or private key in Python? AES-256 is a solid symmetric cipher that is commonly used to encrypt data for oneself. In other words, the same person who encrypts the data also decrypts it, the way personal password managers work.

## Dependencies

For this tutorial, we'll be using Python 3, so make sure you install [pycryptodome](https://www.pycryptodome.org/en/latest/src/introduction.html), which will give us access to an implementation of AES-256:

```
pip3 install pycryptodomex
```

## Padding - Handled by GCM

AES-256 typically requires that the data to be encrypted be delivered in 16-byte blocks, and you may have seen this on other sites or tutorials. However, AES-256 in GCM mode does _not_ require any special padding that we have to do manually.

## Encrypting

Now we create a simple _encrypt(plain\_text, password)_ function. This function uses the password to encrypt the plain text. Therefore, anyone with access to the encrypted text and the password will be able to decrypt it.

```py
def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }
```

## Notes on encrypt() function

1. [Nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce): A random nonce (arbitrary value) must be a random and unique value for each time our encryption function is used with the same key. Think of it as a random salt for a cipher. The library supplies us with a secure nonce.
2. [Scrypt](/cryptography/very-basic-intro-to-the-scrypt-hash/): Scrypt is used to generate a secure private key from the password. This will make it harder for an attacker to brute-force our encryption.
3. [Salt](https://en.wikipedia.org/wiki/Salt_(cryptography)): A new random salt is used for each run of our encryption. This makes it impossible for an attacker to use precomputed hashes in an attempt to crack the cipher. (see [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table))
4. Scrypt [parameters](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt):
    1. N is the cost factor. It must be a power of two, and the higher it is the more secure the key, but the more resources it requires to run.
    2. R is the block size.
    3. P is the parallelization factor, useful for running on multiple cores.
5. [Base64](/bitcoin/base64-vs-base58-encoding/): We encode all of our bytes-type data into base64 a convenient string representation
6. [Tag (MAC)](/cryptography/hmac-and-macs-in-jwts/): The tag is used to authenticate the data when using AES in GCM mode. This ensures no one can change our data without us knowing about it when we decrypt.

## Decrypting

```py
def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted
```

## Notes on decrypt() function

1. The decrypt() function needs the same salt, nonce, and tag that we used for encryption. We used a dictionary for convenience in parsing, but if we instead wanted one string of ciphertext we could have used a scheme like `salt.nonce.tag.cipher_text`
2. The configuration parameters on the Scrypt and AES functions need to be the same as the encrypt function.

## Give Me The Full Code!

You probably want to see it all work in an example script. Look no further!

```py
# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])
    

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


def main():
    password = input("Password: ")

    # First let us encrypt secret message
    encrypted = encrypt("The secretest message here", password)
    print(encrypted)

    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, password)
    print(bytes.decode(decrypted))

main()
```
