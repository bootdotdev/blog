---
title: "What are UUIDs, and should you use them?"
date: "2021-07-23"
categories: 
  - "clean-code"
tags: 
  - "mailing-list"
  - "sharing"
---

A universally unique identifier (UUID) is a 128-bit format for creating IDs in code that has become popular in recent years, especially in relation to database keys. By using UUIDs, you ensure that your ID is not just unique in the context of a single database table or web application, but is truly unique in the universe. No other ID in existence should be the same as yours.

It is important to note that while the probability that a UUID will collide with another is not _zero_, its _practically_ zero. The chances of collision are so astronomically low, worrying about it would be ridiculous. The total number of possible UUIDs is `2^128` or `340282366920938463463374607431768211456`.

## UUID Generator Online

Generate UUID!

<script>function uuidv4() { return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) { var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8); return v.toString(16); }); } const button = document.getElementById('uuidButton'); const result = document.getElementById('uuidOut'); <div></div> const genUUID = () => { result.value = uuidv4(); } <div></div> button.addEventListener('click', genUUID);</script>

## Why use a UUID?

The main advantage of using UUIDs is that you can create a UUID and use it to identify something, such as a row in a database, with near certainty that the identifier will not exist in another row in your system _or anyone else's_. UUIDs used by completely unrelated companies or organizations can be referenced together without duplication.

Let's take a real-world example and analyze why using UUIDs can make our lives easier. Let's pretend we have a web application with a single database. One of the tables in that database is the "users" table. Each user has a primary key, and like many databases, that primary key is just an integer. So the first user will have the ID "1", the next will be "2", and so on.

<table><tbody><tr><td>1</td><td>Plato</td></tr><tr><td>2</td><td>Aristotle</td></tr><tr><td>3</td><td>Marcus Aurelius</td></tr></tbody></table>

That may be fine for a while, but now imagine that we introduce more services into our backend architecture. For example, there may be a separate database that stores social media posts and we need to know which user made the posts. Well, we need to store a user ID, so we just start storing the user's ID in that separate database as a kind of foreign key. If we need a list of posts, we look in the "users" database to see what information we have about the author. So far, so good.

Now let's break things down. Let's say we acquire a new company and that company has their own user database and they have done the same thing using integers for their user IDs, so now we have a system where a single user ID can potentially point to two different records! To fix the problem, we would have to create a new list of IDs and painstakingly go through each data store in our architecture and update the IDs. In some systems, this would be almost impossible, especially without introducing some bugs.

By using UUIDs (or another kind of universally unique ID) we can save ourselves all this headache. I'm open to the possibility that universally unique IDs could create issues in a system's archiecture, I've just never experienced it, and I can't think of why it would be problematic.

## Why are UUIDs only recently gaining popularity?

All I can really do is guess, but I have a couple of candidate hypotheses.

### 1\. Making a UUID is slightly more complicated than just incrementing an integer

You have to have a bit of custom code that generates a specific format of the string, and you need to ensure that you have enough [entropy](https://qvault.io/cryptography/what-is-entropy-in-cryptography/) in your system to ensure uniqueness.

### 2\. They take up a bit more memory

UUIDs take up 128 bits in memory and can take up more if stored as a string. In systems where resources are precious, it could make sense to use a more compact format. That said, in modern web development, I think we'd be penny-wise and dollar-stupid to care about such negligible resource usage.

## The UUID Format

While you could just generate 32 random digits and call your home-grown ID format "good enough", it's nice to use [standards that already exist](https://qvault.io/clean-code/use-existing-standards/). Aside from the fact that there are safe libraries you can use to work with standard UUIDs, it's nice to look at the UUID format and know "hey, this is an ID"! If you roll your own format, you'll likely confuse members of your team. They could think it's an encoded JWT, or perhaps a private key. Best to avoid that confusion.

A UUID is made up of 32 [hex (base-16)](https://simple.wikipedia.org/wiki/Hexadecimal) digits, displayed in five sections. For example, `bc2d0f53-5041-46e8-a14c-267875a49f0c`. The sections are broken in the form 8-4-4-4-12. Including the four hyphens, it comes to a total of 36 characters. UUIDs are also typically displayed in lowercase, which to be honest is a bit unique for hex encoding. You can read more about the specifics of UUID formatting on [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format).

### UUID Versions

There are 5 versions of UUIDs out there. Versions 1 and 2 are time and [MAC](https://en.wikipedia.org/wiki/MAC_address) address-based. The idea is there's some determinism in the system. You can get the same UUID if you use the same time and MAC address as inputs when generating the UUID. Versions 3 and 5 are similar, but instead of using time and MAC addresses, they use namespaces.

**Version 4 is probably what you want.** Version 4 tags are generated completely randomly without any inputs that create predictable outputs. If you're interested in using UUIDs to tag disparate entities in a software system, it's very likely you just want random version 4 UUIDs.

## UUIDs vs GUIDs

The term GUID, which stands for Globally Unique Identifier, is an industry standard defined by Microsoft. As we know, UUID stands for Universal Unique Identifier. So the two terms basically mean the same thing. Apart from the fact that GUIDs (Microsoft's version) and UUIDs (an [open Internet standard defined by RFC4122](https://datatracker.ietf.org/doc/html/rfc4122)) look similar and serve similar purposes, there are minor differences.

Some GUIDs may contain any hex digit in any position, while RFC4122 requires specific values for the version and variant fields. Also, GUIDs are typically written in upper case, while UUIDs should be written in lower case. Sometimes these subtle differences can cause incompatibilities between code libraries.
