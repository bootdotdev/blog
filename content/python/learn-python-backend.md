---
title: "Want to Become a Python Back-end Developer? Start Here."
author: Natalie Schooner
date: "2023-02-17"
categories:
  - "python"
images:
  - /img/800/python-building.png.webp
imageAlts:
  - "Python in front of a building"
---

Myth #1: "Python is too slow for back-end development."

Myth #2: "Nowadays, you should do all back-end development in JavaScript/TypeScript."

Myth #3: "Python is only good for data science and machine learning."

If you take a quick perusal through Reddit or speak with other developers who are more set in their ways, you might run into one of these (incorrect) opinions. Don't listen to them. Python is _great_ for back-end development, and many employers feel the same way – just check out [LinkedIn](https://www.linkedin.com/jobs/search/?currentJobId=3472925498&keywords=python%20backend), [Indeed](https://www.indeed.com/jobs?q=python+backend+developer&l=&from=searchOnHP&vjk=2c0a7341ec7f089d), or [Glassdoor](https://www.glassdoor.com/Job/backend-python-developer-jobs-SRCH_KO0,24.htm) and you'll see thousands of jobs for Python back-end developers.

Who uses Python backends? More companies than you might expect. Google, Spotify, and Pinterest all use Python.

Aside from employer demand, there are plenty of reasons to want to become a Python back-end developer. [Back-end development is a solid job](/backend/how-much-do-backend-devs-make/), secure and with great job prospects and benefits. Python is a fun programming language that can help you do a lot of different tasks. It's the [most popular](https://statisticstimes.com/tech/top-computer-languages.php) programming language, too, and the associated Python back-end salary is high – [around](https://www.indeed.com/career/python-developer/salaries) \$114k a year.

