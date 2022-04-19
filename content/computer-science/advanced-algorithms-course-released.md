---
title: "Advanced Algorithms Course Released on Boot.dev"
author: Lane Wagner
date: "2021-04-05"
categories: 
  - "computer-science"
  - "news"
---

Sorry it took so long for me to get this one out! [Advanced Algorithms](https://boot.dev/course/aaad49fb-0dc5-43c6-992c-96d3f83ee663/573c4cc4-f178-4465-bb76-5ee4718f12a6/dfef3058-b62d-4774-be32-80d933a0a766/) was just released, and I'm excited to let you all get your hands on it, even if you're just auditing it for free! The more advanced material takes quite a bit longer to produce, I wanted to triple check to make sure I got everything correct and that I've presented it in a way that makes it easy to understand.

The course, like it's prerequisite [Bit-O Data Structures](https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a9d59658-4e3c-441e-973b-147cc3c7e9de/666a9872-74d2-46d9-910a-63581b306302/), is written in Python, so most of the algorithms you write will be Python classes. Aside from the Python coding exercises that you can complete in your browser, there's also multiple choice questions that help ensure you've digested the reading material. Sometimes the more math intensive stuff simply can't be learned easily through code, so you've got to do a bit of reading.

While it's not completely necessary to take my [Big-O Data Structures](https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/a9d59658-4e3c-441e-973b-147cc3c7e9de/666a9872-74d2-46d9-910a-63581b306302/) and [Big-O Algorithms](https://boot.dev/course/884342fc-5469-47b4-8125-8bfc897428a8/67214b76-2e4b-4fc1-9610-2cf8c7c1c3a2/02e0d979-6758-493f-bf4f-bf7256fa7174/) courses first, I would recommend it, even if you've learned this stuff before. It doesn't cost any extra, and the refresher will really help. I won't rehash all the Big-O complexity stuff here, because I'm assuming you're already familiar with it. In this course, we focus on implementing some of the more advanced algorithms that you would learn in a CS undergraduate degree and learn how you can recognize when algorithms of this sort will help you in your future career.

## What's included?

There are four modules.

### Module 1 - Graph Theory

In this module, we have a brief refresher on graph data structures, and implement some basic traversal algorithms like breadth and depth-first search. We also cover different types of graphs, like complete and directed graphs, and how they can be represented in code.

### Module 2 - Advanced Searches

In this module, we really round out our experience with graphs. We learn about greedy algorithms, and how they can help us write faster code. We also implement a priority queue so that we can use it as we do a deep dive on Dijkstra's algorithm. Finally, we finished the module by writing an A\* search that can find it's way quickly through a muddy map - similar to what you'd need to write as a game developer.

### Module 3 - Dynamic Programming

In this module we shift gears, and learn about how memoization and tabulation techniques can be used to optimize various algorithms by trading memory for speed. We re-write the classic fibonacci function using dynamic programming, as well as the super useful edit-distance algorithm. Edit distance is used in the real world to calculate the similarity in spellings between words, just like how spell-checkers work.

### Module 4 - Linear Programming

In the final module, we shift course yet again to focus more on the mathematical side of things. Linear programming is a technique used to solve linear systems of equations, specifically optimization problems. We build from scratch a Simplex solver in Python and use it to calculate the exact number of cookies and cakes a baker should produce in order to maximize the profit in her shop.
