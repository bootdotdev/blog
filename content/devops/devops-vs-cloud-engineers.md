---
title: "6 Differences Between DevOps and Cloud Engineers"
author: Natalie Schooner
date: "2023-01-18"
categories: 
  - "devops"
  - "backend"
images:
  - /img/800/cloudspacestation.png.webp
---

The deeper you get into the tech sphere, the more unintelligible the job titles seem to be. Plus, the same title at different companies often encompasses different responsibilities. Ask twenty data scientists what they do and you’ll get twenty different answers.

"DevOps Engineers" and "Cloud Engineers" are two jobs that *sound* very similar, but they’re quite distinct. Like many jobs in the tech space, there’s some overlap between them, but there’s a reason that DevOps Engineer and Cloud Engineer are separate job roles.

DevOps stands for *Dev*elopment and *Op*erations Engineer. The “cloud” in cloud engineering refers to the cloud-based architecture many modern companies rely on for operations.

Let’s break down some key similarities, differences, and career prospects for each role.

## What is the difference between a DevOps Engineer and a cloud Engineer?

*To put it simply, the difference between a DevOps engineer vs a cloud engineer is that cloud engineers are essentially DevOps engineers who specialize in cloud infrastructure products like Azure, AWS, GC, Kubernetes, and Docker.*

There is very little daylight between the two roles. Review just a few job descriptions and you’ll quickly realize that cloud engineers are often just cloud-based DevOps engineers. A cloud engineer will specialize in their deep knowledge of cloud technologies (AWS, GC, MSFT azure), but both roles deal with deployments, live sites, and health metrics of systems.

That said, it’s actually hard to find a DevOps engineering role that *doesn’t* use some kind of cloud-based technology.

The real difference between the non-cloud DevOps and normal DevOps is specific to the kind of product these roles are helping develop.

For example, a product like Microsoft Word is *not* a cloud product. Desktop apps don't (primarily) run in the cloud. Logs emitted (directly) in the cloud. There’s no need for DevOps engineers who deal with deploying client-side code to be as deeply knowledgeable about cloud-based back-end technology. A product like Google Drive, meanwhile, is 100% cloud-based. They need DevOps and cloud engineers to push out new versions, store all of your files, push/pull updates to your files from various devices, etc.

## Six key differences between DevOps Engineers vs cloud Engineers

Now that you’ve got a rough sense of the difference between DevOps engineers and cloud engineers, let’s break down some more distinct differences in these roles.

We'll look at:

1.  Role and responsibilities
2.  Skillset, tools, and technology
3.  Focus
4.  Interaction and collaboration
5.  Pay
6.  Job prospects

### 1. Role and Responsibilities 

A cloud engineer focuses on the design, implementation, and maintenance of cloud infrastructure and services. A DevOps engineer also focuses on the design, implementation, and maintenance of infrastructure and services, just not *necessarily* cloud infra and services.

That’s a lot of jargon, isn’t it?

Let’s use a baking analogy to break it down because I’m a little hungry as I write this. As a DevOps engineer, you’re ensuring the cake is baking evenly and well. If the recipe works well, you make sure that’s noted. If it needs adjustment, you ensure you show what you changed.

What does this look like when mapped onto actual job responsibilities?

DevOps engineers:

* Implement and maintain continuous integration and continuous delivery (CI/CD) pipelines (ensuring the cake is ready to be delivered when it needs to be)
* Manage and configure cloud infrastructure, such as Amazon Web Services, Google Cloud, or Microsoft Azure (Checking the oven settings)
* Collect data on the performance of the software in production (making sure the cake rises)
* Troubleshoot and resolve issues that arise in production (like if the cake starts to look crispy on top!)
* Collaborate with development teams to improve the software development process and implement best practices (working with the other kitchen teams)

Meanwhile, a cloud Engineer is more like the site manager who makes sure the kitchen is fully prepared. They make sure the oven is working properly, they might put in a test cake before the real one to see that it's coming out alright, and they could check that the temperature it says it's at is accurate.

Let’s take a look at actual responsibilities:

* Build and maintain cloud infrastructure, such as servers, storage, and databases (AKA, ensuring that the kitchen has the necessary tools, like ovens, mixers, and baking trays)
* Design, implement, and maintain scalable, highly available, and fault-tolerant systems (making sure that there are enough ovens and mixers, and that cakes can still get baked in the event of a power outage)
* Configure services to get them to talk to each other properly (making sure you have the right attachments for your mixer)
* Manage and secure access control to cloud resources (making the kitchen secure so only authorized staff has access to it)
* Automating the provisioning, scaling, and management of cloud resources using tools such as Terraform, and CloudFormation (making sure that when more ingredients are needed, they are delivered on time)
* Collaborate with development and operations teams to ensure the infrastructure supports the software delivery process (the site manager is working closely with the head chef, aka the DevOps engineer, to make sure that the kitchen is set up and ready)

