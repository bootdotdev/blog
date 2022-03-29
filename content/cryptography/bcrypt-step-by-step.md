---
title: "Bcrypt Step by Step"
author: Lane Wagner
date: "2020-08-24"
categories: 
  - "cryptography"
  - "golang"
  - "security"
---

Bcrypt is a [key derivation function](https://qvault.io/2019/12/30/very-basic-intro-to-key-derivation-functions-argon2-scrypt-etc/), which can be thought of as a special kind of [hash function](https://qvault.io/2020/01/01/very-basic-intro-to-hash-functions-sha-256-md-5-etc/). Its purpose is to _slowly_ convert a piece of input data to a fixed-size, deterministic, and unpredictable output. A common use case is to convert a password into an n-bit [cryptographic](https://qvault.io/cryptography/what-is-cryptography/) key, which can then be used for safe authentication.

## What does a Bcrypt hash look like?

Using Bcrypt on the password _myPassword123_ would produce something like the following:

**_myPassword123_** \->
$2y$12$vUw4OU4EAl4w4vC6/lA33OtDSYGhiIdekdT9iOoSs9/ckwrffaEui

That output can be used to compare against future hashes to see if the original data matches.

### Bcrypt Output Format

$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
\\\_\_\_/\\\_\_/\\\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/\\\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/
Alg   Cost                  Salt                                            Hash

- `2a`: The hash algorithm identifier (Bcrypt)
- `10`: Cost factor (2`10` = 1,024 rounds of key expansion)
- `N9qo8uLOickgx2ZMRZoMye`: 16-byte (128-bit) salt, base64 encoded to 22 characters
- `IjZAgcfl7p92ldGxad68LJZdL17lhWy`: 24-byte (192-bit) hash, base64 encoded to 31 characters

## Why not compare passwords directly?

In web development, it is insecure to store user's passwords in plain text. If an attacker were to gain access to the server's database they could find raw email/password combinations and use them to attack the same users on other sites.

At the _very least_ we must hash user's passwords, but hash functions like [SHA-2](https://qvault.io/2020/07/08/how-sha-2-works-step-by-step-sha-256/) and MD5 are too fast to be secure. Using a KDF like Bcrypt provides security benefits over fast hashes because it is computationally expensive and slow. If an attacker gains access to a database of password hashes made with fast algorithms it is easy for them to "reverse" the hashes by guessing different inputs and seeing if the outputs match.

For example, let's say the attacker finds the following entry in a database:

user@gmail.com 5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764

They can try hashing common passwords like:

password1 ->
0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e
password2 ->
6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4
password3 -> 5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764

  
`password3` produced a matching hash! Now the attacker knows that `user@gmail.com` is likely to use the password `password3` on other sites and can go hack other accounts. This is only possible because the attacker is able to quickly compute many hashes per second and guess millions of potential passwords.

A slow KDF like Bcrypt solves this problem.

## Bcrypt Explained Step by Step

Bcrypt can be visualized with the following Go-like pseudo-code:

```go
func bcrypt(cost int, salt [16]byte, password [72]byte) (hash string) {
	// Initialize Blowfish state with expensive key setup algorithm
	// This is the slow part of the algorithm
	pEighteenSubkeys, sFourSubBoxes := expensiveBlowfishSetup(cost, salt, password)

	// Repeatedly encrypt the text "OrpheanBeholderScryDoubt" 64 times
	// 24 bytes = three 64-bit blocks
	ctext := "OrpheanBeholderScryDoubt"
	for i := 0; i < 64; i++ {
		// Encrypt using standard Blowfish in ECB mode
		ctext = encryptECB(pEighteenSubkeys, sFourSubBoxes, ctext)
	}

	// return the version, cost, salt, and ctext in the proper format
	return "$2a${cost}${salt}{ctext}"
}
```

As you can see, Bcrypt depends heavily on the [Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher)) cipher. Put simply, Bcrypt is an expensive key expansion coupled with Blowfish encryption.

The `expensiveBlowfishSetup` function can be understood by following pseudo-code:

