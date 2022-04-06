---
title: "Naming Variables the Right Way"
author: Lane Wagner
date: "2021-04-01"
categories: 
  - "clean-code"
images:
  - /img/yelling-at-computer.webp
---

I've noticed that bugs introduced into an existing code base are often due to poor variable naming more than one might suspect. For example, a developer uses a `rateLimit` variable expecting it to be denominated in _seconds_ while it really represents _minutes_, resulting in a 6x slower schedule. Another developer expects `dbConnection` to be an open database connection, but instead, it's just the connection URI.

Using descriptive, concise, and conventional variable names often set apart a senior from a junior developer. Here are some of my rules of thumb for high-quality variable nomenclature.

- [1\. Following existing naming conventions of the language or framework you're using](#1-following-existing-naming-conventions-of-the-language-or-framework-youre-using)
- [2\. Single letter variables have a place, and that place is rare](#2-single-letter-variables-have-a-place-and-that-place-is-rare)
- [3\. Include units in your variable names](#3-include-units-in-your-variable-names)
- [4\. Include types in your variables names if it isn't obvious](#4-include-types-in-your-variables-names-if-it-isnt-obvious)
- [5\. Make variables names as long as necessary but no longer](#5-make-variables-names-as-long-as-necessary-but-no-longer)
- [6\. Include the meaning of complex calculations in your variable names](#6-include-the-meaning-of-complex-calculations-in-your-variable-names)
- [7\. Use the properly pluralized form of the variable](#7-use-the-properly-pluralized-form-of-the-variable)
- [8\. Don't use abbreviations or acronyms without sufficient context](#8-dont-use-abbreviations-or-acronyms-without-sufficient-context)
- [9\. No magic numbers or magic values, use a variable](#9-no-magic-numbers-or-magic-values-use-a-variable)

### 1\. Following existing naming conventions of the language or framework you're using

Different languages and frameworks (and the communities that use them) typically have a standard way of styling variable and function names. For example, in Python and Ruby it's preferred to style variables and fields using snake case.

```py
# python snake-case styling
my_num = 15
```

In Java, Go, or JavaScript it's preferred to use mixed-case, also known as "camel case" styling.

```java
// Java camel case styling
int myNum = 15;
```

Don't mix styles! The only thing worse than ignoring popular convention is inconsistency. If you think your way is better _that's okay_, just make sure to enforce it across your entire codebase. Don't be afraid to use static analysis tools to enforce your linting rules! Eslint, `go fmt`, and [black](https://github.com/psf/black) are all great options depending on your language of choice.

Special mention: SQL is its own language, and databases have their own naming conventions. Just because you're working in Java, doesn't mean your table names should be camel case! Use the conventions of the technology.

### 2\. Single letter variables have a place, and that place is rare

Single letter variables make sense in [loops](/golang/golang-for-loop/), and in scopes that are ~5 lines long. The obvious examples are `i`, `j`, and `k` for nested iterations, and `k` and `v` for keys and values in map or dictionary iterations. That said, again, err on the side of being _descriptive_. If you're iterating over rows and columns in a matrix, it might be a lot easier to keep track of if you make the variables a bit longer.

```py
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    # do stuff
```

The problem with the code above is that if I get way down into the body of that nested loop, I may forget if `i` represents the index of a _row_ or the index of a _column_. To avoid confusion, the author of the loop could easily add some more context.

```py
for row_i in range(len(matrix)):
  row = matrix[row_i]
  for column_i in range(len(row)):
    # do stuff
```

### 3\. Include units in your variable names

I've happened across many bugs that were a result of units not being included in the name of the variable. For example, someone might be storing the maximum rate at which an application can make requests to the Twitter API. Let's take a look at what this could potentially look like in Go.

```go
rateLimit := os.Getenv("RATE_LIMIT")
rateLimitNum, err := strconv.Atoi(rateLimit)
if err != nil {
    log.Fatal(err)
}
ticker := time.NewTicker(rateLimitNum * time.Millisecond)
for range ticker.C {
    // do stuff each time the rate limit elapses
}
```

The problem here lies in the ambiguity. At any point, a developer is prone to making a mistake about the units in the `rateLimit`. Even in the environment, it's just called `RATE_LIMIT`. In this example, it's fairly easy to tell that the unit in question is milliseconds, but what if we need to pass around the variable through a few functions or files before it gets used?

Here's a much better solution.

```go
twitterRequestsPerSecondString := os.Getenv("TWITTER_REQUESTS_PER_SECOND")
twitterRequestsPerSecond, err := strconv.Atoi(twitterRequestsPerSecondString)
if err != nil {
    log.Fatal(err)
}
ticker := time.NewTicker(twitterRequestsPerSecond * time.Second)
for range ticker.C {
    // do stuff each time the rate limit elapses
}
```

### 4\. Include types in your variables names if it isn't obvious

In strongly-typed languages like Go and Java, this is less of a problem. Occasionally it makes sense if you need to cast a variable with the same value from one type to another, but mostly you can ignore this tip in typed languages. If you are casting, however, I would recommend having the more usable value be the one you strip the type from.

```go
twitterRequestsPerSecondString:= os.Getenv("TWITTER_REQUESTS_PER_SECOND")
// twitterRequestsPerSecondString = "42" string

twitterRequestsPerSecond, _ := strconv.Atoi(twitterRequestsPerSecondString
// twitterRequestsPerSecond = int 42
```

If you're in a dynamically-typed language like JavaScript or Python you need to be a lot more careful about the names you use to describe variables. Ideally, the name implies the type of variable it is.

- Boolean values should imply binary options. For example, prefer `isLarge = true` over `large = true`. Prefer `canRead = true` over `readPermissions = true`.
- Don't hesitate to use `num`, `min`, `max`, `total` or `count` in variable names for clarity. For example `num_cars = 5` is better than `cars = 5`.
- With arrays, imply the type contained in the array. For example, `fruits` could be an array like `["apple", "banana", "plum"]`, but it could just as easily be an array of _objects_ that describe fruits and their metadata. If it's just strings, imply it: `fruitNames = ["apple", "banana", "plum"]`.

### 5\. Make variables names as long as necessary but no longer

The most common mistake newer developers make in my opinion is erring on the side of shorter variable names. If anything, err on the side of making them longer and more descriptive. That said, if you make them insanely long it can have the opposite effect. Variables names that are too long result in lines of code that extend far off the screen, making the cognitive load of reading and digesting the code much heavier.

Let's take a look at some examples of how to name variables in Python.

```go
conn = psycopg2.connect(postgres_connection_string)
```

You may look at this code and think that it's obvious enough what's going on. A connection to a Postgres database is opened and stored in the `conn` variable. This might make it look worse:

```go
conn = psycopg2.connect(postgres_connection_string)
conn2 = rabbitmq.connect(rabbitmq_connection_string)
```

Because we weren't specific about the kind of connection that was opened, creating new connections gets tricky. A much better solution would be to use a longer and more descriptive name like `pg_connection`. You may have multiple Postgres servers in your stack, in which case you might want to include the name of the server. For example, if the server were named `Pluto`, it could be `pg_connection_pluto`.

### 6\. Include the meaning of complex calculations in your variable names

If you need to do even rudimentary algebra in your code, be sure to document why you're doing it and what each entity means. For example, say you need to get the `y` value of a point on a line. You could just do:

```go
const y = m * x + b
```

If the next dev is familiar with this formula for modeling lines, you'll be fine. That said, make it easier on them by using descriptive variables and [adding in a comment](/clean-code/code-comments/) to explain the math.

```go
// slope-intercept formula
// y = mx + b
const targetY = slope * point.x + yIntercept
```

### 7\. Use the properly pluralized form of the variable

Don't do this:

```py
name = ["lane", "cameron", "lyric", "breanna"]
for n in name:
  print(n)
```

Pluralize it.

```py
names = ["lane", "cameron", "lyric", "breanna"]
for name in names:
  print(names)
```

### 8\. Don't use abbreviations or acronyms without sufficient context

Don't shorten names unless you really need to. It really only makes sense if the variable name is already super long. For example, `con` is a popular abbreviation for a network connection, but it could also mean a drawback (pro vs con), or the [end of an array](https://en.wikipedia.org/wiki/Cons). If you're using it in a longer name with more context it's probably okay to abbreviate, but if not, then just use the full word.

- Bad: `conn`
- Better: `pluto_postgres_conn`
- Bad: `idx`
- Better: `index`

### 9\. No magic numbers or magic values, use a variable

Don't omit variable names by throwing seemingly arbitrary numbers or strings into your code.

Bad:

```go
sleepTime := time.Second
for {
  // do stuff
  sleepTime *= 2
}
```

Better:

```go
sleepTime := time.Second
for {
  // do stuff
  const backoffMultiplier = 2
  sleepTime *= backoffMultiplier
}
```
