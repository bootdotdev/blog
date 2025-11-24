---
title: "Breaking Into Tech on Hard Mode: A Supply/Demand Analysis of Career Options"
author: lane
date: "2025-11-23"
categories:
  - "jobs"
images:
  - /img/800/bootsthinkinschool.png.webp
---

Markets are efficient, _right_?

I understand that every ~10 years we find ourselves in _some_ sort of stock market bubble, but I do believe that _most_ markets are _mostly_ efficient. Everyone out there is looking for a good deal, and despite the well-known irrationalities of human psychology, most of us seem to do a good job of looking out for number one.

That said, when it comes to _which career in tech to choose_, I've come to believe that the market is **far from efficient**. Why? Because learners are choosing career paths on _hard mode_.

See, I (and you may have too) assumed that the number of people trying to learn an employable skill would be proportional to:

1. The likelihood of landing a job in that field
2. The average salary for that skill

- Better chance of employment = lower risk
- Higher salary = higher reward

In theory the _best_ career path for any individual is the one with the _lowest_ competition for jobs, adjusted for salary. In other words, the one with the best combination of:

- The most job openings
- The fewest people trying to learn it
- The highest salary

Here's a formula:

```
score = (job openings / search volume) * average salary
```

For an "efficient market" of eager learners, we'd expect new learners to prefer the career paths with the highest "scores", thus lowering the score for those paths, and on average, somewhat breaking even across all paths.

_But that doesn't seem to be the case at all!_

