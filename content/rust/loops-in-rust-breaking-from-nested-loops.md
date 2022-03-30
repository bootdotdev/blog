---
title: "How to Break From Nested Loops in Rust"
author: Lane Wagner
date: "2020-05-14"
categories: 
  - "rust"
images:
  - /img/photo-1455826581186-3031bc66471d.webp
---

Loops in Rust aren't the same as standard C-style languages. The syntax is different and there are some powerful options that make looping easier. First, let's go over some looping basics, then we will cover how to handle breaking and continuing in nested loops in Rust.

## Standard For-Loop

```rust
fn main() {
    for x in 0..10 {
        println!("{}", x);
    }
}
```

Which prints:

```
0
1
2
3
4
5
6
7
8
9
```

0..10 is an [iterator](https://doc.rust-lang.org/1.2.0/book/iterators.html) where the lower-bound is inclusive and the upper bound is exclusive.

More generically:

```
for var in iterator {
    // do stuff
}
```

In my opinion, all languages should move to a single syntax with for-loops based on iterators. The simplicity makes Rust's loops easy to read, while the ability to create custom [iterators](https://doc.rust-lang.org/stable/rust-by-example/trait/iter.html) makes it more powerful than even more verbose formats like Go's:

```go
for i := 0; i < 10; i++ {
	fmt.Println(i)
}
```

Rust's for-loop doesn't specify what happens after each iteration (i++) or what condition is required to continue the loop (i < 10), an [ite](https://doc.rust-lang.org/1.2.0/book/iterators.html)[r](https://doc.rust-lang.org/1.2.0/book/iterators.html)[ator](https://doc.rust-lang.org/1.2.0/book/iterators.html) is simply supplied.

## Continue and Break

```rust
for x in 0..10 {
    if x > 5 && x < 7 {
        continue
    }
    println!("{}", x);
}
```

The `continue` keyword works in a familiar manner. In this example when `x > 5 AND x < 7` the loop continues to the next iteration without printing. This results in:

```
0
1
2
3
4
5
7
8
9
```

The `break` keyword is also familiar:

```rust
for x in 0..10 {
    if x > 5{
        break
    }
    println!("{}", x);
}
```

which prints:

```
0
1
2
3
4
5
```

## Working With Nested Loops

Nested loops can get tricky in a lot of languages. What if I want to continue through an outer loop when a condition within an inner loop occurs? We can do the following:

```rust
'outer: for x in 0..5 {
    for y in 0..5 {
        if y > 2{
            break 'outer
        }
        println!("x: {}, y: {}", x, y);
    }
}
```

prints:

```
x: 0, y: 0
x: 0, y: 1
x: 0, y: 2
```

By using the label _'outer_ we are able to control explicitly which loop is broken. The default would have been to just break from the inner loop. The same labeling system works with the _continue_ keyword as well.
