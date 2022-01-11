---
title: "Optimize For Simplicity First"
date: "2020-08-15"
categories: 
  - "clean-code"
tags: 
  - "sharing"
---

We can't optimize for everything in software engineering, so we need to start with _something_, and that something should be simple code and simple architecture. For example, to over-optimize for speed in JavaScript, we might write our [for-loops backwards](https://qvault.io/2019/11/08/benchmarking-array-traversal-in-javascript-going-backwards-is-fastest/) to the detriment of readability.

I believe we should optimize for simplicity _first_, and only make complex memory, speed, and abstraction changes as they become necessary.

## But Muh Speed

If it's slow but readable, I can make it fast. If it's broken but readable, I can make it work. If it's impossible to understand, then I have to spend hours trying to understand what the abomination is _supposed_ to do in the first place.

Working, readable software should be the "MVP" of your code. It's trivial to find a bottleneck in code that's easy to understand. That slow chunk of code can be optimized for speed when _and if_ it becomes necessary.

### A Small Caveat

There are cases in which it makes sense to take speed seriously upfront. For example, choosing which language or framework to use for a project is a decision that cannot be undone or changed easily.

## Memory Problems

Do you need Redis? But do you REALLY need Redis? Probably not. In the case of a web API, omit caching on your first iteration. Most servers don't require in-memory caching to effectively service users. When speed starts to become a problem, implement in-memory caching on the server itself if possible. In terms of overall system complexity, the only thing worse than code dependencies is external dependencies.

Only add a new database, queuing system, API service, or NPM module if there are no simpler options.

## Abstractions and DRY Code

There's nothing wrong with writing reusable functions, and most well-written functions will be reusable without adding any needless complexity. However, too often I've seen developers over-generalize a problem to the detriment of readability.

If there's currently only one place in your application where a function is being called, don't worry about making that function the most generalized version of itself. For example, let's say I have some validation middleware in my [Go API](https://qvault.io/golang/boilerplating-a-new-go-program-microservice/):

```
type apiParams struct {
	OrgID  string
	UserID string
}

func validateParams(params apiParams) error {
	if params.OrgID == "" {
		return errors.New("OrgID is required")
	}
	if params.UserID == "" {
		return errors.New("UserID is required")
	}
	return nil
}
```

A useful function to be sure, but my [craving for DRYness](https://qvault.io/clean-code/dry-code/) may tempt me to do the following:

```
type apiParams struct {
	OrgID  string
	UserID string
}

func validateParams(params interface{}) error {
	dat, _ := json.Marshal(params)
	mapParams := map[string]string{}
	json.Unmarshal(dat, &mapParams)

	for k, v := range mapParams {
		if v == "" {
			return fmt.Errorf("%s not found", k)
		}
	}
	return nil
}
```

We've succeeded in making the code more abstract, now any function can pass in any struct to check if common fields exist! The problem is that I've also added new edge cases that will certainly produce bugs under various conditions. For example, what if an integer is passed into my function?

The code was just fine as it was, we had no reason to generalize it. When we finally are forced to generalize it later we'll have more information about _how_ to build a good abstraction.

KISS > DRY. When used properly, DRY code will be simpler than it was before, I don't think these rules-of-thumb are in direct competition.
