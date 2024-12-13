---
title: 'Variable Shadowing In Rust - "Let" Is Immutable But Not Constant'
author: lane
date: "2020-05-13"
categories:
  - "rust"
images:
  - /img/800/Variable_Shadowing.webp
---

Let's take a look at some of the common pitfalls with the keywords _let_ and _mut_**.** Then, we will learn how **immutable != constant** by using _variable shadowing_.

Getting started with Rust can be daunting. Rust is well-known for being a [safe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) language. One of the ways in which Rust is safe is through type-safety. Rust is strongly typed and defaults to immutable values.

## The "let" Keyword

The simplest way to create a new variable in Rust is by using the "let" keyword:

```rust
fn main() {
    let my_num = 5;
    println!("{}", my_num);
}
```

[let](https://doc.rust-lang.org/std/keyword.let.html) introduces a new variable into the current scope. By default, new variables are immutable, which means they can't be reassigned. For example:

```rust
fn main() {
    let my_num = 5;
    my_num = 6;
    println!("{}", my_num);
}
```

which fails to compile with the error: `cannot assign twice to immutable variable`.

## Variable Shadowing - The Dark Side of "let"

As we can see above, Rust's immutability offered by the _let_ keyword allows the compiler to ensure that a given variable can't be changed... kind of. The following does **not** fail to compile:

```rust
fn main() {
    let my_num = 5;
    let my_num = 6;
    println!("{}", my_num);
}
```

We **are** **allowed** to declare a new [variable with the same name](/clean-code/naming-variables/), even all in the same scope. This doesn't mutate `my_num`, it creates a new variable with a new spot in memory. The name `my_num` now refers to the new variable, and the old variable is no longer accessible by its name.

Variable shadowing also works in an inner scope. In the outer scope it is in a way the original variable remains "unshadowed":

```rust
fn main() {
    let my_num = 5;
    // start new scope
    {
        let my_num = 6;
        println!("{}", my_num);
    }
    println!("{}", my_num);
}
```

prints:

```
6
5
```

Notice how the pointer to the new variable is completely different:

```rust
fn main() {
    let my_num = 5;
    println!("my_num pointer address: {:p}", &my_num);
    let my_num = 6;
    println!("my_num pointer address: {:p}", &my_num);
}
```

prints:

```
my_num pointer address: 0x7ffeee0ad6f4
my_num pointer address: 0x7ffeee0ad74c
```

I'm personally not yet a fan of variable shadowing. My first impression is that it ruins the absolute safety that could have been provided. That said, I've heard compelling arguments for why it should exist. Namely that creating a new variable with the same name is terribly convenient.

tl;dr: Even though variables declared with "let" are immutable, the name of the variable can easily point to an entirely new variable. Don't count on it being a true constant.

## Mut - A "Normal" Mutable Variable

Variables declared with "let" can optionally be declared mutable using the "[mut](https://doc.rust-lang.org/stable/rust-by-example/scope/borrow/mut.html)" keyword:

```rust
fn main() {
    let mut my_num = 5;
    my_num = 6;
    println!("{}", my_num);
}
```

Prints **6**

Mutable variables are just that - mutable. The value changes but the underlying address in memory is the same:

```rust
fn main() {
    let mut my_num = 5;
    println!("my_num pointer address: {:p}", &my_num);
    my_num = 6;
    println!("my_num pointer address: {:p}", &my_num);
}
```

prints:

```
my_num pointer address: 0x7ffee5d6e6fc
my_num pointer address: 0x7ffee5d6e6fc
```

There are other interesting keywords to explore as well like [const](https://doc.rust-lang.org/std/keyword.const.html) and [static](https://doc.rust-lang.org/1.29.2/book/first-edition/const-and-static.html), but we'll save those for another article.
