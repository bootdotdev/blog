---
title: "The State of Learning to Code - 2024 Report"
author: lane
date: "2024-10-21"
categories:
  - "education"
images:
  - /img/800/bootsatdesk.png.webp
imageAlts:
  - "Boots writing at a desk"
---

I've been building a learning curriculum for backend developers for the last 3 years, but I've mostly been relying on qualitative feedback and my own intuitions.

_Well now I have my own quantitative data_, and as the founder/grand magus of [Boot.dev](https://www.boot.dev), I'm gonna use it. I figured I'd also share it with you, if you're interested.

## What is this report?

This is primarily an info dump of our Boot.dev learners' stats (aggregated and anonymized of course) with some of my own commentary. Obviously, **I'll only include data that makes me look correct and smart**.

## High-level numbers

I'm not trying to flaunt our growth numbers (but if you want to acquire Boot.dev for north of 10 Billion hmu) but to understand the data that follows, it's important to know a bit about our scale. In some cases we have enough data for statistical significance, in others we might not.

### User data

| Metric                   | Value   | Description                                        |
| ------------------------ | ------- | -------------------------------------------------- |
| Total Registered Users   | 336,271 | Everyone who has made an account, free or paid     |
| Total Individual Members | 18,255  | Folks who are paying (or were gifted) a membership |
| Total Team Members       | 193     | Folks who are part of a team membership            |

### Course data

| Metric         | Value | Description                                                                                                                                                                   |
| -------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total Lessons  | 2090  | All active lessons. A lesson is a single pass/fail assignment that usually takes ~2-10 minutes, with outliers of 1+ hours                                                     |
| Total Chapters | 217   | Chapters are collections of lessons grouped by concept. They usually have 6-16 lessons.                                                                                       |
| Total Courses  | 21    | Courses are collections of lessons broken into chapters. Courses are building blocks of tracks. Courses primarily teach new concepts.                                         |
| Total Projects | 9     | Projects are also collections of lessons and are building blocks of tracks. Projects have much larger lessons with less guidance. Projects primarily practice known concepts. |
| Total Tracks   | 1     | A track is an ordered list of courses and projects. We only have one currently: a backend developer track. Working on new ones.                                               |

### Usage data

| Metric                     | Value      | Description                                                                 |
| -------------------------- | ---------- | --------------------------------------------------------------------------- |
| Lesson Completions         | 10,725,530 | Total number of lessons that have been completed by all users.              |
| Course/Project Completions | 64,286     | Total number of courses and projects that have been completed by all users. |

Here's a chart of lesson completions by month (blue bars) and active members (orange line):

![lesson completions](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/juMFNBi.png)

## The hardest concepts when learning to code

Let's start at the beginning. **Where do people give up**?

Here's the drop-off funnel of chapters 4-14 of the very first course: "[Learn to code with Python](https://www.boot.dev/courses/learn-code-python)".

![python chapter drop off](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/rRTiims.png)

The first bar represents the number of users who did at least one lesson in chapter 4. The next bar represents the number of users who went on to do at least one lesson in chapter 5, and so on.

_I excluded the first 3 chapters because the interactivity paywall is at the end of chapter 3, which skews the results_.

By percentage, chapters 7, 8 and 9 have the biggest drop off rates, 11.5%, 10.5%, and 15% respectively. These chapters cover **comparison operators**, **loops**, and **lists**.

## How does Go compare to Python?

Its important to understand that our Python course is an "intro to coding" course. It starts from zero. Our [Go course is "Go for developers"](https://www.boot.dev/courses/learn-golang) and assumes that you already understand coding concepts, and want to learn the Go-specific syntax and idioms. Most new learners on Boot.dev start in one of two places:

1. Brand new coders in Python
2. Experienced coders who just want to learn back-end development in Go

![go chapter drop off](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/Y8A6Drd.png)

The largest drop offs are in chapters 4, 5, and 8 with 24%, 14% and 22% respectively. These chapters cover **structs**, **interfaces**, and **slices**.

## Giving up vs struggling

Now to be fair, giving up isn't a pure measure of difficulty. It's a combination of difficulty and motivation and probably a few other factors. So let's look specifically at the _hardest_ chapters in each course.

It's interesting to distinguish between "hard" in the absolute sense and "hard" relative to how much you struggle _when you arrive_ at a concept. For example, learning about functions is easier than learning about recursion in the absolute sense, but is it easier in the _relative_ sense? You won't encounter recursion in Boot.dev until you've had 6 additional courses of programming practice. **We mostly care about relative difficulty**. We see it as our job to introduce the right concepts at the right time, with the right amount of practice.

We calculate a "difficulty" score for each lesson based on a few metrics:

- Number of attempts before passing. Weight `.4`
- Number of solution views before passing. Weight `.4`
- Number of chats with AI before passing. Weight `.2`

_We'd like to add "time to complete" as a factor, but its surprisingly tricky to measure accurately... we plan to add it in the future._

We then use a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)/[standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) to normalize the scores. Finally, we map it all onto a scale of 1-10 so its easy to understand what the numbers mean as a user.

_This means difficulty scores are relative to the other lessons in the course._ It would be impossible to have all `10`s, or all `1`s.

Here are the chapters of the Go course, sorted by average lesson difficulty, hardest to easiest:

| Avg Difficulty Score | Chapter              |
| -------------------- | -------------------- |
| 6.667                | Loops                |
| 6.000                | Channels             |
| 4.769                | Maps                 |
| 4.636                | Slices               |
| 4.476                | Functions            |
| 4.250                | Generics             |
| 4.250                | Enums                |
| 4.200                | Conditionals         |
| 4.091                | Structs              |
| 4.091                | Pointers             |
| 4.080                | Variables            |
| 4.000                | Interfaces           |
| 4.000                | Errors               |
| 3.750                | Mutexes              |
| 3.556                | Packages and Modules |
| 3.500                | Quiz                 |

Of course, we run into a _new_ problem... a chapter with more hard lessons will _appear easier_ if it _also_ has a lot of easy lessons. If anything, more lessons (of any kind) should indicate the chapter is hard*er* if only by a little. **It certainly doesn't mean it's easier**.

Let's try sorting by the chapters with the _most lessons over a difficulty score of `6`_:

| Num Difficult Lessons | Chapter              |
| --------------------- | -------------------- |
| 4                     | Channels             |
| 3                     | Maps                 |
| 3                     | Loops                |
| 3                     | Slices               |
| 2                     | Functions            |
| 1                     | Generics             |
| 1                     | Conditionals         |
| 1                     | Variables            |
| 0                     | Errors               |
| 0                     | Structs              |
| 0                     | Mutexes              |
| 0                     | Enums                |
| 0                     | Packages and Modules |
| 0                     | Interfaces           |
| 0                     | Pointers             |
| 0                     | Quiz                 |

As expected (by me) channels (and by extension **concurrency**) bumped up a spot - students anecdotally seem to ask for more help with this chapter in our Discord than any other.

I picked 7-10 as an arbitrary cutoff for "hard" lessons because it gets weird when you _sum_ the difficulties because 3 lessons of difficulty 3 is significantly easier than a single 9. That said, I think we can improve _one last thing_. Let's sum the difficulties, but **only if they're over 6**. That way we give a bit more weight to the harder lessons:

| Sum of Difficult Scores | Chapter              |
| ----------------------- | -------------------- |
| 33                      | Channels             |
| 23                      | Loops                |
| 22                      | Maps                 |
| 22                      | Slices               |
| 15                      | Functions            |
| 7                       | Generics             |
| 7                       | Conditionals         |
| 7                       | Variables            |
| 0                       | Errors               |
| 0                       | Structs              |
| 0                       | Mutexes              |
| 0                       | Enums                |
| 0                       | Packages and Modules |
| 0                       | Interfaces           |
| 0                       | Pointers             |
| 0                       | Quiz                 |

This feels _really close_ to what our students report - so let's roll with it. Maybe in the future we'll add some sort of exponential scaling so that we don't need a cutoff, but I'd need to sit down and test it, and we would probably need more data to make that worthwhile.

**Now let's use this calculation for every chapter on the platform**. Here’s the data formatted as a Markdown table:

| Score | Course                              | Chapter                         |
| ----- | ----------------------------------- | ------------------------------- |
| 76    | Learn Python                        | Loops                           |
| 56    | Learn Data Structures               | Binary Trees                    |
| 46    | Learn Kubernetes                    | Storage                         |
| 46    | Learn HTTP Servers                  | JSON                            |
| 44    | Learn Data Structures               | Tries                           |
| 42    | Learn Functional Programming        | Recursion                       |
| 39    | Learn Algorithms                    | P vs NP                         |
| 37    | Learn SQL                           | Joins                           |
| 34    | Learn Data Structures               | Linked Lists                    |
| 33    | Learn Advanced Algorithms           | Linear Programming              |
| 33    | Learn Go                            | Channels                        |
| 33    | Learn Algorithms                    | Exponential Time                |
| 32    | Learn Memory Management             | Mark and Sweep GC               |
| 31    | Learn Functional Programming        | First Class Functions           |
| 31    | Learn Advanced Algorithms           | Dijkstra's                      |
| 31    | Learn Functional Programming        | Decorators                      |
| 30    | Learn Python                        | Functions                       |
| 29    | Learn Object Oriented Programming   | Polymorphism                    |
| 29    | Personal Project 2                  | Placeholder                     |
| 28    | Learn Data Structures               | Red Black Trees                 |
| 28    | Learn HTTP Servers                  | Authentication                  |
| 27    | Learn Cryptography                  | DES                             |
| 26    | Learn Functional Programming        | Sum Types                       |
| 26    | Learn Functional Programming        | Pure Functions                  |
| 26    | Build a Static Site Generator       | Website                         |
| 25    | Learn HTTP Servers                  | Servers                         |
| 25    | Build a Blog Aggregator             | Following                       |
| 24    | Learn Functional Programming        | Currying                        |
| 24    | Learn SQL                           | Aggregations                    |
| 23    | Learn Memory Management             | Advanced Pointers               |
| 22    | Learn Python                        | Variables                       |
| 22    | Learn Go                            | Maps                            |
| 22    | Learn Object Oriented Programming   | Inheritance                     |
| 22    | Build a Static Site Generator       | Inline                          |
| 22    | Learn Kubernetes                    | Nodes                           |
| 22    | Learn Go                            | Slices                          |
| 20    | Learn Data Structures               | Hashmaps                        |
| 19    | Learn Git                           | Config                          |
| 18    | Learn Memory Management             | Pointers                        |
| 18    | Learn Functional Programming        | Closures                        |
| 18    | Learn Pub/Sub Architecture          | Subscribers & Routing           |
| 18    | Learn Algorithms                    | Sorting Algorithms              |
| 18    | Learn SQL                           | Introduction                    |
| 18    | Learn Data Structures               | BFS and DFS                     |
| 17    | Learn Advanced Algorithms           | Edit Distance                   |
| 17    | Learn Pub/Sub Architecture          | Delivery                        |
| 17    | Learn Memory Management             | Objects                         |
| 17    | Learn CI/CD                         | Database                        |
| 17    | Learn Functional Programming        | What is Functional Programming? |
| 17    | Learn Cryptography                  | RSA                             |
| 17    | Learn Pub/Sub Architecture          | Serialization                   |
| 16    | Learn Object Oriented Programming   | Classes                         |
| 16    | Learn JavaScript                    | Arrays                          |
| 16    | Build a Blog Aggregator             | RSS                             |
| 16    | Learn HTTP Clients                  | DNS                             |
| 16    | Learn Object Oriented Programming   | Abstraction                     |
| 15    | Learn Memory Management             | Stack Data Structure            |
| 15    | Learn Advanced Algorithms           | Heaps                           |
| 15    | Learn CI/CD                         | Build                           |
| 15    | Learn Cryptography                  | Hash Functions                  |
| 14    | Learn Python                        | Dictionaries                    |
| 14    | Learn SQL                           | Basic Queries                   |
| 14    | Learn Python                        | Errors                          |
| 14    | Learn Python                        | Lists                           |
| 14    | Learn Pub/Sub Architecture          | Pub/Sub Architecture            |
| 14    | Learn Advanced Algorithms           | A\* Search                      |
| 14    | Learn Pub/Sub Architecture          | Publishers & Queues             |
| 10    | Learn Cryptography                  | Digital Signatures              |
| 10    | Learn HTTP Servers                  | Routing                         |
| 10    | Learn Pub/Sub Architecture          | Scalability                     |
| 9     | Learn Cryptography                  | AES                             |
| 9     | Learn Pub/Sub Architecture          | Message Brokers                 |
| 9     | Learn SQL                           | Performance                     |
| 9     | Learn Data Structures               | Stacks                          |
| 8     | Learn HTTP Servers                  | Webhooks                        |
| 8     | Learn SQL                           | Constraints                     |
| 8     | Learn Cryptography                  | Block Ciphers                   |
| 8     | Learn Memory Management             | Refcounting GC                  |
| 8     | Build a Static Site Generator       | Blocks                          |
| 8     | Learn CI/CD                         | Formatting                      |
| 8     | Learn Cryptography                  | Encoding                        |
| 8     | Learn Memory Management             | Stack and Heap                  |
| 7     | Learn Object Oriented Programming   | Encapsulation                   |
| 7     | Learn Go                            | Generics                        |
| 7     | Learn Go                            | Conditionals                    |
| 7     | Learn Cryptography                  | KDFs                            |
| 7     | Learn Cryptography                  | Caesar Cipher                   |
| 7     | Learn HTTP Servers                  | Authorization                   |
| 7     | Learn Functional Programming        | Function Transformations        |
| 7     | Learn HTTP Clients                  | Paths                           |
| 7     | Learn Memory Management             | Unions                          |
| 7     | Learn SQL                           | Subqueries                      |
| 7     | Learn Cryptography                  | Asymmetric Encryption           |
| 7     | Learn Cryptography                  | Stream Ciphers                  |
| 7     | Learn CI/CD                         | Tests                           |
| 7     | Learn Cryptography                  | Brute Force                     |
| 7     | Learn HTTP Clients                  | Async                           |
| 7     | Learn HTTP Clients                  | URIs                            |
| 7     | Learn HTTP Clients                  | Methods                         |
| 0     | Learn How to Find a Programming Job | Relocation                      |
| 0     | Learn HTTP Clients                  | Headers                         |
| 0     | Learn Git 2                         | Squash                          |
| 0     | Learn Git 2                         | Stash                           |
| 0     | Learn Git                           | Repositories                    |
| 0     | Learn Algorithms                    | Math                            |
| 0     | Learn Shells and Terminals          | Terminals and Shells            |
| 0     | Build a Static Site Generator       | Static Sites                    |
| 0     | Learn Cryptography                  | Symmetric Encryption            |
| 0     | Learn Git 2                         | Reflog                          |
| 0     | Learn Docker                        | Publish                         |
| 0     | Learn CI/CD                         | Linting                         |
| 0     | Learn HTTP Servers                  | Documentation                   |
| 0     | Learn Shells and Terminals          | Permissions                     |
| 0     | Learn Go                            | Packages and Modules            |
| 0     | Learn Git                           | Internals                       |
| 0     | Learn Advanced Algorithms           | Bellman Ford                    |
| 0     | Learn Git                           | Reset                           |
| 0     | Learn Docker                        | Dockerfiles                     |
| 0     | Learn Git 2                         | Tags                            |
| 0     | Learn Data Structures               | Graphs                          |
| 0     | Learn CI/CD                         | Continuous Integration          |
| 0     | Learn How to Find a Programming Job | Applying                        |
| 0     | Learn CI/CD                         | Security                        |
| 0     | Learn Python                        | Scope                           |
| 0     | Learn SQL                           | Normalization                   |
| 0     | Learn Git                           | Rebase                          |
| 0     | Learn Data Structures               | Queues                          |
| 0     | Learn How to Find a Programming Job | Resume                          |
| 0     | Learn Git 2                         | Rebase Conflicts                |
| 0     | Build a Blog Aggregator             | Aggregate                       |
| 0     | Learn Git                           | Merge                           |
| 0     | Learn CI/CD                         | Deploy                          |
| 0     | Learn Algorithms                    | Polynomial Time                 |
| 0     | Learn How to Find a Programming Job | Strategy                        |
| 0     | Learn SQL                           | Structuring                     |
| 0     | Learn How to Find a Programming Job | LinkedIn Profile                |
| 0     | Learn Advanced Algorithms           | Dynamic Programming             |
| 0     | Learn Kubernetes                    | Namespaces                      |
| 0     | Learn Docker                        | Command Line                    |
| 0     | Learn Memory Management             | Enums                           |
| 0     | Learn How to Find a Programming Job | Networking                      |
| 0     | Learn Git                           | Branching                       |
| 0     | Learn Memory Management             | C Basics                        |
| 0     | Learn Git 2                         | Revert                          |
| 0     | Learn Git 2                         | Worktrees                       |
| 0     | Learn Go                            | Mutexes                         |
| 0     | Learn Shells and Terminals          | Packages                        |
| 0     | Learn Shells and Terminals          | Programs                        |
| 0     | Learn Python                        | Comparisons                     |
| 0     | Learn How to Find a Programming Job | Interviewing                    |
| 0     | Learn Docker                        | Networks                        |
| 0     | Learn Python                        | Testing and Debugging           |
| 0     | Learn Git                           | GitHub                          |
| 0     | Build Asteroids                     | Asteroids                       |
| 0     | Learn Python                        | Sets                            |
| 0     | Learn SQL                           | Tables                          |
| 0     | Learn Git                           | Gitignore                       |
| 0     | Learn Python                        | Computing                       |
| 0     | Learn Python                        | Quiz                            |
| 0     | Learn Shells and Terminals          | Filesystems                     |
| 0     | Learn SQL                           | CRUD                            |
| 0     | Build Asteroids                     | Player                          |
| 0     | Learn Kubernetes                    | Scaling                         |
| 0     | Learn Git 2                         | Cherry Pick                     |
| 0     | Learn Kubernetes                    | ConfigMaps                      |
| 0     | Learn Memory Management             | Structs                         |
| 0     | Learn Git 2                         | Fork                            |
| 0     | Learn HTTP Clients                  | HTTPS                           |
| 0     | Learn How to Find a Programming Job | GitHub Profile                  |
| 0     | Learn Git 2                         | Bisect                          |
| 0     | Build Asteroids                     | Pygame                          |
| 0     | Learn Kubernetes                    | Pods                            |
| 0     | Learn Git                           | Setup                           |
| 0     | Learn Cryptography                  | XOR                             |
| 0     | Learn Git                           | Remote                          |
| 0     | Learn How to Find a Programming Job | Projects                        |
| 0     | Learn HTTP Servers                  | Architecture                    |
| 0     | Learn Go                            | Interfaces                      |
| 0     | Learn HTTP Clients                  | Why HTTP?                       |
| 0     | Learn Kubernetes                    | Ingress                         |
| 0     | Learn JavaScript                    | Runtimes                        |
| 0     | Learn Kubernetes                    | Services                        |
| 0     | Learn Git 2                         | Merge Conflicts                 |
| 0     | Learn Kubernetes                    | Install                         |
| 0     | Learn HTTP Clients                  | cURL                            |
| 0     | Learn Kubernetes                    | Deployments                     |
| 0     | Learn Python                        | Challenges                      |

### To simplify, let's aggregate all this data by course:

| Score | Course                              |
| ----- | ----------------------------------- |
| 222   | Learn Functional Programming        |
| 209   | Learn Data Structures               |
| 141   | Learn HTTP Servers                  |
| 136   | Learn Go                            |
| 129   | Learn Cryptography                  |
| 128   | Learn Memory Management             |
| 110   | Learn Advanced Algorithms           |
| 110   | Learn Python                        |
| 108   | Learn Algorithms                    |
| 99    | Learn Pub/Sub Architecture          |
| 99    | Learn SQL                           |
| 90    | Learn Object Oriented Programming   |
| 78    | Build a Static Site Generator       |
| 73    | Learn HTTP Clients                  |
| 70    | Build a Blog Aggregator             |
| 37    | Learn CI/CD                         |
| 29    | Build a Web Crawler                 |
| 24    | Learn JavaScript                    |
| 7     | Learn Kubernetes                    |
| 0     | Personal Project 1                  |
| 0     | Build a Pokedex                     |
| 0     | Build a Bookbot                     |
| 0     | Learn Docker                        |
| 0     | Personal Project 2                  |
| 0     | Build a Maze Solver                 |
| 0     | Learn How to Find a Programming Job |
| 0     | Learn Shells and Terminals          |
| 0     | Capstone Project                    |
| 0     | Learn Git 2                         |
| 0     | Learn Git                           |
| 0     | Build Asteroids                     |

Now one might look at this, and think [ThePrimeagen](https://www.boot.dev/teachers/the-primeagen) writes courses for n00bs, whilst [TJ](https://www.boot.dev/teachers/tj-devries) writes courses for the elite...

... but to be fair to Prime, his course's data is skewed for two reasons:

- The Git courses don't yet have solutions to view (its tricky to implement solutions in a way that's easy for us to maintain and also easy for the student to grok, but we think we have a solution coming soon)
- The courses that are completed on your local machine (like Git) are harder to "screw up" on submission, because there aren't any hidden test cases currently

Again, adding a "time to complete" metric should really help some of these courses have more accurate scores.

**All that said, the current calculations seems to work really well for the courses that are comprised mostly of self-encapsulated coding lessons**.

## AI Tutors

_It's important to understand that viewing a solution before completing a lesson costs a "seer stone" (10 gems) or 75% of the lesson's XP. Chatting with AI costs a "baked salmon" (2 gems) or 50% of the lesson's XP_.

The total number of messages sent to our AI mentor, Boots, was about 50% higher than the total number of times users viewed solutions.

![total boots vs solutions](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/WpupzA0.png)

What's interesting to me, is that if we aggregate by "count per use average", we see that the boots chats are almost 3-4x more common than viewing solutions:

![unique users boots vs solutions](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/GZ0XzYY.png)

I _think_ this is because people who do use the AI mentor, use it more - but fewer people use it overall (I'm guessing Posthog excludes the `0`'s from the average calculation's denominator).

Now here's my favorite part:

![boots solutions totals before/after](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/b7BKKEa.png)

Boots is disproportionately more popular _before_ a student has completed a lesson, while viewing solutions are more popular _after_ the lesson is complete.

This finding aligns with our hunch: students prefer to be guided using the Socratic method (which is what our AI is prompted to do) than to "cheat". However, once a lesson is complete, students like to see how the instructor solved the problem - more than they like to ask follow-up questions.

### Breaking it down by language

_It's important to remember that our Python course is "Python for beginners" and our Go course is "Go for developers"_. And because we start students with Python, it has about 4.5x more total lesson submissions than Go.

| Language                               | % Boots Used | % Solutions Used | Total Daily Lessons |
| -------------------------------------- | ------------ | ---------------- | ------------------- |
| Learn Python Course                    | 9.05%        | 8.99%            | ~22,000             |
| Learn Go Course                        | 7.14%        | 9.45%            | ~4,500              |
| Learn FP (Hardest Python Course)       | 32.52%       | 21.04%           | ~1,700              |
| Learn HTTP Servers (Hardest Go Course) | 35.6%        | 13.59%           | ~350                |

It seems to me that as the problems get larger and more complex (HTTP servers lessons span multiple files, FP problems tend to be larger and more complex functions) it seems like people lean more and more on the AI mentor over direct solutions.

### Breaking it down by model

For the last 60 days we've been powering Boots 50% with OpenAI's GPT-4o and 50% with Anthropic's Sonnet 3.5. Once you start a conversation with a model, you stick with that model for the duration of the conversation, but each new conversation is randomly assigned to a model.

| Model                      | Like Count | Dislike Count | Total Messages | Like Ratio | Dislike Ratio |
| -------------------------- | ---------- | ------------- | -------------- | ---------- | ------------- |
| claude-3-5-sonnet-20240620 | 932        | 162           | 430023         | 0.0022     | 0.0004        |
| gpt-4o-2024-08-06          | 846        | 267           | 360359         | 0.0023     | 0.0007        |

One thing that's _really interesting_ is that about 20 days into the experiment, GPT-4o had a decisive (iirc 50% better performance), but it has become closer over time. Honestly I think we just need a lot more data; we probably need to update our UI to make the thumbs-up/thumbs-down buttons more prominent so we get more feedback per conversation.

We haven't done this yet, but we plan to also start versioning our system prompts and using the same thumbs up/down system to continually improve the quality of the prompts and context we provide to the models.

## AI content help

Generating content with AI is, by and large, **a terrible idea**. I've experimented with it a lot because it's one of our single biggest time costs - and anything we can do to produce more and better content faster and cheaper is a win.

I'm convinced that as the world becomes flooded with more and more AI slop, the value of highly curated and high-quality content with a \*_chef's kiss_\* human flourish will become _more_ valuable, not less. But that doesn't mean we haven't found _some_ use cases for AI in our content management.

### Use case 1: Diagnosing student errors

We get _a lot_ of reports on lessons. And we take them _very seriously_. As of Oct 17, we've closed 10,964 tickets, and currently have only 73 open. The median time a ticket stays open is 1 day. And that's not even counting all the _reports_ we get, because reports on the _same_ lesson get aggregated into the same ticket - until its closed and a new ticket is started. 1-3 reports per ticket is common.

Anyhow, the point is that we've been building internal systems to make this process more manageable, because although we get a _ton_ of reports, only a fraction of those reports are actionable. We've broken reports down into 5 categories:

- `diagnose-studenterror`: The student is confused about the lesson, but the lesson is correct
- `diagnose-enhancement`: The student has a good idea for an improvement
- `diagnose-bug`: The student has found a valid bug
- `diagnose-badchange`: The student is identifying a bug that's not real, or suggesting a change that would make the lesson worse
- `diagnose-question`: The student is asking a question, not reporting an issue

Of these, only `diagnose-enhancement` and `diagnose-bug` are actionable. Everything else can be safely closed without modifying content - although it would be nice to respond to the student and let them know if they're confused or mistaken.

Well, up until about a month ago, this diagnosing and responding was done manually. In fact, we only responded to students <5% of the time that we would have liked to, because it was so time consuming.

However, now we use GPT-4o diagnose, and based on the diagnosis, provide a simple response to the student. The diagnosis is helpful for us, because we can more quickly close the ticket or start on a content change with confidence. The response is helpful for the student because they instantly understand that:

1. This isn't the place to ask a question
2. They are likely confused - the lesson is in fact correct, and they should more carefully inspect their code, chat with Boots, or view the solution.

We've only been running this for a couple weeks (long enough to diagnose 229 tickets), but so far here's how it breaks down by the numbers:

| Diagnosis               | Count | % of total |
| ----------------------- | ----- | ---------- |
| `diagnose-studenterror` | 63    | ~27%       |
| `diagnose-enhancement`  | 86    | ~38%       |
| `diagnose-badchange`    | 8     | ~4%        |
| `diagnose-bug`          | 35    | ~15%       |
| `diagnose-question`     | 37    | ~16%       |

### Use case 2: Intentionally making content worse

Alright that's a bit tongue in cheek, but... only a bit. I've tried many times to get AI to generate new lessons. I've given it our repository of lessons via fine-tuning, I've tried to shove examples of great human-written lessons in a context window, etc. But what I've gotten back is mostly slop (at least by our standards). Sure, it's usually correct, and it reads like correct English, but its just **so boring**. If you try to get the AI to use more creative language, it only does so superficially and cringily.

So I've mostly given up on that for now - waiting for GPT 5 I guess.

Anyhow, what it _is_ good at is reducing and reformatting. I'll spoil a new feature that we're working on here, called "spellbooks". Your spellbook is a UI feature easily accessibly via a keyboard command, that fuzzy searches through the "pages" you've unlocked. You unlock a spellbook page as you complete lessons. A spellbook page is just a condensed lesson: A short no-nonsense description of the concept, a few code examples, and links to documentation. The intention is:

1. You won't need to take notes
2. You won't need to bookmark lessons
3. You won't need cheatsheets
4. You won't need to navigate back to earlier lessons for examples and documentation

For example, you might be halfway through the Go course but have forgotten the syntax for a `struct`. So you hit `cmd+k` (or whatever keymap we choose) and type "struct" and you get a spellbook entry that looks something like this:

````
A struct in Go is a collection of fields. They're a convenient way to group different types of values together in a single place:

```go
type Person struct {
    Name string
    Age  int
}
```

- [Go reference](https://go.dev/ref/spec#Struct_types)
- [Go tour](https://go.dev/tour/moretypes/2)
````

What's this have to do with AI? Well, as it turns out, AI is really good at taking a larger, more well-written lesson and condensing it down to a spellbook entry. We've written a script that recursively generates spellbook pages for each lesson in a directory. It still requires human verification and touch ups of course, but it's a _lot_ faster than writing them from scratch.

## Resetting lessons

Students like to review stuff. Spellbooks will be nice for recall, but not so much for practice. In the future we have plans for a better "practice" experience, but the quick and dirty thing was to allow users to reset lessons. When they reset, progress bars and navigation are reset, but re-completing the same lessons does _not_ reward XP or chests.

Since adding lesson resets (July 24th, 2024) until now, we've had 3,561,569 successful lesson submissions and 418,289 resets. **That's 11.7% of all successful lesson submissions**.

I was actually blown away by this number - I thought it would be in the 2-3% range, but apparently people like to redo lessons more than I thought.

## People like to RTFM

We have a "listen to the lesson" button that reads you the lessons in a soothing British AI voice:

![audio listen screenshot](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/DJAwHkv.png)

I was surprised that people only seem to use it about 1.4% of the time. People like to read more than I expected.

![Successful lesson submissions vs Audio listens](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/Om023Gs.png)

## Vim mode

Our in-browser editor has a vim-mode, and since adding the configuration to our backend database (it used to live in local storage) we've had `684` people enable it. That's `684` people in one week, and we have roughly 10,000 weekly active users.

So around `6.8%` of active learners are using vim mode, honestly more than I expected!

## Thanks for making it this far

I hope this was interesting to you in one way or another! It was really helpful for me just to sit down and gather all this data, even just for our own product and content development. I figured while I was at it, I might as well ~~turn it into a marketing stunt~~ share it with the world altruistically.
