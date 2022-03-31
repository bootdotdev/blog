---
title: "Check for Standards Before Creating a New One"
author: Lane Wagner
date: "2021-06-07"
categories: 
  - "clean-code"
images:
  - /img/flags.webp
---

I recently had a ticket opened on my team's backlog board requesting the ability to bypass our API's caching system. For context, our front-end team uses my team's API to make fairly heavy requests to ElasticSearch, and one of the features of our API gateway is to cache the results of heavy aggregations for ~30 seconds. It turns out, every once in a while they need to run two of the same query within the ~30-second caching window and want an updated result set.

The request that was opened read something like, "the API needs a parameter to disable caching for certain queries". When working in a REST-ish-ful API there are approximately `math.MaxInt` ways to accomplish that, and some of the first ones that immediately came to mind were:

- A `?cache=false` query parameter
- A `resource/no-cache` endpoint extension
- A `cache: false` HTTP header
- A `"cache": false"` JSON payload in the body

As it turns out, there's already a standard for this sort of thing, the [`Cache-Control` request directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#cache_request_directives).

```
Cache-Control: max-age=<seconds>
Cache-Control: max-stale[=<seconds>]
Cache-Control: min-fresh=<seconds>
Cache-Control: no-cache
Cache-Control: no-store
Cache-Control: no-transform
Cache-Control: only-if-cached
```

Using the standard header `Cache-Control: no-store` not only makes my job easier by requiring fewer API design decisions but also ensures that my API's clients aren't surprised by a new way to accomplish a common task.

I do want to point out, however, that just because you've decided to use a fairly well-supported standard, doesn't mean there aren't other standards your users will expect. It also doesn't mean that your users are aware of the existence of the standard you've chosen.

![](/img/standards.png)

[https://xkcd.com/927/](https://xkcd.com/927/)

Regardless of whether or not you think your API's behavior is "standard" or "to be expected", just add the behavior to your docs anyway. For me, the following snippet in our `Readme.md` was all we needed.

```
## Cache busting

If you don't want your query cached, use the Cache-Control header.

Cache-Control: no-store
```