```go
// pEighteenSubkeys: array of 18 subkeys
// sFourSubBoxes: Four substitution boxes
// Each S-Box is a 256-length array of uint32
func expensiveBlowfishSetup(cost int, salt [16]byte, password [72]byte) (pEighteenSubkeys [18]uint32, sFourSubBoxes [4][256]uint32) {
	// Initialize arrays
	pEighteenSubkeys := [18]uint32
	sFourSubBoxes := [4][256]uint32

	// Fill pEighteenSubkeys and sFourSubBoxes with the hex digits of pi 
	// This initial state works as in the original Blowfish algorithm
	// it populates the P-array and S-box entries with the fractional part of pi in hexadecimal
	pEighteenSubkeys = fillWithPi(pEighteenSubkeys)
	sFourSubBoxes = fillWithPi(sFourSubBoxes)

	// Permutate P and S based on the password and salt
	pEighteenSubkeys, sFourSubBoxes = expandKey(pEighteenSubkeys, sFourSubBoxes, salt, password)

	// This is the "Expensive" part of the "Expensive Key Setup"
	// Otherwise the key setup would be identical to Blowfish
	// Expand the key an exponentially increasing number of times
	// depending on the cost factor
	for i := 0; i < math.Pow(2, cost); i++ {
		pEighteenSubkeys, sFourSubBoxes = expandKey(pEighteenSubkeys, sFourSubBoxes, 0, password)
		pEighteenSubkeys, sFourSubBoxes = expandKey(pEighteenSubkeys, sFourSubBoxes, 0, salt)
	}

	return pEighteenSubkeys, sFourSubBoxes
}
```

`The expandKey function` is executed an exponentially increasing number of times depending on the value of the `cost` parameter. The `expandKey` function is explained by the following pseudo-code:

```go
func expandKey(pEighteenSubkeys [18]uint32, sFourSubBoxes [4][256]uint32, salt [16]byte, password [72]byte) (
	pEighteenSubkeys [18]uint32, sFourSubBoxes [4][256]uint32
	) {

	// Mix password into the pEighteenSubkeys array
	// by XORing password with subkeys
	for i := 0; i < 18; i++{
		// treat the password as cyclic, XOR 32 bit chunks of password with subkeys
		pEighteenSubkeys[i] ^= password[i % 18]
	}
 
   // Treat the 128-bit salt as two 64-bit halves 
   saltHalf[0] = salt[0:63]
   saltHalf[1] = salt[64:127]

   // Initialize an 8-byte (64-bit) buffer with all zeros.
   block := [8]byte

   // Mix internal state into P-boxes   
   for i := 0; i < 9; i++ {
	  // XOR 64-bit block with a 64-bit salt half
	  // Each iteration alternating between saltHalf[0], and saltHalf[1]
      block ^= saltHalf[(i-1) mod 2]

	  // Encrypt block using current key schedule with blowfish block encryption
	  block = Encrypt(pEighteenSubkeys, sFourSubBoxes, block)
	  
	  // Split block and use as new subkeys
      pEighteenSubkeys[2*i] = block[0:31]
	  pEighteenSubkeys[2*i + 1] = block[32:63]
   }

   // Mix encrypted state into the internal S-boxes of state
   for i := 0; i < 4; i ++ {
      for j := 0; j < 127; j++ {
		// Encrypt block using blowfish block encryption
		// where salt[i] is 64 bit chunks
        block = Encrypt(pEighteenSubkeys, sFourSubBoxes, block ^ salt[i])
        sFourSubBoxes[2*i] = block[0:31]
		sFourSubBoxes[2*i + 1] = block[32:63]
	  }
	}
    return pEighteenSubkeys, sFourSubBoxes
}
```

It helps me to visualize the details of the pseudo-code by using a more "real" programming syntax like Go. If that doesn't help you then take a look at the code on the [Wikipedia](https://en.wikipedia.org/wiki/Bcrypt#Algorithm) page here.

## Other hash function explainers

If you're looking for an explanation of a different hash function, we may have you covered

- [How SHA-2 Works Step by Step](https://qvault.io/2020/07/08/how-sha-2-works-step-by-step-sha-256/)
- [(Very) Basic Intro to the Scrypt Hash](https://qvault.io/2020/07/25/very-basic-intro-to-the-scrypt-hash/)
- [(Very) Basic Intro to Hash Functions](https://qvault.io/2020/01/01/very-basic-intro-to-hash-functions-sha-256-md-5-etc/)
