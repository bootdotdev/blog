---
title: "4 Key Differences Between DevOps and DevSecOps"
author: Natalie Schooner
date: "2023-01-23"
categories: 
  - "devops"
  - "backend"
images:
  - /img/800/cyberpunk-devsecops.png.webp
---

Doesn’t it seem like every day there’s a new mishmash of responsibilities into a job title? One day soon, someone will be hired as a DevOpSysSecInfraArc engineer.

But today you’re focused on finding the difference between DevOps vs DevSecOps. I could somewhat trivially summarize this entire article simply by telling you to closely examine the job titles. It’s in the name. DevOps engineers work on development and operations, while DevSecOps do the same, but with a greater focus on security – *Dev*elopment, *Sec*urity, and *Op*erations engineering.

Of course, that’s not very helpful to anyone trying to understand the difference between DevOps vs DevSecOps roles in greater detail, so I’ll go into a little more depth explaining what the key differences are.

With two roles as similar as DevOps vs DevSecOps, I find it useful to start with an analogy. (I’ve done this before when looking at [DevOps vs Cloud engineers](https://blog.boot.dev/devops/devops-vs-cloud-engineers/).)

Imagine a DevOps engineer is responsible for building a well-oiled machine. A DevOps engineer is in charge of making sure each component (development, testing, deployment) works together seamlessly to produce a smooth and efficient process.

DevSecOps is like giving that engineer a gun and telling her that someone’s going to try to break in. The DevSecOps engineer not only ensures that the machine is running smoothly but is also protected from any potential threats or vulnerabilities.

In this article, I’ll break down the key differences by:

1. Roles and responsibilities
2. Necessary background, education, and skills
3. Salaries
4. Job prospects

Let’s jump in.

## 1. Roles and responsibilities

As I mentioned earlier in my analogy, a DevOps engineer is primarily responsible for building the architecture to get stuff to deployment. That includes building, maintaining, testing, and monitoring performance.

That main job breaks down into additional roles and responsibilities, but that's the role in a nutshell.

As a DevSecOps, you’ll be doing the same but with more of an emphasis on security. This might be because you’re working with projects that require a high level of security clearance. It might be because you’re working for the government in some capacity, or because the product is especially vulnerable to attack.

Either way, you’re no longer just “building CI/CD pipelines” the way you would if you applied for a DevOps role. Now you’re “building *and securing* CI/CD pipelines.” (Those quotes are from two real job descriptions for DevOps and DevSecOps respectively!)

Let’s dive deeper.

### As a DevOps, you’re mainly focused on four areas: 

**You’re automating infrastructure**. This means you’re automating the provisioning, configuration, and management of servers and other infrastructure.

**You’re working on continuous integration and delivery,** more commonly shortened to CI/CD. This means you’re building software systems so software engineers can regularly integrate their code changes into a shared repository (CI) and then once those code changes are integrated and don’t break anything, you make systems to automatically deploy those changes to a staging environment to be tested further (CD).

You’re building this system so software engineers can deploy changes more quickly and reliably.

**You’re also monitoring and logging**. This means you’re monitoring the performance and health of systems to make sure they’re optimized.

And finally, **you’re collaborating and communicating**. You sit in the middle of software development, operations developers, and other stakeholder teams. You are the person that people point fingers at when things start to break because it’s your job to hold everything together and scale it up in a reliable and sustainable manner. Luckily, you’re also the person that everyone trusts to keep things running.

### How do the responsibilities of a DevOps compare to a DevSecOps engineer? 

You’re still **building automated systems**, but with more of a focus on security automation. You are using tools and processes to automate testing and scanning.

You have a totally different role in **compliance**. There are lots of industry-specific regulations that your employer needs to be kept abreast of. For example, if you work for a healthcare company, you’ll be operating under HIPAA regulations which regulate how data can be collected, stored, and sold.

You’re **managing risk**. This is also a different role. You’ll be in charge of identifying, assessing, and ideally mitigating potential security threats in the development process.

Finally, you’re back to **collaboration and communication**. Security is only as strong as its weakest point, so you’ll need to work closely with Development teams, Operations teams, and security teams to make sure everyone is up to date on best Sec practices, and that security is fully integrated through the software development life cycle.

{{< cta1 >}}

## 2. Necessary background, education, and skills

That was a long old section. This one will be a little shorter. And to make it handy, I’ll summarize it all here in some charts:

### Skills

<div class="tablewrap">

| DevOps                                             | DevSecOps                                          |
| -------------------------------------------------- | -------------------------------------------------- |
| Automation tools (Ansible, Chef, Puppet)           | Security automation and security testing tools     |
| Containerization/orchestration (Docker, K8s)       | Containerization/orchestration (Docker, K8s)       |
| Cloud platforms like AWS, Azure, GCP               | Cloud platforms like AWS, Azure, GCP               |
| Monitoring and logging tools (Prometheus, Grafana) | Monitoring and logging tools (Prometheus, Grafana) |
| CI/CD tools (Jenkins)                              | CI/CD tools (Jenkins)                              |
| Scripting/programming                              | Scripting/programming                              |
| Linux/Unix admin skills                            | Linux/Unix administration                          |
| Communication, collaboration                       | Communication, collaboration                       |
| Problem-solving, analytical thinking               | Problem-solving, analytical thinking               |
| *                                                  | Compliance regulations and industry standards      |
| *                                                  | Network and web application security concepts      |

</div>

### Background

<div class="tablewrap">

| DevOps                | DevSecOps             |
| --------------------- | --------------------- |
| Software engineering  | Software engineering  |
| System administration | System administration |
| IT Operations         | Cyber Security        |

</div>

### Education

<div class="tablewrap">

| DevOps                                     | DevSecOps                                     |
| ------------------------------------------ | --------------------------------------------- |
| BA in CS, software engineering, or related | BA in Computer Science, InfoSec, or related   |
| Or equivalent work experience              | OR qquivalent work experience                 |
| Applicable certifications                  | Applicable certificates like CISSP, CEH, GSEC |

</div>

What sort of background do you need to be able to handle all those important responsibilities? What degree do employers require? What skills and knowledge matter most?

Looking at that chart, you can see there are a lot of similarities. The main differences are that DevSecOps engineers are expected to have a background in security, they can have a degree in InfoSec, and they need to know more about compliance regulations and security concepts.

Let’s look at each of those backgrounds, skills, and educational requirements.

### Background of a DevOps engineer vs a DevSecOps engineer

As both a DevOps engineer and a DevSecOps engineer, you’ll be expected to have a background in either software engineering or systems administration. As a DevSecOps, you’ll also be expected to have a background in security, too.

### Education of a DevOps engineer vs a DevSecOps engineer

Educational requirements are *very flexible* in this field. Most job descriptions will say they need someone with a BA in computer science, software engineering, or infosec if you want to get into DevSecOps.

But the truth is that, for both roles, if you show up with a solid portfolio of projects, the skills I’ll get into below, and some certifications, they certainly won’t close the door on you. There simply aren’t enough skilled workers in the field for employers to need you to wave around a diploma to get hired.

### Skills of a DevOps engineer vs a DevSecOps engineer

This is the real non-negotiable set of requirements to get hired as either a DevOps engineer or a DevSecOps engineer. Here’s a more comprehensive breakdown of the skills required:

* **Automation**: Experience with automation tools such as Ansible, Chef, or Puppet. Understand infrastructure as code and have the ability to automate provisioning, configuration, and management of servers and other infrastructure. If you’re going into DevSecOps, you’ll also want knowledge of security automation.
* **Containerization and orchestration**: Knowledge of containerization and orchestration technologies like Docker and Kubernetes, Mesosphere, or Docker Swarm.
* **Cloud**: Understand cloud-native architecture and be able to design, build, and manage cloud-based systems like AWS, Azure, or GCP.
* **Monitoring and logging**: Know how to collect, analyze, and act on log data to improve system performance and troubleshoot issues using monitoring and logging tools like Prometheus, Grafana, or Elasticsearch.
* **CI/CD**: Experience with CI/CD tools like Jenkins, Travis CI, or CircleCI. Understand how to automate the building, testing, and deployment of code.
* **Scripting and programming**: Understand how to write scripts and code to automate tasks and improve system efficiency. Python is a good language to know here.
* **Linux/Unix administration**: Understand how to manage and troubleshoot Linux/Unix-based systems.
* **Networking**: Strong understanding of networking concepts, including IP addresses, DNS, load balancing, and firewalls.
* **Troubleshooting and problem-solving**: Understand how to identify and solve problems quickly and effectively.
* **Communication**: Strong communication skills to effectively collaborate with cross-functional teams and stakeholders.

Then as a DevSecOps, you’ll also need:

* Experience with **security automation tools** like vulnerability scanners, penetration testing tools, and security testing frameworks.
* Knowledge of **regulatory requirements** such as HIPAA, PCI-DSS, and SOC2, and industry standards such as ISO 27001 and NIST, depending on which industry you’re in.
* Experience with identifying, assessing, and mitigating **potential security threats** and vulnerabilities in the development process.

That’s *in addition* to all the regular DevOps skills I listed above.

## 3. Salaries

Now we’re onto the money. In previous articles, I’ve found it useful to break down not just a salary comparison but also to look at median salaries in the top five cities in comparison to cost-of-living, rent, and taxes.

Let’s take a look at the top five cities for DevOps engineers, according to [Indeed’s listings](https://www.indeed.com/career/development-operations-engineer/salaries?salaryType=YEARLY&from=careers_serp).

<div class="tablewrap">

| City          | Monthly salary | Monthly salary after taxes | Average 1Br rent | Monthly cost of living | Take-home monthly pay |
| ------------- | -------------- | -------------------------- | ---------------- | ---------------------- | --------------------- |
| San Francisco | 12,169.50      | 7,747                      | 2,995            | 1,369.40               | 3,382.60              |
| Boston        | 11,682.75      | 7,941                      | 3,070            | 1,212.40               | 3,658.60              |
| Houston, TX   | 11,159.75      | 8,141                      | 1,303            | 962.50                 | 5,875.50              |
| New York, NY  | 11,113.83      | 7,092                      | 3,680            | 1,437.10               | 1,974.90              |
| Dallas, TX    | 10,566.83      | 7,736                      | 1,450            | 1,103.90               | 5,182.10              |

</div>

And here’s what that looks like when you put these numbers in a nice chart:

![chart for table](https://i.imgur.com/T1TEgnk.png)

As you can see, San Francisco has the highest base salary. But if you want the highest take-home salary after taxes, cost of living, and rent, you should actually get a DevOps job in Houston, Texas.

It’s a little harder to look at DevSecOps jobs because they’re not as common as DevOps jobs, so Indeed hasn’t made a handy landing page with all the information about the top-paying cities.

However, we can look at a few job listings for DevSecOps engineers and DevOps engineers at the same company, to see how the salaries compare.

* You can get a [Sr. DevSecOps job](https://www.indeed.com/cmp/Career-Movement/jobs?jk=a9cf3737660f6afe&start=0) in Columbus, Ohio at a company called Career Movement, earning a salary of $150k to $200k. The same company [would hire](https://www.indeed.com/cmp/Career-Movement/salaries/Development-Operations-Engineer) a DevOps engineer at a salary of $133k.
* Capgemini [is hiring](https://www.indeed.com/jobs?q=devsecops&l=&from=searchOnHP&vjk=e5ad8d106fc003f1) a DevSecOps engineer for an estimated $113k-$143k a year, located remotely. The [same company hires](https://www.indeed.com/cmp/Capgemini/salaries/DevOps-Architect) DevOps engineers at a median salary of $137k
* Nexient [is hiring](https://www.indeed.com/jobs?q=devsecops&l=&from=searchOnHP&vjk=e5ad8d106fc003f1) a DevSecOps Manager for an estimated $114k-$145k per year remotely. Its [DevOps salary](https://www.indeed.com/cmp/Nexient-2/salaries/Development-Operations-Engineer) is quite low, just $93k.

It seems like *most* companies who are hiring or have hired DevOps engineers or architects in the past are hiring DevSecOps engineers at a higher rate. This makes sense since it seems like the roles aren’t doing different things.

It’s more like if you’re a DevSecOps, you do all the same stuff as a DevOps engineer plus a Sec component.

In fact, I noticed very few places hiring both DevOps and DevSecOps roles at the same time. Many newer companies seemed to be forgoing DevOps engineers and going straight into hiring DevSecOps engineers instead to get a two-for-one bargain.

{{< cta2 >}}

## 4. Job prospects

All the money in the world doesn’t mean anything unless there are jobs available. Right now, DevSecOps is a relatively new field that combines the responsibilities of a traditional DevOps role with a focus on security.

That’s why job prospects for DevSecOps roles may be more limited than for traditional DevOps roles. But I expect demand for this type of position to grow as organizations increasingly recognize the importance of security in the development process.

DevOps roles, on the other hand, are in high demand as organizations look to improve the speed and reliability of their software delivery processes.

In short, both roles are expected to grow in the future, but demand for DevSecOps roles may increase at a faster rate.

Let’s take a more granular look by checking out the number of job openings for both DevOps and DevSecOps engineers across three of the most popular hiring platforms: LinkedIn, Indeed, and Glassdoor.

<div class="tablewrap">

| Platform  | DevOps                       | DevSecOps                    |
| --------- | ---------------------------- | ---------------------------- |
| LinkedIn  | 164k job openings available  | 14k job openings available   |
| Indeed    | 8,642 job openings available | 8,644 job openings available |
| Glassdoor | 4,335 job openings available | 4,318 job openings available |

</div>

These are accurate as I write this article.

As you can see, the numbers of job openings are actually similar on Indeed and Glassdoor. I expect that’s due to the huge amount of overlap between DevOps and DevSecOps engineers. LinkedIn is the exception, perhaps because their search parameters are different. There we can see that there are ten times more job openings for DevOps versus DevSecOps engineers.

Honestly, if you have the skill set to be a DevSecOps engineer, I’d recommend applying for any regular DevOps role and using your skillset to bargain for a higher salary. You’ll be doing the same role, plus additional responsibilities. All you need to do is convince your future employers that the “Sec” part of DevOps is non-negotiable.

And if you’re a DevOps engineer? It might be a good time to pick up some DevSecOps skills and certifications, like knowledge about regulations and governance.

## Final thoughts on the differences between DevOps and DevSecOps

In summary, what is the difference between DevOps vs DevSecOps? There’s not a huge difference between them, honestly. There are a few alternate skill sets necessary. That accounts for a higher DevSecOps salary. But the two are mostly interchangeable, and you’ll notice that many employers don’t hire for both.

DevSecOps is a role that combines traditional DevOps responsibilities with a heightened focus on security. Today, it’s a relatively new field. But it’s gaining traction. While job prospects for DevSecOps roles may not be as plentiful as traditional DevOps positions, there is a growing demand for this type of role as organizations come to realize the importance of security in the development process.

DevOps, on the other hand, is an in-demand field, as organizations look to improve the speed and reliability of their software delivery. Both roles are expected to see growth in the future, with DevSecOps potentially seeing an even higher rate of growth as the need for secure development continues to increase.
