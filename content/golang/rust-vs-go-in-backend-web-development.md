---
title: "Rust Backend vs Go Backend in Web Development"
author: Lane Wagner
date: "2020-07-17"
categories: 
  - "golang"
  - "rust"
images:
  - /img/go-vs-rust.webp
---

Rust and Go are two of the industry's biggest successes when it comes to developing modern programming languages. Both languages compete in terms of backend [web development](https://qvault.io/golang/top-web-development-languages/), and it's a fierce competition. Golang and Rust are new languages, have growing communities, and are fast and efficient. When it comes to microservice architectures, frameworks, and apps, Rust and Go are household names on the backend.

## Similarities

### Rich Standard Libraries

Rust and Go share many traits, especially when it comes to web development. They both have rich standard libraries, though Go tends to have more internet-focused protocols such as [HTTP](https://golang.org/pkg/net/http/) supported of out the box.

### Open-Source

Both languages are open-source, meaning no company will be yanking the source code out from under us anytime soon, though it is worth noting that Google drives the development of Go, while Rust is more of a community project. There are pros and cons of company support. Go benefits from the resources and PR of a major tech company, while Rust will never have the risk of Google-specific agendas being pushed on the project.

### Relatively New Languages

Go and Rust are both new languages, which means they don't come with the legacy and backward-compatibility baggage that you find with languages like Java and Javascript.

Rust v1 released: May 15, 2015

Go v1 released: March 28, 2012

{{< cta1 >}}

## Performance

Performance metrics generally put Rust squarely ahead of Go, but not by a lot. The Rust compiler and language design allow developers to easily take advantage of optimizations that achieve speeds comparable to the likes of C. On the other hand, Go trades a small amount of speed for simplicity and elegant syntax.

![](/img/rust-vs-go-speed.png)

[benchmarksgame](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust-go.html)

## Memory Management

Both languages claim the title of "memory-safe" but take different approaches to achieve it. Rust catches memory errors at compile-time while Go uses a garbage collector at runtime.

Rust makes use of compile-time ownership strategy through [zero-cost abstractions](https://boats.gitlab.io/blog/post/zero-cost-abstractions/). If a Rust program is not memory safe, it will fail to compile. To anyone who frequently deals with memory errors in C languages, this is recognized as an amazing feature. Instead of clever compiler optimizations, the Go compiler adds a small runtime to the completed executable that manages the allocation and release of memory. 

While both approaches have their pros and cons, generally speaking Rust's compiler optimizations result in more performant programs. Alternatively, Go's application code is cleaner because memory management is fully handled by the runtime.

![](/img/rust-vs-go-memory.png)

[benchmarksgame](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust-go.html)

## Development Speed

There are times during the development of a web application that development speed is more important than app speed. Python is a great example, it is one of the slowest languages but has some of the cleanest syntax. While Go is generally faster and uses less memory than languages like Java, C#, JavaScript, Python, and Ruby, it makes a performance trade-off to allow for fast and simple development.

It's also worth noting that Go and Rust are both growing in popularity. If you want to read more on that, take a look this related article, ["Rust vs Go - Which is More Popular?"](https://qvault.io/2020/05/06/rust-vs-go-which-is-more-popular/).

{{< cta2 >}}

## Code Comparison

Now that we've compared and contrasted Rust and Go conceptually, let's take a look at what a simple HTTP server would look like in both languages.

### Rust HTTP Backend Server Example

```rust
// example taken from https://gist.github.com/mjohnsullivan/e5182707caf0a9dbdf2d

use std::net::{TcpStream, TcpListener};
use std::io::{Read, Write};
use std::thread;


fn handle_read(mut stream: &TcpStream) {
    let mut buf = [0u8 ;4096];
    match stream.read(&mut buf) {
        Ok(_) => {
            let req_str = String::from_utf8_lossy(&buf);
            println!("{}", req_str);
            },
        Err(e) => println!("Unable to read stream: {}", e),
    }
}

fn handle_write(mut stream: TcpStream) {
    let response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html><body>Hello world</body></html>\r\n";
    match stream.write(response) {
        Ok(_) => println!("Response sent"),
        Err(e) => println!("Failed sending response: {}", e),
    }
}

fn handle_client(stream: TcpStream) {
    handle_read(&stream);
    handle_write(stream);
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    println!("Listening for connections on port {}", 8080);

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(|| {
                    handle_client(stream)
                });
            }
            Err(e) => {
                println!("Unable to connect: {}", e);
            }
        }
    }
}
```

As you'll notice in the code above, we can spin up a fairly simple HTTP server without anything more than the standard library, though we have to implement some of the HTTP protocol ourselves. Notice that we include the `HTTP/1.1 200 OK` response directly in the data stream we are responding with. This isn't to say there aren't other crates that would make our lives easier, but out-of-the-box Rust forces us to do more of the heavy lifting ourselves.

If you take a look at the standard HTTP create, you'll see that it's an intentional choice not to standardize an implementation.

> You will notably _not_ find an implementation of sending requests or spinning up a server in this crate. It's intended that this crate is the "standard library" for HTTP clients and servers without dictating any particular implementation. Note that this crate is still early on in its lifecycle so the support libraries that integrate with the `http` crate are a work in progress! Stay tuned and we'll be sure to highlight crates here in the future.
> 
> [http - Rust](https://docs.rs/http/0.2.1/http/)

Golang HTTP Backend Server Example

```go
package main

import (
	"encoding/json"
	"net/http"
)

func hello(w http.ResponseWriter, req *http.Request) {
	type response struct {
		Message string `json:"message"`
	}
	resp := response{
		Message: "hello world",
	}
	respBytes, _ := json.Marshal(resp)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(200)
	w.Write(respBytes)
}

func main() {
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8080", nil)
}
```

With Go, on the other hand, it's extremely easy to spin up a production web server, we even get [support for JSON](https://qvault.io/golang/json-golang/), headers, and status codes right from the standard library.

## Concurrency

Concurrency is a necessity in backend applications. Some languages run in single-threaded environments which means they use some clever tricks to simulate concurrency without achieving true parallelism. Both Rust and Go have elegant solutions to build [fully parallel applications](https://qvault.io/2020/05/11/concurrency-in-rust-can-it-stack-up-against-gos-goroutines/), but Go takes the cake again in terms of simplicity, with the `go` keyword being the only syntax necessary to spin up a new thread:

```
go someFunc()
```

## The Winner

As usual, there is no outright winner, the results are more nuanced than that.

### Rust is Favored For...

- Computation Speed
- Memory usage
- Fine-tuning and control over the final executable

### Go is Favored For...

- Simple syntax
- Beginner-friendly
- Developer speed
- Concurrency mechanisms

One mark of a successful [computer scientist, even a self-taught one](https://qvault.io/2020/11/18/comprehensive-guide-to-learn-computer-science-online/), is being able to choose good tools for a given project. It doesn't mean you need to be an expert with every language, database, technology, and framework under the sun, but it does mean you need to be familiar with enough of them to make informed decisions. Being capable to make those decisions will set you apart and give you more opportunities to advance your [programming career](https://qvault.io/2020/12/09/highest-paying-computer-science-jobs/).
