---
title: "Do Backend Developers Need to Know SQL?"
author: Natalie Schooner
date: "2023-03-02"
categories: 
  - "backend"
images:
  - /img/800/giant-future-database.png.webp
imageAlts:
  - "Midjourney prompt: giant futuristic database, 4k realistic detailed background"
---

A while back, one of my friends bragged that he bagged a six-figure backend developer job after watching a few YouTube videos on APIs and reading parts a bit of the PostgreSQL documentation.

"It's so easy, anyone can do it," he said smugly as I labored to learn the basics of computer science the hard, slow, old-fashioned way (taking courses, reading books, building projects on my own). "You don't need to know the first thing about SQL to become a backend developer."

A few weeks later, of course, he was summarily fired for being incompetent at his job. This proves a few things, first, my friend is a bit of a loser, but also that it's not enough to *look* good on paper to be a backend developer. You have to know these topics inside and out. [Learning SQL](https://boot.dev/courses/learn-sql) is no exception.

You might luck out like my pal did, but even if you do manage to snag a job through trickery and deceit, it's not enough to have a passing familiarity with CRUD operations and joins. You need to know the language well, and you need to understand the database theory behind it. Otherwise, you'll both struggle to get a job as a backend developer, and you definitely won't be able to keep it.

The short answer to your question? Yes, incontrovertibly yes - *backend developers need to know SQL*.

If you want the long answer, then we'll cover:

* What is SQL?
* Is SQL frontend or backend?
* Why do backend devs need to know SQL?
* How can you learn SQL?
* What other database tools and technologies should you know?

## What is SQL?

Before I explain in more detail why it's so imperative that backend developers know SQL, let's break down what SQL is in case it's a new-ish concept to you.

> If you want to gain a solid understanding of SQL skills, look no further - we've got a [great course covering the basics of SQL](https://boot.dev/courses/learn-sql) and beyond.

SQL, or Structured Query Language, is a programming language used to manage and manipulate relational databases.

At its core, SQL allows you to query and extract data from databases using commands like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. These commands let you perform operations like retrieving specific data, adding new data to a database, modifying existing data, and removing data altogether.

It's not *exactly* a programming language (though I did include it as [one of the top backend technologies to learn in 2023](/backend/top-backend-technologies/#8-sql)) but it is a *query* language. Backend developers typically use SQL to communicate between their application code and relational databases.

### Is SQL front-end or back-end? 

SQL is about as back-end as a language as you can get. When you think about the difference between [frontend and backend](/backend/frontend-vs-backend-meaning/) technologies, the frontend is what the user interacts with. The backend, usually hooked up to the database, is the process that fulfills that user request. SQL is the language used to store, manipulate, and retrieve data from that database.

Why is SQL backend? Let's look at an example to illustrate why SQL is a backend language.

