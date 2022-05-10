---
title: "The Problem with Education is a Problem of Incentives"
author: Lane Wagner
date: "2022-05-10"
categories: 
  - "education"
images:
  - /img/800/cellular-education-classroom-159844.webp.webp
---

I've found that almost anyone I talk to agrees with the statement:

> There is something wrong with education, particularly higher education.

Interestingly enough, everyone also has very different ideas about what the problems are, and how we should solve them. A few popular ideas include:

* Pay teachers more
* Make university free
* Cancel existing student debt
* Online-first university

A couple weeks ago I was listening to an old [Indiehackers](https://www.indiehackers.com/) podcast where the interviewer was speaking with Austen Allred, the founder of Lambda School (now Bloom University). Austen said that he believed the biggest problem with education is one of incentives - particularly that *universities don't care whether or not their students are placed in a good job upon graduation*. I tend to agree, though [Boot.dev](https://boot.dev), my current side-project, has ended up taking a different path than the one Lambda took.

Lambda School has been in the news over the past few years, sometimes good things were reported, sometimes not. I'm not here to gossip, instead, I simply want to look at them as an example of how Austen's original beliefs on educational incentives ended up panning out. First, let's talk about where Austen and I agree, and then we'll get into some of the things I think we can learn from Lambda school, and how we can make education even better.

## What does it mean to "align incentives"?

Let's look at a simple example using a hypothetical company "Auto Parts United". Here are a few of their salespeople, all of whom will be guinea pigs trying out 4 new compensation structures.

| Name   | Base | Commission | Explanation                                               |
| ------ | ---- | ---------- | --------------------------------------------------------- |
| Sally  | 50k  | 10%        | Flat 10% commission                                       |
| John   | 100k | 0%         | No commission                                             |
| George | 40k  | 10%, 20%   | 10% commission for the first 10 sales, then 20%           |
| Taylor | 70k  | 10% capped | 10% commission for the first 10 sales, then no commission |

Based on historical data, the accounting department at "Auto Parts Unlimited" was able to show that if a salesperson made the *average* number of sales, 20 sales each month, then all of these compensation packages would end up paying them the same $100k yearly. As you can probably guess however, these different compensation structures create **very** different incentives for the salespeople.

Now, I don't run a sales organization, but I can tell you with confidence that the "Johns" and "Taylors" of the company aren't going to be great performers once the new compensation packages are rolled out. They aren't incentivized to sell! John is incentivized to *appear as if* he is sellng so he doesn't lose his cushy 100k salary. Taylor is incentivized to quickly make 10 sales, then slack off for the rest of the month.

Only "George" and "Sally" have their incentives *aligned* with those of the company. When the company does well, George and Sally do well. This kind of system is ideal in almost any relationship that can support it. Win-win/lose-lose deals are much more sustainable than any sort of once sided structure. We see examples of this kind of alignment all over the place, though some end up being less aligned than others. For example:

* Pay-for-what-you-use server costs
* Percentage-based transaction fees
* Free returns on e-commerce purchases

## The problem with university

I think it's safe to say that Austen was right when he pointed out on the podcast that universities aren't incentivized enough to care about job placement rates. Not only do the institutions have no reason to worry about job placement, oftentimes the professors themselves consider teaching an afterthought. Many are there primarily to do research, publish papers, and advance the boundaries of their field.

## How Lambda School approached a new incentive model

Lambda was the pioneer of the "income share agreement", or ISA. The idea is that you do not pay upfront for your tuition. Instead, *if* you get a job upon graduation, you pay the school back a percentage of your wages until you hit a cap. What this does is ensure that Lambda School is incentivized to make sure you get a job upon graduation.

Okay, so far so good. ISAs fixed everything right?

## If ISAs are so great, why all the fuss about Lambda?

If you want to dig up the dramatic history about Lambda School I'll let you do that, I don't want to get into the nitty-gritty of he said/she said. Instead, I'll give you my summary based on the digging I've done. I've found that most of the more viral complaints boil down to two simple gripes.

1. Some students have vocally complained that the quality of the education has declined over time.
2. Some students consider it to be *very* expensive. Most students end up paying somewhere between $20,000 or $40,000 dollars for the ~6-month program.

If I had to guess about the cause of these problems, I'd say it's likely that margins ended up being tighter than anticipated, and the bets they made on their student's placement rates ended up being worse than anticipated. Lambda pays for each student's education up front, *whether or not* that student gets a job. If any poor-performers are sucking up resources without landing jobs, Lambda is footing the bill. Over time, Lambda gathers data on their costs, and realizes they need to charge a lot of money to the best performers to subsidize the cost of those who don't pay.

This gets interesting because while it *sounds like* Lambda is paying for the education of any students who are unable to get jobs. In reality, if Lambda is to continue as a successful business, the high performers end up paying for the tuitions of the under performers.

To sum all this up, what is Lambda *highly* incentivized to do?

* To only allow the highest performers into the program, who ironically are the ones who need it least.
* To ensure that everyone who goes through the program lands a job paying at least $50k

Let's review what they *are not highly* incentivized to do:

* Teach their students in a way that will help them advance post-placement
* Provide an education to those that are less likely to be high performers

## What other models could be better?

Instead of immediately hypothesizing about better solutions, let's look at a few more competitors in the "learn to code" space, and guess at what incentive structures they might have.

### Dev Mountain

Dev Mountain is a traditional web development bootcamp in my area. I expect their product is similar to Lambda in that it's an in-person web development school. They charge around $10k for a 16-week program.

#### Likely incentivized to:

* Prepare students for a job, but only so they can keep their marketing "placement rate" high.
* Keep costs lower so that students can afford them up-front

#### Not likely incentivized to:

* Create an engaging and motivating experience
* Care how much students earn in their first job

### Codecademy

Codecademy has a straightforward business model. They charge $19-39 per month at the time of writing for "pro" access to their online courses. Unlike lambda school, their digital content is consumed at scale asynchronously by students, meaning they can get away with *much* lower tuition costs.

#### Likely incentivized to:

* Create an engaging experience so that you don't cancel your subscription
* Keep the monthly cost low to compete with other digital information products

#### Not likely incentivized to:

* Prepare students for a job
* Care how much students earn in their first job

### FreeCodeCamp

FreeCodeCamp is unique on this list - they're totally free! That said, that doesn't mean the creators and maintainers don't have an incentive structure. There is always an incentive mechanism, even if it's not obvious.

#### Likely incentivized to:

* Keep costs extremely low
* Monetize users indirectly (for example via ads, data mining, or something else)
* Prioritize traffic and engagement over learning outcomes

#### Not likely incentivized to:

* Prepare students for a job

### Udemy

Udemy is a marketplace, they don't create their own content, instead they allow creators to publish their work on the platform and then Udemy takes a cut.

#### Likely incentivized to:

* Emphasize a *quantity* of learning content
* Prioritize content made by teachers who have marketing skills

#### Not likely incentivized to:

* Prepare students for a job
* Create a cohesive learning path

## So what would a better incentive structure look like?

First off, let's address the elephant in the room, I'm a big 'ol hypocrite at the moment. [Boot.dev](https://boot.dev) is my side project, and its business model is basically a carbon copy of Codecademy's. For now, I'm trying to get the project to a level of revenue where I can afford to go full-time on it. In the meantime, I'm thinking about how a different model could create a better incentive structure. We'll get there, but we aren't there yet.

Okay, so what might this "better model" look like? Well, we want a platform that is strongly incentivized monetarily to do as many of the following as possible:

* Create an engaging experience while prioritizing learning outcomes
* Ensure students land their first coding job
* Help students continue to be successful in their careers after their first job
* Prioritize quality over quantity so that the best materials are easily accessible
* Refrain from serving ads or selling user data
* Ensure that slower learners can be successful as well
* Keep overall costs for students as low as possible so that price is never a barrier

### Free + recruitment fee

One plan would be to go the FreeCodeCamp route. We could open up all the learning content for free, then instead of selling ads, I could monetize through job placements. I'd like to do more research on this path, but with the data I have currently I forsee some problems:

* Companies won't pay to recruit junior talent, only senior talent
* Boot.dev would be incentivized to create an amazing product for recruiters while education becomes an afterthought
* There is no monetary incentive to help students who get stuck - they are likely under performers who won't be placed

### Codecademy + Career coaching/tutoring services

The big problem with our current model at Boot.dev (the Codecademy model), is that we have no real monetary incentive to help students land a high paying job, other than to collect some sweet testimonials. We also aren't incentivized to care about what happens to them after they graduate. In fact, you could even argue that our current model actively doesn't want them getting a job, because they will be more likely to cancel their subscription.

This is the hypothetical model that I think has the most promise:

1. Students pay a small monthly tuition for access to the learning content

This ensures that the learning side of the platform remains top-of-mind for us. When I say small, I mean less than it is now. Something like $15/mo. I never want to be turning people away due to a price barrier.

2. A free-if-you-get-placed career coaching funnel for students that complete our materials.

The career coaching services and materials would ensure that we care about the career success of our students. We could even offer them to those who are looking for second and third jobs, or even just looking to get promoted or snag a raise. It also has the nice side-effect of helping us keep our learning content streamlined and career-applicable, because in order to maximize revenue we need to be able to place those students in jobs.

Payment for the optional career coaching might be an ISA model, or maybe it's a flat fee that's paid back x months after the desired career outcome - I'm not sure. But all in all, I think this **could** be a great path forward for us. 

If you have any other ideas, or think we could be doing something better, let me know on [Twitter](https://twitter.com/wagslane). Also, if you know anyone who's looking to throw funding at a project with traction, we're [happy to chat](/contact).
