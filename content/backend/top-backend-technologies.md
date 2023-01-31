---
title: "The Top 22 Backend Technologies to Learn in 2023"
author: Natalie Schooner
date: "2022-11-16"
categories: 
  - "backend"
images:
  - /img/800/technology.png.webp
toc: true
---

A backend technology is anything used server-side to build stable and efficient web architectures.  Back-end technologies include programming languages, databases, communication mechanisms, or frameworks that make up the building blocks of a web application's back-end.

In other words, we're talking about any kind of tech that helps you, as a backend developer, build or maintain the backend of a website.

Even established backend developers need to constantly keep up to date with the best backend technologies of the day. You never know what a new company will use to maintain its backend, or if the company will require a migration from an older product to something more modern. You may even get the chance to create a new project and select a backend technology *yourself*.

As technology moves so fast in this field, it’s beneficial for your development as a backend dev to be familiar with the most useful and most used backend technologies today. Here are the top 22 backend technologies you should be familiar with. We’ll cover eight languages, six relational databases, five nonrelational databases, and three message queues.

## Top eight back-end languages

We already covered the [top eight backend programming languages](/backend/best-backend-programming-languages/) in a recent post, but I’ll summarize them all here briefly for your convenience:

### 1. Go

![go-banner](/img/800/go-banner.webp)

