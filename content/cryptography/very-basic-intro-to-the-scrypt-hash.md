---
title: "(Very) Basic Intro to the Scrypt Hash"
date: "2020-07-25"
categories: 
  - "cryptography"
  - "security"
---

Scrypt is a slow-by-design [key derivation function](https://qvault.io/2019/12/30/very-basic-intro-to-key-derivation-functions-argon2-scrypt-etc/) designed to create strong cryptographic keys. Simply put, the purpose of the Scrypt hash is to create a fingerprint of its input data but to do it _very slowly_. A common use-case is to create a strong private key from a password, where the new private key is longer and more secure. Here at [Qvault,](https://qvault.io) we use a similar KDF for securing user passwords.

Let's pretend your password is `password1234`. By using Scrypt, we can extend that deterministically into a 256-bit key:

```
password1234 -> 
AwEEDA4HCwQFAA8DAwwHDQwPDwUOBwoOCQACAgUJBQ0JAAYNBAMCDQ4JCQgLDwcGDQMDDgMKAQsNBAkLAwsACA==
```

That long 256-bit key can now be used as a private key to encrypt and decrypt data. For example, it could be the key in an [AES-256](https://qvault.io/2020/01/02/very-basic-intro-to-aes-256-cipher/) cipher.

Some cryptocurrencies, like [Litecoin](https://litecoin.org/), use Scrypt as their proof-of-work algorithm due to how slow and memory-intensive the key derivation process is. By using a slower and more memory-intensive algorithm, it's harder for engineers to create specialized hardware (ASICs) to mine the coin.

## Other [hash function](https://qvault.io/2020/01/01/very-basic-intro-to-hash-functions-sha-256-md-5-etc/) explainers

Before we move on, if you're looking for an explanation of a different hash function, we may have you covered

- [SHA-2 Hash Step by Step](https://qvault.io/2020/07/08/how-sha-2-works-step-by-step-sha-256/)
- [Bcrypt Step by Step](https://qvault.io/2020/08/24/bcrypt-step-by-step/)
- [(Very) Basic Intro to Hash Functions](https://qvault.io/2020/01/01/very-basic-intro-to-hash-functions-sha-256-md-5-etc/)

## Why Not Encrypt With The Password Directly?

Most encryption algorithms, including AES-256, require that a key of sufficient length is used. By hashing the password, we can derive a longer, more secure, fixed-size key.

Furthermore, using a KDF like Scrypt provides additional benefits over a traditional hash function like [SHA-2](https://qvault.io/2020/07/08/how-sha-2-works-step-by-step-sha-256/):

- Computationally expensive and slow
- Memory intensive (potentially several gigabytes of RAM is used to execute the hash)

Often times [brute-force attackers](https://qvault.io/2020/02/11/how-do-brute-force-attackers-know-they-found-the-key/) will try to break encryption by guessing passwords over and over until they get it right. AES-256 and SHA-2 are fast, so an attacker would be able to guess many passwords per second. By using a slow hashing function like Scrypt to derive a key, we can force the attacker to waste more resources trying to break in.

## Scrypt Step-by-Step

Scrypt can be visualized by some psuedo-code:

```
func Scrypt(
	passphrase, // string of characters to be hashed
	salt,  // random salt
	costFactor, // CPU/Memory cost, must be power of 2
	blockSizeFactor,
	parallelizationFactor, // (1..232-1 * hLen/MFlen)
	desiredKeyLen // Desired key length in bytes
) derivedKey {
	// we'll get to this
}
```

Let's go through the steps of converting those inputs into the desired `derivedKey`

### 1 - Define Blocksize

```
const blockSize = 128 * blockSizeFactor
```

### 2 - Generate Initial Salt

Scrypt uses [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) as a child key-derivation function. We use it to generate an initial salt. `PBKDF2` has the following signature:

```
func PBKDF2(
	prf,
	password,
	salt,
	numIterations,
	desiredKeyLen
) derivedKey {}
```

We use it as follows:

```
const initialSalt = PBKDF2(HMAC-SHA256, passphrase, salt, 1, blockSize * parallelizationFactor)
```

### 3 - Mix Salt

Next, we mix the salt. We split `initialSalt` into `splitSalt`, which is a 2D array of bytes. Each sub-array contains 1024 bytes

```
splitSalt := [][1024]byte(initialSalt)
for i, block := range splitSalt {
	newBlock := roMix(block, costFactor)
	splitSalt[i] = newBlock
}
```

Where `roMix` is the following function:

```
func roMix(block, iterations){
	v := []
	x := block
	for i := 0; i < iterations; i++ {
		v[i] = x
		x = blockMix(x)
	}
	for i := 0; i < iterations; i++ {
		j := integerify(x) % iterations
		x = blockMix(x ^ v[j])
	}
	return x
}
```

`integerify` is defined by [RFC-7914](https://tools.ietf.org/html/rfc7914) and `blockMix` is:

```
func blockMix(block){
	r := len(block) / 128
	// split block into an array of 2r 64-byte chunks
	chunks := get2r64ByteChunks()

	x := chunks[len(chunks)-1]
	y := []
	for i := 0; i < len(chunks); i++{
		x = salsa20-8(x ^ chunks[i])
		y[i] = x
	}
	return [y[0], y[2], ...y[2r-2], y[1], y[3], ...y[2r-1]]
}
```

`salsa20-8` is the 8-round version of the algorithm defined [here](https://en.wikipedia.org/wiki/Salsa20).

### 4 - Finalize Salt

Now `splitSalt` has been mixed in such a computationally exhausting way that we will call it an `expensiveSalt`. Expensive salt will be a single array of bytes, so we need to [concatenate](https://qvault.io/golang/strings-builder-concatenation-golang/) all the subarrays in `splitSalt`.

```
expensiveSalt := append([], splitSalt...)
```

### 5 - Return Final KDF

```
return PBKDF2(HMAC-SHA256, passphrase, expensiveSalt, 1, desiredKeyLen)
```

The final pseudocode for our top level function is as follows:

```
func Scrypt(
	passphrase, // string of characters to be hashed
	salt,  // random salt
	costFactor, // CPU/Memory cost, must be power of 2
	blockSizeFactor,
	parallelizationFactor, // (1..232-1 * hLen/MFlen)
	desiredKeyLen // Desired key length in bytes
) derivedKey {
	const blockSize = 128 * blockSizeFactor

	const initialSalt = PBKDF2(HMAC-SHA256, passphrase, salt, 1, blockSize * parallelizationFactor)

	splitSalt := [][1024]byte(initialSalt)
	for i, block := range splitSalt {
		newBlock := roMix(block, costFactor)
		splitSalt[i] = newBlock
	}

	expensiveSalt := append([], splitSalt...)

	return PBKDF2(HMAC-SHA256, passphrase, expensiveSalt, 1, desiredKeyLen)
}
```

Or, if you prefer, the pseudocode as defined by [Wikipedia](https://en.wikipedia.org/wiki/Scrypt):

```
Function scrypt
   Inputs:
      Passphrase:                Bytes    string of characters to be hashed
      Salt:                      Bytes    random salt
      CostFactor (N):            Integer  CPU/memory cost parameter - Must be a power of 2 (e.g. 1024)
      BlockSizeFactor (r):       Integer  blocksize parameter (8 is commonly used)
      ParallelizationFactor (p): Integer  Parallelization parameter. (1..232-1 * hLen/MFlen)
      DesiredKeyLen:             Integer  Desired key length in bytes
   Output:
      DerivedKey:                Bytes    array of bytes, DesiredKeyLen long

   Step 1. Generate expensive salt
   blockSize ← 128*BlockSizeFactor  //Length (in bytes) of the SMix mixing function output (e.g. 128*8 = 1024 bytes)

   Use PBKDF2 to generate initial 128*BlockSizeFactor*p bytes of data (e.g. 128*8*3 = 3072 bytes)
   Treat the result as an array of p elements, each entry being blocksize bytes (e.g. 3 elements, each 1024 bytes)
   [B0...Bp−1] ← PBKDF2HMAC-SHA256(Passphrase, Salt, 1, blockSize*ParallelizationFactor)

   Mix each block in B Costfactor times using ROMix function (each block can be mixed in parallel)
   for i ← 0 to p-1 do
      Bi ← ROMix(Bi, CostFactor)

   All the elements of B is our new "expensive" salt
   expensiveSalt ← B0∥B1∥B2∥ ... ∥Bp-1  //where ∥ is concatenation
 
   Step 2. Use PBKDF2 to generate the desired number of bytes, but using the expensive salt we just generated
   return PBKDF2HMAC-SHA256(Passphrase, expensiveSalt, 1, DesiredKeyLen);
```
