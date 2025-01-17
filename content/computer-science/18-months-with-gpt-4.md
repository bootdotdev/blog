---
title: "18 Months with GPT-4: Now Can I Fire my Developers?"
author: lane
date: "2025-01-17"
categories:
  - "computer-science"
images:
  - /img/800/golemnumber2.png.webp
imageAlts:
  - "fantasy, golem, wizard, wizard inspecting golem, fantasy golem, fantasy wizard, wizard pondering golem"
---

As the founder of a company where my largest static expense is engineering salaries, I'm over here just chomping at the bit, eagerly awaiting the moment I can fire everyone and line my pockets with all those juicy savings. See, about one year ago, I wrote an article titled, ["9 Months with GPT-4: Can I Fire my Developers Yet?"](/computer-science/ai-taking-programming-jobs) and I thought I'd give you a little update on Allan's employment status.

...he's still here.

![ron swanson glare](https://media.tenor.com/kSmVJHqqPtgAAAAM/ron-swanson-no.gif)

Actually, we've doubled the size of our dev team. So, what's the deal? Do I hate money? Is it because it's actually the new gpt4-o-3-preview-lightning that's the one that will make us all obsolete? Or am I maybe just a really bad prompt engineer?

Well, I can assure you [I don't hate money](https://www.boot.dev/pricing). And maybe the next model will be a game changer, but I'm not holding my breath. And honestly, I always considered myself a good Googler, and I think I'm a pretty good prompter.

So I don't know, but let's dig into some of my experiences over the last year.

## What's changed the most?

First off, the quality of code-related-responses from the "top" models like gpt-4o, and Anthropic's Claude Sonnet 3.5 are... _pretty amazing_. I mean, we're all kinda used to it now, but had you shown my workflow today to my developer self in 2019 I would have been floored.

_LLMs are great, and our whole team uses them daily_.

As a backend developer, I used to Google stuff... 50 times a day? Maybe more. It was a lot. Anytime I had even the smallest question, I'd hit Google. I would find docs, ask stack overflow, reference a blog post, research best practices, look for a vendor or library, the list goes on.

_But_, today **about 50% of those queries** I now send to an LLM instead of Google. That's a crazy number. But, it saves me time. Finding what I wanted via Google took maybe 2-3x times longer, because I now have an LLM chat directly in my editor at all times (shoutout [Zed](https://zed.dev/) btw).

If I'm skeptical of the response, its not working the way I expect, or I need a source, sure, I still use Google, but in many cases I actually trust the LLM _more_ than an outdated post on Reddit that's still somehow dominating the SERP. For example, the other day I was trying to use the Google Analytics API, and the feature I needed (I swear to God I searched for hours) wasn't documented anywhere. But, because the LLM had slurped up enough weird web forum data, it new what I should try. I tried it. It worked.

So at least on that front, Google is losing some ground to LLMs, but I'm still not any closer to firing Allan.

So, what's changed the most for me in the last 9 months? **More of my questions are sent to the AI**.

## Reformatting

Another one of my favorite uses for an LLM is to give it a dump of nasty data and to just ask it to put it in a nicer format. "Hey, my coworker sent me this JSON, can you put it into a Go struct"? Or, "I have this CSV, can you make it into a markdown table"?

I probably shouldn't trust it as much as I do, but I've yet to _notice_ an issue, and it does save me a lot of time.

## What about code generation?

Code generation honestly is less useful to me than just having a chat open where I can ask questions. That said, I do make use of inline code generation tools. My take? _It mostly just saves me typing time_. And I'm all for that, because I'm not the fastest typist in the world... I'm ashamed to say that after using a computer my entire life I only clock in around 80 wpm. Which actually isn't _too_ bad if you consider that I retaught myself to type the correct way just one year ago.

I've also found that I move a lot faster, particularly when writing Go. Go is a simple but fairly verbose language. It doesn't have much built-in syntactic sugar. My single most generated snippet of code?

```go
if err != nil {
    return fmt.Errorf("can't do the thing: %w", err)
}
```

I use inline code gen for other things as well, but honestly, I have been completely underwhelmed with its ability to _solve high level problems_. I've been impressed with its ability to predict the next couple of lines I was going to type, but all the problem solving typically happens as I'm _structuring_ my code and dancing around the codebase looking for clues, not as I'm _writing_ the solution.

For example, all before the auto complete has a chance to help, I'm busy:

- Reading the ticket
- Finding the disparate parts of the system it applies to
- Thinking through how potential solutions will affect existing users, existing infra, and the features I know we have planned for later
- Writing the shells of the functions I need to implement

_Most_ of the work of a developer has more to do with understanding the problem, the system, and how the users will interact with it than it does with the actual writing of the code. So, yes, I generate code, it saves me some time (particularly typing time) but I can't just give my barista a ChatGPT subscription and expect them to perform well on our dev team.

In my last article I said:

> ChatGPT and Copilot make us about 20-30% more effective with our (programming) work

That number hasn't really changed over the last year for me. Maybe it's up a percent or two, but its not a measureable difference.

## Anything else LLMs have been good for?

If we set aside the idea of automating traditional programming (product development) work, **yes**, there are a few things we've had massive (like 4x) efficiency improvements in thanks to LLMs.

### 1. Generating summaries

We write a lot of courses, and we write them by hand. AI slop is mostly just that, slop. It doesn't have personality, supplies no real world experiences, and has a terrible sense of humor. However, when we feed the _good, detailed, personable_ thing that we wrote by hand into the LLM, we can generate great cheatsheets of the material. That's what made it possible for us to quickly launch Boot.dev's new spellbooks feature.

### 2. Customer support

I do think LLMs pose a real threat to customer support roles. If your role can mostly be reduced to "read a thing someone sent in, categorize it into 1 of 6 common issues, and do a pre-defined thing" then you're probably going to be replaced by an LLM fairly soon.

We've built an internal bot that triages customer reported issues. It's not perfect, but we're always updating its prompt and examples, and we would spend at least 2x more time on customer issues if we didn't have it. It's also worth noting however, that the LLM isn't the _only_ part of that bot. A lot of the logic in the bot is just standard programming stuff, and would be _worse_ if we used an LLM. Things like connecting the customer's account to the issue, checking for duplicates, and chaining issues together are all done by "normal" code.

### 3. Translating programming language

This one's pretty unique to us, but we spend months writing these in-depth, interactive coding courses, and then we want to allow students to take them in other programming language. Same concept or project, new language. At the moment, we're translating a lot of our Go content into TypeScript. We've had a lot of success by feeding an LLM some well written Go code, and getting back some TypeScript that does mostly the same thing.

It's far from perfect. Maybe 50% of the output code is useable, and the rest needs to be refactored or rewritten, but I actually think there's some promise here. We don't do many leetcode-style practice challenges at the moment (like challenges not tied to a specific concept) but we have some ideas for how we could use LLMs to save us a ton of time creating pretty incredible practice and review problems... I'll have to update you on that next year.

## Wait, what about o1 and o3?

OpenAI's o1 and o3 models are interesting - they're _way_ slower and _way_ more expensive, but they outperform on a lot of tasks by taking advantage of "thinking time". OpenAI calls it "private chain of thought". I've had more success with o1 than with gpt-4o when it comes to more complex single-shot prompts (e.g. do this, then do that, then do that, then give me the result). The problem is, I just don't _have_ many problems that need that extra little boost of "thinking time". I usually need a fairly simple piece of information, or a bit of code reformatted, or a line of code generated.

I think o1 and o3 will have a big impact on very specific problems, but they've had far less impact on my day to day as a developer than gpt-4o and Claude Sonnet 3.5.

## Predictions for the next year

1. Developers will continue to use copilot-like tools more and more
2. More Google search queries will be replaced by LLMs
3. More developers will write code using LLMs to power internal automations for their companies
4. More developers will write code using LLMs to power user facing product features
5. Developers will continue to develop
