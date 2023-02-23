---
title: "Golang Conversions - Ints To Strings And Strong Typing"
author: Lane Wagner
date: "2020-03-31"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/photo-1500589177368-c810ea3db799.jpeg
---

Go is a strongly typed language, which means at any point a developer should know exactly what **type** of value they are dealing with. For example, if we have a function that prints a string, we can't just give it an integer and expect it to work. We have to cast it to a string explicitly:

```go
func main() {
	num := 5
	numString := strconv.Itoa(num)
	printString(numString)
}

func printString(s string) {
	fmt.Println(s)
}
```

If we don't cast the value, the go compiler won't even let us compile the program.

## Dynamic Typing is Slow

Developers coming from dynamically typed languages often get annoyed with Go's strong typing. They think that the compiler should just _know what they mean_ and do the type cast implicitly. Strongly typed languages won't guess for you. They make you make the decisions.

There is a reason for this. Type conversions take time and resources. If the Go runtime were to dynamically type every value then programs would run a lot slower in general. If you want slow programs then go back to Python or Javascript.

## Strong Typing Is Explicit

In addition to strong typing being faster, strong typing allows the developer to know exactly what type of value they are dealing with. I can't tell you how many times in Python I've had to run a program and print out what type of object something is. (Looking at you NumPy)

## Strong Typing Saves Memory

![red floppy disk](https://i0.wp.com/boot.dev/wp-content/uploads/2020/03/photo-1533279443086-d1c19a186416.jpeg?fit=742%2C417&ssl=1)

In one of our production apps, we were storing millions of **ints** in memory. Being on 64-bit machines, this means that we were storing 64 bits for each integer when in reality the integer stored was never greater than 10. By swapping out **ints** for **uint8s** we saved 80% of the memory that our application was using. The guy paying our cloud bill was quite happy about that.

While changing int and float types can save memory, beware of these kinds of optimizations. A program can become quite hard to read if every other line is:

```go
toRound := float64(someNumber)
toSave := float32(toRound)
```

The truth is that most of the standard library functions and popular packages (and hopefully the stuff you write too) uses "default" sizes. For example, [math.Round](https://golang.org/pkg/math/#Round) uses `float64`s and [time.AddDate](https://golang.org/pkg/time/#Time.AddDate) uses `int`s. Unless the memory savings are significant, it's usually best to stick with "normal".

{{< cta1 >}}

{{< cta2 >}}

## Interfaces - Not Duck Types

Interfaces allow for a kind of [polymorphism in Go](/golang/golang-interfaces/). Their purpose is **not** to give developers a way to sneak dynamic typing into the language. I've seen developers do things like:

```go
func jsonToDynamic(dat []byte) {
	m := map[string]interface{}{}
	json.Unmarshal(dat, &m)
	// do something with m["hello"]
}
```

I humbly ask... why? [When unmarshalling JSON](/golang/json-golang/), 99% of the time we should know the shape of the object. If we know the shape of the object, then we should unmarshal into a struct where each field's type is declared. We will even get a nice unmarshal error if the shape is malformed.
