---
title: "Well, We Might Have a Video Call for That!"
author: Lane Wagner
date: "2021-09-27"
categories: 
  - "news"
images:
  - /img/videocall.jpeg
---

This article contains some of my thoughts on communications for distributed teams and is a response to [No, we won’t have a video call for that!](https://xahteiwi.eu/resources/presentations/no-we-wont-have-a-video-call-for-that/) by Florian Hass. Read his article first if you haven't yet, he makes some great points!

I really enjoyed Florian's article, and while we agree on a lot of things, like [Scrum being a bad idea](https://wagslane.dev/posts/leave-scrum-to-rugby/), I found some key points I disagree with. Let's start with the disagreements, because they tend to be more interesting, and then I'll follow up by emphasizing some of his ideas I agree with.

Like Florian, my thoughts here **are not science**. I'm presenting anecdotes and sharing what I've found works well through personal experience. I have zero data to back this up.

## "A capable distributed team habitually externalizes information"

> Information is generally far less useful when it is only stored in one person’s head, as opposed to being accessible in a shared system that everyone trusts and can use. If you take important information out of your own head and store it in a medium that allows others to easily find and contextualise it, that’s a win for everyone....
> 
> ...While _sharing_ information in a chat is extremely easy, it is also a “fire and forget” mode of communications. Chat makes it difficult to find information after the fact. If you’ve ever attempted to scour a busy Slack or IRC archive for a discussion on a specific topic that you only remember to have happened a “few months ago”, you’ll agree with me here.

While I agree with this in a lot of cases, the problem is that most communication contains information that simply doesn't need to be distributed to everyone. If I documented even as little as 10% of the information my team communicates between itself on slack, our Wiki would get insanely unwieldy.

**The only thing worse than no documentation is inaccurate documentation.**

I worry that by "habitually externalizing information" too often, by adding it to Google docs or wiki pages, we run the risk of creating vast amounts of of information that won't be kept up to date. Having so much potentially useless content cluttering up our centralized documentation ironically makes everything harder to search through. You'll likely end up with duplicate and even conflicting documents.

That said, I agree that for a remote team, externalizing the right information is vitally important. I work at a seed-stage startup currently, and for the first few months one team member manually did all the deploys alone, leaving the rest of the team clueless as to how it all worked. They were unable to deploy when the "deploy guy" was sick or on vacation. Additionally, because it was a tedious manual process, human error intermittently caused issues, and valuable engineering hours were wasted doing monotonous tasks. When I came on board, I created some simple CI/CD scripts and we documented the few remaining manual steps in the README.

Processes like deployments, access to company secrets, development environment setup, etc **must be externalized** and rigorously kept up to date.

{{< cta1 >}}

## "Avoid anything that makes a distributed team run synchronously"

> The reason for this is not just working in different timezones, but also the fact that everyone will have their own daily routine, and/or have their individual times when they are most productive. Which you _will not attempt to synchronize._ (Doing so would mean setting the entire team up for failure.)

If you've read my article about [meetings](https://qvault.io/news/too-many-meetings/), you might assume that I completely agree with Florian here. My only problem with this section of his article is that I _really_ enjoy taking certain email threads or slack conversations into an impromptu, synchronous slack call. This happens for me ~2 times a day on average. Don't get me wrong, I don't want a meeting when it can be an email or a quick slack message. What I hate is having a _discussion_ over email or slack. It's just so damn slow.

Examples of good email/slack messages:

- Can you get me access to the applicants resumes when you have a chance?
- What was the name of the database that stores BI information again?
- Would you be interested in a team hack-a-thon this month?

Examples of discussions that are most effective on a call:

- Can we talk about the decision to use React classes? I have some thoughts on classes vs hooks, and I'm worried we're starting work we'll just have to undo.
- I'm trying to decide between Mongo and PostgresQL, can I pick your brain?

I'm not making a case that everyone needs to drop everything immediately, or be available 24/7 to hop on calls. When work is being blocked until a discussion can happen, we should have that talk as soon as the parties involved are available. If everyone's calendars aren't always packed to the brim, we'll be able to be more flexible and unblock each other more quickly.

**Synchronicity isn't an inherent problem. Discussions with a good amount of back and forth are more effectively communicated synchronously, while the majority of communication is best handled asynchronously.**

## "A chat ping is a shoulder tap."

This one depends on the person being pinged. I would much rather receive a slack message than an email, pretty much 100% of the time. **I hate email.**

I simply don't feel the need to respond immediately to slack messages, and will usually wait until the end of a meeting, or until a break in my coding rhythm to respond to slack messages. I turn off my notification sounds, and just let the indicator icon in slack let me know I have an outstanding notification when I open the app.

That said, people are different. I like to talk to my coworkers about the way they prefer to be contacted and respect their preferences where possible.

## So where do we agree?

- Scrum is generally a bad idea, agile is a good one
- Externalize the important stuff
- If it can be a simple email or slack message, don't make it a call
- Come to a meeting with a clear agenda and action items
- Have fewer meetings
- Todos belong in an issue tracker, not a slack channel
- "How do I..." questions should be asked in public channels, not DMs