Say, for instance, you want to log into [Boot.dev](https://boot.dev) to take another lesson in the Learn SQL course. When you log in to the application, the front end sends a request to the backend to retrieve your profile data. The backend then uses SQL queries to retrieve your profile information from the database, such as your name, email address, and profile picture.

Once the backend has retrieved your profile data, it sends it back to the front end in a format that can be displayed on your screen. The front end then uses HTML and CSS to render the profile data and display it to you.

## How can you learn SQL for the backend? 

[Like Go](/golang/become-golang-backend-dev/), SQL is one of these languages that is primarily back-end oriented. If you learn SQL, you're learning SQL for the backend by default.

That being said, if you want to learn SQL for the back-end, there are a few key competencies you should check off. Here's a list:

* Tables: Know how to create and structure tables in an efficient and organized manner to build a robust and effective database.
* Constraints: Understand how to apply constraints to data so that it remains accurate and consistent over time, helping to prevent errors and maintain data integrity.
* CRUD: Create, read, update, and delete information in a database.
* Basic Queries: Write more flexible and powerful SQL queries, allowing you to retrieve the exact data you need.
* Structuring: Know how to order and limit data sets to manage large amounts of data and improve query performance.
* Aggregations: Understand how to perform calculations on entire data sets to extract meaningful insights from large amounts of data.
* Subqueries: Nest queries within one another to perform complex queries and generate more specific results.
* Normalization: Learn how to normalize a database to ensure that data is consistent and accurate, even as it grows and changes over time.
* Joins: Understanding how to join multiple tables together to combine data from multiple sources.
* Performance: Optimize SQL queries to ensure that databases are running and keeping applications running smoothly in production.

### How can I learn this long laundry list of SQL skills?

First, not coincidentally, this is a list of exactly the lessons you'll learn from our [Learn SQL](https://boot.dev/courses/learn-sql) course. You will build out real database tables and practice querying them in flexible ways right in your browser. Not only will you understand how to use SQL, but you will also learn when you should use it and in what situations. It's a great course!

Want a more DIY approach? You can also look on YouTube and Google for tutorials covering each of these skills. For example, searching "[sql normalize a database" on YouTube](https://www.youtube.com/watch?v=siiYInWniFs) delivers a great 10-minute video tutorial on the subject.

Finally, there are so many great textbooks on the subject that can help you learn the basics of SQL. I know, textbooks feel old and clunky, but in my opinion, textbooks are massively underrated. They are:

* Curated
* Complete
* Comprehensive

In a way that a lot of online blogs and YouTube tutorials aren't, because they're written to be self-contained units of knowledge.

I love "Head First SQL" by Lynn Beighley and "SQL Cookbook" by Anthony Molinaro.

(I've written before about my strong feelings on [the best books to learn computer science](/computer-science/computer-science-books/) if you agree and want to learn more.)

## Why do backend devs need to know SQL?

"Why do backend devs use SQL at all?" moaned my fired friend as we commiserated over the loss of his job. "It's a terrible language." My friend had never written any SQL, instead relying on high level libraries to do the work for him. While it's okay to ORMs and libraries, it's still important to understand SQL for when you need to do something a bit more complex, or to do something manually.

My friend didn't mean it, he was just grouching. SQL is a pretty great language - simple, relatively intuitive, with a solid community of SQLovers who haunt StackOverflow and Reddit, ready to answer your questions whenever.

SQL is the tried and true language for managing relational databases. While there are other database tools available (and we'll get into those in the sections below) SQL is widely used and supported by all major relational database management systems.

It lets backend developers interact with data stored in databases in a standardized way, making it easy to work with, no matter what database system your company uses.

It also has robust features for database design, transaction management, and security. In short, it's an essential tool for backend developers who work with relational databases.

As a backend developer, here are a few ways you might use SQL in your day-to-day job:

### Manage data

As a backend developer, you work with databases to create, modify, and retrieve data. For example, if you are working on an e-commerce website, you might retrieve all the orders placed by a specific customer so that you can display them on their account page. You'd use SQL to do that.

### Optimize queries

With SQL, you can write complex queries to retrieve data from multiple tables at once. As a backend developer, you optimize these queries to make them efficient and effective.

For example, if you're working on a healthcare system that stores patient data, you might need to retrieve all the patients who have a specific medical condition. By writing an optimized SQL query, you can quickly retrieve this information without causing delays in the application.

### Design databases

Not only does SQL retrieve and modify data, but it's also used to design and create databases,

Imagine you're a backend developer working on a social media platform. You might need to design a database that stores user information, posts, comments, and likes. You'd use SQL to create a well-designed database so the application can handle a large volume of data and is easy to maintain.

### Integrate databases with other technologies

The potential tech stack of a backend developer just grows and grows. Luckily, SQL can be used to integrate databases with other technologies.

As a backend developer, you might need to integrate the database with other tools, such as data analytics or machine learning.

For example, if you are working on a financial application, you can use SQL to integrate the database with a tool that analyzes financial data and provides insights into investment opportunities.

Overall, SQL is a powerful tool that is essential for backend developers who work with databases. When you're a SQL master, you have the power to manage data efficiently, optimize queries, design databases, and integrate with other technologies.

## What other database tools and technologies should you know as a backend developer?

"I've heard something about a NoSQL movement," you might be musing. "Do I still need to know SQL if I join a NoSQL company?"

Mhmmm... probably. I believe all backend developers should know SQL, or at least know the basics. There are even a few additional tools and technologies that are SQL-adjacent, or database-related, that you should still know.

### Databases

SQL is like a universal language for interacting with databases, while databases like MySQL, PostgreSQL, and SQLServer are specific software programs that use SQL to manage and store data in a structured way.

When you use a database like MySQL or PostgreSQL, you're using SQL as the language to communicate with the database and insert, retrieve, update, or delete data.

Here's a short table summarizing the main databases you should be aware of:

| [PostgreSQL](/backend/top-backend-technologies/#1-postgresql)                     | Gold standard, open-source, used by pros, and the go-to for production |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [SQLite](/backend/top-backend-technologies/#2-sqlite)                             | Slimmer, lighter SQL database. Serverless and self-contained           |
| [MySQL](/backend/top-backend-technologies/#3-mysql)                               | Legacy, the old "standard" but not as good as PostgreSQL nowadays      |
| [MariaDB](/backend/top-backend-technologies/#4-mariadb)                           | Faster, more lightweight than MySQL, not as heavy-duty as PostgreSQL   |
| [Oracle](/backend/top-backend-technologies/#5-oracle)                             | Enterprise, high degree of scalability                                 |
| [Microsoft SQL Server](/backend/top-backend-technologies/#6-microsoft-sql-server) | Best for .NET projects. Not open source. Used by Microsoft (of course) |

I've written more on the subject in my [blog post](/backend/top-backend-technologies/#top-six-back-end-sql-databases) on the top backend SQL databases portion.

### NoSQL databases

Wait a minute, why am I forcing you to read about NoSQL specifically in an article about why backend developers should know *SQL*?

I know I said SQL is the "universal language," but not so fast. While SQL is the *most* common type of database, there are also NoSQL databases like MongoDB, Cassandra, and Redis that store data differently and can be more suitable for certain use cases.

I've written quite a bit about these, so if you want to learn more, I recommend reading the [NoSQL portion](/backend/top-backend-technologies/#top-five-back-end-nosql-databases) of my blog post on the [top backend technologies](/backend/top-backend-technologies) to know in 2023. SQL is great, but there are limitations.

Each of these databases was typically created to address one of those limitations. You need to know about these because they mostly patch the blind spots of SQL.

Here's a brief table summarizing the main differences:

| [MongoDB](/backend/top-backend-technologies/#1-mongodb)       | The most standard of the NoSQL databases. Used for querying information in a series of JSON-like docs.                              |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [Redis](/backend/top-backend-technologies/#1-mongodb)         | Hyper-optimized for more ephemeral work like caching and in-memory data structuring. Typically used in addition to other databases. |
| [Elasticsearch](/backend/top-backend-technologies/#1-mongodb) | Search and log analysis                                                                                                             |
| [Firebase](/backend/top-backend-technologies/#4-firebase)     | Owned by Google, cloud-hosted Backend-as-a-service                                                                                  |
| [Cassandra](/backend/top-backend-technologies/#5-cassandra)   | Peer-to-peer network, used for super high volume workloads                                                                          |

## Final thoughts 

Do backend developers need to know SQL? Yes, yes, a thousand times yes. It's a truly fundamental, necessary language to get a job as a backend developer and excel.

It's a great language to know for the backend since it's all to do with manipulating data and databases. It's relatively easy to learn – if you prefer hands-on learning and practicing as you go, SQL can be fun to learn because you can see the results of your queries right away, so there's an instant-gratification element.

Hand-in-hand with SQL come a couple of other key competencies to know, such as SQL databases and even NoSQL databases. I recommend being familiar with at least one or two from each list so you can make an informed decision when applying for jobs.

Hopefully, this article has answered the question of whether you should finally start poking around in SQL, and given you a list of places to start. Best of luck on your backend development job-hunting journey.
