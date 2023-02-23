---
title: "Running Rust in the Browser with Web Assembly"
author: Lane Wagner
date: "2020-10-12"
categories: 
  - "rust"
images:
  - /img/800/rust.jpeg
---

I've recently been working on getting Rust support in the [boot.dev app](https://boot.dev/). To write a more engaging course, I want students to be able to write and execute code right in the browser. As I've learned from my previous posts on this topic, the easiest way to sandbox code execution on a server is to _not_ execute code on a server. Enter Web Assembly, stage left.

## Deprecation Disclaimer!

This recently stopped working due to the `io::set_print` function being completely deprecated. I'm leaving the post up for historical knowledge's sake, but this won't work anymore!

{{< cta1 >}}

## How It Works

The architecture is fairly simple:

- User writes code in the browser
- Browser sends code to server
- Server adds some glue and compiles code to WASM
- Server sends WASM bytes or compiler errors back to browser
- Browser runs WASM and displays console output, or shows compiler errors

Writing code and shipping it to the server hopefully needs no explanation, it's a simple text editor coupled with the fetch API. The first interesting thing we do is compile the code on the server.

## Compiling the Code

Boot.dev's server is written in Go. I have a simple HTTP handler with the following signature:

```go
func (cfg config) compileRustHandler(w http.ResponseWriter, r *http.Request)
```

At the start of the function we unmarshal the code which was provided in a JSON body:

```go
type parameters struct {
	Code string
}

decoder := json.NewDecoder(r.Body)
params := parameters{}
err := decoder.Decode(&params)
if err != nil {
	respondWithError(w, 500, "Couldn't decode parameters")
	return
}
```

Next, we create a temporary folder on disk that we'll use as a "scratch pad" to create a Rust project.

```go
usr, err := user.Current()
if err != nil {
	respondWithError(w, 500, "Couldn't get system user")
	return
}
workingDir := filepath.Join(usr.HomeDir, ".wasm", uuid.New().String())
err = os.MkdirAll(workingDir, os.ModePerm)
if err != nil {
	respondWithError(w, 500, "Couldn't create directory for compilation")
	return
}
defer func() {
	err = os.RemoveAll(workingDir)
	if err != nil {
		respondWithError(w, 500, "Couldn't clean up code from compilation")
		return
	}
}()
```

As you can see, we create the project under the `.wasm/uuid` path in the home directory. We also `defer` an `os.RemoveAll` function that will delete this folder when we are doing handling this request.

Next we setup a helper function that will run an operating system command and return the stderr, if it exists:

```go
func runCmd(workingDir, name string, args ...string) error {
	cmd := exec.Command(name, args...)
	cmd.Dir = filepath.Join(workingDir)
	stdErrReader, err := cmd.StderrPipe()
	if err != nil {
		return err
	}
	if err := cmd.Start(); err != nil {
		return err
	}
	stdErr, err := ioutil.ReadAll(stdErrReader)
	if err != nil {
		return err
	}
	if err := cmd.Wait(); err != nil {
		if len(stdErr) > 0 {
			return fmt.Errorf("%s", stdErr)
		}
		return err
	}
	return nil
}
```

Next, (back in the HTTP handler) we use that function to create a new Rust project in our temporary directory:

```go
const projectName = "main"
err = runCmd(workingDir, "cargo", "new", projectName)
if err != nil {
	respondWithError(w, 500, err.Error())
	return
}
```

After that, we need to write the code we were given to disk. Before we do that, however, we need to add some glue. The glue code will override Rust's print macros so that we can provide JavaScript functions that will capture stdout. I thank [Sterling Demille](https://github.com/DeMille) for open sourcing this glue:

