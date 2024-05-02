---
title: "How to Use Mutexes in Go"
author: Lane Wagner
date: "2020-03-19"
categories: 
  - "golang"
images:
  - /img/800/How to use Mutexes.webp
---

Golang is King when it comes to concurrency. No other language has so many tools right out of the box, and one of those tools is the standard library's [sync.Mu](https://golang.org/pkg/sync/)[t](https://golang.org/pkg/sync/)[ex{}](https://golang.org/pkg/sync/). Mutexes let us safely control access to data across multiple goroutines.

## What problem do mutexes solve?

We don't want multiple threads accessing the same memory at the same time. In concurrent programming, we have many different threads (or in Go, [goroutines](/rust/concurrency-in-rust-can-it-stack-up-against-gos-goroutines/)) that all potentially have access to the same variables in memory.

One case that mutexes help us avoid is the **concurrent read/write problem**. This occurs when one thread is writing to a variable while another variable is concurrently reading from that same variable. The program will panic because the reader could be reading bad data that is being mutated in place.

## What is a mutex?

Mutex is short for _mutual exclusion_. Mutexes keep track of which thread has access to a variable at any given time.

![mutex diagram](/img/800/download.png)

Let's see some examples! Consider the following program:

```go
package main

import (
	"fmt"
)

func main() {
	m := map[int]int{}
	go writeLoop(m)
	go readLoop(m)

	// stop program from exiting, must be killed
	block := make(chan struct{})
	<-block
}

func writeLoop(m map[int]int) {
	for {
		for i := 0; i < 100; i++ {
			m[i] = i
		}
	}
}

func readLoop(m map[int]int) {
	for {
		for k, v := range m {
			fmt.Println(k, "-", v)
		}
	}
}
```

The program creates a map, then starts two goroutines which each have access to that same map. One goroutine continuously mutates the values stored in the map, while the other prints the values it finds in the map.

If we run the program, we get the following output:

```
fatal error: concurrent map iteration and map write
```

In Go, it isn't safe to read from and write to the same map at the same time.

## Mutexes to the rescue

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	m := map[int]int{}

	mux := &sync.Mutex{}

	go writeLoop(m, mux)
	go readLoop(m, mux)

	// stop program from exiting, must be killed
	block := make(chan struct{})
	<-block
}

func writeLoop(m map[int]int, mux *sync.Mutex) {
	for {
		for i := 0; i < 100; i++ {
			mux.Lock()
			m[i] = i
			mux.Unlock()
		}
	}
}

func readLoop(m map[int]int, mux *sync.Mutex) {
	for {
		mux.Lock()
		for k, v := range m {
			fmt.Println(k, "-", v)
		}
		mux.Unlock()
	}
}
```

In the code above we create a `sync.Mutex{}` and [name it mux](/clean-code/naming-variables/). In the write loop, we `Lock()` the mutex before writing, and `Unlock()` it when we're done. This ensures that no other threads can `Lock()` the mutex while we have it locked - those threads will block and wait until we `Unlock()` it.

In the reading loop we `Lock()` before iterating over the map, and likewise `Unlock()` when we're done.

## What is a read/write mutex, or RWMutex?

Maps are safe for concurrent read access, just not concurrent read/write or write/write access. A read/write mutex allows all readers to access the map at the same time, but a writer will lock out everyone else.

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	m := map[int]int{}

	mux := &sync.RWMutex{}

	go writeLoop(m, mux)
	go readLoop(m, mux)
	go readLoop(m, mux)
	go readLoop(m, mux)
	go readLoop(m, mux)

	// stop program from exiting, must be killed
	block := make(chan struct{})
	<-block
}

func writeLoop(m map[int]int, mux *sync.RWMutex) {
	for {
		for i := 0; i < 100; i++ {
			mux.Lock()
			m[i] = i
			mux.Unlock()
		}
	}
}

func readLoop(m map[int]int, mux *sync.RWMutex) {
	for {
		mux.RLock()
		for k, v := range m {
			fmt.Println(k, "-", v)
		}
		mux.RUnlock()
	}
}
```

By using a [sync.RWMutex](https://golang.org/pkg/sync/#RWMutex), our program becomes more efficient. We can have as many readers as we want to access our data, but at the same time can assure that writers have exclusive access.
