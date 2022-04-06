---
title: "From Beginner to Experienced: 7 Best Practices for Every Python Developer"
author: Zulie Rane
date: "2022-01-04"
categories: 
  - "python"
images:
  - /img/stretching-women.jpeg
---

If you’re looking to improve your coding, there are lots of steps you can take, but the first is focusing on Python best practices. It’s really important that your code is readable, testable, and maintainable. From picking good variable names, refactoring code that gets repeated out into its own method, or having clean and logical lines of inheritance and abstraction, there are a lot of qualities that differentiate code that someone wants to work with from code that everyone dreads having to maintain or develop further. 

My first steps at Python were pathetic. Over half of my own coding problems were just because I didn’t know to set up a virtual environment. I cringe to even look back at how I documented my code. As soon as I stepped back and started working on Python best practices, coding got easier for me. The same was true of any other language I tried to learn.

To help others avoid my old issues, I’ve put together a comprehensive guide full of resources to clearly outline the Python best practices you should follow when coding in Python.

Don’t forget that overall programming best practices are always relevant – things that supersede programming languages. It’s always important to pay attention to the performance of your programs, and know the Big O performance of the data structures and algorithms you choose to utilize or implement. There are a lot of helpful courses out there, like these for [Big O](https://boot.dev/course/884342fc-5469-47b4-8125-8bfc897428a8/67214b76) and Advanced Algorithms. Both of these courses are based in Python, so if you’re particularly interested in strengthening your Python skills and refreshing your knowledge of runtime performance and algorithm design, they’d be a good fit for you.

 If you’re looking for a deep dive on general best coding practices, I highly recommend the book Clean Code: A Handbook of Software Craftsmanship by Robert C. Martin, a.k.a. “Uncle Bob”. It is a great read with fun examples, and it will be relevant to your work, no matter what you are programming.

Here is how to write good Python code.

## Python Best Practices #1: Typing

You may think you already know how to use a keyboard, but let me tell you! But actually, let’s talk about data types and how to enforce their use when programming. If you are familiar with Java, you’re familiar with the differences between [compile-time and run-time polymorphism](https://www.geeksforgeeks.org/difference-between-compile-time-and-run-time-polymorphism-in-java/). Python is not nearly as strict when it comes to types as Java is, but it can be extremely helpful to draw stricter boundaries when programming in Python.

Python is a dynamically-typed language, so variables can change type over their lifetime, and the Python interpreter only does type checking as the code runs. This kind of loosey-goosey type structure can lead to confusion as well as runtime errors if you’re not careful. So what’s a good Python coding practice to better handle typing?

The package [typing](https://docs.python.org/3/library/typing.html) allows assigning types to variables. This allows for better code completion in your IDE. This package is great at assisting static type checkers and linters catch potential errors and leads to better code completion. Although it will never be quite as strict as type checking when Java or C code is compiled, having these type hints and variable annotations can make keeping track of what each variable should be a lot easier.

There also exist tools for static type checking, like [mypy](http://mypy-lang.org/). This can make it easier to find bugs with less debugging. Static typing also makes your code a lot easier to understand. Mypy is able to infer the types of other variables, so static and dynamic typing can be mixed when using it, so you only need to statically type where it makes sense.

## Python Best Practices #2: Docstrings

Writing meaningful comments and documentation is always important. It helps others understand the gist of a class, method, or package by reading through it without having to thoroughly inspect the code just to get an idea of what’s going on. For example, if you’re debating between using two methods from a package that do similar but distinct things, it’s great to have documentation to quickly understand what the difference is without having to read through the source code. 

Your documentation and comments are useless, however, if you don’t update them when you make changes to your code, so be sure to pay attention to them and update them when needed.

A docstring is a string literal that is the first statement in a class, function, or module. Following this format, the [docstring](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring) “becomes the __doc__ special attribute of that object”. All objects that are public or are exported as part of a module should have a docstring. Docstrings unequivocally belong to Python best practices, as they are ubiquitous in the Python community. Every professional Python package makes use of them.

[Sphinx](https://www.sphinx-doc.org/en/master/) is the most common package used to automatically generate HTML code for a documentation website from your d

## Python Best Practices #3: Logging

When it comes to good coding practices for Python, logging has to be on that list. If you have server applications or use multi-threading, debugging becomes an extremely frustrating and usually fruitless exercise. A simple solution would be to litter your code with print statements in order to understand what is going on at runtime. 

The problem with using print statements is that they need to be removed from production code, but you need them for local development. Are you going to remove them every time you push to master and put them back in after you are working on your own branch again? That’s incredibly time consuming, annoying, and inefficient.

To solve this problem, use logging. Logging is an elegant solution to understanding the runtime execution of your application. 

Logging allows you to control whether the statements are outputted and even where they end up. You could output them to a file or silence them entirely. You can also annotate each log with a category. They typically are something like `verbose`, `information`, `debug`, `warning`, `error`, and `critical`.

## Python Best Practices #4: Testing

Testing is a crucial part of software development. Any piece of code that goes into production should be tested, and preferably on many different levels. Tests range from tiny [unit tests](clean-code/writing-good-unit-tests-dont-mock-database-connections) all the way up to all-encompassing end-to-end or acceptance tests.You can read more about the software [test hierarchy here](https://www.softwaretestinggenius.com/simple-explanation-of-hierarchy-of-testing-levels/).

[Unittest](https://docs.python.org/3/library/unittest.html) is a standard Python package that serves as a testing framework. It was inspired by the ubiquitous [JUnit](https://junit.org/junit5/). Unittest “supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework”

Although unittest is a handy framework, there is still room for improvement. [Pytest](https://docs.pytest.org/en/6.2.x/) is a great package for elevated testing. For example, using pytest, you can easily parametrize fixtures and functions using the parametrize decorator, where you can pass in arguments for tests along with the corresponding expected output.

## Python Best Practices #5: Architecture

Structuring your Python project is key to its success. It’s very important that you set up your repository with a meaningful and simple folder structure. You should be able to quickly find what you’re looking for, and files should be strictly organized. Tests should be kept separate from production code.

Watch your dependencies. You should not have any circular dependencies, where two classes rely on each other. This will lead to confusing import statements as well as purposes. Every file should only contain one class, and each class should have one purpose. 

You should also take care to not have components that are highly coupled. [High coupling](https://livebook.manning.com/book/code-like-a-pro/chapter-10/) means two pieces of code are highly interdependent and making changes to one significantly impacts the other. If, for example, one small change to class X causes half of your tests for class Y to fail, those two classes are most likely way too tightly coupled.

## Python Best Practices #6: Logging Package Management

Package managers are important when it comes to [managing](https://blog.idrsolutions.com/what-is-a-package-manager-and-why-should-you-use-one/) external dependencies and creating project environments. Python is well known for having plenty of libraries available, and package managers make it easy to use those libraries.

[Pip](https://pypi.org/project/pip/) is Python’s official package manager. Pip allows you to install and manage libraries that are outside of Python’s standard library, like [numpy](https://numpy.org/) or [TensorFlow](https://www.tensorflow.org/). It’s also great for managing the requirements for your scripts and applications, as well as uninstalling libraries when they are no longer in use.

Another important aspect of managing your application’s execution environment is virtual environments. A virtual machine is a computer that is running in a virtual environment. A great way of managing your virtual environment is by using [anaconda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Anaconda allows you to switch between different environments. For example, you could have one virtual environment that has Python 2 installed and another with Python 3 on the same physical device! You can also have different versions of packages or different packages altogether in different environments. This allows you to manage complex and thorough development and testing environments.

## Python Best Practices #7: Naming conventions

Last but not least is naming conventions. The names of variables, modules, and classes, and functions is incredibly important. Although Python is known as one of the most readable programming languages, if your [variables and objects are named poorly](/clean-code/naming-variables), or even worse, in a confusing manner, then any other developers will struggle trying to make heads or tails of your code. 

Python has an [official guide](https://www.python.org/dev/peps/pep-0008/) to it as well, which is a great jumping-off point. The key here is consistency. If you’re working with others, make sure you’ve all agreed to one naming strategy.

## Python Best Practices Are Critical to Good Coding

When it comes to relevant Python best practices in terms of project development, it’s important that you pay special attention to architecture, testing, and logging. These three are crucial components for writing scalable programs, especially if you are collaborating with others.

Whether you program for fun or it is your full-time job, it’s important to write clean code. Your coworkers or even your future self (let’s be honest – who can actually remember the details of features you worked on a year ago) will be grateful to work with code that is well-documented, has meaningful comments, is easy to read, and is thoroughly covered with tests. If you take care to follow these practices, your work can have a lot more impact and you’ll save yourself a lot of future headaches.
