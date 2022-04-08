---
title: "Unexpected Printf Behavior in Go WASM - Nothing Prints"
author: Lane Wagner
date: "2020-08-10"
categories: 
  - "golang"
images:
  - /img/800/fmt.Printf.png
---

While working on [boot.dev's](https://boot.dev) [Go Playground](https://boot.dev/playground/go), I came across a very strange error. The standard library's [fmt.Printf()](https://golang.org/pkg/fmt/?m=all#Printf) function prints nothing to the console when called. _Nothing._

For those of you who are familiar with the function, when compiled to a "normal" executable `fmt.Printf` prints a formatted string to standard output. As per the official documentation, this program:

```go
package main

import (
	"fmt"
)

func main() {
	const name, age = "Kim", 22
	fmt.Printf("%s is %d years old.", name, age)
}
```

Will print:

```
Kim is 22 years old.
```

The interesting thing is that when the same exact program is compiled using Web Assembly, we get a different result. If you want to try it, copy the above program and run it [here](https://boot.dev/playground/go).

Spoiler alert: _It doesn't print anything._

However, if you change the program slightly:

```go
package main

import (
	"fmt"
)

func main() {
	const name, age = "Kim", 22
	// add a newline character
	fmt.Printf("%s is %d years old.\n", name, age)
}
```

Then it may print the expected:

```
Kim is 22 years old.
```

thought if you run the two programs back to back, you may actually find that this is printed instead:

```
Kim is 22 years old.Kim is 22 years old.
```

## Why?

When compiled to Web Assembly, the `fmt.Printf` function is writing to a buffer, and that buffer is not cleared until a newline character is printed to standard out. In other words, you can call `fmt.Printf` as many times as you want, but nothing is printed until a `\n` character comes through standard output.

Take a look at the `writeSync()` code in Go's [wasm\_exec.js](https://github.com/lane-c-wagner/classroom.qvault.io/blob/master/public/wasm_exec.js#L43), which is a required include to execute Go Web Assembly in the browser:

```go
writeSync(fd, buf) {
	outputBuf += decoder.decode(buf);
	const nl = outputBuf.lastIndexOf("\n");
	if (nl != -1) {
		console.log(outputBuf.substr(0, nl));
		outputBuf = outputBuf.substr(nl + 1);
	}
	return buf.length;
}
```

As you can see, `console.log()` is only called on the buffer if a newline is found within the output string, otherwise the output is just appended to the stateful `outputBuf`.

My current working theory is that it was implemented this way because there is no way to print to the console in a browser without appending a newline. JavaScript's [console.log()](https://developer.mozilla.org/en-US/docs/Web/API/Console/log) _always_ appends a newline.
