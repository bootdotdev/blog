---
title: "What is Backend-as-a-Service?"
author: natalie
date: "2022-12-05"
categories:
  - "backend"
images:
  - /img/800/ruinreborn_remove_--ar_9151_--v_6.1_c4f1fc2e-5249-484a-9b60-7935d18172ed_3.png.webp
imageAlts:
  - "A fantasy ship at harbor"
---

Plenty of people have heard of SaaS, or Software-as-a-Service, which is simply software made available by a third party over the internet. Think Salesforce, WordPress, or MailChimp. And most people know what a "[backend developer](/backend/become-backend-developer/)" is, that is, someone who is responsible for things building server-side systems like user authentication and data storage.

Backend-as-a-Service (BaaS) is a recent phenomenon that combines both concepts. BaaS is a cloud service model that takes care of everything beyond the front-end. This means if you plan on using a BaaS, in theory, all you'll need to build is a UI application, either on mobile or on the web, and the BaaS will take care of almost everything else. Backend service providers take care of everything behind the scenes, so if you want to develop a website but are only comfortable with implementing the front end, you can still produce a fully-functioning website using a BaaS.

A back-end as a service allows front-end developers to avoid writing back-end code almost entirely. As you'd expect, it only works well at the moment for simple, predictable backends. This is comparable to SaaS, which also has limited customization. Sure, WordPress might let you change the theme, but writing some of your CSS isn't permitted.

Most BaaS products on the market include services like cloud storage, database management, hosting, push notifications, security settings, and user authentication. Having all these services covered accomplishes much of the heavy lifting of producing a modern, secure website or app.

