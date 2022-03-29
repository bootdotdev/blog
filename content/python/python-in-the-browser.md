---
title: "Running Python in the Browser with Web Assembly"
author: Lane Wagner
date: "2020-09-24"
categories: 
  - "javascript"
  - "python"
---

I've been wanting to expand [Qvault's curriculum](https://qvault.io/), and one of the most requested programming languages has been Python. Because my courses allow students to write and execute code right in the web browser, I decided to look into existing projects that allow a Python interpreter to run in the browser using Web Assembly. I settled on a tool called [Pyodide](https://github.com/iodide-project/pyodide), which does just that.

To see it in action, check out the [finished product, a Python playground](https://app.qvault.io/playground/py).

## What is Pyodide?

Pyodide is an open-source project that comprises a Python interpreter that has been compiled to Web Assembly.

> WebAssembly (abbreviated _Wasm_) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable compilation target for programming languages, enabling deployment on the web for client and server applications.
> 
> [webassembly.org](https://webassembly.org/)

In other words, normally only JavaScript can run in a browser, but if you can compile your source code to Wasm, then you can run _any_ programming language in the browser. (At the time of writing we run Python, Rust, and Go this way on our [playground](https://app.qvault.io/playground/py) and in our [courses](https://qvault.io/))

> Pyodide brings the Python 3.8 runtime to the browser via WebAssembly, along with the Python scientific stack including NumPy, Pandas, Matplotlib, parts of SciPy, and NetworkX. The `packages` directory lists over 35 packages which are currently available.
> 
> [Github Project](https://github.com/iodide-project/pyodide)

## How did I do it?

My Python execution plan is quite similar to the way I run Go code in the browser. There are basically three steps:

- Write a worker file that defines how code is executed
- Write a worker helper that abstracts the details of spinning up, communicating, and terminating workers
- Implement the helper in the view so that users can execute code and see the code's output

If you want to know how that all works please read [this article about Web Workers and WASM in Go before continuing.](https://qvault.io/2020/09/23/running-go-in-the-browser-with-wasm-and-web-workers/)

If you have finished that first article on Web Workers, then all you will need to understand the difference between our Python and Go logic is the worker file itself:

```js
// pull down pyodide from the public CDN
importScripts('https://pyodide-cdn2.iodide.io/v0.15.0/full/pyodide.js');

addEventListener('message', async (e) => {
  // wait for the interpreter to be fully loaded
  await languagePluginLoader;

  self.runPythonWithStdout = () => {
    try {
      // execute the code passed to the worker
      pyodide.runPython(e.data);
    } catch (err){
      postMessage({
        error: err
      });
      return;
    }

    // capture the code's standard output
    // and send it back to the main thread
    let stdout = pyodide.runPython("sys.stdout.getvalue()")
    if (stdout) {
      stdout = stdout.split('\n')
      for (line of stdout){
        postMessage({
          message: line
        });
      }
    }
  }

  // redirect stdout to io.StringIO so that we can get it later
  pyodide.runPython(`
    import io, code, sys
    from js import runPythonWithStdout
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    ## This runs self.runPythonWithStdout defined in the JS
    runPythonWithStdout()
  `)

  postMessage({
    done: true
  });
}, false);
```

As you can see, the only particularly challenging part for our use case was adding the glue to properly capture the code's standard output.
