---
title: "Systems and Processes that Aren't in Code are Terrifying"
date: "2019-10-03"
categories: 
  - "clean-code"
---

My worst enemy is processes that a developer spun up years ago on a server everyone has forgotten about. I don't know how to find these systems reliably, I don't know where they came from, what depends on them, and if they are safe to delete. For example, the dreaded `15 6 2 1 * /home/lane/backup.sh`. You may recognize this as a Unix cronjob, a job that is scheduled to run on a server periodically.

You may be thinking, _"Why is that scary? We use cronjobs all the time!"_

If the code that manages the crontab is exists in source control within the organization's central repositories, then I actually have very little to complain about. My beef is when an engineer hops onto a server and starts up a cron job without that configuration existing anywhere in code.

You may say,

> Well, the cron schedule may not exist in code, but the script/program it runs does!

**I don't care.**

![gordon ramsay](/img/26ipc1.jpg)

I want to be able to look at the code base and know if the program is long-running, should be run manually, or if it runs on a specific schedule. It is fine if it's going to be run using crontab. We just make sure that the CI/CD config file (or something similar that is source controlled) specifies how that is triggered.

Or even better, program in Go so that spinning up side processes within your app is simpler than using the crontab ;)

## Other Angst-y Things

Crontabs are just a common example of hard to discover processes. Others, for example, may include:

- Database processes that were added manually, instead of by the app that owns the DB
- .bash\_profile or .bashrc files that kick off server startup jobs
- Third party apps that were installed on the server to take care of special tasks (I don't know, defragging the disk maybe). Those processes should be documented in code, probably config files that your organization typically uses to start its apps.

Internal documentation certainly sucks, so document your processes in code instead. A config file that specifies how a process is started is much better than a PDF, because the config file can't become outdated (if it does, things break).
