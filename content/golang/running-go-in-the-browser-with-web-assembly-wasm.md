---
title: "Running Go in the Browser With Web Assembly (WASM)"
author: Lane Wagner
date: "2020-07-01"
categories:
  - "golang"
images:
  - /img/800/maxresdefault.webp
---

If you are familiar with the [Go Playground](https://play.golang.org/), then you know how convenient it is to be able to have a Go scratchpad in the browser. Want to show someone a code snippet? Want to quickly test some syntax? Browser-based code pads are helpful. On that note, I [created a new playground](https://www.boot.dev/playground/go). The cool thing about this new playground that it doesn't use a remote server to run code, just to compile it. The code runs in your browser using [web assembly (WASM)](https://webassembly.org/).

The Playground can be found here: [Boot.dev playground](https://www.boot.dev/playground/go)

Update: There is now a sequel to this article outlining how we run the WASM inside Web Workers which can be [found here](/golang/running-go-in-the-browser-wasm-web-workers/).

## How Does It Work?

When a user clicks "run", the code (as text) is sent back to our servers. The server is written in Go. As such the handler for the API looks something like this:

```go
func compileCodeHandler(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()

	// Get code from params
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

	// create file system location for compilation path
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
	f, err := os.Create(filepath.Join(workingDir, "main.go"))
	if err != nil {
		respondWithError(w, 500, "Couldn't create code file for compilation")
		return
	}
	defer f.Close()
	dat := []byte(params.Code)
	_, err = f.Write(dat)
	if err != nil {
		respondWithError(w, 500, "Couldn't write code to file for compilation")
		return
	}

	// compile the wasm
	const outputBinary = "main.wasm"
	os.Setenv("GOOS", "js")
	os.Setenv("GOARCH", "wasm")
	cmd := exec.Command("go", "build", "-o", outputBinary)
	cmd.Dir = workingDir
	stderr, err := cmd.StderrPipe()
	if err != nil {
		respondWithError(w, 500, err.Error())
		return
	}
	if err := cmd.Start(); err != nil {
		respondWithError(w, 500, err.Error())
		return
	}
	stdErr, err := ioutil.ReadAll(stderr)
	if err != nil {
		respondWithError(w, 500, err.Error())
		return
	}
	stdErrString := string(stdErr)
	if stdErrString != "" {
		parts := strings.Split(stdErrString, workingDir)
		if len(parts) < 2 {
			respondWithError(w, 500, stdErrString)
			return
		}
		respondWithError(w, 400, parts[1])
		return
	}
	if err := cmd.Wait(); err != nil {
		respondWithError(w, 500, err.Error())
		return
	}

	// write wasm binary to response
	dat, err = ioutil.ReadFile(filepath.Join(workingDir, outputBinary))
	if err != nil {
		respondWithError(w, 500, err.Error())
		return
	}
	w.Write(dat)
}
```

As you can see, the handler simply takes code as input and responds with a slice of WASM bytes.

## What About the Front-End?

The front end is quite simple. First, we need to include the official Go WASM executor in our page. Assuming you have a go installation on your machine, this JavaScript file can be found at:

```bash
$(go env GOROOT)/misc/wasm/wasm_exec.js
```

Then include the script in the body of your html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Boot.dev Classroom - Learn Coding</title>
  </head>
  <body>
    <script src="wasm_exec.js"></script>
  </body>
</html>
```

Because Boot.dev's Classroom's front-end is written as a [Vue.js](https://vuejs.org/) single page app, I've created a small es6 module that runs a WASM byte array and returns the output as an array of lines:

```js
const go = new window.Go();

export default async function runGoWasm(rawData) {
  const result = await WebAssembly.instantiate(rawData, go.importObject);
  let oldLog = console.log;
  let stdOut = [];
  console.log = (line) => {
    stdOut.push(line);
  };
  await go.run(result.instance);
  console.log = oldLog;
  return stdOut;
}
```

That's it! Running Go in the browser is pretty easy :)

If you want to try our [Learn Go](https://www.boot.dev/courses/learn-golang) course that uses the WASM playground as its backbone, [sign up here!](https://www.boot.dev/)
