---
title: "Go-CoNLLU - Some Much Needed Machine Learning Support in Go"
author: Lane Wagner
date: "2020-06-08"
categories: 
  - "golang"
  - "open-source"
images:
  - /img/800/photo-1527474305487-b87b222841cc.webp
---

Python is commonly seen as the AI/ML language, but is often a dull blade due to unsafe typing and being slow, like _really_ slow. Many popular natural language processing toolkits only have Python APIs, and we want to see that change. At [Nuvi](https://nuvi.com), a [social media marketing tool](https://bulk.ly/social-media-tools/), we use Go for the majority of our data processing tasks because we can write _simple_ and _fast_ code. Today we are open-sourcing a tool that has helped make our ML lives easier in Go. Say hello to [go-conllu](https://github.com/nuvi/go-conllu).

## What is CoNLL-U?

The Conference on Natural Language Learning (CoNNL) has created multiple file-formats for storing natural language annotations. [CoNLL-U](https://universaldependencies.org/format.html) is one such format and is used by the [Universal Dependency Project](https://universaldependencies.org/), which hosts many annotations of textual data. In order to use these corpora, we need a parser that makes it simple for developers to utilize the data.

![Universal Dependencies Machine Learning Logo](/img/800/logo-ud.png)

Universal Dependencies

{{< cta1 >}}

## How Does Go-Conllu Help?

[Go-conllu](https://github.com/nuvi/go-conllu) parses conllu data. It is a simple and reliable way to import conllu data into your application as Go structs.

[The GoDoc can be found here with the specifics](https://godoc.org/github.com/nuvi/go-conllu)

Let's take a look at the example quick-start code from the Readme. First, download the package.

```
go get github.com/nuvi/go-conllu
```

Then in a new project:

```go
package main

import (
	"fmt"
	"log"

	conllu "github.com/nuvi/go-conllu"
)

func main() {
	sentences, err := conllu.ParseFile("path/to/model.conllu")
	if err != nil {
		log.Fatal(err)
	}

	for _, sentence := range sentences {
		for _, token := range sentence.Tokens {
			fmt.Println(token)
		}
		fmt.Println()
	}
}
```

All the sentences and tokens in the corpus will be printed to the console.

If you need a .conllu corpus file you can download the Universal Dependencies English training model here: [en\_ewt-ud](https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-train.conllu)[\-](https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-train.conllu)[train.conllu](https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-train.conllu)