```rust
// copied from https://github.com/DeMille/wasm-glue
#![feature(set_stdio)]
#![feature(panic_col)]

use std::ffi::CString;
use std::os::raw::c_char;
use std::fmt;
use std::fmt::Write;
use std::panic;
use std::io;


// these are the functions you'll need to privide with JS
extern {
    fn print(ptr: *const c_char);
    fn eprint(ptr: *const c_char);
    fn trace(ptr: *const c_char);
}


fn _print(buf: &str) -> io::Result<()> {
    let cstring = CString::new(buf)?;

    unsafe {
        print(cstring.as_ptr());
    }

    Ok(())
}

fn _eprint(buf: &str) -> io::Result<()> {
    let cstring = CString::new(buf)?;

    unsafe {
        eprint(cstring.as_ptr());
    }

    Ok(())
}

/// Used by the "print" macro
#[doc(hidden)]
pub fn _print_args(args: fmt::Arguments) {
    let mut buf = String::new();
    let _ = buf.write_fmt(args);
    let _ = _print(&buf);
}

/// Used by the "eprint" macro
#[doc(hidden)]
pub fn _eprint_args(args: fmt::Arguments) {
    let mut buf = String::new();
    let _ = buf.write_fmt(args);
    let _ = _eprint(&buf);
}

/// Overrides the default "print!" macro.
#[macro_export]
macro_rules! print {
    ($($arg:tt)*) => ($crate::_print_args(format_args!($($arg)*)));
}

/// Overrides the default "eprint!" macro.
#[macro_export]
macro_rules! eprint {
    ($($arg:tt)*) => ($crate::_eprint_args(format_args!($($arg)*)));
}


type PrintFn = fn(&str) -> io::Result<()>;

struct Printer {
    printfn: PrintFn,
    buffer: String,
    is_buffered: bool,
}

impl Printer {
    fn new(printfn: PrintFn, is_buffered: bool) -> Printer {
        Printer {
            buffer: String::new(),
            printfn,
            is_buffered,
        }
    }
}

impl io::Write for Printer {
    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
        self.buffer.push_str(&String::from_utf8_lossy(buf));

        if !self.is_buffered {
            (self.printfn)(&self.buffer)?;
            self.buffer.clear();

            return Ok(buf.len());
        }

        if let Some(i) = self.buffer.rfind('\n') {
            let buffered = {
                let (first, last) = self.buffer.split_at(i);
                (self.printfn)(first)?;

                String::from(&last[1..])
            };

            self.buffer.clear();
            self.buffer.push_str(&buffered);
        }

        Ok(buf.len())
    }

    fn flush(&mut self) -> io::Result<()> {
        (self.printfn)(&self.buffer)?;
        self.buffer.clear();

        Ok(())
    }
}


/// Sets a line-buffered stdout, uses your JavaScript "print" function
pub fn set_stdout() {
    let printer = Printer::new(_print, true);
    io::set_print(Some(Box::new(printer)));
}

/// Sets an unbuffered stdout, uses your JavaScript "print" function
pub fn set_stdout_unbuffered() {
    let printer = Printer::new(_print, false);
    io::set_print(Some(Box::new(printer)));
}

/// Sets a line-buffered stderr, uses your JavaScript "eprint" function
pub fn set_stderr() {
    let eprinter = Printer::new(_eprint, true);
    io::set_panic(Some(Box::new(eprinter)));
}

/// Sets an unbuffered stderr, uses your JavaScript "eprint" function
pub fn set_stderr_unbuffered() {
    let eprinter = Printer::new(_eprint, false);
    io::set_panic(Some(Box::new(eprinter)));
}

/// Sets a custom panic hook, uses your JavaScript "trace" function
pub fn set_panic_hook() {
    panic::set_hook(Box::new(|info| {
        let file = info.location().unwrap().file();
        let line = info.location().unwrap().line();
        let col = info.location().unwrap().column();

        let msg = match info.payload().downcast_ref::<&'static str>() {
            Some(s) => *s,
            None => {
                match info.payload().downcast_ref::<String>() {
                    Some(s) => &s[..],
                    None => "Box<Any>",
                }
            }
        };

        let err_info = format!("Panicked at '{}', {}:{}:{}", msg, file, line, col);
        let cstring = CString::new(err_info).unwrap();

        unsafe {
            trace(cstring.as_ptr());
        }
    }));
}

/// Sets stdout, stderr, and a custom panic hook
pub fn hook() {
    set_stdout();
    set_stderr();
    set_panic_hook();
}
```