Go is the fastest-growing and most-desired backend language, used by companies like Uber, YouTube, and Spotify. Backend developers like it because it’s super safe to use, it’s incredibly simple to pick up, and it’s fast. You can get started [learning Go here](https://boot.dev/learn/learn-golang).

### 2. Python

![python-banner](/img/800/python-banner.webp)

Python is the most popular backend programming language for beginners. It has a simple and limited syntax, which makes it easy to read and write. Its immense number of libraries makes it incredibly versatile. Companies like Airbnb, SpaceX, and Stripe rely on Python to maintain their backends. You can get started [learning Python here](https://boot.dev/learn/learn-python).

### 3. JavaScript

![js-banner](/img/800/javascript-banner.webp)

JavaScript is the most popular backend language for all developers, though it’s mostly used for frontend dev. However, its frameworks like NodeJS make it a popular choice for backend developers too. Companies like Facebook, Google, and eBay use JavaScript. You can get started [learning JavaScript here](https://boot.dev/learn/learn-javascript).

### 4. Rust

![rust-banner](/img/800/rust-banner.webp)

Rust is a newbie on the backend development scene, but it’s the most beloved language for the seventh year running – ever since its inception. It’s open source, it has rich libraries, and it’s one of the fastest languages around. Meta is notable for being quick to jump on the Rust bandwagon, having used it since 2016. AWS also uses it to write infrastructure-level networking.

### 5. Java

![java-banner](/img/800/java-banner.webp)

This is a legacy backend language. It’s the safe bet, unpopular with newbies but so entrenched in so many companies’ backends that it’s not going anywhere anytime soon. Companies like Google, Netflix, Uber, and Facebook all still rely on it. It may not be the top choice in the future, but for now, it’s good to be familiar with it.

### 6. PHP

![php-banner](/img/800/php-banner.webp)

Nobody (literally just 2% of StackOverflow survey respondents) wants to learn PHP. But it’s on 75% of websites today. Like Java, it’s not the best or sexiest language but it’s worth knowing. Meta in particular has used it to develop Facebook’s backend since 2004. Slack uses PHP to streamline web request time.

### 7. Ruby

![ruby-banner](/img/800/ruby-banner.webp)

Want money? Learn Ruby. Thanks to the Ruby on Rails framework, Ruby backend developers command a hefty salary. However, it’s still pretty niche among other languages like JavaScript. Currently, companies like Crunchbase and Etsy use Ruby on Rails to develop and maintain their backends.

### 8. SQL

![sql-banner](/img/800/sql-banner.webp)

Gotcha! SQL isn’t a programming language like the other seven. But it’s, as we’ll get into below, a very useful and popular query language. Backend developers often use SQL to communicate between relational databases. It’s hard to find a company that wouldn’t find SQL knowledge useful, so count this as a must-know language to be hired. You can [learn SQL here](/news/learn-sql-course-released/).

## Top six back-end SQL databases

OK, we’ve covered coding languages. Now onto databases. A SQL database is a relational database, which means that it stores data in tables that are related to one another. Think rows and columns.

Relational databases usually scale vertically. Data lives on a single server, and you can scale by adding more computer power, like CPU, GPU, and RAM, to that one server.

“Top” is subjective, but I’m somewhat data-driven. These are the top backend SQL databases as defined by [StackOverflow’s tremendous annual developer survey](https://survey.stackoverflow.co/2022/#technology).

It's worth pointing out that SQL is a query language, and when you learn it once, it enables you to work with *all* of the specific SQL databases we're about to cover in more detail. You can [learn SQL here](/news/learn-sql-course-released/).

### 1. PostgreSQL

![postgres-banner](/img/800/postgres-banner.webp)

PostgreSQL is the gold-standard when it comes to open-source, professional-grade SQL databases. It’s used more by professionals (46.5% pros versus 25.5% learning to code). Unlike MySQL, it’s seen as the go-to database for production, high-volume data operations.

It doesn’t just store data – it lets you define data types, index types, and functional languages. Plus, it is fully open source and very customizable. It’s used by a long laundry list of companies including (but not limited to) Apple, BioPharm, Cisco, Etsy, Facebook, Instagram, Skype, and Spotify.

#### Where can I learn PostgreSQL?

I like the [Complete Python and PostgreSQL Developer Course](https://www.udemy.com/course/complete-python-postgresql-database-course) which will teach you Python and PostgreSQL by building real-world projects.

### 2. SQLite

![sqlite-banner](/img/800/sqlite-banner-bg.webp)

A descriptive name: SQLite is a slimmer, lighter SQL database. It’s a popular database, used by [32% of Stack Overflow survey respondents](https://survey.stackoverflow.co/2022/#most-popular-technologies-database). It’s serverless and self-contained.

Compared to Postgres, it’s very easy to get up and running. However, the tradeoff is that it only supports a limited set of data types (Blob, Integer, Null, Text, and Real). It’s also not good for multiple users, it’s not very scalable, and it’s not optimized for performance.

For all that, it’s the most widely-deployed database in the world because it’s so lightweight. It’s also totally free to use and open source, though you can opt to pay for support with a professional license.

The SQLite site [documents](https://www.sqlite.org/famous.html) plenty of examples of companies that use it, including

* Apple for most of the native applications running on Mac OS-X desktops and servers, and iOS devices.
* Adobe as the application file format.
* Facebook as the SQL database engine in their osquery product.

#### Where can I learn SQLite?

Our very own [Learn SQL course](https://boot.dev/learn/learn-sql) uses SQLite as the engine, so it's the best place to get started!

### 3. MySQL

![mysql-banner](/img/800/mysql-banner.webp)

MySQL is the "standard" SQL database. It’s the most used database overall, with [46.85%](https://survey.stackoverflow.co/2022/#most-popular-technologies-database) of Stack Overflow respondents using it. It’s a decent fit for many projects. That said, there are not many reasons to use it over PostgreSQL these days. They are *very* similar technologies, but many developers agree with me that Postgres is simply the more modern solution.

It used to be fully open source but was acquired by Oracle a while back. Oracle distributes it under a dual license – you can use the OSS version if you like, but if you work at a company that doesn’t want its MySQL-based product to be OSS as well, you’ll have to pay for a license.

Who uses it? Well, who doesn’t use it is a better question. Content management systems like Drupal and WordPress rely on MySQL, so it’s on virtually every blog post you’ll ever read. Companies like Facebook, Google, GitHub, Netflix, Spotify, and others use MySQL.

#### Where can I learn MySQL?

I recommend Programming With Mosh’s free three-hour [tutorial](https://www.youtube.com/watch?v=7S_tz1z_5bA) on the subject. He offers a fuller paid tutorial (linked on the video), so if you enjoy this free one, consider that one.

### 4. MariaDB

![mariadb-banner](/img/800/mariadb-banner.webp)

MariaDB is used by a smaller percentage of developers – just 17.9%. It has an interesting history – back when Oracle was acquiring MySQL, a bunch of developers got worried about what that would mean for one of the most relied-upon SQL databases. MariaDB is a fork of MySQL and fully open source, licensed under GPL which has very, very few limitations for academic, commercial, or personal use.

Those developers made some improvements, too: MariaDB has 12+ storage engines and 200k+ connections, making it faster and more lightweight than MySQL. It’s used by a more niche selection of companies like Bandwidth, DigiCert, InfoArmor, Oppenheimer, Samsung, SelectQuote, and SpendHQ. However, I expect it will grow in popularity over the coming years.

#### Where can I learn MariaDB?

The best source is the [MariaDB website](https://mariadb.com/kb/en/training-tutorials/) itself.

### 5. Oracle

![oracle-banner](/img/800/oracle-banner.webp)

Didn’t Oracle acquire MySQL? Why does it have a separate entry on this list?

Oracle is a company that owns both the Enterprise "Oracle" database as well as the partially open-source MySQL. Used by just 11.5% of developers, it’s not as customizable as MySQL, but it is better for a higher degree of scalability. It’s not set up to do whatever you want, it’s set up to do a few limited things with larger databases and more interactions, and with a larger concurrency pool than MySQL. It’s also more secure.

Companies like Netflix, LinkedIn, eBay, and Intuit use Oracle. It's typically used by very large enterprises, and I wouldn't recommend it for anything smaller.

#### Where can I learn Oracle?

I recommend [Oracle’s learning platform](https://education.oracle.com/learning-explorer). As a paid product, they have a vested interest in teaching you how to use it for free.

### 6. Microsoft SQL Server

![microsoft-sql-server-banner](/img/800/microsoft-sql-server-banner.webp)

Also referred to as MSSQL, this SQL database is used by 26.7% of Stack Overflow survey respondents. As the name gives away, this database was developed by Microsoft, so it’s not OS. You need licenses to run it.

This database is primarily used with .NET. As you might imagine, it’s better for Windows-based projects that gel well with Microsoft products. It’s more secure than MySQL. Unlike MySQL, which allows processes to manipulate binaries and database files directly, MSSQL requires users to run an instance to do that.

Of course, Microsoft itself uses MSSQL, but other notable companies like Accenture and Costco use it as well.

#### Where can I learn MSSQL?

Udemy’s [course](https://www.udemy.com/course/ms-sql-server-learn-ms-sql-server-from-scratch/) is relatively affordable ($85) and comprehensive for beginners.

{{< cta1 >}}

## Top five back-end NoSQL databases

What is a NoSQL database? It’s a non-tabular database that uses different data models for storing, managing, and accessing data. It can be document-oriented, key-value, graph, wide-column, or something else.

Unlike SQL databases, NoSQL databases are good at storing unstructured data like texts, photos, videos, and PDF files. They also tend to be better about scaling up read-only operations. That said, each NoSQL database is different, and they're all designed to optimize for specific things that you wouldn't necessarily get out of a standard SQL database.

Pros: Many of these databases scale horizontally, and tend to have better read performance. However, many make this tradeoff by giving up things like [data integrity](/bitcoin/achieving-data-integrity-using-cryptography/) and [ACID compliance](https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/).

Again, I’m using “top” here as defined by StackOverflow’s survey.

### 1. MongoDB

![mongodb-banner](/img/800/mongodb-banner.webp)

Like many other databases we've talked about here, MongoDB offers a free open-source version and a paid Enterprise version. It’s the most standard of the NoSQL databases, so I’ll be using it as a basis for comparison for the NoSQL databases.

It's used by [28.3% of respondents to the Stack Overflow survey](https://survey.stackoverflow.co/2022/#most-popular-technologies-database) which makes it the most popular NoSQL database. MongoDB allows you to query documents by single or multiple keys, ranges, or search texts. Rather than representing information in tables and rows, it represents information as a series of JSON-like documents. It has a more loose structure than the strict row/column format of a SQL database.

Forbes used MongoDB to migrate to the cloud. Toyota used it as well. Sonoma used it to scale its app. At the end of the day, Mongo vs SQL is mostly an architectural difference when it comes to managing data. One isn't better than the other, just different.

#### Where can I learn MongoDB?

MongoDB has its own “[university](https://university.mongodb.com/)” with a great set of tutorials to learn MongoDB.

### 2. Redis

![redis-banner](/img/800/redis-banner-bg.webp)

Redis is the second most popular NoSQL database, used by 22.1% of respondents. Unlike MongoDB, you can only carry it through primary key access, which means it's got a more limited query functionality. It's worth noting that this functionality can be extended with Redis modules, but the out-of-the-box Redis is more limited.

One of the primary reasons for it's popularity is that it doesn't compete with the other databases used here. It's usually used *in addition* to one of them. It's hyper-optimized for more ephemeral work like caching and in-memory data structuring.

The main differentiator between Redis and MongoDB is that it uses an in-memory key storage value. This means that data is stored on the host’s RAM, not on the desk. This makes it fast – it can make millions of requests per second. But it means you are limited in terms of the dataset’s size. It’s also single-threaded.

If you have small data sets and you're looking for speed, choose Redis. That's what Twitter, GitHub, Snapchat, Craigslist, Stack Overflow, and [more](https://techstacks.io/tech/redis) companies did.

#### Where can I learn Redis? 

The Redis help [docs](https://redis.io/docs/getting-started/) are a good place to start.

### 3. Elasticsearch

![elasticsearch-banner](/img/800/elasticsearch-banner.webp)

Elasticsearch, as the name implies, is a more limited and yet more powerful type of NoSQL database used by 12.2% of respondents. It's open source and built with Java. It does now have closed licensing models for new versions beyond version 7.9.

As you may have been able to guess, Elasticsearch is used for search and log analysis. It's typically used in conjunction with Kibana and Logstash, more commonly known as the ELK stack. It operates as a search platform for access, retrieval, and reporting of data, logging and log analytics, and the analysis of infrastructure metrics. Some companies use it for security and business analytics as well.

It’s used by Uber, Shopify, Udemy, and [others](https://stackshare.io/elasticsearch).

#### Where can I learn Elasticsearch?

Elastic.co has its [own](https://www.elastic.co/training/) training, certification, and events for you to peruse.

### 4. Firebase

![firebase-banner](/img/800/firebase-banner-bg.webp)

Google has a habit of saying, “Hey the existing technology doesn't really work for us. Let's make something brand-new that suits our needs, and make it so good that other people start to use it too!” Google did it with [Golang](https://go.dev) and with Firebase.

While only 8.72% of Stack Overflow respondents use Firebase, it does have some pretty nifty use cases. It's owned by Google and is fully cloud-hosted. This cloud hosting means that you can store and sync data between users in real time. A copy of every database change is actually retained in the Cloud Firestore.

You can also execute backend code that responds to events triggered by your database using Cloud Functions for Firebase. Firebase is optimized in particular as a "back-end as a service". The idea is that by using Firebase, you don't need your own application servers. Your mobile apps can talk directly to the database.

Firebase is used by the NYT, Lyft, Accenture, Instacart, and [others](https://careerkarma.com/blog/companies-that-use-firebase/). Like Go, I expect this number to grow as more people use and evangelize it.

#### Where can I learn Firebase? Where to learn:

Google offers some great [pathways](https://firebase.google.com/community/learn) to learn Firebase.

### 5. Cassandra

![cassandra-banner](/img/800/cassandra-banner.webp)

I'm not talking about the prophetess, though that's what the name pays homage to. The Cassandra database has a much smaller user base, with only 2.7% of Stack Overflow respondents reporting that they use it. It's an interesting one because it’s a *very* distributed and scalable database. All the master nodes are in communication with each other in a peer-to-peer network, which means there’s no single point of failure. By comparison, PostgresQL has a primary node/replica node model.

At the end of the day, Cassandra is use for *extremely* high volume work loads. Heck, [Discord uses it](https://discord.com/blog/how-discord-stores-billions-of-messages#:~:text=Cassandra%20was%20the%20only%20database,any%20impact%20on%20the%20application.) to store the billions and billions of messages sent on their app.

It's highly available with partition tolerance as per the CAP theorem. This means that it's less consistent, but it's more available than MongoDB. It's also one of the few NoSQL databases that is not an object-oriented model. It uses a more traditional table structure.

Sky uses Cassandra for database persistence. Spotify uses it for personalization. Target uses it to maintain stability and consistency.

#### Where can I learn Cassandra?

Udemy has a solid [course](https://www.udemy.com/course/apache-cassandra) for $50.

## Top four message queues

What is a message queue?

Let's look at it like this: a message is basically just data that was sent from a sender app to a receiver application. That data can be an array of bytes with some metadata attached. For example, the `accounts application` may publish a "Joe created an account" message, then the `emails application` receives that message and sends a welcome email to Joe.

A "message queue" is just an ordered list of those messages coming from a sender that need to be handled by a receiver.

It may help to think of a message queue as an asynchronous communication protocol. You can send messages and let them be handled when the systems are ready to handle them. Meanwhile, you can go on and do other things without needing to wait for an immediate response.

This approach allows scaling because you're not blocking the app from receiving more messages.

There are two typical systems for message queues: Pub/sub, and message broker. A pub/sub system is a message distribution pattern that lets producers PUBlish each message they want to any services that SUBscribe to them, like a broadcast style. It’s a one-to-many relationship.

Meanwhile, a message broker will do a little more – it will validate, route, store, and deliver messages to intended recipients. Brokers are intermediates between other apps and can translate messages between different protocols.

### 1. RabbitMQ

![rabbitmq-banner](/img/800/rabbitmq-banner.webp)

RabbitMQ is the most widely deployed open-source message broker. It's lightweight and easy to use for both on-prem and cloud deployment. It's versatile as it can support multiple messaging protocols. And it can meet high-skill availability requirements because it can be deployed to both distributed and federated configurations.

The consumer will set a prefetch limit, and RabbitMQ will push messages up to that limit.

It’s used by T-Mobile and Runtastic to give some examples.

#### Where can I learn RabbitMQ?

If this sounds like your cup of tea, you can learn RabbitMQ on RabbitMQ’s own [website](https://www.rabbitmq.com/getstarted.html). They have a ton of great tutorials to get started.

### 2. Kafka

![kafka-banner](/img/800/kafka-banner.webp)

Kafka, by contrast, is a pub/sub message bus. It's geared for streams and high-ingress data replay. It actually isn’t even a queue – instead, it appends messages to a log, where they remain until they're read or the retention limit is reached.

It's used by 10.3% of respondents to the Stack Overflow survey. (This isn't super helpful because neither RabbitMQ nor SQS showed up at all on the survey, so it's hard to compare, but I wanted to include it.)

It's pull-based, which means that users can request message batches. It can be used for batch messages for higher throughput and more effective message delivery.

It's trusted by some of the best in business, including Goldman Sachs, Target, and Cisco.

#### Where can I learn Kafka? 

I recommend [Udemy’s Learn Kafka for beginners course](https://www.udemy.com/course/apache-kafka/) which comes to $99.

### 3. PubSub

![pubsub-banner](/img/800/pubsub-banner.webp)

PubSub is Google's proprietary cloud offering for message queues. It's *very* similar to Apache Kafka, but requires no configuration or maintenance - the only way to use it is through Google's cloud offering. We actually use PubSub to run [Boot.dev's back-end learning platform](https://boot.dev).

#### Where can I learn PubSub? 

I recommend [the offical docs from Google](https://cloud.google.com/pubsub#section-5).

### 4. SQS

![sqs-banner](/img/800/sqs-banner.webp)

Like Google, Amazon is starting to get into the habit of just building the services they need to make their business a success. SQS is an example of this. SQS stands for simple queue service. It's a pub/sub message broker system. Because it's based on AWS, it's great for scaling up and down. However, also because it's based on AWS, it doesn't actually have any hosting available outside AWS. It's also expensive.

Basically, if you're using AWS, it's a great choice. If not, maybe choose something else.

It’s used by Cigna, Amtrak, Tableau and [others](https://discovery.hgdata.com/product/amazon-simple-queue-service-sqs).

#### Where can I learn SQS?

Amazon’s [own](https://aws.amazon.com/sqs/getting-started/) learning portal is the best place to learn SQS.

{{< cta2 >}}

## Top five bonus back-end technologies

Aside from these languages and databases, I'd recommend looking into a few other domain-specific technologies if you're interested in going as deep as you can into back-end development.

* Docker: Containerization
* Kubernetes & Helm: Container management
* Github actions: CI/CD
* Bash: Shell scripting
* AWS/GCP: Cloud environments

## Final thoughts

If you’re a backend developer, you may be slightly overwhelmed with this extensive (and yet not even exhaustive!) list of the top backend technologies. *Remember, you don’t have to know all of them.* But it’s worth being familiar with one or two from each list so you can make an informed decisions when applying to jobs, or when choosing a new backend technology to use.

This list of backend languages, SQL databases, NoSQL databases, and message queues will go a long way toward getting you well-versed in the most important backend technologies you should be familiar with in 2023.
