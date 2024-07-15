---
title: "JavaScript vs Java - Differences, Similarities, and History"
author: Lane Wagner
date: "2020-11-06"
categories: 
  - "javascript"
images:
  - /img/800/java-vs-javascript.webp
---

The naming of Java and JavaScript confuses many new programmers. They sound so similar, so one might think they have the same use-cases, similar properties, or maybe the same company created both languages. None of those assumptions are true! JavaScript is primarily used as a front-end in-the-browser language, like how we use it for [boot.dev's courses](https://boot.dev/). Java has been used for everything from games, to desktop apps, to backend APIs. Let's go over the differences between JavaScript vs Java in this quick read.

## Java - Brief History

In 1991, James Gosling of Sun Microsystems created Java. Sun Microsystems wrote software for many different devices. Eventually, re-compiling or restructuring code to run on various CPU architectures became too time-consuming.

The founding team had a hard time thinking of a good name for their project, and while out for coffee, decided to name the language after their coffee.

### Cross-Platform (JVM)

Java is a general-purpose programming language that allows developers to run code on any device. It compiles code into Java-specific byte code, then [the Java Virtual Machine (JVM)](https://en.wikipedia.org/wiki/Java_virtual_machine) converts that byte code into machine compatible code. Because it compiles code in this way, Java becomes completely cross-platform. This is a major contributing factor to Java's success.

### Object-Oriented Design

Java rose quickly to fame and adoption mostly due to its cross-platform nature and [object-oriented programming (OOP](https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/)) pattern. OOP was and remains popular due to the ability to reuse code and think about entities within a program as hierarchies of types. Java is the king of the OOP design pattern. It requires that everything in the program be a class, even the main function!

OOP was so popular in the early 2000s that it became (in my opinion) overly widespread. These days it has more appropriately found its correct place in programming, but when JavaScript was first coming into existence OOP was the name of the game.

## JavaScript - Brief History

In 1995, 4 years after Java got its start, Brendan Eich created JavaScript while he worked for Netscape. At the time, Netscape had complete market control of the web browsing industry, while Microsoft was just starting with the Internet Explorer project.

In an attempt to beat Microsoft, Netscape partnered with Sun Microsystems. They branded it with the name JavaScript to latch onto the Java hype train that was certainly plowing ahead in the developer community.

### JavaScript's Success

JavaScript started as a small scripting language to perform actions on the client-side within the browser. Development was rushed and interesting design choices were made, including:

- Optional semi-colon line endings
- Objects and classes but with limited [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
- Single-threaded (Callback based, no concurrency)

However, JavaScript was positioned uniquely. This would contribute to it becoming the [most used programming language](https://octoverse.github.com/#top_languages) today. The following points attributed to its widespread success:

- The "JavaScript" naming ploy to steal marketing hype
- Not seen as competition because web development was "not serious development"
- Monopolizing browser programming, again, because other projects didn't see browser scripting as a serious programming

Many developers considered "front-end" development to be for artists and designers. After all, "It's just styling and templating, right?"

This was the case for a long time. However, in the last decade, front-end development has become just as serious as backend development. Single page apps, and frameworks like Angular, React, and Vue, have pushed logic that used to be controlled by the backend directly into the user's browser.

## Runtimes, Speed, and Benchmarks

![runner in starting blocks](/img/800/photo-1461896836934-ffe607ba8211-1024x683.jpeg)

Most compiled languages like C, C++, and Go compile code directly into machine instructions. Those instructions are specific to a CPU architecture and operating system. **Neither Java nor JavaScript are typically compiled in this way.**

Java and JavaScript operate in distinct ways. For this comparison, we will assume Java is compiled to JVM bytecode, and JavaScript is being run in a NodeJS interpreter.

Note: Java can be compiled to native code, or run via an interpreter, and JavaScript can run outside a browser via Node, but we will stick to these specific use cases for now.

### Java Virtual Machine (JVM)

The JVM compiles code (_.java_ files), into compiled classes (_.class_ files). These class files make up a complete compiled Java program, with the requirement that one of the class files has a "main" function as an entry point. Class files are typically archived and **distributed together in a .jar file**. Due to this, is it easier for users to download a single executable file.

The JVM runs **faster than interpreted languages** like JavaScipt because it compiles code to machine code before runtime. The JVM is **slower than most natively compiled languages**. This is because it misses out on architecture-specific optimizations, and still has to do JVM --> CPU conversions at runtime.

### NodeJS - V8 Engine

JavaScript is an interpreted language that has many different interpreter implementations. One of the most common ways for JavaScript to run in production is by using the NodeJS interpreter. Node uses Chrome's [V8 engine](https://v8.dev/) to interpret and run JavaScript.

As you can see in the following benchmarks, Java fairly consistently performs better than Node in regards to memory and CPU:

![binary trees](/img/800/Screen-Shot-2020-01-13-at-8.51.55-AM.png)

[source](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/javascript.html)

What really slows JavaScript down is that it is interpreting code at runtime. At \*roughly\* each line of execution, the interpreter has to convert the JavaScript into machine code, a very slow process to be doing at runtime.

## Classes and OOP

In Java, **everything** is a class and OOP is enforced in an authoritarian manner.

In JavaScript, classes are optional, and [functional programming](https://boot.dev/courses/learn-functional-programming) is possible and even [encouraged](/clean-code/benefits-of-functional-programming/) lately. JavaScript has most of the OOP paradigms available in the language. However, [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) is not as robust as it is with Java.

## Threading and Concurrency

**JavaScript is single-threaded**, which means that it will never execute code at the same time. Concurrent programming is a feature of most languages, and JavaScript is fairly unique in not being able to accomplish the task.

**In Java concurrency is readily available** and you can [read more about it here](https://howtodoinjava.com/java-concurrency-tutorial/).

The way JavaScript makes up for being single-threaded is by use of [asynchronous programming and the event-loop](https://dev.to/steelvoltage/if-javascript-is-single-threaded-how-is-it-asynchronous-56gd). Whenever an API Call or some other long-running process needs to happen without blocking the execution of the rest of the program, the event-loop is responsible for doing the waiting. When the asynchronous task completes, the main thread is able to detect the results of the task.
