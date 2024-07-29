---
title: "Authenticate Users with \"Sign In With Google\" in Golang"
author: Lane Wagner
date: "2020-07-22"
categories: 
  - "golang"
images:
  - /img/800/Screen-Shot-2020-07-20-at-3.webp
---

Users love convenience. If your goal is to make it easy for users to register with your app or website, then implementing the "Sign in with Google" option should be at the top of your priority list. If you are like me, then you may find Google's documentation on the subject to be lackluster at best, and downright confusing at worst. Here we will go step-by-step through the authentication process so you can implement Google sign-in easily.

## Front-End Stuff

We aren't going to focus on the front-end part of the authentication process because that's the easy part. That said, for any of this to make sense we will briefly touch on how it works.

The front-end's job is to do some redirect OAuth magic to obtain a [JWT](/golang/jwts-in-golang/) signed by Google. This is accomplished by [including Google's SDK](https://developers.google.com/identity/sign-in/web/sign-in#load_the_google_platform_library) in your HTML, [making an application](https://developers.google.com/identity/sign-in/web/sign-in#create_authorization_credentials) in GCP, and [creating a button](https://developers.google.com/identity/sign-in/web/sign-in#add_a_google_sign-in_button) using the proper class. I would recommend following [Google's quick tutorial](https://developers.google.com/identity/sign-in/web/sign-in) to get this working.

Once you are done with all that, you should have a button on your web page. When a user clicks on the button and authorizes their Google account, you will get a [JWT](https://developers.google.com/identity/sign-in/web/sign-in#get_profile_information) back in the `onSignIn` callback function:

```js
function onSignIn(googleUser) {
  const googleJWT = googleUser.getAuthResponse().id_token
}
```

All we care about is that JWT. We are going to create a backend function in Go that receives the JWT and ensures it's validity before allowing the user to login to our app.

## Validation Function

Let's build a single function that validates JWT's from Google. It has the following function signature:

```go
// ValidateGoogleJWT -
func ValidateGoogleJWT(tokenString string) (GoogleClaims, error) {

}
```

`ValidateGoogleJWT` takes a JWT string (that we get from the front-end) and returns the validated `GoogleClaims` struct if the JWT passes our checks. Otherwise, we will return an error explaining what went wrong.

## Claims

JWT's are just [JSON objects](/golang/json-golang/) that are signed with a private key to ensure they haven't been tampered with. The signed JSON object's fields are referred to as "claims". We will be using the most popular JWT library in Go to build our solution: [https://github.com/golang-jwt/jwt](https://github.com/golang-jwt/jwt), and the claims that Google sends have the following shape:

```go
// GoogleClaims -
type GoogleClaims struct {
	Email         string `json:"email"`
	EmailVerified bool   `json:"email_verified"`
	FirstName     string `json:"given_name"`
	LastName      string `json:"family_name"`
	jwt.StandardClaims
}
```

## Google's Public Key

Google hosts their public key over HTTPS. Each time we need to verify a request we can go grab their public key as follows:

```go
func getGooglePublicKey(keyID string) (string, error) {
	resp, err := http.Get("https://www.googleapis.com/oauth2/v1/certs")
	if err != nil {
		return "", err
	}
	dat, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	myResp := map[string]string{}
	err = json.Unmarshal(dat, &myResp)
	if err != nil {
		return "", err
	}
	key, ok := myResp[keyID]
	if !ok {
		return "", errors.New("key not found")
	}
	return key, nil
}
```

The keyID is in the JWT header under the `kid` field. If you are confused, don't worry, it will make sense in the next section.

## Complete Validation Function

Now that we have our claims structure and a way to fetch Google's public key we can finish our validation function:

```go
// ValidateGoogleJWT -
func ValidateGoogleJWT(tokenString string) (GoogleClaims, error) {
	claimsStruct := GoogleClaims{}

	token, err := jwt.ParseWithClaims(
		tokenString,
		&claimsStruct,
		func(token *jwt.Token) (interface{}, error) {
			pem, err := getGooglePublicKey(fmt.Sprintf("%s", token.Header["kid"]))
			if err != nil {
				return nil, err
			}
			key, err := jwt.ParseRSAPublicKeyFromPEM([]byte(pem))
			if err != nil {
				return nil, err
			}
			return key, nil
		},
	)
	if err != nil {
		return GoogleClaims{}, err
	}

	claims, ok := token.Claims.(*GoogleClaims)
	if !ok {
		return GoogleClaims{}, errors.New("Invalid Google JWT")
	}

	if claims.Issuer != "accounts.google.com" && claims.Issuer != "https://accounts.google.com" {
		return GoogleClaims{}, errors.New("iss is invalid")
	}

	if claims.Audience != "YOUR_CLIENT_ID_HERE" {
		return GoogleClaims{}, errors.New("aud is invalid")
	}

	if claims.ExpiresAt < time.Now().UTC().Unix() {
		return GoogleClaims{}, errors.New("JWT is expired")
	}

	return *claims, nil
}
```

Make sure that you have your client id (the one you used on your front-end that you got from GCP) set here in the backend as well.

If the function returns without an error then you have a struct containing a valid email, first name, and last name, all collected and verified by Google! In your login HTTP handler, you can return a valid cookie or JWT of your own that you use to identify logged-in users on your site. For example:

```go
func (cfg config) loginHandler(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()

	// parse the GoogleJWT that was POSTed from the front-end
	type parameters struct {
		GoogleJWT *string
	}
	decoder := json.NewDecoder(r.Body)
	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 500, "Couldn't decode parameters")
		return
	}

	// Validate the JWT is valid
	claims, err := auth.ValidateGoogleJWT(*params.GoogleJWT)
	if err != nil {
		respondWithError(w, 403, "Invalid google auth")
		return
	}
	if claims.Email != user.Email {
		respondWithError(w, 403, "Emails don't match")
		return
	}

	// create a JWT for OUR app and give it back to the client for future requests
	tokenString, err := auth.MakeJWT(claims.Email, cfg.JWTSecret)
	if err != nil {
		respondWithError(w, 500, "Couldn't make authentication token")
		return
	}

	respondWithJSON(w, 200, struct {
		Token string `json:"token"`
	}{
		Token: tokenString,
	})
}
```

Let me know if this guide can be improved or if you have any questions. This is _roughly_ the process that we use at [boot.dev](https://boot.dev/) and it has worked well for us.