Anecdotally, back in 2020 it bothered me that the number of people wanting to learn frontend development seemed _so much_ higher than the number of people wanting to learn backend development. It struck me as odd, because on average backend developers earn a bit more and there are _more_ [backend developers overall](https://survey.stackoverflow.co/2025/developers#3-role).

Noting the gap in the market, I decided to build Boot.dev and teach backend development, and frankly things have gone quite well.

> "It's not that fewer people want to learn backend development"
>
> (I said to myself)
>
> "It's that not many online courses focus on teaching it."

Fast forward to 2025, and we've shipped most of the backend courses in our Boot.dev roadmap, so this weekend I sat down to do some research on where we should go from here. I get a lot of requests for other career learning paths, so I decided to try to quantify the demand for the various roles we're considering teaching:

- Backend Developer
- Frontend Developer
- Fullstack Developer
- Data Engineer
- DevOps Engineer
- Data Analyst
- AI Engineer

For each role I wanted to answer each of these questions, so that I could plug the results into my formula:

1. How many people **want to learn** those skills?
2. How much does the average person in those roles **earn**?
3. How many **jobs openings** are there for those roles?

So I cobbled together a few data sources:

- The [Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025)
- Counts of Job Listings from the [JobData API](https://jobdataapi.com/titles/)
- Google search volume (from Google Ads Keyword Planner)
- ~~[The Bureau of Labor Statistics](https://www.bls.gov/bls/blswage.htm)~~ (just kidding this was basically useless due to overly broad categories)

**Let's talk about what I found.**

> **Disclaimer:** You might be thinking, "Lane, what's an 'ai engineer'?" and to that I say, "Great question! I don't know, and I don't think anyone else does either". Though it does seem like it _might_ mean some combination of:
>
> - Training custom LLMs from scratch
> - Fine tuning existing LLMs
> - Prompt/context engineering or building RAG systems
> - Using ChatGPT, but like, using it _really really good_
> - Backend development, but where you also call the Anthropic API

## How many people want to learn each skill?

If you have a Google Ads account, you can access their Keyword Planner tool, which gives you the average monthly search volume for any given search term. The data is quite reliable and granular, the only challenge comes with identifying the best keyword(s) to use for each role. I ended up using the following search terms, averaging the searches in the United States over the last 12 months (November 2024 - November 2025):

| Role                | Search Term             | Monthly Searches | Percentage of Total |
| ------------------- | ----------------------- | ---------------- | ------------------- |
| Backend Developer   | backend course          | 50               | 0.24%               |
| Frontend Developer  | frontend course         | 1,300            | 6.21%               |
| Fullstack Developer | fullstack course        | 1,600            | 7.64%               |
| Data Engineer       | data engineer course    | 2,400            | 11.47%              |
| DevOps Engineer     | devops course           | 880              | 4.20%               |
| Data Analyst        | data analyst course     | 8,100            | 38.70%              |
| AI Engineer         | machine learning course | 1,600            | 31.53%              |

As someone who sells interactive backend courses for a living, this is a pretty scary table... it also explains why it was so easy to get Boot.dev to rank #1 for "backend course" on Google... but I digress.

Now, before you freak out, let me throw down a few caveats and justifications for the keywords I chose:

- "ai engineer course" had `1,600` searches, but I think "engineer" is a bit too specific to capture the machine learning crowd, which is clearly a big part of the AI pie (as we'll see in the jobs data later)
- "ai course" had `12,100` searches, but I think it's much too broad, as you'll see a bunch of people trying to learn how to use ChatGPT or Midjourney, which is not what we're looking for here
- "software engineer course" and "coding course" had `5,400` apiece, and even though some of those searchers will likely go on to backend roles, I think it's too broad to be useful in our breakdown
- I wanted to find a way to include terms like "java course", "python course", and "golang course" in the backend category, but I think it muddies the waters more than it clarifies them, so I left all technology-specific terms out, especially considering that "python course" is far from specific to backend dev.

While these search terms are imperfect, they're my best attempt for now, and we'll roll with them whilst keeping the limitations of the data in mind.

## How much does the average person earn in each role?

This is probably the easiest question to answer with a high degree of confidence, thanks to the [Stack Overflow Developer Survey for 2025](https://survey.stackoverflow.co/2025/work#3-salary-by-developer-type). They ask respondents about their salary, and break it down by role so we can get a good idea of what each role pays on average. This is 2025 data for the United States:

| Role                | Average Salary (USD) |
| ------------------- | -------------------- |
| Backend Developer   | $175,000             |
| Frontend Developer  | $145,000             |
| Fullstack Developer | $138,000             |
| Data Engineer       | $150,000             |
| DevOps Engineer     | $165,000             |
| Data Analyst        | $100,000             |
| AI/ML Engineer      | $189,500             |

Aside from the looming question of "what the hell is an AI engineer?", this all seems reasonable. Data analyst roles typically require less technical training than the others, so that disparity makes sense. One thing that _might_ jump out at you is that full stack developers make _less_ than backend and frontend developers... but you need to know what "fullstack" _truly_ means in the industry.

Many folks assume that "fullstack" means "GOATed senior web developer that can do everything", but in reality, it usually means "developer that works at a company small enough (and with a product simple enough) that everyone can do everything". In that light, the pay disparity, again, checks out.

## How many jobs openings are there for each role?

I dug around quite a bit trying to find decent data on this... I really wish LinkedIn or Indeed would publish a big "job openings dataset", or make it easier to get aggregate counts of postings. Alas, that's not the case. Additionally, the Bureau of Labor Statistics publishes numbers, but their data is useless for this sort of analysis because the BLS has never heard of a "fullstack developer" or a "devops engineer". "Programmer" and "IT guy" is about as specific as they get when it comes to technical roles.

So, I ended up using the [JobData API](https://jobdataapi.com/). It ingests hundreds of thousands of job postings from around the web, and on [this page](https://jobdataapi.com/titles/) you can see the number of postings during the last 30 days for each job title. It's not great for looking at trends over time, but the data seems pretty solid for a November 2025 snapshot. Here's a small sample of the data:

```
Host (477)
Customer Success Manager (475)
Manager (468)
DevOps Engineer (468)
Trading Assistant (467)
Auxiliaire de vie H/F (465)
Project Engineer (462)
Team Member: Food Champion (461)
Kid Check Attendant - Cast Member (461)
Trading Assistant - Shift (461)
Food Prep, Cook, and Pizza Maker - Cast Member (461)
Outpatient Registered Nurse - RN (456)
Program Manager (456)
Retail Customer Service (455)
Medical Director (455)
Project Coordinator (448)
(USA) Coach/Ops Mgr Trainee (443)
Veterinary Assistant (443)
Groomer (439)
Field Sales Representative (437)
Senior Product Manager (433)
Sous Chef (432)
Verizon Sales Consultant (429)
Inside Sales Representative (427)
Bar & Waiting Staff (427)
```

_There are 2,073 total roles in the data_.

Anyhow, I downloaded the data and manually [classified](https://github.com/bootdotdev/jobdata-november-2025?tab=readme-ov-file) all the _applicable_ roles (which ended up being about `100 / 2,073`) into the 7 roles that we care about. For example:

- "Business Analyst" -> Data Analyst
- "Cloud Engineer" -> DevOps Engineer
- "Lead Machine Learning Engineer" -> AI Engineer
- "Senior Python Developer" -> Backend Developer
- ...

It's not perfect, but I'm pretty happy with it. I uploaded both the raw and classified data to [GitHub here](https://github.com/bootdotdev/jobdata-november-2025) if you'd like to scrutinize my decisions. Once aggregated, we get these counts:

| Role                | Number of Job Postings | Percentage of Total |
| ------------------- | ---------------------- | ------------------- |
| Backend Developer   | 1,162                  | 6.25%               |
| Frontend Developer  | 1,506                  | 8.10%               |
| Fullstack Developer | 8,118                  | 43.65%              |
| Data Engineer       | 1,546                  | 8.31%               |
| DevOps Engineer     | 1,680                  | 9.03%               |
| Data Analyst        | 1,900                  | 10.22%              |
| AI Engineer         | 2,686                  | 14.44%              |

As you can guess, making a classification isn't always cut-and-dry, so I tried to stick to these rules:

- Removed managerial roles
- Removed finance-specific roles
- Removed hardware/embedded roles
- Removed overly generic roles like "Engineering Manager"
- Removed testing/qa roles
- Removed customer support/sales roles
- Removed product/project management roles
- If a programming language is in the title, best-guess the role type

With the data and my classification rules in mind, here are a few things worth noting:

- I suspect **backend openings are under-classified and fullstack openings are over-classified**. I classified "Lead Software Engineer" and "Software Engineer II" as "fullstack" due to the generic nature of the titles, but I suspect there are more pure-backend devs with those titles than pure-frontend devs.
- I suspect **data analysis is under-classified**. I ignored roles that _use_ data analysis but require additional training. Roles like "financial analyst" and "marketing analyst" were removed, so I might be under-counting there.
- We still have no idea what an "AI Engineer" is, but at least in this dataset it's _mostly_ synonymous with "ML engineer", which should usually involve training or fine-tuning models (which is why I think the "machine learning course" search keyword was a good choice).

## Bonus: How many people are already working in each role?

This is a slightly separate question, but I thought it would be good for purely observational purposes, and to point out another separate source of data.

[Stack Overflow](https://survey.stackoverflow.co/2025/developers#3-role)'s poll shows the percentage of respondents working in each role, but Stack Overflow's community is biased _really hard_ toward web development, leading to some crazy numbers:

| Role                | Percentage of Respondents |
| ------------------- | ------------------------- |
| Backend Developer   | 11.0%                     |
| Frontend Developer  | 4.30%                     |
| Fullstack Developer | 27.9%                     |
| Data Engineer       | 1.9%                      |
| DevOps Engineer     | 2.5%                      |
| Data Analyst        | 1.1%                      |
| AI Engineer         | 1.5%                      |

The relationship between backend, frontend and fullstack all feels reasonable, but I _really doubt_ there are 4x more frontend developers in the US than data analysts (right?!?). It seems more likely that data analysts simply don't hang out on Stack Overflow. So, I'm going to mostly ignore this data, except as another source to show the relationship between frontend, backend, and fullstack developers, which I _do_ think is fairly accurate.

## Which skills should I be learning?

The _real_ (commercially safe for me to say) answer to this question is "whichever one you find most interesting and believe you can find a job for". After all, _you_ only need _one_ job. But, of course, we're here to crunch some _data_, so let's quantify the options. Here's everything we have so far:

| Role                | Percentage Job Postings | Percentage Search Volume | Average Salary (USD) |
| ------------------- | ----------------------- | ------------------------ | -------------------- |
| Backend Developer   | 6.25%                   | 0.24%                    | $175,000             |
| Frontend Developer  | 8.10%                   | 6.21%                    | $145,000             |
| Fullstack Developer | 43.65%                  | 7.64%                    | $138,000             |
| Data Engineer       | 8.31%                   | 11.47%                   | $150,000             |
| DevOps Engineer     | 9.03%                   | 4.20%                    | $165,000             |
| Data Analyst        | 10.22%                  | 38.70%                   | $100,000             |
| AI Engineer         | 14.44%                  | 31.53%                   | $189,500             |

Remembering our formula from earlier (I'll also divide by `1,000` to make the numbers a bit more manageable):

```
score = (job openings / search volume) * (average salary / 1,000)
```

We can calculate the "score" for each role, and then reorder the rows from "best" to "worst":

| Role                | Percentage Job Postings | Percentage Search Volume | Average Salary (USD) | Score |
| ------------------- | ----------------------- | ------------------------ | -------------------- | ----- |
| Backend Developer   | 6.25%                   | 0.24%                    | $175,000             | 4,577 |
| Fullstack Developer | 43.65%                  | 7.64%                    | $138,000             | 788   |
| DevOps Engineer     | 9.03%                   | 4.20%                    | $165,000             | 355   |
| Frontend Developer  | 8.10%                   | 6.21%                    | $145,000             | 189   |
| Data Engineer       | 8.31%                   | 11.47%                   | $150,000             | 109   |
| AI Engineer         | 14.44%                  | 31.53%                   | $189,500             | 87    |
| Data Analyst        | 10.22%                  | 38.70%                   | $100,000             | 26    |

The crazy low number of people searching for "backend course" and the relatively high number of people searching for "machine learning course" and "data analyst course" does almost all the heavy lifting at the edges here.

> Hold on Lane, isn't it super convenient that this table makes it look like everyone should be learning backend development, and you _sell backend courses_ on Boot.dev?

Yes! And you should probably be wary of that bias...

But I will tell you that I didn't set out to prove that "Backend is a great choice" as I started putting this data together, my goal really was to find out which career path we should focus on teaching _next_ and I just happened to find some unexpected data and decided to share it here. In fact, something that's super inconvenient for me is that we decided months ago that data analysis would be our next learning path, and this data suggests that it's actually the _worst_ one for students to jump into...

That said, there's another variable that's not captured here: _how hard it is to learn the skills_. Data analysis roles often require less study and training overall, which helps to explain why those courses would be so popular with students, especially those who are looking for a quick career change.

So, I _really_ don't want anyone to make any multi-year career decisions based on this article alone... **do your own research!** The economy is in a crazy weird place right now, and has been for a while. The only thing I can say for certain is that no matter which way you go about bettering yourself, _don't stop bettering yourself_! AI has been making a lot of waves and my biggest fear is that it's convinced entire swaths of people that _learning stuff is useless_, and that's just as false as it's always been.

In the immortal words of The Hitchhiker's Guide to the Galaxy: _Don't Panic!_

Good luck.
