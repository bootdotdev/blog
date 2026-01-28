---
title: "Backend Developers are UX Designers Too"
author: lane
date: "2021-04-12"
categories:
  - "clean-code"
images:
  - /img/800/ruinreborn_fantasy_art_simple_background_enumeration_--ar_169_c021d043-1ff0-4fbc-975e-8bad0af765d0_0.png.webp
---

Too often I neglect the idea of UX design in backend work. The goal of user experience design is to give users a product that's easy to use. In the world of front-end development, that typically means making it obvious how to navigate your site, using commonly-understood icons, or implementing well-contrasted colors for foreground and background, making your site easy to read.

I'm here to contend that UX is extremely important in backend development as well, the difference is simply that our users are typically other developers, sometimes even internal employees, rather than users of the final product.

## What is UX (user experience) design?

> User experience design (UXD, UED, or XD) is the process of supporting user behavior through usability, usefulness, and desirability provided in the interaction with a product. User experience design encompasses traditional human-computer interaction (HCI) design and extends it by addressing all aspects of a product or service as perceived by users.
>
> [Wikipedia](https://en.wikipedia.org/wiki/User_experience_design)

In other words, UX design is all about making it easy for your users to interact with your product, and get their tasks done in a straightforward manner.

## Examples of UX Design

![door push handle ux](/img/800/door-push-handle.jpeg)

Bad UX Design on Door

Sometimes it's easier to understand through bad examples. In the image above, a door with a handle is clearly labeled _push_. Why does the door have a handle at all if it can't be pulled? It's just bad UX and gives off mixed signals. If the builder had used push plates, there would be no need for words at all. [Simplicity breeds understanding](https://wagslane.dev/posts/optimize-for-simplicit-first/).

![](/img/800/push-panel-on-door.jpg)

I like to think of good UX design as the death of user manuals. Remember user manuals? You might still get them for tools or household appliances. In the early days of software, installable CD ROMs often came with user manuals. Can you imagine needing to open a user manual to figure out how to login to Facebook? No, the goal with UX is to make your software (or product) so easy to use that you get very few questions, even without providing explicit instructions.

## Why does this matter in backend code?

It mostly comes down to one thing, **clean APIs**. As backend developers, our users are other developers. If you've ever had the misfortune of sifting through outdated or poorly written API documentation, hopefully, you'll appreciate the point I'm trying to make here.

Let's take a look at an example of a poorly written REST API to demonstrate what I mean.

```md
# Users API - A list of endpoints

## Create new user

POST /user/create

### Request body

json
{
"email": "johndoe@example.com",
"password": "somethingsecure"
}

### Response

json
{
"id": "some-new-id"
}

## Delete user

POST /users/delete/{email}

## Get user

GET /user/{id}

## Update user

PUT /user

json
{
"id": "some-id-here",
"email: "johndoe@example.com",
"password: "somethingsecure"
}
```

There's a lot wrong here. While this API is probably usable, it makes me want to cry. Nothing about it is obvious, and no internal patterns are adhered to. I don't even care that much if the API isn't very RESTful at all, but can it please be non-RESTful in a consistent way?

### Problem #1 - Plurality seems arbitrary

Some of the endpoints use `/users` while others use `/user`. When should I expect one over the other? It's not clear so back to the user's manual (documentation) for me I suppose.

### Problem #2 - When does the path include the verb?

The endpoints for creating and deleting users have the appropriate verb ("create" and "delete" in their path. For some reason, the `GET` endpoint operates directly on the root `/users` path. Why? I have no idea.

### Problem #3 - Inconsistent use of HTTP methods

Some APIs (GraphQL) always use `POST`, or sometimes `GET`. That's fine, at least it's consistent so you know what to expect. Here, it appears that we're going to use the standard RESTful verbs, `GET`, `PUT`, `POST` and `DELETE`, but for some reason, the endpoint for deleting users uses the `POST` method, seemingly just to confuse us.

### Problem #4 - Inconsistent primary keys

In a RESTful-ish API, you'd expect the primary key used in a resource path to be the same. For example, updating might be `PUT users/{id}`, deleting would be `DELETE users/{id}`, etc. In this API, we see the `id` in the request body for updating, deleting uses an `email` in the path, and the `GET` endpoint simply takes an `id` in the path.

### Think about your UX. If you do that you'll be one step ahead of many backend engineers

Let's strive to make our APIs easy to understand and work with. Many companies like Stripe and Mailgun have made created entire products that are just APIs. As such, their API UX design is of utmost importance.

The buck doesn't stop with REST, It was just a quick example. If you're writing a [library or package](/golang/how-to-separate-library-packages-in-go/), it has an API, so make sure it's a good one. Keep your authentication protocols simple. Make decisions that simplify the lives of your users, even if it means a smidge of extra code on your end. Remember, it's easy to change internal logic, but fixing a bad API is difficult - it requires breaking changes and major version upgrades.