There are numerous BaaS providers, each with a different pricing plan and a slightly different offering of the services they include with each tier or product. HiTechNector compiled a comprehensive [list of BaaS providers](https://www.hitechnectar.com/blogs/top-14-backend-as-a-service-providers/), including:

- 8 Base
- Apache Usergrid
- AWS Amplify
- Back4App
- Backendless
- Built.io backend
- Couchbase
- Windows Azure Mobile Services
- Firebase
- Supabase

Firebase is probably the best-known option of these, focusing on BaaS for mobile and web apps. Other options have specialized services, like built.io backend which offers social media integration.

[Supabase](https://supabase.com/) is a particularly interesting option, which spins itself as an open-source alternative to [Firebase](https://firebase.google.com/). Both are built around a central store and don't require extra tools or software, you can build your mobile app or website and connect directly to the BaaS from there. Both [Firebase and Supabase](https://supabase.com/alternatives/supabase-vs-firebase) have excellent client-side libraries to easily set up your front end to communicate with the backend.

Supabase is a normal BaaS with paid tiers with increasing specs, but the cool aspect of Supabase is that you have the option to self-host. If you want to, you can take on the burden of the infrastructure yourself while still using the cookie-cutter backend code. This may be a more economical option, but it requires you to worry about how to upgrade your middleware without creating downtime for your service. The easiest way to self-host the open-source option of Supabase is by using a PaaS (Platform-as-a-Service) like Docker, following [Linode's guide](https://www.linode.com/docs/guides/installing-supabase/).

## How is BaaS different from PaaS?

Imagine you are a store owner who sells blankets. You have a physical store where customers come in, browse your blankets, make payments, and collect their purchases. This store is equivalent to the front end of an application.

On the backend, you need a way to restock your blankets. Using a PaaS would be like if you bought an 18-wheeler. You've acquired the infrastructure, and you're free to use it as you see fit. You can go collect blankets and bring them back to your store, no problem. However, you've still got to figure out the best route to your blanket supplier's warehouse, where to stop for gas, and you'll need to hire a driver. There's still a lot of work to be done, even though you now have the right equipment to transport your blankets.

A BaaS would be the equivalent of getting your blankets automatically delivered from your blanket supplier when you request them. They would simply appear on your store's doorstep within a prearranged timeframe. You don't have to worry about the driver, gas, or routes.

A PaaS offers you more flexibility – you have complete control over the route, the gas, and so on – but it comes at a cost. It requires a significant time investment to develop all of the backend services you require.

## When to use a BaaS?

There are a lot of reasons why it makes sense to use a BaaS. First, it's fast. Second, it's good for prototyping. Third, it's good for those without much backend experience. Let's break those down.

## Using a BaaS to save time

If you're under a big time crunch, contracting a BaaS can help get you set up quickly with reliable, secure services. Using a BaaS generally saves a lot of time, and it also makes it easy to get a functioning backend connected to your custom frontend in a few hours, even if you've never used a BaaS before.

## Using a BaaS to build a prototype

When you're making a prototype of something, a BaaS is also super helpful since you can build something viable without spending too much time or developer resources on a prototype. Most prototypes don't need much custom functionality, and a lot of the BaaS providers have free tiers that tend to be enough to have your prototype running for some test users or a demo.

## Using a BaaS when you're not an expert

Finally, another motivating factor in using a BaaS is a lack of expertise. If you have no experience as a back-end developer, and maybe have no interest in gaining those skills, then a BaaS is a great option for your own projects. There are a lot of complex and risky functionalities like database migrations and secure connections that a BaaS can accomplish for you with very little effort on your part. Since a BaaS is sophisticated, it can help ensure your application can smoothly scale to handle spikes or sustained increases in load.

## Using a BaaS when you're not concerned with the cost

Using another company's products is never free. At a small scale, it's almost always cheaper to buy than build, but at a certain level of scale, control of your own code helps save on costs. [Paying software engineers 6+ figures](/jobs/how-much-do-software-engineers-make/) to build simple apps may not be economical, but Netflix will gladly pay high engineering salaries because small tweaks to their codebase can save millions of dollars in computing costs.

## Are backends-as-a-service the future?

Is BaaS the future? For certain types of companies, yes! For others, probably not. While BaaS solves a lot of headaches for traditional backend users, particularly for non-tech people or organizations looking to prototype something, it will be difficult for BaaS to overtake the tech market unless the BaaS providers reach a level of customization that is yet to be seen.

Baas will probably have a lifecycle similar to that of WordPress and other blogging tools. If all you need is a blog or a simple e-commerce store, then WordPress does great. The minute you need to customize further it's time to build your own application. Similarly, with a backend-as-a-service I think simple CRUD apps will use out-of-the-box solutions just fine. That said, for companies that are innovating and building custom applications, I think it will be harder to use a BaaS, even if the tools improve.

## Is BaaS the right option for you?

BaaS is okay for prototypes, small services, and situations where you need very little customization. It's the cookie-cutter way of getting the job done, which is acceptable in some situations.

Let's go back to our blanket example to demonstrate why. What if you decide to open another location? Your BaaS (the delivery company in this analogy) might not agree to add a second stop to your delivery route. Maybe you've had security issues, and you need them to provide a delivery safe that they'll leave on your doorstep and give you the combination. These are two viable scenarios, but your BaaS provider may not offer those as products.

As soon as you try to do anything vaguely sophisticated with a BaaS, you get to the point where you're dealing with some custom backend components on your own and trying to patch them into your existing workstream using the BaaS. It can get messy keeping up with version updates, choosing compatible technologies, and getting it all integrated with your front end.

If you have any functional requirements that extend out of the provided functionalities that the BaaS that you've contracted has, it can be quite a headache to get those few last-mile functionalities working, properly integrated with the BaaS and your front end.

Trying to customize using tools that were not meant for customization is an exhausting and frustrating challenge. If you've ever fought with Microsoft Word's formatting for a few minutes, you'll know. Overcoming that challenge with an entire backend system is significantly more difficult.

If your requirements shift from a cookie-cutter backend, **your best bet is to [learn to develop your backend](https://www.boot.dev/tracks/backend-python-golang)**. A lot of traditional backend elements are similar, and it's easy to find tutorials online for how to implement basic elements, like how to [enable user authentication](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) for a Python Flask app.

If you're already implementing the front end, then you know how to code. Backend development is a great skill set to add to your toolbox. If you want to be a back-end developer, or need custom work that a BAAS can't handle out-of-the-box, you can learn back-end development through coding programs like those of [Boot.dev](https://www.boot.dev/).

Tackling the actual infrastructure, like having your server, is a whole different ball game, but there are Paas (Platform-as-a-Service) providers that allow you to implement your backend, but not have to worry about the actual platform everything is running on.