The issue is Python is typically taught either as a beginner's programming language or specifically for data science. It's great for both those purposes – the syntax and simple vocab make it a breeze to pick up, while extensive libraries make it ideal for data science. That's not a problem, it just means you'll need to also [learn some back-end skills](https://www.boot.dev) on top of just Python programming if you want to become a back-end developer who writes Python.

In this article, I'll break down how to become a Python [back-end developer](/backend/become-backend-developer/). I'll discuss:

- What exactly a Python back-end developer does
- What back-end development skills you need
- What Python skills you need, aside from the usual suspects
- What projects and certifications can help

Let's dive in.

## I mean, what even does a Python back-end developer do all day?

Pretty much the same as a Javascript, Go, Rust, or any other kind of back-end developer. The job description of a back-end developer remains pretty stable no matter what kind of programming language you use to accomplish your goals.

As a Python back-end developer, you'll:

- Create the back-end of a website or app
- Maintain and robustify the servers that house data
- Deploy code to production
- Work with DevOps teams
- Work with the frontend team to integrate your back-end logic with a user interface
- Integrate with and query databases
- Do some security testing and hardening
- Look at a lot of logs

If you know anything about back-end development, that list of tasks should look pretty familiar to you since it's basically unchanged from any other back-end job description.

(If you don't know much about back-end development and want to learn more, I've covered back-end development [job descriptions pretty here](/backend/backend-job-description/) if you want to check out more info about that.)

Let's take a closer look at where you can learn the skills you need to become a Python back-end developer specifically.

## I already know Python, can I be a Python back-end developer yet?

Let's take a moment and reflect on how great a language Python is. It's so flexible, so scalable, and so rich in libraries and frameworks that make it so useful for doing so many things. That's awesome.

But that also means you can spend years programming in Python without ever touching any of the skills you'd need to become a Python back-end developer.

### Basic Python

Of course, to become a Python backend developer, you will need basic Python skills. These you probably already know, so I won't spend much time here – just make sure you're comfortable writing for loops, you know how to write functions, and you're familiar with classes and objects.

If you want a quick revision, we've got a [solid Python course here](https://www.boot.dev/courses/learn-code-python), or you can review Python's [shockingly readable documentation](https://docs.python.org/3/).

### Front-end

> "Did I click on the wrong article? Why am I learning about front-end?"

As I alluded to above, the back-end of an app doesn't work in a vacuum. You'll be building a system that _talks_ to the front-end, or what your user sees and interacts with.

Imagine trying to design a plug that fits into a socket you've never seen. Possible, right? But hard. It's much easier if you are familiar with the socket first.

Similarly, it's possible to do back-end work without ever knowing how the front-end works, but it's so much easier once you know a bit about the front-end.

You don't have to be an expert by any means, but I recommend picking up some basic front-end skills, or at the very least, the networking layer than acts as the glue between a front-end and back-end. Let's talk about that.

### Networking

I'm not talking about making friends, although that never hurts. I'm talking about the services that allow communication between different systems and services.

Here are a few networking skills it's useful to know as a Python back-end developer, along with a few places to learn more about them:

- Understand TCP/IP and HTTP protocols. Check out this [HTTP course](https://www.boot.dev/courses/learn-http-clients-golang) to learn all you'll need to know about how front-end apps request information from a back-end.
- Be familiar with RESTful API design. This is a common architectural pattern to build web APIs that are scalable, maintainable, and easy to use. StackOverflow has a solid [guide](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/) on the subject.
- Be aware of some of the networking libraries such as [Requests](https://pypi.org/project/requests/), [Twisted](https://twisted.org/), or [SocketIO](https://python-socketio.readthedocs.io/). These help services communicate over the network, handling connections and data exchange. I've linked to the relevant documentation for each library.

### Linux

As you may already know, Linux is the most popular operating system for servers and cloud-based infrastructure.

As a Python back-end developer, you should know how to operate in a Linux environment, which you'll almost certainly be working with. Do you know how the command line works? Can you work without a GUI?

The answer to both of those questions should be "yes" before you pursue your path any further.

### API design

API design is a pretty critical part of being a Python back-end developer. As a backend developer, you could be in charge of designing and implementing the API endpoints that power the front-end or client side of the application. You need to ensure that the API is well-designed, scalable, and secure, and can handle expected traffic levels.

To secure your job, you should be intimately familiar with concepts such as:

- Endpoint design
- Data modeling
- Request and response formats
- Authentication and authorization
- Rate limiting
- Error handling
- and more.

Now, web frameworks, such as Flask and FastAPI, provide built-in support for building RESTful APIs. But as I'll get into below, it's good to know the "why" before you look for "how" shortcuts.

### Web frameworks: Django, Flask, and FastAPI

One reason Python is good for back-end development is its frameworks. They make complex, hairy, repetetive things simple.

This is the longest section because as a Python back-end dev, this is the real non-negotiable bit. You should be deeply familiar with at least one of these frameworks since any Python back-end development job will require at least one of them.

But… before I jump in, a brief caveat as promised. Over here at Boot.dev, we've got a complex relationship with frameworks. (You can read more about that [here](/backend/dont-start-with-frameworks/) if you're interested.)

The TL;DR is that we don't recommend _starting_ with frameworks to [learn back-end development](https://www.boot.dev), since it's like learning to bake by using cake mix.

You can get a result that _looks_ good, but you're left with no understanding of the chemistry that makes it all work. And that means that when things go wrong, you have no clue how to look under the hood and get things working again.

But once you're familiar with the why behind the tasks that frameworks do, like building a server, it often makes sense to use frameworks to make your work go faster.

There's some [discussion](https://www.reddit.com/r/Python/comments/sl6jne/django_or_flask_and_why/) about which of these frameworks is "better," but in reality each has its place.

I recommend beginning with [Flask](https://flask.palletsprojects.com/) since it's simpler. It's so easy to get up and running \* you can easily build a little demo prototype app, but it's also easy to scale it up. It offers basic features, but if you want to get more complex, you'll need to know how to add libraries or plugins.

[Django](https://www.djangoproject.com/start/) is a good next step. It's commonly described as a comprehensive, batteries-included web framework for Python. A team player that can do it all. It's got a much steeper learning curve, but it's typically used in bigger enterprises because of its standard structure and conventions.

[FastAPI](https://fastapi.tiangolo.com/) is perfect for building high-performance APIs and web applications, especially if you need async support and automatic API documentation.

However, at the end of the day, you should research which technologies are being used by the companies you're interested in working for. If you're applying for a job at a company that uses Django, you should know Django. If they use Flask, you should know Flask. And so on.

### Security and authentication protocols

A lot of being a back-end dev is doing things that rightfully should be their jobs, like DevOps, database admin, and security, without complaining. As a Python back-end developer, it's no different.

As a backend developer, you need to be aware of security issues that can arise when communicating over the network. You should have a thorough understanding of concepts like encryption, SSL/TLS, and OAuth that can help you build more secure and reliable systems. While not _required_, [understanding the basics of the cryptography](https://www.boot.dev/courses/learn-cryptography-golang) involved in these protocols can help you build more secure systems.

### Databases \* SQL and NoSQL

As a Python back-end developer, most employers will expect you to know all about backend technology, and that includes SQL and NoSQL databases.

I think SQL is more standard and hence more important to know, but it's a good idea to be familiar with NoSQL as well.

SQL is a language used to query relational databases, which store more standard data formats. NoSQL databases store less conventional data, such as images, graphs, or key-value pairs.

I've touched on these before in [this article](/backend/top-backend-technologies/#top-six-back-end-sql-databases), but I'll briefly summarize them again here. To be a good back-end developer, you should be familiar with the following SQL database concepts:

- Data modeling and database schema design
- SQL queries, subqueries, and joins
- Indexing and optimizing database performance
- Relational data integrity and constraints

I recommend getting your feet wet with PostgreSQL, SQLite, MySQL, and MariaDB. If you want to [learn SQL, check out this course](https://www.boot.dev/courses/learn-sql).

As for NoSQL, these are the concepts you'll need:

- Data modeling and document design
- Distributed architecture and scaling
- Querying and indexing with NoSQL-specific query languages or APIs
- Data sharding and partitioning strategies
- Key-value storage and caching

You're most likely to come across MongoDB, but you might also stumble upon Redis, Elasticsearch, or Firebase.

As a Python back-end developer specifically, I recommend checking out [SQLalchemy](https://www.sqlalchemy.org/) and [PyMongo](https://pymongo.readthedocs.io/) libraries, which are used respectively for SQL and NoSQL.

### DevOps

If you're not directly doing DevOps tasks like automating the build, testing, and deployment of software, you'll be working closely with the DevOps teams who do.

As a Python back-end developer, understanding DevOps has become increasingly important. In fact, at smaller companies, sometimes the roles of [DevOps and Backend Developer are combined](/devops/backend-devops-roles-merging/).

DevOps is a set of practices that combines software development and IT operations to create a more efficient and reliable software development process. Along with automation, you should know how to manage infrastructure and monitor performance and logs.

To be fair, this is true of all flavors of back-end developers, not just a Python exclusive.

## How do I prove I know all this Python stuff to become a back-end dev?

OK, say you know all these technologies, frameworks, and concepts already. Employers won't just take your word for it.

You'll be tested on these concepts at the interview stage, but A) anyone can be trained to parrot out the correct answer, and b) employers will be looking at your portfolio pre-interview. If you want to become a Python back-end dev, your project portfolio is of utmost importance.

There are two paths I recommend to develop projects you can put on your portfolio: come up with your own projects that illustrate your mastery (or at least familiarity) with the skills above, and nab certificates from external, trusted sources.

Both are good at polishing your skills and giving you a tangible thing you can point to and say, "Yeah, I know how APIs work."

Let's take a look at a few examples of both.

### Personal portfolio projects

I've covered what I consider to be the [best backend project ideas here](/backend/best-backend-projects/), most of which you can repurpose to use with Python. I'll add a few more options for Python back-end development project ideas, with linked tutorials:

- [Build a developer portfolio](https://kristian-roopnarine.medium.com/how-to-make-a-developer-portfolio-with-django-rest-and-react-e16e52261f2f). Use a popular web framework like any of the ones I mentioned above. This will help show that you know how REST APIs work, you're familiar with the framework you use, and if you want, you can add [user authentication](https://kristian-roopnarine.medium.com/how-to-implement-login-logout-and-registration-with-djangos-user-model-59442164db73?source=author_recirc-----e16e52261f2f----2----------------------------).
- [Convert your Python code into a library or package](https://towardsdatascience.com/how-to-convert-your-python-project-into-a-package-installable-through-pip-a2b36e8ace10). This proves you're familiar with Working with Python Modules, creating Python Libraries/Packages, and uploading and maintaining packages on PyPI. More importantly, it helps prove that you want to build things that make an impact on other programmers, which is a key part of being a back-end developer.
- Develop a platform-specific app (like [Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/steps-to-build-a-custom-skill.html), [Monday](https://developer.monday.com/apps/docs), and [Whatsapp](https://theappsolutions.com/blog/development/cost-to-develop-messaging-app-like-whatsapp/)). Bonus points if you do this especially for an employer's platform, like Meta or Slack. This is so useful to show that you have read the platform's documentation and that you're flexible enough to adopt a tech stack, learn how to debug, and build something to purpose. It is also a great chance to show off your front-end skills.

### Get certified

Once you've added all your projects to your custom-build portfolio, you may want to add some certificates in Python back-end development. A certificate is just like a shiny badge saying to employers, "Look, someone other than my mom thinks I'm great at Python" or any other back-end development skill.

Here are some options to pursue which will demonstrate your capability in Python, back-end development, or both.

- [Our back-end learn path](https://www.boot.dev/tracks/backend) at Boot.dev. To get the certificate, you'll need to prove mastery of Python (as well as Javascript and Go, two other important back-end programming languages). This course runs through all the critical skills I mentioned in the earlier section about necessary competencies. You'll also get some extra projects, as a bonus, to put on your portfolio.
- Check out Coursera \* they have a slew of back-end certificates available from [IBM](https://www.coursera.org/professional-certificates/ibm-backend-development) to [Meta](https://www.coursera.org/professional-certificates/meta-back-end-developer) to Microsoft.
- Look to your local (or not-so-local) [universities](https://www.pce.uw.edu/certificates/python-programming) to see if they offer any certificates.

## I'm finally ready to get the job!

By now, you should know:

- What a Python back-end developer does
- What Python and non-Python skills you need to be hired as a Python back-end developer
- How to can prove and demonstrate those competencies with portfolio projects and certifications

All you need is to look for a job.

You can find jobs simply by searching "Python back-end developer" on any of the big job boards, but you also shouldn't be afraid to apply to any back-end development job that doesn't specify a particular language. As I've stressed throughout this article, many of the skills, competencies, and technologies overlap for Python back-end devs and back-end devs of any other language.

If you're set on specifically being a Python back-end dev, I recommend keeping a close eye on [Python.org's job board](https://www.python.org/jobs/type/back-end/), which as you may imagine offers exclusively Python-related jobs. As I write this, there are 25 back-end jobs available!

No matter if you're an experienced back-end dev, looking to get more into Python-based work, or you're a die-hard Pythonista who wants to get a back-end job, you'll be able to find the perfect career opportunity for you. Python is great, and being a back-end developer is (in my biased opinion) one of the best jobs in the world.

Want to be a Python back-end developer? It comes down to this: Get the skills, prove the skills, and put yourself out there. If you want a complete back-end learning path, then you should definately [check out Boot.dev](https://www.boot.dev). Good luck!
