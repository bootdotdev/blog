---
title: "Go's WaitGroup vs JavaScript's PromiseAll"
author: Lane Wagner
date: "2020-06-04"
categories: 
  - "golang"
  - "javascript"
images:
  - /img/the-11-types-of-people-you-find-waiting-in-line-2-5580-1395413282-13_dblbig.webp
---

In applications that are i/o heavy, it can get clunky to synchronously execute high-latency functions one after the other. For example, if I have a web page that needs to request seven files from the server before it can show the page, I need to asynchronously fetch all those files at the same time. The alternative of making each request one at a time will take much too long. This is where JavaScript's [PromiseAll](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) and Go's [WaitGroup](https://golang.org/pkg/sync/#WaitGroup) come in.

![](/img/Screen-Shot-2020-06-03-at-7.23.33-AM-1-1024x606.png)

Let's take a look at an example of synchronous\* JavaScript code:

```js
const fetch = require('node-fetch')

async function runSync() {
    const resp = await fetch('https://boot.dev')
    let text = await resp.text()
    console.log(text)
    const resp2 = await fetch('https://github.com')
    text = await resp2.text()
    console.log(text)
    const resp3 = await fetch('https://gitlab.io')
    text = await resp3.text()
    console.log(text)
}

runSync()
```

\*Note: Due to some technicalities with JavaScript, the above utilizes asynchronous code (see [async/await](https://javascript.info/async-await)), but for the purposes of our discussion, each _fetch()_ is synchronous in relation to each other.

On order to speed this up, we want each network call to the server (using `fetch()`) to happen at the same time. Take a look:

```js
const fetch = require('node-fetch')

async function runAsync() {
    const promise1 = fetch('https://boot.dev')
    const promise2 = fetch('https://github.com')
    const promise3 = fetch('https://gitlab.io')

    await Promise.all([promise1, promise2, promise3]).then(async (values) => {
        let text = await values[0].text()
        console.log(text)
        text = await values[1].text()
        console.log(text)
        text = await values[2].text()
        console.log(text)
    });
}

runAsync()
```

## WaitGroup

In Go, we have a similar concept, the standard [sync package's](https://golang.org/pkg/sync/) [WaitGroup](https://golang.org/pkg/sync/#WaitGroup) type. First however, let's take a look at how to synchronously fetch data over the wire:

```go
package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func main() {
	getAndPrintData("https://boot.dev")
	getAndPrintData("https://github.com")
	getAndPrintData("https://gitlab.io")
}

func getAndPrintData(url string) {
	resp, _ := http.Get(url)
	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	fmt.Println(buf.String())
}
```

As before, the problem here is that each network call is done in succession, wasting time. Let's use some goroutines, which we start by using the `go` keyword:

```go
package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func main() {
	go getAndPrintData("https://boot.dev")
	go getAndPrintData("https://github.com")
	go getAndPrintData("https://gitlab.io")
}

func getAndPrintData(url string) {
	resp, _ := http.Get(url)
	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	fmt.Println(buf.String())
}
```

If you run this code, you will see that nothing is printed and the program exits almost immediately. The problem is that after starting three separate goroutines and yielding execution back to the main thread, there is nothing stopping main() from exiting. Once main exits, it cleans up its goroutines before they can get a response.

In order to make sure that we wait for all of our functions to complete, but to still allow them to execute at the same time, we use a `WaitGroup`.

```go
package main

import (
	"bytes"
	"fmt"
	"net/http"
	"sync"
)

func main() {
	wg := sync.WaitGroup{}
	wg.Add(3)

	go func() {
		defer wg.Done()
		getAndPrintData("https://boot.dev")
	}()
	go func() {
		defer wg.Done()
		getAndPrintData("https://github.com")
	}()
	go func() {
		defer wg.Done()
		getAndPrintData("https://gitlab.io")
	}()
	wg.Wait()
}

func getAndPrintData(url string) {
	resp, _ := http.Get(url)
	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	fmt.Println(buf.String())
}
```

First, we create a `WaitGroup`, in our case, `wg`. Then we use the `Add()` function to let the WaitGroup know there are 3 counters to wait for. We pass a pointer to the WaitGroup to each goroutine and use [the `defer` keyword](/golang/defer-golang/) to mark a counter done when each goroutine exits.

In the main thread we use the _Wait()_ function to block the main thread until all of the goroutines have exited.

WaitGroups in Go are very similar to PromiseAll in JavaScript and can be a useful tool when developing web client applications.
