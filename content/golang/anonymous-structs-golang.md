---
title: "What Are Golang's Anonymous Structs?"
author: Lane Wagner
date: "2020-04-21"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/Golangs_Anonymous_Structs.webp
---

An anonymous struct is just like a normal struct, but it is defined *without a name* and therefore *cannot be referenced* elsewhere in the code.

Structs in Go are similar to structs in other languages like C. They have typed collections of fields and are used to group data to make it more manageable for us as programmers.

To create an anonymous struct, just instantiate the instance immediately using a second pair of brackets after declaring the type:

```go
newCar := struct {
    make    string
    model   string
    mileage int
}{
    make:    "Ford",
    model:   "Taurus",
    mileage: 200000,
}
```

Contrast this with creating a named struct type:

```go
// declare the 'car' struct type
type car struct {
    make    string
    model   string
    mileage int
}

// create an instance of a car
newCar := car{
    make:    "Ford",
    model:   "taurus",
    mileage: 200000,
}
```

If you're interested in doing a deep dive into the Go programming language, check out my ["Learn Go" course on Boot.dev](https://boot.dev/courses/learn-golang).

## When should I use an anonymous struct?

I often use anonymous structs to [marshal and unmarshal JSON data](/golang/json-golang/) in HTTP handlers. If a struct is only meant to be used once, then it makes sense to declare it in such a way that developers down the road won't be tempted to accidentally use it again.

Take a look at the code below. We can marshal the [HTTP request](https://boot.dev/courses/learn-http) directly into an unnamed struct inline. All the fields are still accessible via the dot operator, but we don't have to worry about another part of our project trying to use a type that wasn't intended for it.

```go
func createCarHandler(w http.ResponseWriter, req *http.Request) {
    defer req.Body.Close()
    decoder := json.NewDecoder(req.Body)
    newCar := struct {
        Make    string `json:"make"`
        Model   string `json:"model"`
        Mileage int    `json:"mileage"`
    }{}
    err := decoder.Decode(&newCar)
    if err != nil {
        log.Println(err)
        return
    }
    makeCar(newCar.Make, newCar.Model, newCar.Mileage)
    return
}
```

### Don't use `map[string]interface{}` for JSON data if you can avoid it.

Instead of declaring a quick anonymous struct for JSON unmarshalling, I've often seen `map[string]interface{}` used. This is *terrible* in most scenarios for several reasons:

1. **No type checking.** If the client sends a key called "name" with a `bool` value, but your code is expecting a `string`, then unmarshalling into a map won't catch the error
2. **Maps are vague.** After unmarshalling the data, we are forced to use runtime checks to make sure the data we care about exists. If those checks aren't thorough, it can lead to a nil pointer dereference panic being thrown.
3. **`map[string]interface{}` is verbose**. Digging into the map isn't as simple as accessing a named field using a dot operator, for example, `newCar.model`. Instead, it is something like:

```go
func createCarHandler(w http.ResponseWriter, req *http.Request) {
    myMap := map[string]interface{}{}
    decoder := json.NewDecoder(req.Body)
    err := decoder.Decode(&myMap)
    if err != nil {
        log.Println(err)
        return
    }
    model, ok := myMap["model"]
    if !ok {
        fmt.Println("field doesn't exist")
        return
    }
    modelString, ok := model.(string)
    if !ok {
        fmt.Println("model is not a string")
    }
    // do something with model field
}
```

Anonymous structs can clean up your API handlers if used properly. The strong typing they offer while still being a "one-off" solution is a powerful tool.

## Bonus - Use a slice of anonymous structs for easy test data

Anonymous structs are great for writing [table driven tests](https://dave.cheney.net/2019/05/07/prefer-table-driven-tests).

```go
var cars = []struct {
    make string
    model string
    topSpeed 
}{
    {"toyota", "camry", 100},
    {"tesla", "model 3", 250},
    {"ford", "focus", 120},
}
```

## Bonus #2 - Group a set of global (gasp) variables in a struct

```go
var apiSettings struct {
    secret      string
    dbConn   string
}

apiSettings.secret = "super-secr3t-p@$$"
```
