---
title: "What is Go Good For? (And What Is Golang Used For?)"
author: Jamie Dunmore
date: "2021-07-16"
categories: 
  - "golang"
images:
  - /img/800/What-is-Go-good-for-golang-min.webp
---

In 2007, frustrated by some of C++'s inefficiencies and overcomplicated nature, and desiring a programming language designed specifically for multi-core processors and effectively managing large projects, three Google engineers, Robert Griesemer, Rob Pike, and Ken Thompson, designed the Go language.

The goal was to build an improved C++ that was much easier to use — Go was developed based on C's disciplined syntax — but also took inspiration from some of Python's simplicity and Javascript's useful features.

This combination makes Go one of the most effective languages for large-scale infrastructure, and one of the simplest languages for debugging complex projects.

![go vs python javascript c c++](/img/800/Go-language-vs-Python-Javascript-C-min-1.png)

The open-source Go project was first announced in 2009, and version 1.0 was officially released in 2012. Major new features have since been added, such as [generics](/golang/how-to-use-golangs-generics/) and error handling in 2018.

**Go vs Golang: what to call Go**  
  
The official name of the language is Go, with the confusion over its name mostly due to the [golang.org](http://golang.org) domain name (go.org wasn't available).  
  
Though the official term is Go, some find Golang is more convenient to use and prevents confusion with the strategy game Go, so it survives as a cherished alternative name.

## What is Go?

### Go is statically typed

The difference between Go and dynamically typed languages like JavaScript and Python:

- With static languages, **you need to declare your variable data types before you use them**.
- With dynamically typed languages, **you only perform type checking at runtime** — rather than at compile time.

Statically typed programs will fail to compile until errors have been fixed, whereas dynamic scripts can start up even if they contain key errors that may crash later during execution.

- For more differences between Go and dynamically typed languages like Python, read our [Go vs Python guide](/golang/golang-vs-python/)

Go's static typing ensures conversions and compatibility while avoiding the run-type errors and difficulty debugging that can occur with dynamically typed languages.

![dynamic vs statically typed languages golang](/img/800/Static-vs-dynamic-languages-min.png)

### Go is compiled rather than interpreted

As a compiled language, Go is expressed in the instructions of the target machine in 0s and 1s. Whereas interpreted languages are interpreted (without compiling it into machine code), the program instructions use a virtual machine rather than the target machine. 

This lets Go run faster and offer better performance than interpreted language programs. Compiled language errors prevent the code from compiling, whereas errors in the interpreted language programs are found at run-time, with interpreted languages able to modify code even while the program is still running.

![interpreted vs compiled languages go golang](/img/800/Compiled-vs-Interpreted-languages-golang-min-1.png)

### Concurrent & multi-core support

Since Go was designed from the very beginning to run on multiple cores, it has rich support for concurrency and for scaling when more cores are added.

Go uses "goroutines" and channels, concurrent functions that allow the rest of the program to compute while they run, making for efficient dependency management.

Goroutines are great as they continue if you have a network timeout or even an entire database failure, so you can work around any problems that come up. Go's automatic garbage collection mimics Python and makes for a more convenient coding experience. 

Go modules is Golang's simple package manager publishable using a small set of commands. Go's `gofmt` tool is helpful for automatically formatting and indenting code, with other tools like Go run, Go get and Godoc also convenient. It's very versatile, and easy to replace your scripting languages with Golang.

### Go is highly paid and in high demand

Now over 10 years since Go's original open-source release, Go is the second highest-paid language with [median earnings of $140,000 in the USA](https://insights.stackoverflow.com/survey/2020#technology-what-languages-are-associated-with-the-highest-salaries-worldwide-united-states), is one of the most loved languages by programmers, and Go devs are in higher demand than ever before.

It's never been a better time to learn Go, and here's why:

{{< cta1 >}}

## What is Go Good For?

### Simple Syntax & Easy To Learn

Go contains a small number of popular concepts inspired by other languages, designed to create the simplest possible code. This saves time scanning code to check it, as well as time saved writing less code.

For example, Go has very few data types, such as `int`, `string`, `bool`, `float64` and `complex128`, and each has default options that cover most uses. With such few options and concepts to learn, experienced programmers can learn Go in just a few days.

The language itself is similar to C, just without some of C's frustrating inefficiencies that reduce the time required to clean complex code. If you have either previous Java or C experience, you'll have no issues understanding Go as all these languages follow the same procedural approach.

- And if you're struggling to find a course that teaches you Go right from the beginning, try our [Learn Go course](https://boot.dev/learn/learn-golang).

### Go is Fast

Go code is compiled and directly translated into processor-understandable formats. This makes it far faster than languages like Java that first need to compile into byte code, before executing it via a virtual machine (VM). 

Boasting small application sizes, Go binary files can be up to 10x smaller than their Java equivalent. This is especially notable for large applications deployed on multiple servers, heavily reducing file loading time and [making for much-improved performance](https://www.bmc.com/blogs/go-vs-java/#:~:text=Go%20is%20faster%20than%20Java,Go%20performed%20better%20than%20Java.).

Go programs are lightweight, as Go runtimes clean up unused memory as extra code within the executable binary. This makes it easier to write memory-efficient Go code as the Go compiler has some spare code logic within each program.

Languages like Rust and C++ use slightly less memory than Go, however, this is because they afford developers more control over memory usage, whereas Go runtime automatically handles this for efficiency.

### Designed for multi-core processors and is well-scaled for concurrency, making it ideal for large-scale projects

Many languages designed prior to the adoption of multi-core processors (such as Java, JavaScript, C++ and Python) have difficulties scaling and are one-threaded. As a more modern language designed for multi-core processors, Go contains effective support for parallel processes (as do C#, Erlang and other languages). It's also designed in the internet age, so Go doesn't require third-party libraries for web service support.

Goroutines are scalable and non-blocking, ideal for when multiple concurrent processes are required — and take up just 2kb of overhead memory. Goroutines are a convenient combination of Javascript's async features with standard Java multi-threading. As a result, open-source projects like Kubernetes, Docker, InfluxDB and Jaeger all opted for Go as their programming language.

Golang's quick and efficient compilation makes it effective for even the largest projects. Even the most complex projects can be quickly built and worked on efficiently to reduce bugs and aid easy debugging.

On large projects where many developers work together to maintain and develop in teams, it's integral that they be able to work in sync and understand each other's solutions. Go is designed based on the philosophy that there should be very few solutions (ideally just one) rather than a wide variety of ambiguous solutions so that maintaining these large and complex projects is as simple as possible. 

## What is Go Used For?

### Infrastructure 

Popular open-source tools like Kubernetes, Docker and Prometheus are written in Go for container deployment, scaling and management for running and bundling applications.

Cloud service tools like Terraform and OpenShift are written in Go to offer additional cloud and deployment options, with OpenShift running on top of Kubernetes and used by companies such as [KPMG to automate and enhance their AI workflows](https://www.redhat.com/en/about/press-releases/kpmg-automates-accelerates-and-enhances-artificial-intelligence-workflows-red-hat-openshift).

For server-side operations, Netflix uses Go for some of its server architecture, [writing its Rend proxy on Go](https://netflixtechblog.com/application-data-caching-using-ssds-5bf25df851ef). Netflix said:

> "The decision to use Go was deliberate, because we needed something that had lower latency than Java (where garbage collection pauses are an issue) and is more productive for developers than C, while also handling tens of thousands of client connections. Go fits this space well."

Dropbox also switched from Python to Go in 2014 for performance-critical backend features.

### Command-line interfaces

Companies like Comcast, GitHub, Stripe and Uber use Go for their command-line interfaces. Comcast [maintains an open-source client library written in Go](https://github.com/Comcast/pulsar-client-go), whereas Uber uses Go for [CLI API for Jaeger](https://www.jaegertracing.io/docs/1.14/cli/).

### Web applications

Large web apps like Monzo's online banking app have been built in Go since their inception, and now use it to host over 1,600 microservices. Monzo has been using Go solely since 2015, working with Kubernetes and [highlighting that Go is](https://www.theregister.com/2020/03/09/monzo_microservices/) "_quite simple, it's statically typed, and it makes it easy for us to get people on board._"

SoundCloud have also been using Go [since as early as 2012](https://developers.soundcloud.com/blog/go-at-soundcloud) in their build and deployment system, though they mostly use Ruby on Rails. SoundCloud developed what eventually became Prometheus in 2012, which is now used by [AT&T, Honeywell, JP Morgan & Chase, and many other large companies](https://discovery.hgdata.com/product/prometheus).

Our [boot.dev web app](https://boot.dev/), designed to teach you computer science interactively, is also written in Go.

Other large companies that use Go include Google & YouTube (obviously), Medium, BBC, Dailymotion, SendGrid, and Badoo.

### Cryptography and Cryptocurrency

Most notably, implementations of the Bitcoin Lightning Network are written in Go, as well as Geth, the main Ethereum implementation.

### Machine learning and data science

Both Go and Python have been considered some of the best programming languages for AI and machine learning, yet Go trails way behind R and Python as the most popular data science and machine learning languages.

Go can handle [complex math problems much faster than Python](https://www.rtinsights.com/why-golang-and-not-python-which-language-is-perfect-for-ai/), though Python has advantages with its versatility, readability and multi-purpose use for data science. You can now run Tensorflow models in Go as opposed to just Python to take advantage of some of Go's speed advantages.

We believe that Go will become a much more widely adopted machine-learning language in the future.

{{< cta2 >}}

## Limitations of Go

- **Go doesn't support generic functions** -- You can't write implicit code, and the lack of generics support hurts efficiency and reduces your code's reusability. That said, generics are coming in version 2.

- **Go code takes longer to write than Python** -- Go's simple syntax makes it easy to code in, but Python can often write in just a few lines what Go would require more than double to replicate.

- **Not suitable for some types of applications** -- Go is great for some things like maintaining complex systems serving large audiences for backend system scaling, but the same features that make it so exceptional for these uses, like its small memory footprint, also make it less useful for simpler and smaller-scale projects. For rapidly prototyping an application or creating a bite-size demo, you'd favor Python and its dynamic typing over Go.

- Go is newer, and therefore **has a less extensive library** and community than some languages, such as Python.

## Conclusion: Should You Code in Go?

Go programmers command some of the highest salaries, love writing code with Go, and companies are clamoring to hire Go devs.

So should you learn Go, too?

We absolutely think so.

We're huge fans of Golang at Boot.dev, and created our [Learn Go courses](https://boot.dev/learn/learn-golang) to help teach Go as effectively as possible — by learning by doing. Our interactive lessons have you code in Go to fix problems, create programs, and we even built a specialized [Go Interview Prep course](https://boot.dev/golang/interview-prep-golang-course-released/) for landing a job once you've gained the core skills.
