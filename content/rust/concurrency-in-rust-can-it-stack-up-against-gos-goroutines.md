---
title: "Concurrency In Rust; Can It Stack Up Against Go's Goroutines?"
author: Lane Wagner
date: "2020-05-11"
categories: 
  - "golang"
  - "rust"
images:
  - /img/photo-1518181835702-6eef8b4b2113.webp
---

One of the primary goals of the Go programming language is to make concurrency simpler, faster, and more efficient. With Rust growing in popularity let's see how its concurrency mechanisms stack up against Go's.

## A Refresher On Goroutines

In Go, concurrency is accomplished by spawning new [goroutines](https://tour.golang.org/concurrency/1):

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		for {
			fmt.Println("one second passed")
			time.Sleep(time.Second)
		}
	}()
	fmt.Println("waiting 10 secs for goroutine")
	time.Sleep(time.Second * 10)
}
```

In the example above, we use the _go_ keyword to signify that we want to run the provided anonymous function in a goroutine. Execution at that point splits - execution continues on the main thread, but the runtime is now running the goroutine in parallel.

Goroutines are lightweight and take advantage of all of the processing power available. If two goroutines are running they will efficiently use at most two cores. If one hundred goroutines are running they will use at most one hundred cores, but can efficiently run on as few as one.

## What About Rust?

In Rust, there are two approaches we can take to run code concurrently. [Async/Await](https://rust-lang.github.io/async-book/01_getting_started/04_async_await_primer.html), and [threading](https://doc.rust-lang.org/book/ch16-01-threads.html). Async/Await is a paradigm that is orthogonal to threading, which means that it has the potential to run tasks on a single thread OR on multiple threads depending on the [executor](https://docs.rs/futures/0.2.1/futures/executor/index.html) that is used.

Threading on its own makes use of multiple cores and uses typical operating-system threads.

## Async/Await

Let's take a look at async first. and don't forget to add the following dependencies to your project's `Cargo.toml`:

```toml
[dependencies]
futures = "0.3.5"
async-std = "1.5.0"
```

```rust
use std::time::Duration;
use futures::executor::block_on;
use async_std::task;

fn main() {
    let future = async_main();
    block_on(future);
}

async fn async_main() {
    print_for_five("await 1").await;

    let async_one = print_for_five("async 1");
    let async_two = print_for_five("async 2");

    futures::join!(async_one, async_two);
}

async fn print_for_five(msg: &str) {
    for _ in 0..5 {
        task::sleep(Duration::from_secs(1)).await;
        println!("one second has passed: {}", msg)
    }
}
```

We start by creating a new async function, _async\_main_, then use the _block\_on_ executor to block and execute _async\_main_. Because _async\_main_ is an asynchronous function, we are able to _await_ other async functions inside of it, as well as execute them concurrently.

The first call in _async\_main_ is an _await_ on our async _print\_for\_five_ function which prints the message "one second has passed: await 1" once each second for 5 seconds. Because we used the _await_ keyword, _async\_main_ will block and wait for _print\_for\_five_.

Next, we create two futures (very similar to JavaScript [promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)) by calling _print\_for\_five_ anew with new messages. The futures do not begin execution until the next line where we use the _join_ macro. _Join_ executes the futures concurrently and blocks until all the futures have completed. Join is very similar to JavaScript's [PromiseAll](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all).

The program will print the following:

```
one second has passed: await 1
one second has passed: await 1
one second has passed: await 1
one second has passed: await 1
one second has passed: await 1
one second has passed: async 1
one second has passed: async 2
one second has passed: async 1
one second has passed: async 2
one second has passed: async 1
one second has passed: async 2
one second has passed: async 1
one second has passed: async 2
one second has passed: async 1
one second has passed: async 2
```

Where the last ten lines are all printed within five seconds of each other because `print_for_five("async 1")` and `print_for_five("async 2")` were executed concurrently.

The `block_on` executor that we used blocks the main thread, which means that all the concurrency happened on a single thread.

{{< cta1 >}}

## Rust's Threading

Threading in Rust takes advantage of multi-core hardware. When a new thread is spawned, the operating system knows that these separate threads of the program can be executed in parallel on different cores at exactly the same time.

Let's take a look at the following example:

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for _ in 1..10 {
            println!("Hello after 1 second from the spawned thread");
            thread::sleep(Duration::from_millis(1000));
        }
    });

    for _ in 1..5 {
        println!("Hello after 1 second from the main thread");
        thread::sleep(Duration::from_millis(1000));
    }
}
```

We spawn a new thread using the standard library's _spawn_ function. The _spawn_ function take a closure as its argument and executes it in parallel. As you can see by running the program, it only takes five seconds to print all ten statements because each thread is sleeping independently.

## Which is Best?

You've heard it before but no approach is _best_, they are all just _different_. I argue that Go is the best at keeping it **simple**. Go provides only one method (goroutines) to achieve concurrency, and the syntax is elegant. Rust provides two methods which are tailored to different problems.

## Goroutines vs Async/Await

Goroutines are very different from async/await. Async/Await explicitly accomplishes concurrency, but not necessarily parallelism. In other words, while async/await _logically_ executes two functions at once, it doesn't always _practically_ do so. It all depends on the [executor](https://docs.rs/futures/0.2.1/futures/executor/index.html) that is used.

![](/img/Untitled.jpg)

Async/Await is a useful paradigm for programs that have heavy I/O wait times but aren't doing long-running compute-heavy workloads.

Async/Await can also be good for many short-lived async tasks where new operating system threads would be clunky and expensive.

## Goroutines vs Threading

Goroutines are more lightweight and efficient than operating-system threads. As a result, a program can spawn more total goroutines than threads. Goroutines also start and clean themselves up faster than threads due to less system overhead.

The big advantage of traditional threading (like that of Rust) over the goroutine model is that no runtime is required. Each Go executable is compiled with a small runtime which manages goroutines, while Rust avoids that extra fluff in the binary.
