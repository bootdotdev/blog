---
title: "How To Separate Library Packages in Go"
author: Lane Wagner
date: "2020-03-29"
categories: 
  - "golang"
images:
  - /img/800/photo-1550535424-b498819c412f.webp
---

I've often seen, and have been responsible for, throwing code into packages without much thought. I've quickly drawn a line in the sand and started putting code into different folders (which in Go are different packages by definition) just for the sake of findability. Learning to properly build small and reusable packages can take your Go career to the next level.

## What is a Package?

In Go, code is organized into packages. Every folder that contains Go code is a package. Runnable programs must have a package called "**main**" which acts as an entry point to the program. All other packages can be named (almost) anything, and they export code that can be used in other packages and runnable programs. These kinds of non-runnable packages we call "**library**" packages by convention.

Library packages allow developers to export code so it can be used by the outside world. **Packages are essentially APIs** where exported functions are user-facing and unexported functions are only for internal use.

{{< cta1 >}}

## Rules Of Thumb

Now that we've gone over the basics of what a package _is_ let's talk about how to write good packages. The rest of this article will focus on some good rules of thumb to know _when_, _how_, and _why_ to separate code into a new package.

## 1\. Hide Internal Functions

Oftentimes an application will have complex logic that requires a lot of code. In almost every case the logic that the application cares about can be exposed via an API, and most of the dirty work can be kept within a package. For example, imagine we are building an application that needs to classify images. We could build a package:

```go
package classifier

// ClassifyImage classifies images as "hotdog" or "not hotdog"
func ClassifyImage(image []byte) (imageType string) {
	return hasHotdogColors(image) && hasHotdogShape(image)
}

func hasHotdogShape(image []byte) bool {
	// internal logic that the application doesn't need to know about
	return true
}

func hasHotdogColors(image []byte) bool {
	// internal logic that the application doesn't need to know about
	return true
}
```

We create an API by **only** exposing the function(s) that the application-level needs to know about. All other logic is unexported to keep a clean separation of concerns. The application doesn't need to know **how** to classify an image, just the **result** of the classification.

## 2\. Don't Change a Package's API

The unexported functions within a package can and should change often for testing, refactoring, and bug fixing.

A well-designed library will have a stable API so that users aren't receiving breaking changes each time they update the package version. In Go, this means not changing exported function's signatures.

## 3\. Don't Export Functions From Main

Any capitalized function in Go is exported, which means that other programs can import and call those functions. Main packages can contain exported functions, but as a general rule **don't do it**. It is confusing to future readers of the code, and in most cases accomplishes nothing.

## 4\. Packages Should Have No Knowledge of Dependents

Perhaps one of the most important and most broken rules is that a package shouldn't know anything about its dependents. In other words, a package should never have specific knowledge about a particular application that uses it. For example:

```go
package classifier

// ClassifyImage uses a slightly different algorithm if
// the image comes from boot.dev
func ClassifyImage(image []byte, isBootdotdevImage bool) (imageType string) {
	return hasHotdogColors(image) && hasHotdogShape(image)
}
```

Here is an example of a clear violation of this rule. An image classifier shouldn't have knowledge of a "boot.dev image", which we can infer is an application that happens to depend on this package. The author should have made different types of classifiers for general use, and then the dependents of the package would be able to choose the correct one. Two apps that depend on the same package needn't know about each other.
