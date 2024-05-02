---
title: "Using 'Go Generate' To Deploy Multi-Process Apps"
author: Lane Wagner
date: "2020-04-22"
categories: 
  - "clean-code"
  - "golang"
images:
  - /img/800/Using Go Generate.webp
---

In microservice architectures, it's fairly common to have a project that includes different worker types. A [Makefile](https://en.wikipedia.org/wiki/Makefile) can be used to manage the creation of multiple programs, but the Go toolchain has a tool that can be used as well, [go generate](https://blog.golang.org/generate). Here are some examples of how it can be used:

- **API/Worker** - We have an API that allows clients to start/stop long-running jobs, and a worker which accesses the same database to run the jobs.
- **NLP Classifier** - We have different processes that share a majority of the same code, but have different quirks depending on if they are classifying sentiment, vulgarity, or subjectivity.

In other words, we have one git repository, but from that code, we want to generate `n` number of executables.

## Repository Structure

Our normal single-process repositories have the following structure:

- `main.go`
- `foo.go (other main package source files)`
- `bar.go`
- `internal (folder for packages intended just for this project)`
    - `database (package for database access)`
        - `database.go`
    - `rabbit (package for rabbitmq access)`
        - `rabbit.go`  
            

As you can see, when there is only one program (one main.go) it's really easy to build and deploy. We just run:

```
go build
```

from the root of the repository.

## Structure With Multiple Programs

Now let's say we have a project that has an API that is responsible for managing some long-running jobs. For example, we can pretend it manages RSS scraping jobs. Here is how we would build out the repository:

- `cmd`
    - `api`
        - `main.go`
    - `worker`
        - `main.go`
- `internal (folder for packages intended just for this project)`
    - `database (package for database access)`
        - `database.go`
    - `rss (package for rss scraping logic)`
        - `rss.go`
- `gen.go`

Here we have a **cmd** folder in the root, which then holds a directory for each executable. This allows us to still scope packages to the entire project, share a CI/CD pipeline, and keep code that is tightly coupled all in one place.

## How Do We Build It?

In the above project structure, you may have noticed the `gen.go` file. Here is what it looks like:

```go
package main

//go:generate go build ./cmd/api
//go:generate go build ./cmd/worker
```

Now we can run **go generate** from the root of our project and both executables will be built at the root.

## Can We Do More?

Have more steps in the build process? Go generate is quite flexible, lets's build the production docker image as well (assuming we have a Dockerfile in the root of the project):

```go
package main

//go:generate go build ./cmd/api
//go:generate go build ./cmd/worker
//go:generate docker build .
```

The **generate** function is a powerful tool and can do a lot more than just build a list of executables. Nevertheless, we've found this to be a convenient way to keep our projects "go native".
