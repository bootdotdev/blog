---
title: "Snyk Security Review"
date: "2019-07-16"
categories: 
  - "security"
---

We recently integrated [Snyk](https://snyk.io/) into Qvault as a way to get more visibility into known vulnerabilities in Qvault's codebase. Snyk has already patched a [critical vulnerability in lodash](https://snyk.io/blog/snyk-research-team-discovers-severe-prototype-pollution-security-vulnerabilities-affecting-all-versions-of-l) for us. This allowed us to continue releasing new versions before the official fix for [lodash](https://github.com/lodash/lodash) was published a few days ago.

We can't speak to whether Snyk is a cost-effective tool for commercial applications. However, their support for the open-source community by offering free integrations is worth the few minutes it takes to install.

![snyk](images/download.png)

Their [quick start page allows developers to integrate their GitHub](https://app.snyk.io/signup) repository, then use the command-line tool to detect and apply any patches to their code.

![](https://img.shields.io/snyk/vulnerabilities/github/q-vault/qvault.svg?logo=snyk&label=Vulnerabilities)

Snyk Badge

We added a badge to our [github repo](https://github.com/lane-c-wagner/qvault) that shows in near real-time whether or not the Qvault code contains any known vulnerabilities according to Snyk. If you are into open source and are looking for a way to keep your code secure, Snyk is a tool you should look into.
