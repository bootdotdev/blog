---
title: "Running Go in the Browser with WASM and Web Workers"
author: Lane Wagner
date: "2020-09-23"
categories: 
  - "golang"
  - "javascript"
images:
  - /img/800/WASM-Web-Workers.png
---

We've recently made big changes to how we execute Go in the browser on [boot.dev](https://boot.dev/) and want to explain the enhancements. Web Workers are the reason we've been able to solve some of the serious browser-related coding problems that were holding us back. Consider this article a sequel to [Running Go in the Browser with Web Assembly](/golang/running-go-in-the-browser-with-web-assembly-wasm/).

While publishing our latest course, [Learn Algorithms](https://boot.dev/learn/learn-algorithms), we needed a way to print console output while code is still executing. We ran into a problem when running computationally expensive algorithms in the browser; the browser gets so bogged down that it can't render new lines of output. We decided to implement web workers, and they solved the problem handily.

## The Problem

In the old boot.dev, console output was all printed at once. The program executed, then the output was displayed. We found this to be less than ideal because it is often useful to see _when_ something prints, especially when trying to optimize an algorithm for speed.

For example, this code used to print all of its output at once:

```go
package main

import (
	"fmt"
)

func main(){
	const max = 100000000
	for i := 0; i < max; i++{
		if i % (max/10) == 0{
			fmt.Println(i)
		}
	}
}
```

Since adding Web Workers, now it appropriately prints each number at the time of execution. You can see for yourself on the [playground here](https://boot.dev/playground/go).

## What Is a Web Worker?

> Web Workers are a simple means for web content to run scripts in background threads.
> 
> [Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

In other words, its a way for us to finally break free from the single-threaded clutches of JavaScript! We can offload expensive tasks to another thread of execution. Doing this leaves the browser free to render updates on the screen.

## How It Works - The Worker

As you know, we compile code in the editor to WASM on our servers. If you are curious about that part, you can read about it in our [previous post.](/golang/running-go-in-the-browser-with-web-assembly-wasm/) Once the code is compiled to Web Assembly, it's shipped back to our front end for execution.

To run a Web Worker, we need a script that defines the worker. It's just a JavaScript file:

```js
addEventListener('message', async (e) => {
	// initialize the Go WASM glue
	const go = new self.Go();

	// e.data contains the code from the main thread
	const result = await WebAssembly.instantiate(e.data, go.importObject);

	// hijack the console.log function to capture stdout
	let oldLog = console.log;
	// send each line of output to the main thread
	console.log = (line) => { postMessage({
		message: line
	}); };

	// run the code
	await go.run(result.instance);
	console.log = oldLog;

	// tell the main thread we are done
	postMessage({
		done: true
	});
}, false);
  
```

The worker communicates with the main thread by listening to `message` events, and sending data back via the `postMessage` function.

Note: I omitted the wasm\_exec.js file that is necessary for the worker to be able to run Go code, but it can be found on your machine if you have Go installed.

```
cat $(go env GOROOT)/misc/wasm/wasm_exec.js
```

## How it Works - Main Thread

Now that we have a worker file that can execute compiled Web Assembly, let's take a look at how the main thread communicates with the worker. I built an ES6 module that exports some helper functions:

```js
export function getWorker(lang) {
  return {
    webWorker: new window.Worker(`/${lang}_worker.js`),
    lang
  };
}

export function useWorker(worker, params, callback) {
  const promise = new Promise((resolve, reject) => {
    worker.webWorker.onmessage = (event) => {
      if (event.data.done) {
        resolve();
        return;
      }
      if (event.data.error) {
        reject(event.data.error);
        return;
      }
      callback(event.data.message);
    };
  });
  worker.webWorker.postMessage(params);
  return promise;
}

export function terminateWorker(worker) {
  worker.webWorker.terminate();
}
```

When the page loads we will create a new Web Worker using `getWorker`. When the user runs some code we send the code to the worker using `useWorker`. When we navigate away from the code editor we can clean up the worker using `terminateWorker`.

The `useWorker` function is the post interesting part. It takes the worker that was created with `getWorker`, an object called `params` that will be passed to the worker (it contains the compiled WASM), and a callback function to execute when the worker is finished with the job.

For example, in our Vue app we use these functions as follows:

```js
this.output = [];
this.isLoading = true;
const wasm = await compileGo(this.code);
await useWorker(this.worker, wasm, (data) => {
  this.output.push(data); 
});
this.isLoading = false;
```

And because `this.output` is a reactive property on our Vue instance, each time we receive data from the Web Worker, new output is printed to the console.