### 2. Skill sets, tools, and technology

DevOps Engineers typically have a strong background in software development and operations, while cloud Engineers tend to have more expertise in cloud technologies and platforms, such as AWS, Azure, or GCP.

In baking terms, this is like saying DevOps engineers are amazing at measuring flour, while cloud engineers are certified in hygenics to ensure the kitchen stays clean.

*Just kidding.*

At this point, the baking analogy begins to lose its usefulness – I mean, what does skill for measuring flour even mean? Hopefully, you’ve got a clear idea of the main differences between DevOps engineers vs cloud engineers. Let’s look at the actual skills you’d be expected to have as a DevOps engineer versus a cloud engineer.

To be a DevOps engineer, here are the skills and familiarities you’ll be expected to have:

* Tools like Ansible, Jenkins, Python, or Docker for automation and scripting
* Infrastructure-as-code (IAC) tools like Terraform or cloud formation
* Cloud infrastructure, such as Amazon Web Services, Google Cloud, or Microsoft Azure
* Version control systems, such as Git or SVN
* Container orchestration tools, such as Kubernetes or Docker Swarm
* Monitoring and logging tools, such as Prometheus or Elasticsearch
* CI/CD pipeline tools
* And of course, strong communication and collaboration skills, since DevOps Engineers often work closely with development and operations teams

This area of comparison between cloud engineers versus DevOps engineers has the most overlap. As a cloud engineer, you’ll be expected to have mastery of a lot of the same tools as you would as a DevOps engineer. In the list below, I’ve noted all the areas of overlap between DevOps engineers and cloud engineers.

You’ll need:

* Strong experience with cloud infrastructure providers like AWS, GCP, Azure, and their services (overlaps with DevOps)
* Experience with (IAC tools, such as Terraform, and cloudFormation (overlaps with DevOps)
* Strong knowledge of virtualization technologies, such as VMWare, Hyper-V
* Familiarity with networking concepts and technologies, such as VPCs, VPNs, DNS, and load balancers
* Understanding of security best practices and compliance requirements, such as SOC2, ISO 27001
* Automation and scripting skills, such as experience with tools like Ansible, Jenkins, or Python (overlaps with DevOps)
* Knowledge of containerization and container orchestration tools, such as Docker and Kubernetes (overlacdps with DevOps)
* Experience with monitoring and logging tools, such as cloudwatch, Stackdriver, Prometheus (overlaps with DevOps)

The areas where there isn’t as much overlap are:

* Security (cloud engineer specialty)
* Virtualization technologies (cloud engineer)

### 3. Focus

I find the best way to tell the difference between DevOps engineers vs cloud engineers is by understanding the key deliverables.

* In a nutshell, DevOps engineers focus on providing **faster and more efficient software delivery**.
* Cloud Engineers do that too, but they do so **using cloud-based technologies**.

Cloud engineers are also *more* focused on the infrastructure itself, rather than the processes around deploying systems *on* that software. I've also found, at least anecdotally, that [DevOps engineers tend to write more code themselves](/devops/devops-engineers-should-code/), while cloud engineers tend to use more off-the-shelf tools. Along with writing more code, that means that DevOps engineers might also tend to work more directly with back-end engineers, sometimes even [taking on some of their responsibilities](/devops/backend-devops-roles-merging/).

It may be useful to get a deeper look. The primary goal of DevOps engineers at work is to improve collaboration and communication between development and operations teams and automate the software deployment process. Organizations look to their DevOps engineering teams to facilitate the fast release of software updates and new features, while also reducing the risk of issues or downtime in production.

Cloud engineers do the same. They build, deploy, and maintain the infrastructure that runs software applications – all using cloud tech.

In summary, DevOps engineers streamline the software delivery process and make sure that the software runs efficiently in production. Cloud Engineers do that too, but they do it using their deep knowledge of off-the-shelf cloud products like Azure, Google Cloud, Civo, and AWS.

### 4. Interaction with teams

No employee or team works in a vacuum. If you were paying attention in earlier sections, you’d notice that both DevOps engineers and cloud engineers are expected to work and collaborate with different teams across the company.

Few software departments employ both DevOps engineers and cloud engineers. Some products lend themselves more to classic DevOps, and some require more cloud infrastructure. The work relating to setting up and using the cloud infrastructure could fall to someone with the title of DevOps engineer OR cloud engineer, depending on the company and its history.

DevOps engineers interact with many teams across an organization, including development, operations, and Quality Assurance (QA) teams. This is to streamline the software delivery process and make it more efficient, which all three teams play a role in.

Cloud engineers interact with development, operations, and infrastructure teams as well, but their focus is primarily on the infrastructure that supports software applications.

### 5. Pay

I’ve written before about how much salaries can vary across locations, and how much the cost of living affects the actual take-home money you earn.

Of course, it’s a given that both [the salaries for DevOps engineers and cloud engineers](/devops/devops-salary/) are generous. The median annual salary for each role in the United States, based on data from Glassdoor, is:

* DevOps engineer: `$115,000 - $140,000`
* Cloud engineer: `$120,000 - $150,000`

But let’s take a look at a more usable number, based on location, cost of living, rent, and taxes for DevOps vs cloud engineers.

Here’s the salary data for DevOps engineers in the top five cities:

| City          | Median salary | Monthly salary | Monthly cost of living | Average 1Br rent | Monthly salary after taxes | Take-home monthly pay |
| ------------- | ------------- | -------------- | ---------------------- | ---------------- | -------------------------- | --------------------- |
| San Francisco | 146034        | 12,169.50      | 1,369.40               | 2,995            | 7,747                      | 3,382.60              |
| Boston        | 140193        | 11,682.75      | 1,212.40               | 3,070            | 7,941                      | 3,658.60              |
| Houston, TX   | 133917        | 11,159.75      | 962.50                 | 1,303            | 8,141                      | 5,875.50              |
| New York, NY  | 133366        | 11,113.83      | 1,437.10               | 3,680            | 7,092                      | 1,974.90              |
| Dallas, TX    | 126802        | 10,566.83      | 1,103.90               | 1,450            | 7,736                      | 5,182.10              |
| Source:       | Indeed        | Numbeo         | Zumper                 | SmartAsset       |


As you can see, while San Francisco is the highest paid, Houston delivers the highest take-home pay thanks to a low cost of living and rent burden.

Let’s have a look at cloud engineer salary data:

| City           | Median salary | Monthly salary | Monthly cost of living | Average 1Br rent | Monthly salary after taxes | Take-home pay |
| -------------- | ------------- | -------------- | ---------------------- | ---------------- | -------------------------- | ------------- |
| New York, NY   | 154753        | 12,896.08      | 1,437.10               | 3,680            | 7,092                      | 1,974.90      |
| Houston, TX    | 132402        | 11,033.50      | 962.50                 | 1,303            | 8,141                      | 5,875.50      |
| Washington, DC | 132066        | 11,005.50      | 1,198.10               | 2,350            | 7,263                      | 3,714.90      |
| Austin, TX     | 128532        | 10,711.00      | 1,050.40               | 1,667            | 7,835                      | 5,117.60      |
| Atlanta, GA    | 125676        | 10,473.00      | 1,067.70               | 1,692            | 7,123                      | 4,363.30      |
| Source:        | Indeed        | Numbeo         | Zumper                 | SmartAsset       |

Here's [the source of that data](https://docs.google.com/spreadsheets/d/1aGHwqVBMGHooQAJjrTZuPs9S2A-f0yV1P8WJX3W57gg/edit?usp=sharing) if you're interested.

New York has the highest salary, but it has by far and away the lowest take-home pay. If you lived in Houston or Austin, you could be taking home nearly three times as much per month.

Quick caveat: these estimates vary based on company size and level of expertise, among other things. *This is just an estimate.* It's always a good idea to research the specific job posting to get a better understanding of the salary range for a particular role and company.

### 6. Job prospects 

It’s tough to compare the job prospects of DevOps engineers and cloud engineers because both are frankly great. Even just twenty years ago, DevOps engineers and cloud engineers weren’t even job titles. Today, they’re some of the most in-demand IT jobs out there. Employment prospects for DevOps Engineers and Cloud Engineers can vary depending on location and industry, but in general, both roles are in high demand in the current job market. Yes, even despite all the recent tech layoffs!

As [reported](https://www.bain.com/insights/tech-talent-war-tech-report-2021/) by Consultancy Bain & Company in September 2019, job postings for DevOps professionals skyrocketed by 443% between 2015 and 2019, making it a hotter field than even machine learning, and leaving data science and software engineering in the dust with growth rates of only 167% and 69% respectively.

Cloud Engineers are also in high demand as more companies are moving their operations and applications to the cloud. The Open Source Job Report [reported](https://8112310.fs1.hubspotusercontent-na1.net/hubfs/8112310/LF%20Research/Open%20Source%20Jobs%20Report%202021%20-%20Report.pdf) that 61% of professionals surveyed claimed that their organizations increased the use of cloud technology in 2021, which of course means that there’s a growing demand for cloud engineers.

To increase the chances of finding a job, it's a good idea to have a strong set of skills, and relevant experience and continue to learn new technologies and tools that are in demand by the industry.

## Final thoughts on DevOps engineers vs Cloud Engineers

This has been a thorough and hopefully conclusive answer to the difference between DevOps engineers vs cloud engineers. There is a fair amount of similarity between the roles, not least of which is the great job prospects. There’s truly no bad choice here.

If you’re deciding which to go for, this guide will help you determine which job responsibilities you’d prefer to focus on.
