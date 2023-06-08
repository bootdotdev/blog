---
title: "Is Golang Best For Backend or Frontend Development?"
author: Natalie Schooner
date: "2022-12-19"
categories: 
  - "golang"
images:
  - /img/800/gopherphone.webp
---

Put simply, **Golang is best for the backend side of a web application or website**. There are many reasons that this is the case, so let's dive in, but before we do, let's cover some quick definitions.

Golang, also called Go, was developed by Google in 2009. Those developers wanted a sexy, agile, effective language that would be simpler to read and work with than C and C++, which is what they were relying on at the time (to their dismay).

Thus, Golang was born. Go is a statically-typed language with syntax loosely derived from C, but with additional useful features like garbage collection, type safety, and concurrency.

OK, now let's look at what the "backend" and "frontend" are. Handily I already wrote an article on [backend vs frontend](/backend/frontend-vs-backend-meaning/), so I'll just quote myself:

> What is the "front-end"?
> 
> The frontend of the software is what the user sees. If you look at a website, even something as simple as a login page, everything you see on the page is considered the frontend. Frontend code dictates the style and layout of the page.

> What is the "back-end"?
> 
> The backend of software exists behind the scenes. Once you've entered your username and password, the application needs to verify whether the information is correct. Your profile and password are saved on the server, and the backend is responsible for validating your login and letting the front-end know that it was successful.

## Why is Go best for back-end programming?

If you know anything about programming, you may already be starting to get an inkling about why Go is best for the backend. In case not, I'll spell it out here:

* **Go has built-in concurrency called "goroutines"**. This means it can multitask, which is important for implementing high-performance servers and networked applications.
* **Networking**. Go has a robust standard library that offers support for plenty of common backend networking tasks, like HTTP handling and TLS (Transport Layer Security) encryption.
* **Go goes fast**. Go is famous for its rapid compilation times and efficient runtime performance, which is great for backend applications that need to handle a high volume of requests.

Go is used heavily by Google to support their back-end infrastructure. It's good for back-end development because that's what it was *designed* for.

## Can Go be used on the front-end?

I mean, if you really want to, you can use Go as a frontend language, the same way you *can* use a hammer to make a screw go in.

One way to use Go on the front-end is by compiling it to WebAssembly (Wasm). WebAssembly is a binary format that is supported by modern web browsers, and it allows developers to run code in the browser that was written in languages other than JavaScript. When it comes to writing front-end code, at least on the web, there are only two options:

* JavaScript
* Web Assembly (WASM)

Web Assembly is still new, but it does work. So, if you really want to write so front-end applications in Go, you can, but I'd argue you're better off waiting on the tooling to mature a bit more.

In short, let go (pun intended) of those dreams and use Go in a context where it shines: as a command-line interface tool, and as a backend language.

> [Using Go for the frontend] will have you swimming upstream against a relentless current, assuming you actually want to get something accomplished. Of course if you are just doing the work for learning and exploration sake, more power to you!
>
> [Mike Schinkel, Golangbridge forum](https://forum.golangbridge.org/t/using-golang-as-front-end-framework/27226/7)

## What has Go been used for?

Go is *primarily* a backend language, and has been used to build components in:

* Docker. The Docker daemon, a system that manages containers, is [built with Go](https://docs.docker.com/language/golang/#:~:text=Go%20is%20undeniably%20a%20major,Kubernetes%20are%20written%20in%20Go.).
* Kubernetes. The Kubernetes control plane, which is the backend component that manages a cluster of servers, is [built with Go](https://docs.docker.com/language/golang/#:~:text=Go%20is%20undeniably%20a%20major,Kubernetes%20are%20written%20in%20Go.).
* Terraform. The Terraform backend, which is the component that manages and applies infrastructure changes, is [written in Go](https://pkg.go.dev/github.com/markcaudill/terraform-http-backend).
* InfluxDB. The InfluxDB server, which is a backend component that stores and retrieves data, is [built with Go](https://blog.gopheracademy.com/birthday-bash-2014/why-influxdb-uses-go/).

And of course, Go's own progenitor Google has made use of Go to create or support:

* Google App Engine: Google App Engine is a cloud computing platform that allows developers to build and deploy web applications and mobile backends. The [App Engine runtime](https://github.com/golang/appengine), which is in charge of executing applications and handling requests, is built with Go.
* dl.google.com: dl.google.com is a web service that provides access to Google's software downloads, including Chrome, Android Studio, and various other tools. The [dl.google.com backend](https://groups.google.com/g/golang-nuts/c/BNUNbKSypE0/m/E4qSfpx9qI8J?pli=1), which is responsible for serving download files and tracking download statistics, is served by Go.
* gVisor: gVisor is an open-source security sandbox that allows developers to run untrusted code in a secure environment. [gVisor is built with Go](https://github.com/google/gvisor).
* Google Cloud Functions: Google Cloud Functions is a serverless computing platform that allows developers to run code in response to events. [The Cloud Functions runtime](https://cloud.google.com/functions/docs/concepts/go-runtime), which is responsible for executing functions and handling requests, is built with Go.

## Which Go frameworks should I use?

I could talk about any number of popular Go frameworks here:

* [Echo](https://echo.labstack.com/) is a high-performance, minimalist web framework
* [Gin](https://gin-gonic.com/) claims to be the fastest full-featured web framework
* [Buffalo](https://gobuffalo.io/) even offers a frontend pipeline

But honestly? The best answer might just be *none*. In most cases, you probably shouldn't use a framework at all.

Go markets itself as a simple, fast, powerful language. Go frameworks often just gild the lily. They promise shiny tools that offer out-of-the-box, batteries-included functionality. Interestingly enough, Go doesn't need most of that functionality.

Frameworks are *super* helpful in many contexts. However, if you're just building simple CRUD apps in Go, you probably don't need one. Go's standard library is so inundated with web tooling that it's already kind of like a web framework. Using a go web framework on top of that means you might be less effective and commit yourself to design decisions that you might not need to make yet.

## But I thought we *always* use frameworks!?!

Let's look at Python as an illustrative counter-example. Python developers often rightfully reach for frameworks like Django and Flask because the language doesn't provide rich networking capabilities on its own. Python leaves those implementation details to each framework's implementations.

Most Go web frameworks actively hide the http.Response and http.Request objects away in exchange for ease of use. This effectively means that when you use a framework with Go, you're slapping a big shiny box on top of the guts of whatever you're working on. It looks great, but when it stops working, you will have a harder time understanding why or how to fix it.

In short, new Golang developers are often curious about frameworks for the same reason they like Go: frameworks promise to be no-frills, simple, and conventional. But Go already is all those things.

I'll end with a great quote from [experienced Go programmer Pancy](https://pancy.medium.com/you-should-try-go-first-or-at-least-go-through-what-i-wrote-before-bringing-up-rails-convention-592782ea0ee4):

> I have been programming in Go for more than a year and haven't had any success adopting a framework that's more intuitive than piecing packages myself.

## Should you use Go for the backend only?

Go is a great language for a lot of reasons: it's fast, it's simple, and as I kept harping on above, it's an all-in-one option. It's very easy to learn and it's satisfying to build things in.

That's why I recommend [learning Go](https://boot.dev/learn/learn-golang) no matter where you are on your coding journey. For the same reasons that make Go a great backend language, Go is a just good language to learn, full stop. Even if you plan to go fully frontend in your programming career, it never hurts to have the flexibility to be able to code in Go.

If you want to get started learning Go, I recommend you take our course to [learn Go](https://boot.dev/learn/learn-golang).
