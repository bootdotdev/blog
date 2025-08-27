---
title: Boot.dev Launches the Training Grounds
author: lane
date: "2025-08-27"
categories:
  - "news"
images:
  - /img/800/traininggroundsscreenshot.png.webp
imageAlts:
  - "Boot.dev Training Grounds Screenshot"
---

We've always said Boot.dev is fun... but we've never said it's _easy_.

I mean, it's not for lack of _trying_. We do everything we can to make the content as easy to understand as it can be:

- We make meticulous updates to the explanations and lessons based on user feedback
- We have an AI assistant (Boots) that helps you when you get stuck
- We provide solutions to every challenge if you're _still_ stuck

What we _won't_ do, is _not_ teach the hard stuff. Some traditional bootcamps and e-learning platforms simply avoid the problem altogether by pretending that you don't need to learn hard things... we don't like that. That has the side-effect of flooding the market with lower-skill developers who expect to land jobs they aren't qualified for.

So we've never been interested in that.

Boot.dev takes time, and yes, at times the courses are hard. But there's not much worth doing in life that's easy, right?

Okay so what do I mean by "hard"? Well, its not like the courses skip stuff or explain it poorly. I know that's a bold claim, just know that we at least _try our hardest_ by spending a lot of time tweaking the content and making micro-quality-updates based on your reports:

![closed ticket reports on Boot.dev](/img/800/userreportsscreenshot.png.webp)

_We've handled 21,219 reports on lessons_!

So no, when I talked about "hard" I'm talking about a **lack of practice**. That's where we've _failed_.

For example, say you're learning about functions in Python, you:

1. Read the explanation
2. Watch the video
3. Start the challenge.
4. Get stuck
5. Chat with Boots (AI assistant)
6. Complete it with his helpful nudges

Great. You solved it. But are you really ready to move on to the next concept?

You got _help_ with functions... so it would be nice if you could now pracitce functions _again_, and hopefully complete it this time _without help_?

Well, pre-training grounds, you only had two options:

1. Reset the lesson and do it again - but that sucks because you already know the answer to that one
2. Forge ahead to the next concept and challenge - but now you're building on top of a shaky foundation.

So it can feel like everything is moving really fast. And the answer the the problem?

**More practice challenges of course**!

But that's easier said than done.

We have over 2,500 hand-crafted lessons and their associated challenges on Boot.dev, so to add just 2 more optional challenges to each lesson would mean we'd need to write 5,000 more lessons by hand. That's a lot.

But the _worst_ part about doing that is that _most_ students don't need all 5,000. They only need a few extra practice challenges on _specific_ lessons. Which lessons? That varies wildly from student to student.

So even if we did all that work (which would mean releasing fewer new courses) we'd still have some concepts with not enough practice, and many with more than anyone needed.

All this to say... we launched The [Training Grounds](https://www.boot.dev/training) today, **and it solves this problem**!

Of course it's 2025 so obviously it's an AI thing, but I swear it's not just one shot slop! we've been working on this system for quite awhile now, and a lot goes into it. It works like this:

1. You click "Next Challenge"
2. The system looks at:

- What courses you've completed
- What topics you've learned recently
- What you've been struggling with
- What might need to be reviewed based on time elapsed ([spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition))

3. Based on all that it selects a topic, a difficulty, and a challenge type, and other metadata that will consistute a "good challenge" for you
4. It sources examples from our existing hand-written challenges that match the type of challenge it's trying to create
5. It creates a new challenge from scratch (GPT5/Claude Sonnet 4 at time of writing), using those examples as inspiration
6. It runs the challenge on our backend to ensure it's valid and has a correct solution
7. It makes any updates based on the execution results
8. It serves it to you in the Training Grounds

Now, you _do_ occasionally get a really dumb AI-slop challenge. Cost of doing business with AI I guess.

But not very often - we've been working really hard to fine-tune the system. And as we get more and more skip/rating feedback into the system, we should be able to ship some big quality improvements over the next few months.

And of course you can skip a challenge at any time and provide a reason, and the system will see that note and generate fewer challenges like that for you in the future.

Now the biggest drawback at the moment is that we've been entirely focused on the _quality_ of challenges - so... it's **kinda slow**. It takes about **45 seconds** to generate a new challenge. That's a limitation of how quickly our backing LLMs can output the tokens to write the challenges. Thinking tokens are slow and expensive, but the quality is so much better that it's worth it.

That said we have some ideas for updates over the next couple months that will make challenge assignment a _lot_ faster - things like reassigning already generated 5-star challenges across students, and pregenerating challenges in the background.

So anyways, here's the [link to the Training Grounds](https://www.boot.dev/training) if you want to check it out!
