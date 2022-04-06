---
title: "Roles in the Boot.dev Discord Server"
author: Lane Wagner
date: "2021-12-19"
categories: 
  - "news"
images:
  - /img/discord.jpeg
---

In our [community Discord server](https://discord.gg/EEkFwbv), we have two main groups of roles you can take on as a member, _earned_ roles and _declared_ roles. Earned roles, as you would expect, you have to earn! You can get them in various ways as we'll discuss shortly, but you can't just ask for them. Declared roles on the other hand you simply assign to yourself, and are a way of showing the community what kinds of technologies you enjoy learning about, and what your programming goals are.

## Declared roles

We have a Discord bot in our community server that you can issue commands to by typing a command in the `#qvault-bot-cli` channel. The commands take the following form.

```
qvault {command}
```

You can also shorten the `qvault` command by using the `qv` alias.

```
qv {command}
```

To add a role, use the `add-role` command. You can add one or many roles

```
qvault add-role javascript
```

```
qvault add-role python golang
```

To remove a role, use the `rm-role` command. You can remove one or many roles.

```
qv rm-role python
```

Keep in mind, this will _only work for declared roles_. The following roles are all declared roles that you can update on your own.

### Roles to show off your career goals

- goal-backend-job
- goal-frontend-job
- goal-devops-job
- goal-mobile-job
- goal-data-job

### Roles to show off your favorite technologies

- javascript
- golang
- python
- rust
- java
- typescript
- c++
- sql
- html-css

### Roles to signal programming experience

- xp-new (never programmed before)
- xp-beginner (programmed but haven't had a job)
- xp-junior (in the first year of your professional career)
- xp-mid (a professional developer for more than a year)
- xp-senior (you've held a "senior" title)

### Roles to signal preferred pronouns

- he-him
- she-her
- they-them
- ask-pronouns

## Earned Roles

There are several roles you will automatically earn through your activity within Qvault's courses and projects. In order to connect your discord account to your Qvault account so that roles can be properly assigned, run the following command.

```
qvault sync {api_key}
```

Where `{api_key}` is the API key for your account on the [Qvault website](https://boot.dev/), which you can change and update in your [settings](https://boot.dev/dashboard/settings). Here are the roles that you'll unlock automatically:

- pupil - You've completed at least 3 exercises in any course
- scholar - You've completed at least 1 course
- sage - You've completed 4 or more courses

If for any reason you didn't get a role auto-assigned that you've earned, just message one of the Qvault team members and they'll unlock it for you.

Thanks for reading and welcome to our coding community if you're new!
