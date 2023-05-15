---
title: "Practical Patterns for Technical Writing"
author: Ben Barten
date: "2020-09-22"
categories: 
  - "clean-code"
images:
  - /img/800/Practical-Patterns-Techincal-Writing.webp
---

Writing technical documents like API or architectural documentation which exceeds a simple flow diagram can be a daunting task. If you have some experience with technical documents, you will probably agree that there is nothing more frustrating than bad documentation.

Lately, technical writing has become a more important part of my job, so I put together some of my findings. I use the following checklist and hopefully, it can help you as well.

## Overview

We will work our way from a very high-level view of the document to a detailed analysis of how various word choices can make a technical document more readable. We'll go over:

1. Your audience
2. Structuring your document into paragraphs
3. Active voice vs. passive voice
4. Writing clear and concise sentences
5. Simple but undervalued: lists & tables
6. The actual words
7. Iterate and review
8. Conclusion

## Your Audience

Before you start writing, you should **be clear about who is your audience**. In some cases, it might make sense to explicitly state who this is in the actual document. Make clear which knowledge or skill prerequisites the reader needs to have to understand your document.

Technical documentation aims to break down a complex topic to make it understandable to a broader audience. Therefore, your writing should fit your audience. Use simple words and do not try to sound overly professional or academic. Avoid slang and try to stay culturally neutral.

## Structuring Your Document Into Paragraphs

The system you are describing usually consists of multiple parts. The structure of your document should mimic these parts and nothing more. There are multiple studies on [how people read online](https://www.nngroup.com/articles/how-people-read-online/). In short, people usually scan documents and do not read every sentence. Thus, t**he structure of your document should be self-explanatory**. If a reader needs to read a two-sided introduction to understand what the document is about, it is likely that you will lose their attention.

To make your structure easily understandable, it helps to ask the three Ws which I picked up in this [Google course on technical writing](https://developers.google.com/tech-writing/overview).

### The 3 W's

1. What are you trying to tell the reader?
2. Why is it important for the reader to know this?
3. How should the reader use this knowledge?

## Active Voice vs. Passive Voice

One of the most important things I've learned was the difference between active and passive voice. Here is an example:

Passive voice: **The data can be requested from the resource via this endpoint.**

Active voice: **Request the data from the resource via this endpoint.**

Active voice is more precise on what to do and is typically also shorter and easier to process. Passive voice, on the other hand, is indirect and does not make clear who or what the actor in the sentence it. We know that the data can be requested from the resource, but who should be doing it?

If you spot passive voice in your documents (form of be + past participle), try to convert it to active voice to make it more direct.

## Writing Clear and Concise Sentences

Technical writing aims to transfer complex knowledge to a broader audience. Therefore, clarity is a top priority. Write short sentences with precise, strong, and specific verbs that leave no room for misinterpretation. Concentrate on the actual facts and avoid marketing speak. Technical writing does not want to convince the reader, because they are already convinced by the time they are reading the document.

Most likely, you are more familiar with clean code principles than writing skills. Luckily, best practices from the software development world can be translated into technical writing. Here are some easy rules which might remind you of some coding principles:

- Keep your sentences short. Short sentences are easier to read, maintain and process.
- One sentence should focus on one idea.
- Eliminate or reduce extraneous words (i.e. at this point in time → now, determine the location of → find)
- If a sub-clause introduces a new idea, consider putting it in the main clause.
- Convert long sentences into lists.

## Simple but Undervalued: Lists & Tables

Lists and tables are beautiful tools to structure your document and improve how understandable they are.

### Lists

First of all, every list should be introduced by a sentence that describes what the list contains. Bulleted lists are used for unordered lists and numbered lists for ordered items. If your list item is a sentence then you should use sentence punctuation. If it is not, leave out the punctuation completely. Numbered lists often describe a sequence of steps to follow. Therefore, you should start items with imperative words to make the intention clear.

### Tables

Tables basically follow the same rules. Make sure to have **clear headers** for every row and column. Avoid putting more than two sentences into a table field. Otherwise, it will easily be bloated and hard to understand for the reader.

## Word Choice

So far, we've had a high-level view of the concepts of technical writing. Here are some really easy to use tips on how to improve the actual words you are writing.

**Define new or unfamiliar words.** If a word is likely not familiar to part of your audience, explain it. You can link to an existing resource or if you introduce the term, make sure to define it. There is nothing more frustrating than reading an explanation that contains words you don't understand.

**Use terms consistently.** If you start by using a certain term for something, do not introduce many variations of it. If you have to, make it clear to the reader (i.e. "Golang, or Go for short")

**Use acronyms properly.** Acronyms should always be introduced. Even though it might be obvious, do it anyway. Write the full term with the acronym in parentheses bold. (i.e. **Transfer Control Protocol (TCP)**).

**Disambiguate pronouns.** Pronouns can only be used after introducing the noun. Furthermore, they should be used as close as possible to the noun. A rule of thumb can be: If you introduced a second noun between your noun and the respective pronoun, avoid the pronoun and rather repeat the noun.

## Iterate and Review

As with anything, iteration, fast feedback, and reviews are important. Make use of the people around you. Maybe some of the people you work with are similar to your target audience. If you do not have access to people for a peer review, you can define personas and try to put yourself into the shoes of one of these personas and read your document.

## Conclusion

Following these rules will most likely improve your technical writing by quite a bit. Especially in smaller companies, where you do not have explicit technical writes, learning this skill is quite valuable. Documentation is key to providing an excellent developer experience for your users.

  
If you want to know more about the topic or have a chat, I am happy to talk to you. Just follow me on Twitter at [@ben\_barten](https://twitter.com/ben_barten). For more of my content, check out [benbarten.com.](https://benbarten.com/)
