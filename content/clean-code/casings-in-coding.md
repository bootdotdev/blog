---
title: "Snake Case or Camel Case? A Guide to Programming Naming Conventions"
categories: 
  - "clean-code"
author: Lane Wagner
date: "2022-12-09"
images:
  - /img/800/snakescamels.png.webp
imageAlts:
  - "Art by Stable Diffusion. Prompt: 'snakes and camels sci fi cinematic'"
---

The following names are all *valid* variable names in nearly every programming language:

* `dogName`
* `dog_name`
* `DOG_NAME`
* `dog-name`

But which one should you use in your projects? Let's chat about the popular naming conventions used in programming, and why you might choose one over another.

Snake case and camel case are probably the most popular styles, so let's cover those first.

*If you'd rather watch than read, then here's the video version of this article.*

{{< bdyoutube u9ue_Oj-rVg >}}

## Snake Case

Snake case, also known as "underscore case," uses underscores to separate words in a variable or function name. For example, a snake case variable might be named `user_id` or `user_name`. This naming convention is commonly used in programming languages like:

* Python
* Ruby
* PHP

## Camel Case

Camel case, on the other hand, uses no separators between words but capitalizes the first letter of each word except the first word. For example, a camel case variable might be named `userId` or `userName`. This naming convention is commonly used in languages like:

* Go
* JavaScript
* Java
* C#

{{< cta1 >}}

## Which is the best casing style for code?

So which convention should you use? The answer ultimately depends on your personal preference and the conventions used by your team or the language you're working with. However, some general guidelines can help you make a decision.

First, consider readability. In general, snake case is considered easier to read because the underscores make it clear where one word ends and the next begins. Camel case, on the other hand, can be harder to read because the lack of separators can make it difficult to quickly parse a variable name. That said, I find camel case easier to *write*. Camel case doesn't require the use of the `shift` key, and uses one less keystroke.

In the end, the choice between snake case and camel case is largely a matter of personal preference and the conventions of your language or team. Whichever convention you choose, the important thing is to be consistent and use a naming convention that makes your code readable and maintainable.

## Less popular casing styles

### Pascal Case

This convention is similar to camel case, but it capitalizes the first letter of every word, including the first word. For example, a Pascal case variable might be named `UserId` or `UserName`. This naming convention is commonly used in:

* Delphi
* Object Pascal
* Vue and React component names
* Exported symbols in Go

Like camel case, Pascal case can be harder to read than snake case because of the lack of separators between words. However, it does have the advantage of being easy to differentiate from camel case when scanning a block of code. Some programmers prefer Pascal case for this reason, while others find it less readable than camel case or snake case. Ultimately, the choice between Pascal case and the other conventions is a matter of personal preference and the conventions of your language or team.

### Kebab Case

Kebab case is also known as "hyphen-separated lowercase" or "spinal case." This convention uses hyphens to separate words in a variable or function name, and all words are lowercase. For example, a kebab case variable might be named `user-id` or `user-name`.

Kebab case is not as commonly used as the other conventions, but it is gaining popularity in some circles. Like snake case, it is considered easy to read because the hyphens make it clear where one word ends and the next begins. However, some programming languages do not allow hyphens in variable names, so you may need to use a different naming convention if you're working in one of these languages.
