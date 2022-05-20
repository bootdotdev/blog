---
title: "An Overview of Boot.dev's Full-Stack Architecture"
author: Lane Wagner
date: "2022-01-10"
categories: 
  - "misc"
images:
  - /img/800/qvault-architecture-2.webp
---

Because I've had several inquiries on this topic, I thought it would be interesting to publish some information on how the boot.dev website and platform work, and how I've organized all the technologies I'm using. I'll do my best to keep this list updated in the future as I migrate from older tools and technologies to newer ones, but assume that this might be a bit out of date by the time you read it.

## The blog - WordPress

boot.dev started as a simple tech blog, it was essentially just my personal blogging site. Eventually, when I added the app to host interactive coding courses, I deployed it to [https://boot.dev](https://boot.dev). So, there are technically two different "front-ends" on boot.dev.

1. The blog and landing pages (WordPress) - [https://boot.dev/](https://boot.dev/)
2. The courses and projects (a custom Vue.js web app) - [https://boot.dev/](https://boot.dev/)

I use a custom deployment of [WordPress](https://wordpress.org/download/) hosted on [GCP's compute engine](https://cloud.google.com/compute) to serve all my blog posts and landing pages. This has been convenient because I don't need to edit code to update simple visuals. That said, it's also been a giant page in the butt as the site has grown, because sometimes it would be easier to just write some code. I'm looking at moving the blog to [Hugo](https://gohugo.io/) and hosting it on [Netlify](https://www.netlify.com/).

{{< cta1 >}}

## The app's front-end - Vue.js SPA on Netlify

All the coding courses and projects on boot.dev exist within a Vue.js web app. I'm currently running the front-end as a [single page app](https://en.wikipedia.org/wiki/Single-page_application) hosted on Netlify. I ended up choosing Netlify over Github Pages because Netlify has some server-side-rendering built-in that gives me an SEO boost.

One thing that you might be wondering is how does the code you write within a boot.dev course get executed? Well, I actually think I'm the only educational site taking this unique approach, but it actually runs in your own browser. I spin up a [web worker](/golang/running-go-in-the-browser-wasm-web-workers/) that executes your JavaScript code, or if it's a different language, it [compiles to Web Assembly](/golang/running-go-in-the-browser-with-web-assembly-wasm/) first.

Here are some additional details on the technologies I'm using within the Vue app.

- [Vue 3](https://v3.vuejs.org/)
- [Vite](https://vitejs.dev/) - I switched from [Webpack to Vite](/javascript/migrating-vue-webpack-to-vitejs/) recently and couldn't be happier.
- [Vuex](https://vuex.vuejs.org/)
- [Eslint](https://eslint.org/)
- [Codemirror](https://codemirror.net/) - Codemirror has been pretty good, it's what I use to manage the in-browser code editor.
- [Markdown-it](https://github.com/markdown-it/markdown-it) - All of the instructions in the app are written in Markdown, so the front-end needs a Markdown renderer.
- [Tailwind CSS](https://tailwindcss.com/) - Tailwind has been amazing. I would highly recommend it if you have a hard time writing "clean" css.

## The app's back-end - Golang server on Kubernetes

The backend of the boot.dev app consists of two services, both written in [Golang](https://go.dev/), running on a [Kubernetes](https://kubernetes.io/) cluster in Google Cloud Platform on [auto-pilot mode](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview). One of them is an HTTP server that acts as the RESTful backend for the frontend. The other server powers the [Discord bot for our community](/news/roles-qvault-discord-server/).

I use Kubernetes so I don't have to worry about scalability or portability. If the app gets a big rush of traffic k8s will auto-scale the number of servers to handle the load. I also like that my server's applications are deployed on lightweight docker containers that I could easily move to another infrastructure technology if needs be.

It's also worth pointing out that when you run code in the boot.dev app that needs to compile to WASM, like Golang for example, your code is shipped to the backend for compilation before the WASM is sent back to your browser for execution.

Here are some more of the technologies I use on the backend:

- [JWT-go](https://github.com/dgrijalva/jwt-go)
- [DiscordGo](https://github.com/bwmarrin/discordgo)
- [Sendgrid](https://sendgrid.com/)
- [Gorm](https://gorm.io/index.html)
- [Gorilla/Mux](https://github.com/gorilla/mux)

## The database - Postgres on Cloud SQL

I really like [PostgresQL](https://www.postgresql.org/). I'm of the opinion that it's one the best general-purpose solution for new apps, though I do try to build my apps so [I can move to more specialized storage mechanisms](/clean-code/death-taxes-and-database-migrations/) if need be. The application backend uses this Postgres instance running in Google Cloud SQL to persist things like user preferences, exercise completions, etc.

{{< cta2 >}}

## Payments - Stripe

Not too much to say about Stripe, other than it makes payments pretty seamless for our [pro accounts](https://boot.dev/pricing). My biggest complaint about Stripe is that I had to write an annoying about of code for the "lifetime subscription" option because Stripe doesn't have that built-in.

## Deployments and source control - Github/Github Actions

I really don't like doing monotonous tasks if I can avoid it. Running tests and deploying applications can be painfully time consuming, so I've automated all of that with Github actions. Each time code is updated in Git, a new deploy is automatically triggered, and I've set this up both for the Vue.js frontend and the Golang backend.
