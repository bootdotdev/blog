---
title: ""
author: Lane Wagner
date: "2021-04-05"
categories: 
  - "computer-science"
  - "news"
draft: true
---

GitHub has been re-founded on copilot, rumors of an AI superior to GPT-4 are abounding, and you still can't even write a red-black tree.

I'm rightfully asked frequently about the future of AI-assisted programming, and while the short answer is "I don't know", boy oh boy do I have some opinions to share.

## First, let's understand the state of the world

GPT-4 is, at least as I write this, the most advanced general-purpose LLM model on the market. It's important to understand that there is a big difference between a product that uses a model, and the model itself. For example:

* Chat GPT is a web app that uses GPT-3.5 and GPT-4
* Boots is our (Boot.dev's) GPT-4 powered teaching assistant
* GitHub Copilot is a VSCode plugin that uses GPT-4 (although I believe its a modified version)

It's important to understand that there is a *really big* difference between the GPT-3.5 and GPT-4 models. GPT-4 has about **10x** more parameters than GPT-3.5 and is trained on a much larger dataset. "Parameters" is a confusing term, but it's basically just the number of decision-making knobs the model has fine-tuned throughout its training. To get really hand-wavy about it, the more parameters a model has, the more sophisticated its understanding of the world can be.

It's worth understanding the difference between GPT-3.5 and 4 because I've heard quite a few people say, "eh, Chat GPT is not that great", only to find out they had only tried GPT-3.5. Chat GPT is not a model, it's just a web app.

## Will AI eventually replace all knowledge workers?

Probably. I don't see any reason from a physics/information theory perspective as to why it wouldn't, but the key phrase is "eventually". Saying "the market will crash" is almost certainly true, but it's not very useful. The question is *when*. You can only profit as an investor if you can predict with some accuracy *when* a market will crash.

The big problem is that it seems unclear whether improvements in the effectiveness of LLMs will have compounding, linear, or diminishing returns.

![growth graph](/img/800/growthgraphai.png.webp)

What often happens in the world of technology is that a new technology is invented, and it has compounding returns for a while, but then it hits a wall and we sit around waiting for a breakthrough in science to push us to the next level. For example, the invention of the magnetic hard disk was a huge breakthrough, but spinning disks can only get so small and fast. SSDs were a huge breakthrough, but they also have limitations in size and speed. LLMs are obviously a big step forward in AI, but the question is whether or not we'll hit a wall and have to wait around for something novel before we get AGI.

If LLMs turn out to have compounding gains in effectiveness for long enough (blue line), we might as well all give up now. Ultron will exist within the next few decades, and the last thing you'll have to worry about is whether your Python skills are marketable or not. The only issue in the case of AGI is whether or not the value produced by AI is harnessed and distributed to humanity in a way that you can benefit from.

However, if the returns of LLMs turn out to be linear or diminishing, or even just *become* linear or diminishing, then we knowledge workers will continue to have an important part to play in the world economy.

## I'm gonna fire my developers and hire GPT-4

I've been aggressively using and testing GPT-4 ever since it was released. I run a business where essentially all costs are labor costs that can be categorized in two ways:

* Creating text-based content
* Writing software

As it so happens, those are the two things that GPT-4 is best at, so if I can increase efficiency in those two areas, I can dramatically increase my profit margins. You can see why I've been so interested in GPT-4.

First, let's talk about **firing Allan**, my most tenured full-time employee.

I pay for ChatGPT Pro and GitHub Copilot for everyone at Boot.dev. I figure if it makes them even 5% more effective, it pays for itself. I'll get into specifics later about *how* exactly LLMs help us, but to slap a number on it, I'd say that they're making us around 10-20% more effective with our work. Certainly enough to pay for itself, but not enough to drastically disrupt our operations at the moment.

But for the sake of argument, let's pretend that GPT-4 makes developers 400% more effective. What do I need Allan for right??? I can just fire him and do all his work myself. I'll even have hours to spare!

This is smol-brain business logic.

I have an *incredible amount* of technical projects that, upon completion, will add immense business value. Major refactors and migrations, ambitious new features, and annoying bugs that at present are sitting *way back* on the back burner. It's all about balancing ROI at companies, and the companies that reinvest in growth outpace the ones that don't.

If I got 400% more out each dev I hire, I'd hire *more* devs, not *fewer*. I'd be able to tackle more projects, and I'd be able to tackle them faster. Now, there are obviously companies that don't work this way as well. For example, maybe companies that don't sell tech as their product will be able to get away with fewer devs working on internal tooling and IT systems. However, for companies like mine where technology is the driver of revenue, I don't see why I would want fewer devs, even if GPT-4 were 10x more effective.

## But you won't need developers, just product managers

Sorry if you're a "product person", but whenever I hear that it immediately translates in my head to "I'm the ideas guy".

![idea person product manager anakin meme](/img/800/anakinpadeproductmanager.png.webp)

So the idea here is that, well, maybe you won't need fewer people, but they won't need to be developers. Anytime they need to write code, they'll just whip out the 'ol LLM and get to work.

To be clear, *we have experience with this already*. In the early 2000's, if you wanted to do ecommerce, you had to hire a developer to build you a custom ecommerce site. They had to build shopping carts, checkout, coupon codes, billing, inventory management, all from scratch. Today, if you're doing something super common, like ecommerce or blogging, there are zero reasons to build it from scratch.

Despite the proliferation of low-code tools over the last 20 years, the demand for developers has only exploded over the same period. Why? Because even though we automate vast swaths of common functionality, companies are constantly looking to get an edge, either by building internal tools to increase their own efficiency, or by building novel software products that they can sell to others who want that edge.

So, will LLMs make certain tasks that only developers can do today more accessible to non-developers? I believe so. Let me give some examples.

## ChatGPT makes Winston a coder

The blog you're reading right now is a static site generated with Hugo. Blog posts are written in Markdown, and Git/GitHub is our CMS (content management system).

We have an employee here at Boot.dev that takes care of a lot of the non-technical operations tasks. He's a great writer, he's creative, but hasn't done much with code in the past (though ofc now learning on Boot.dev). Before ChatGPT I would have had to provide a ton of documentation to him on how to use VS Code, edit markdown, commit to Git, and open pull requests for him to make changes to the blog.

I've given him access to ChatGPT Pro, and, yes, it takes him longer than it would take one of our engineers at present, but he's able to walk himself through the process much more quickly than he could have just Googling and reading documentation.

The flip side of this is that if I assign one of our engineer's bug tickets to Winston, ChatGPT access is not closing the knowledge gap required to make effective changes, and it's not even close.

## I've tried to write blog posts with ChatGPT

GPT-4 is really good at dumping mostly accurate information onto a page, in the voice of a well-known author. It's *truly terrible* at writing something engaging that feels human.
