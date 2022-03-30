---
title: "JWT Authentication in Golang"
author: Lane Wagner
date: "2020-02-20"
categories: 
  - "cryptography"
  - "golang"
  - "security"
images:
  - /img/logo-400.webp
---

Go is becoming very popular for backend web development, and JWT's are one of the most popular ways to handle authentication on API requests. In this article, we'll go over the basics of JWT's and how to implement a secure authentication strategy in Go!

## What is a JWT?

> JSON Web Tokens are an open, industry-standard [RFC 7519](https://tools.ietf.org/html/rfc7519) method for representing claims securely between two parties.
> 
> [https://jwt.io/](https://jwt.io/)

More simply put, JWT's are [encoded JSON objects](https://qvault.io/golang/json-golang/) that have been signed by the server, verifying authenticity.

For example, when a user logs in to a website secured via JWTs, the flow should look something like this:

1. The user sends a username and password to the server
2. The server verifies username and password are correct
3. The server creates a JSON object (also known as the "claims") that looks something like this:
    1. `{"username":"wagslane"}`
4. The server [encodes](https://qvault.io/2019/08/14/stop-with-the-obfuscation-encoding-and-encryption-are-not-the-same/) and [signs](https://qvault.io/2019/12/12/hmac-and-mac-explained-simply-building-secure-auth-with-jwts/) the JSON object, creating a JWT:
    1. `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndhZ3NsYW5lIn0.ov6d8XtwQoKUwsYahk9UwH333NICElFSs6ag6pINyPQ`
5. The user's web client saves the JWT for later use
6. When the user makes a request to a protected endpoint, it passes the JWT along in an HTTP header
7. The server checks the signature on the JWT to make sure the JWT was originally created by the same server
8. The server reads the claims and gives permission to the request to operate as "wagslane"

## Create a JWT

We're going to use a popular library for dealing with JSON Web Tokens in Go, [jwt-go](https://github.com/dgrijalva/jwt-go). Make sure you have the code cloned locally:

```bash
go get github.com/dgrijalva/jwt-go
```

For simplicity, we're going to use a symmetric encryption scheme. If you go this route, it just means that any server that can verify that a JWT is valid will also be allowed to issue new JWTs.

First, define a struct that will be used to represent claims to identify your users:

```go
type customClaims struct {
	Username string `json:"username"`
	jwt.StandardClaims
}
```

The `jwt.StandardClaims` struct contains useful fields like `expiry` and `issuer name`. Now we'll create some actual claims for the user that just logged in:

```go
claims := customClaims{
	Username: username,
	StandardClaims: jwt.StandardClaims{
		ExpiresAt: 15000,
		Issuer:    "nameOfWebsiteHere",
	},
}
```

Next let's create an unsigned token from the claims:

```go
token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
```

Then we sign the token using a secure private key. In production make sure you use a real private key, preferably at least 256 bits in length:

```go
signedToken, err := token.SignedString([]byte("secureSecretText"))
```

Finally, the signed token can be sent back to the client.

## Validating a JWT

When the client makes a request to a protected endpoint we can verify the JWT is authentic using the following steps.

\*Note: It's idiomatic to use the `Authorization` HTTP header:

```
Authorization: Bearer {jwt}
```

After receiving the JWT, validate the claims and verify the signature using the same private key:

```go
token, err := jwt.ParseWithClaims(
	jwtFromHeader,
	&customClaims{},
	func(token *jwt.Token) (interface{}, error) {
		return []byte("secureSecretText"), nil 
	},
)
```

If the claims have been tampered with then the `err` variable will not be `nil`.

Parse the claims from the token:

```go
claims, ok := token.Claims.(*customClaims)
if !ok {
	return errors.New("couldn't parse claims")
}
```

Check if the token is expired:

```go
if claims.ExpiresAt < time.Now().UTC().Unix() {
	return errors.New("jwt is expired")
}
```

You now know the username of the authenticated user!

```go
username := claims.Username
```

For full examples take a look at the package's [tests](https://github.com/dgrijalva/jwt-go/blob/master/example_test.go). Let me know if I missed anything by hitting me up on [Twitter](https://twitter.com/wagslane)!
