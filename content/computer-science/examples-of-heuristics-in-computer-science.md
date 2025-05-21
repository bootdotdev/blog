---
title: "Examples of Heuristics in Computer Science"
author: winston
date: "2020-11-30"
categories:
  - "computer-science"
images:
  - /img/800/ruinreborn_fantasy_art_simple_background_map_--ar_169_--profi_2fd12f2f-856b-47aa-b621-93e69f142dea_3.png.webp
---

Heuristics in [computer science](/computer-science/comprehensive-guide-to-learn-computer-science-online/) and artificial intelligence are "rules of thumb" used in algorithms to assist in finding approximate solutions to complex problems. Often, there's simply too much data to sift through to come to a solution promptly, so a heuristic algorithm is used to trade exactness for speed. However, because heuristics are based on individual rules unique to the problem they are solving, the specifics of the heuristics vary from problem to problem.

Heuristics aim to produce solutions in a _reasonable time frame_ that are _good enough_ for solving the problem at hand. The solution produced using a heuristic may not be the perfect or exact solution, but it's valuable as an approximate or best-guess solution. Some problems would require hundreds of thousands of years for an exact answer, but we can produce an approximate solution almost instantly.

## Heuristic Trade-Offs

The entire value proposition of a heuristic is based on trade-offs. Typically we are trading accuracy for time. That said, there are several different levers we have to pull when designing a good heuristic.

- _Optimality:_ Many problems have multiple solutions, for example, "what is a good path to get from city A to city B? Do we need the best path, or will a good path be good enough?
- _Completeness:_ When there are multiple valid solutions to a problem do we need to find all of them? Will a subset of valid solutions suffice?
- _Accuracy:_ Many questions don't have a correct answer. For example, "Will Tommy like a pair of boots or a pair of gloves for Christmas?" A heuristic can improve accuracy in these situations.
- _Execution time_: The primary goal of a heuristic is to provide a quick answer that's good enough. Some heuristics are only marginally quicker than classic methods.

Example problems and some of their common heuristics are given below.

## Traveling Salesperson Problem (TSP)

![](/img/800/tsp-1024x606.jpg)

The TSP is a famous [algorithm with a Big-O](https://www.boot.dev/courses/learn-algorithms-python) complexity of `O(n!)` and asks the question:

> Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

For a low number of cities, this question could be reasonably brute-forced. However, as the number of cities increases, it becomes increasingly difficult to come to a solution.

The nearest-neighbor (NN) heuristic solves this problem nicely: the computer always picks the nearest unvisited city next on the path. NN does not always provide the best solution, but it is close enough to the best solution that the difference is often negligible for the purpose of answering the TSP. By using this heuristic, the Big-O complexity of TSP can be reduced from `O(n!)` to `O(n^2)`.

## Knapsack Problem

![](/img/800/knapsack.jpg)

The knapsack problem poses the issue:

> Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

An example heuristic for this problem is a greedy algorithm, which sorts the items in descending order of value per weight, and then proceeds to insert them into the "sack". This ensures the most valuably "dense" items make it into the sack first.

## Search Optimization

Search engine optimization has been sought after for as long as search engines have been around. Individuals using search engines want to find the information they are looking for as swiftly as possible. With such an incredible amount of information available, search engines must utilize heuristics to expedite the search process. At the start, a heuristic could try each possibility at each step, but as the search continues, it can choose to stop the search at any time if the current possibility is worse than the best solution already located. In this way, the search engine can be optimized for speed and correctness.

## Applying Heuristics to Your Algorithms

To apply heuristics to your algorithms, you need to know the solution or goal you're looking for ahead of time. If you know your end goal, you can specify rules that can help you achieve it. If the algorithm is being designed to find out how many moves a knight can make on a square, 8x8 chessboard while visiting every square, it's possible to create a heuristic that causes the knight to always choose the path with the most available moves afterward.

However, because we're trying to create a specific path, it may be better to create a heuristic that causes the knight to choose the path with the fewest available moves afterward. Since the available decisions are much narrower, so too are the available solutions, and so they are found more quickly.
