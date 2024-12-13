---
title: "Troubleshooting the Boot.dev Code Editor: Common Snags"
author: hunter
date: "2023-12-07"
images:
  - /img/800/frozen_wizard.png.webp
categories:
  - "wiki"
---

As a Boot.dev student, you may have encountered frustrating moments when your code editor freezes or is stuck "Setting up your environment", leaving you wondering what went wrong. Don't worry; we're here to help. These issues can be caused by various factors, and in this blog post, we'll explore some common culprits and provide solutions to help you get back to coding smoothly.

## 1. Chrome Extensions Blocking the Python Interpreter

One of the most prevalent reasons for code editor freezing is the interference of Chrome extensions like IDM (Internet Download Manager) or others that block the Python interpreter. Even disabling these extensions may not always resolve the issue. If you suspect an extension is causing the problem, try the following solutions:

- **Disable Extensions:** Temporarily disable all extensions in your browser and check if the code editor functions correctly. If it does, enable extensions one by one to identify the problematic ones.

- **Switch Browsers:** If disabling extensions doesn't work, try using a different browser. Sometimes, another browser might not have the same extension conflicts, and your code editor will work flawlessly.

## 2. Pi-hole Blocking jsdelivr (OS Dependent)

Some users have reported issues with the code editor freezing due to pi-hole blocking jsdelivr, a content delivery network (CDN) used by many web-based code editors. To tackle this problem:

- **Whitelist jsdelivr:** Configure your pi-hole to whitelist jsdelivr to ensure that it doesn't block the necessary resources for our code editor.

## 3. Brave Browser's Shield

If you're using the Brave browser, its built-in security feature called "Brave Shields" can sometimes interfere with the functionality of certain websites and online code editors. To resolve this:

- **Disable Brave Shields:** Temporarily disable Brave Shields. You can do this by clicking on the lion icon in the address bar and toggling off Brave Shields for Boot.dev.

## 5. ISP-related Problems (Location Dependent)

In rare cases, your internet service provider (ISP) may be causing issues. This issue is location-dependent and not something you can control directly. If you suspect your ISP is causing the problem:

- **Contact ISP Support:** Reach out to your ISP's customer support to inquire about any known issues in your area and seek assistance in resolving the problem.

If you've tried the solutions listed above and are still experiencing issues, don't hesitate to ask for help in the [Discord community](https://www.boot.dev/community).
