---
title: "Security in Dependencies"
author: Lane Wagner
date: "2019-08-21"
categories: 
  - "security"
---

Choosing the right dependencies is a difficult task. Assuming the developer of an application is the best programmer in the world, the "best" thing to do would be to write the entire codebase alone. This would eliminate the bugs, vulnerabilities, and malicious intrusions of inferior developers.

The trouble is that we like to move quickly in order to be able to compete in the market and offer new features. We try to avoid re-inventing the wheel when the wheel in question is widely used, is peer-reviewed, and we consider it stable and trusted.

Let's explore the decision making behind which dependencies we should use, and which we should avoid.

## Can We Write it?

This should be the first question asked when a new dependency is being considered. If it fits within the scope of a project it is almost always safest to write and own the code ourselves. Pertinent questions include:

- How long will it take us to write it?
- Do we need the whole package? Can we re-write the section we need?
- Is this something we have domain expertise in?
- Will our implementation be better? (don't write your own cryptography)
- Does the language's standard library already have this functionality?

## Review

If we decide that we shouldn't write the code ourselves, we find a valid candidate package. We take a look at the code and ensure:

- Does the code have tests? Are they relevant?
- Is the library architected well? Is the code of high quality?
- How many contributors are there?
- How many other projects are dependent on this package?
- Is the project actively maintained? When was the last release?
- Does this project have dependencies? If so, we need to review those as well (best to **try to avoid child dependencies** where possible).

## Locking Versions

For any dependencies that are more security-critical, it is important to lock versions, and ideally [vendor the original source code](https://qvault.io/2020/11/16/should-you-commit-the-vendor-folder-in-go/). For example, we perhaps have done a solid review of package '**abc**' and determined that **v1.4.4** is stable and secure. We want to ensure that we don't carelessly update that package without reviewing the changes. A package manager like yarn keeps the digital fingerprints of each dependency so that once v1.4.4 code is brought in, it can't be maliciously swapped out.

Vulnerabilities in updates aren't protected by this feature. For this reason, we try to use **'1.4.4'** vs **'~1.4.4'** or **'^1.4.4'**. By not including the tilde or the caret, we tell yarn that we don't want to automatically update this package.

When locking versions in this way we need to be more diligent about regularly reviewing and manually applying updates because many times new updates fix old security holes.

## Communication

When we decide that we want to use a dependency, especially if we don't know much about it, we should reach out to the developer to ask questions and ensure that it is well maintained.

We hope this quick guide gives some insight into our process for dependency management and gives you some good tips for building your own projects. Stay safe and have fun building!
