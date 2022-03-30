---
title: "Range Over Ticker In Go With Immediate First Tick"
author: Lane Wagner
date: "2020-04-30"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/Profile_-_Tick_Toc_Croc.webp
---

The Go standard library has a really cool type - [Ticker](https://gobyexample.com/tickers). Tickers are used when you want to do something at a regular interval, similar to JavaScript's [setInterval](https://www.w3schools.com/jsref/met_win_setinterval.asp). Here's an example:

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.NewTicker(time.Second)
	go func() {
		for range ticker.C {
			fmt.Println("Tick")
		}
	}()

	time.Sleep(time.Second * 4)
	ticker.Stop()
	fmt.Println("Ticker stopped")
}
```

As per the [docs](https://golang.org/pkg/time/#Ticker), a ticker is a struct that holds a receive-only channel of [time.Time objects](https://qvault.io/golang/golang-date-time/).

```go
type Ticker struct {
    C <-chan Time // The channel on which the ticks are delivered.
}
```

In the example at the beginning of the article, you will notice by running the program that the first tick sent over the channel happens **after** the first interval of time has elapsed. As such, if you are trying to build, for example, a rate limiter, it can be inconvenient because to get the first immediate execution, it would seem your best option is:

```go
func doSomethingWithRateLimit() {
	ticker := time.NewTicker(time.Second)
	doSomething()
	for range ticker.C {
		doSomething()
	}
}
```

There is in fact a better option!

In Go, a channel can also be iterated over in a normal [for-loop](https://qvault.io/golang/golang-for-loop/), so our solution is to build a for loop that executes automatically on the first iteration, then waits for each subsequent loop.

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.NewTicker(time.Minute)
	for ; true; <-ticker.C {
		fmt.Println("hi")
	}
}
```

Hopefully this helps keep redundant code out of your projects!
