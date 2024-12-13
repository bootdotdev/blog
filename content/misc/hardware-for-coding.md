---
title: "As a Developer, What Hardware Do You Truly Need?"
author: lane
date: "2023-04-21"
categories: 
  - "misc"
images:
  - /img/800/mathematiciantablets.webp
imageAlts:
  - "Mathematician with tablets: fantasy art"
---

Let's be real here: we live in an age where everyone and their dog seems to think they need the latest, most expensive gadgets to get anything done. But when it comes to [learning how to code](https://www.boot.dev), do you really need that shiny, wallet-draining powerhouse of a machine?

**Nope.**

Let's chat about the hardware you need to get started with coding, and dispel the myth that you need to spend a fortune on your setup like a Macbook-toting [soydev](https://www.urbandictionary.com/define.php?term=Soydev).

## Memory: The real MVP

RAM (Random Access Memory) is where it's at, and this is where you're not going to want to cheap out. If you're not familiar with what RAM does, let me give you the lowdown.

RAM is the temporary storage your computer uses to maintain the data it needs to run apps. More RAM means you can run more apps simultaneously, which is super important when you're coding, because you'll likely have a bunch of programs open at once. For example:

* Text editor
* Web browser with 50+ tabs (guilty!)
* Terminal
* Slack
* Discord
* Spotify

Opening files: When you open a file, the data is loaded into RAM, so having more of it means you can open larger files without your machine choking.

Compiling code: Compiling is the process of turning your code into an executable program. This can be a memory-intensive operation, especially for larger projects. More RAM helps speed up the process.

For most use cases, you probably won't want less than 4GB of RAM. There isn't a true minimum, because, depending on the programs you use, you can get away with quite little, but if you can get 8 you'll be in a good place, and 16+ will feel like a dream.

## CPU: Nothing too wild

The CPU (Central Processing Unit) is the brain of your computer, executing instructions and performing calculations.

It might seem counter-intuitive, but a powerful CPU isn't always necessary for coding. As long as your editors and day-to-day apps aren't lagging, you're going to be fine. Remember, a good CPU won't make the programs you write any faster. You need great hardware for running in production, but not necessarily for development.

So, while a good CPU can certainly help, you don't *need* the latest, most powerful CPU to get started. A mid-range processor from the last few years should be more than enough for most coding tasks.

## Hard Drive: SSDs slap hard

You'll just save so much time when you start up your computer and load applications if you have a solid-state drive (SSD). SSDs are faster than traditional magnetic (spinning disk) hard drives, and they're also more reliable.

You don't *need* one, but you'll be much more productive if you have one. As far as storage space goes, I would hesitate to ever go below 256 GB, just because you'll probably have a lot of apps and data on your local device. That said, if you can get a full TB of storage you'll be in a fantastic place.

## GPU: Nice, but far from necessary

The GPU (Graphics Processing Unit) is another piece of hardware you might be curious about. But unlike RAM, a powerful GPU isn't always necessary for coding.

The GPU is responsible for rendering images, animations, and other visual elements on your screen. While it's *critical* for tasks like gaming and video editing, coding web apps usually doesn't require much GPU horsepower. That said, here are some tasks that do:

* **Machine learning:** If you're diving into the world of AI and machine learning, a beefy GPU is your best friend. It'll help you train models faster, allowing you to iterate and improve your algorithms more quickly.
* **Game development:** If you're creating the next gaming masterpiece, a solid GPU will help you render graphics, run game engines, and test your creations in real-time.
* **3D rendering:** For 3D modeling or animation, a powerful GPU will make your life a lot easier by speeding up rendering times.

## Peripherals: Keyboards, mice, and monitors

A comfortable keyboard and mouse can make a big difference in your coding experience, but if you're just getting started you probably won't have a strong opinion about what you like yet. You can get started with super cheap stuff and it probably won't hinder your productivity very much. Later on, as you understand your own workflow and preferences, you can invest in a different mouse/keyboard combo.

As far as monitors go, I would never recommend working with a screen less than 1080p. If you can get a 1440p or 4K monitor, you'll be in a great place. But again, you don't *need* a fancy monitor to get started. I know "10x" devs that work with 1, 2, or even 4 monitors, but the truth is you won't know what works best for you until you've been coding for a while. I'd start with a simple single monitor setup, and only make changes if you feel like you need to.

## Using lightweight apps

Now that we've covered the core hardware components, let's talk about the software side of things. Choosing the right tools for coding can make a huge difference in terms of hardware requirements and overall efficiency.

[Vim](https://www.vim.org/) (or [NeoVim](https://neovim.io)) is a prime example of a lightweight tool that doesn't require much in terms of hardware. It's a text editor with a small memory footprint, making it ideal for coding on less powerful machines. But Vim is just one example—there are plenty of other lightweight tools out there, each catering to different programming languages and tasks.

Lightweight tools put less strain on your system, so you'll experience fewer slowdowns and crashes, even if your hardware isn't top-of-the-line. Since lightweight tools use fewer resources, they generally load and run faster, which means you can write, test, and debug your code more quickly. Generally speaking, if you're happy and efficient using the lighter-weight stuff, there's no reason not to use it.

## Using bloatware

In contrast to lightweight tools, heavier apps like Electron and full-fledged IDEs (Integrated Development Environments) like Visual Studio can consume a *lot* more resources. These tools typically offer more features and integrations, which can be helpful for development but also require more memory and processing power. They may also include graphical interfaces and other fancy visual elements, which can further bloat their resource usage.

Generally speaking, I'd stay as far away as you can from the *truly* heavy apps like Visual Studio, Android Studio, and XCode. If it takes 30+ seconds to start up, it's just not going to be fun to work with. Of course, sometimes you can't escape depending on what you're trying to accomplish, but if you can avoid it, do.

Electron apps are essentially just more browser windows. They work by running web technologies (HTML, CSS, and JavaScript) inside a sandboxed browser. They're certainly not as efficient as command-line tools like Vim, but they're often not as bad as some of the bloaty IDEs listed above. As long as you aren't opening too many of them, and as long as you have a decent amount of RAM, you'll probably be okay.

## Final thoughts

* Memory (RAM) is crucial for running applications, opening files, and compiling code. Aim for at least 8GB, but 16
GB is even better.
* A mid-range CPU should be sufficient, but if you have the budget, this isn't a bad place to spend it.
* An SSD somewhere between 256-1024 GBs will put you in a great spot.
* A great GPU is only important for specific tasks like machine learning, game development, or 3D rendering.
* In terms of performance: command line tools > Electron apps > IDEs.
* If you don't know what you like, start with cheap peripherals and a single 1080p monitor. You can always upgrade later.

The bottom line is that learning to code is possible with a wide range of hardware configurations. It's not about having the most expensive, high-powered machine—it's about understanding what you actually need for the tasks you'll be working on and finding the tools that best suit your needs and budget. At the end of the day, you can realistically learn to code on a Raspberry Pi; you just might have to be a little more patient.

Don't let hardware be a barrier to entry. Dive into some code, explore your options, and remember that the most important tool in your arsenal is your own determination and curiosity. As they say, necessity is the mother of invention, so let your passion for coding be the driving force behind your success, not the latest shiny gadgets.
