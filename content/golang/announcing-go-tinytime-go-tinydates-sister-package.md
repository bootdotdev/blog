---
title: "Announcing Go-TinyTime, Go-TinyDate's Sister Package"
author: Lane Wagner
date: "2020-04-02"
categories: 
  - "golang"
  - "open-source"
images:
  - /img/800/everyday-myths-time.jpeg
---

[time.Time](https://golang.org/pkg/time/#Time) is the perfect choice for [handling times in Go](/golang/golang-date-time/) in most cases, it even comes in the standard library! The problem is that the `time.Time{}` struct uses more than **24 bytes** of memory under most conditions. [Go-TinyTime](https://github.com/wagslane/go-tinytime) solves this problem by restricting the available dates to the range between 1970 - 2106, and only supporting UTC timezones. This brings data usage down to just **4 bytes** of memory.

[Go-TinyDate](https://github.com/wagslane/go-tinydate) is its sister package that allows for a much larger date range but doesn't get more than **day** precision. Between **time.Time**, **go-tinydate**, and **go-tinytime** all of our time problems can be solved using the same API.

Don't forget to ⭐ the [Github](https://github.com/wagslane/go-tinytime)

## How Does It Work?

A normal time.Time object takes at least 16 bytes of memory:

```go
type Time struct {
	wall uint64 // 8 bytes
	ext  int64 // b bytes
	loc *Location // 8 bytes if not nil, plus location memory
}
```

If there is a location set (which there usually is), then this can be higher, usually about 24 bytes.

TinyTime, on the other hand, uses only 4 bytes.

```go
type TinyTime struct {
	unix uint32
}
```

We sacrifice timezones and dates older than the unix epoch of 1970, but if these are acceptable tradeoffs, we can save a lot of memory.

{{< cta1 >}}

## When Should It Be Used?

As the TinyTime [Readme](https://github.com/wagslane/go-tinytime/blob/master/README.md) states, if you aren't hurting for resources, better to stick with the standard time.Time. The following situations can be good reasons to use to TinyTime:

- You are working in embedded systems and every byte counts
- You are working on a system that stores thousands of dates, and reducing memory costs by >75% is significant
- If you are sure you will never need more than second precision
- Or you know you will never need timezones other than UTC

## API

The tinytime.TinyTime API largely mirrors that of time.Time. The only methods missing are the ones that make no sense without timezone support. You can swap out the vast majority without any changes. Check out the [godoc for reference](https://godoc.org/github.com/wagslane/go-tinytime).

{{< cta2 >}}

## TinyDate

If you need a larger date range, be sure to check out the [intro to Go-TinyDate](/open-source/i-wrote-go-tinydate-the-missing-golang-date-package/).

![tiny fragile box](/img/800/package-1024x683.jpeg)