All we need to do is concatenate that glue code to the user provided code, and call `hook()` as the first thing in `main()`.

```go
func writeRustToDisk(workingDir, projectName, code string) error {
	// remove old code
	codePath := filepath.Join(workingDir, projectName, "src", "main.rs")
	os.Remove(codePath)

	// create the new file
	f, err := os.Create(codePath)
	if err != nil {
		return errors.New("Couldn't open code file for compilation")
	}
	defer f.Close()

	// write the glue
	_, err = f.WriteString(rustGlue)
	if err != nil {
		return errors.New("Couldn't write code to file for compilation")
	}

	// add the hook
	code = addHook(code)

	// write the rest of the code
	dat := []byte(code)
	_, err = f.Write(dat)
	if err != nil {
		return errors.New("Couldn't write code to file for compilation")
	}
	return nil
}
```

Where `rustGlue` is just a string constant containing the glue from the previous step, and `addHook` is a function that uses a regex to insert the `hook()` call properly:

```go
func addHook(code string) string {
	regex := regexp.MustCompile(`(fn\s*main\(\)\s*)\{`)
	return regex.ReplaceAllString(code, `fn main(){hook();`)
}
```

Next, the all-important compilation step:

```go
err = runCmd(
	filepath.Join(workingDir, projectName),
	"cargo",
	"+nightly",
	"build",
	"--target",
	"wasm32-unknown-unknown",
	"--release",
)
if err != nil {
	errString := err.Error()
	fmt.Println(errString)
	parts := strings.Split(errString, workingDir)
	if len(parts) < 2 {
		respondWithError(w, 500, errString)
		return
	}
	respondWithError(w, 400, parts[1])
	return
}
```

A simple `cargo build` with `WASM` as the target. If there is an error, we strip out some of the filesystem information before sending it back to the frontend.

We use `[wasm-gc](https://lib.rs/crates/wasm-gc)` to optimize the build:

```go
err = runCmd(
	filepath.Join(workingDir, projectName),
	"wasm-gc",
	"target",
	"wasm32-unknown-unknown",
	"release",
	"main.wasm",
)
if err != nil {
	respondWithError(w, 500, err.Error())
	return
}
```

Finally we send the WASM back to the frontend as raw bytes:

```go
dat, err := ioutil.ReadFile(filepath.Join(workingDir, projectName, "target", "wasm32-unknown-unknown", "release", "main.wasm"))
if err != nil {
	respondWithError(w, 500, err.Error())
	return
}
w.Write(dat)
```

## Frontend - Executing the WASM Bundle

The Rust front-end has a lot of similarities to the Go front end. They both use Web Workers to optimize the user experience of executing potentially expensive code in the browser. If you need to catch-up on how that's done, read up on my [web workers explanation here](/golang/running-go-in-the-browser-wasm-web-workers/).

The main difference here comes down to the `rust_worker.js` file. The equivalent of `go_worker.js` from the referenced article:

```js
// send(line) sends a single line of stdout back to the browser to // be rendered in the on-screen console
function send(line){
  postMessage({
    message: readString(line)
  });
}

// keep a WebAssembly memory reference for readString
let memory;

// read a null terminated c string at a wasm memory buffer index
function readString(ptr) {
  const view = new Uint8Array(memory.buffer);

  let end = ptr;
  while (view[end]) ++end;

  const buf = new Uint8Array(view.subarray(ptr, end));
  return (new TextDecoder()).decode(buf);
}

// addEventListener is a handler that get's called whenever the
// main thread (editor) sends us some WASM to execute
addEventListener('message', async (e) => {
  const result = await WebAssembly.instantiate(e.data, {
    // here we define the print, eprint, and trace
    // functions as specified in the glue from above
    // they just send stdout back using the send function
    env: {
      print(ptr){
        send(ptr);
      },
      eprint(ptr) {
        send(ptr);
      },
      trace(ptr) {
        send(ptr);
      }
    }
  });

  memory = result.instance.exports.memory;

  // run the main() function of the WASM code 
  await result.instance.exports.main();

  // let the editor know we've sent all the output and have
  // finished
  postMessage({
    done: true
  });
}, false);
```
