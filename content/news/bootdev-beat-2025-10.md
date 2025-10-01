---
title: "The Boot.dev Beat. October 2025"
author: lane
date: "2025-10-01"
categories:
  - "news"
images:
  - /img/800/pythogoras.webp.webp
imageAlts:
  - "Pythogoras the Serpent God"
---

Searchable challenges in the Training Grounds, and realtime voice chats with Boots are now a thing. Also, my children and those of half my employees are sick with the flu... I hope you've all been able to avoid it!

Tiredly,
Lane

## Patch notes

### 1. Search for Challenges

Reception of the [Training Grounds](https://www.boot.dev/training) has been fantastic - for the last four weeks we've been laboring to make updates according to your feedback. Our aim has been to improve the quality and relevance of the challenge problems - the biggest update is that you can now **search for existing challenges** to work on instantly!

![search for challenges screenshot](/img/800/searchchallenges.png.webp)

### 2. Realtime Voice with Boots

Real-time voice chats with Boots are now live! We've replaced the "record a message" functionality with an actual "phone call" with Boots. Each time you begin speaking, if your code editor has changed, he automatically has the new context, so you can have buttery smooth conversations with him about the state of your editor.

![realtime boots chat screenshot](/img/800/realtimeboots.png.webp)

Note: we're not exactly sure how expensive this is gonna be under production usage, so there may or may not be daily usage limits of some sort implemented at some point, but for now we're just monitoring it to see what that looks like, because realtime chat tokens do be expensive out here.

### 3. New Chapter of Lore

We're now up to **9 chapters of [lore](https://www.boot.dev/lore)** in the Boot.dev universe! If you're unfamiliar, this is a web novel about Boots, Ballan, Kahya and friends. It's where the characters for the Boss battles come from. Here's an excerpt from the latest chapter:

> Boots set them down some distance away from the prison, in the shadow of the Western Ward. The enormous pylon, for all its purported magical properties, felt mostly inert to Ballan's senses. He supposed that was because the magic it was generating was diffused over a large area. Everyone knew the wards deterred larger monsters and other creatures from the Wilds from approaching the area. All to keep the city of Avony safe - and it worked. Avony was one of the safest places in the World, as far as Ballan knew.
>
> Which was why he found himself reflecting on how many times he had almost died recently. It was… too many. More than three? And how many times had he been an inch from death without knowing it.
>
> Ballan stared blankly at the smooth, brown stone of the monolithic Ward. Vaguely he was aware of conversation happening around him, but he did not really come back to his senses until Tilda walked up to the Ward, felt around for a moment, and then removed a stone plate from the structure, revealing a small… hiding place of some kind?

- [...read the full chapter here](https://www.boot.dev/lore/moment-to-breathe).

### 4. Miscellaneous improvements

- Cryptography courses now use Argon2ID instead of Bcrypt
- AI Agent course now renders calculator output nicely through the LLM
- Updated all Go content to Go version 1.25
- Improvements to the training grounds testing you on unlearned topics
- Boots now uses Claude Sonnet 4.5 instead of 4
- Major updates to DSA2 course and Get a Job Course - more to come
- K8s course now uses Gateway API insead of Ingress

## What is yet to come

- A new Bash course
- A new logging and telemetry course
- A new RAG course
- More data analytics courses
- Walkthrough of the HTTP servers course
