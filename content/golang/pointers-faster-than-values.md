---
title: "Are Pointers in Go Faster Than Values?"
author: lane
date: "2024-07-19"
categories: 
  - "golang"
images:
  - /img/800/arrowpointing.png.webp
imageAlts: 
  - "Arrow pointing"
---

I was recently working on a lesson about pointer performance for Boot.dev's [Golang course](https://www.boot.dev/learn/learn-golang) when I found myself repeating some advice I've given many times before.

*Begin quote:*

Occasionally, new Go developers hear "pointers don't pass copies" and take that to a logical extreme, concluding: "Pointers are always faster because copying is slow. I'll always use pointers!"

*No. Bad. Stop.*

**Here are my rules of thumb:**

1. First, worry about writing clear, correct, maintainable code.
2. If you have a performance problem, fix it.

Before even thinking about using pointers to optimize your code, use pointers when you need a shared reference to a value; otherwise, just use values.

**If you *do* have a performance problem, consider:**

1. [Stack vs. Heap](https://go.dev/doc/faq#stack_or_heap)
2. Copying

Interestingly, local non-pointer variables are generally faster to pass around than pointers because they're stored on the [stack](https://computersciencewiki.org/index.php?title=Stack_memory), which is faster to access than the [heap](https://computersciencewiki.org/index.php/Heap_memory). Even though copying is involved, the stack is so fast that it's no big deal.

Once the value becomes large enough that copying is the greater problem, it can be worth using a pointer to avoid copying. That value will probably go to the heap, so the gain from avoiding copying needs to be greater than the loss from moving to the heap.

One of the reasons Go programs tend to use less memory than Java and C# programs is that Go tends to allocate more on the stack.

*End quote*

## Is this advice accurate? How can we know?

While my research into the Go docs, various community articles, and even consulting the all-knowing (lul) Chat GPT confirmed the validity of my advice, I wanted to see for myself.

So, I wrote this benchmark that you can try for yourself if you're curious!

```go
package main

import (
	"fmt"
	"testing"
)

type data struct {
	a, b, c, d, e, f, g, h, i, j int64
}

var globalPtr *data
var globalValue data

func newDataPtr(i int) *data {
	data := &data{int64(i), int64(i + 1), int64(i + 2), int64(i + 3), int64(i + 4), int64(i + 5), int64(i + 6), int64(i + 7), int64(i + 8), int64(i + 9)}
	return data
}

func newData(i int) data {
	data := data{int64(i), int64(i + 1), int64(i + 2), int64(i + 3), int64(i + 4), int64(i + 5), int64(i + 6), int64(i + 7), int64(i + 8), int64(i + 9)}
	return data
}

func BenchmarkProcessValue(b *testing.B) {
	for i := 0; i < b.N; i++ {
		globalValue = newData(i)
	}
	// use it to avoid compiler optimization
	fmt.Println(globalValue.a)
}

func BenchmarkProcessPointer(b *testing.B) {
	for i := 0; i < b.N; i++ {
		globalPtr = newDataPtr(i)
	}
	// use it to avoid compiler optimization
	fmt.Println(globalPtr.a)
}
```

Slap that in a `bench_test.go` file and run `go test -bench=. -benchmem` to see the results. This is what I got:

```
wagslane@MacBook-Pro-2 test % go test -bench=. -benchmem

goos: darwin
goarch: arm64
pkg: github.com/bootdotdev/go-api-gate/test
BenchmarkProcessValue-12        273343356                4.236 ns/op           0 B/op          0 allocs/op
BenchmarkProcessPointer-12      61566219                17.72 ns/op           80 B/op          1 allocs/op
PASS
ok      github.com/bootdotdev/go-api-gate/test  2.912s
```

As you can see, passing by value rather than reference (pointer) is indeed faster in this case, even though the value is being copied.

That said, I admit it took me about 20 minutes of trial and error to get this benchmark into the state that I wanted to make sure it was testing what I wanted to test. There were initial drafts that I *thought* were copying to the heap, but they weren't. That in and of itself is a good lesson: the Go compiler is pretty smart and will optimize things for you. Don't go crazy trying to use pointers or non-pointers to optimize your code until you have something tangible to benchmark and optimize!
