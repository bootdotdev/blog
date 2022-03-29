---
title: "I Wrote Go-TinyDate, The Missing Golang Date Package"
author: Lane Wagner
date: "2020-03-23"
categories: 
  - "golang"
  - "open-source"
---

[time.Time](https://golang.org/pkg/time/#Time) makes dealing with dates and times in Go a breeze, and it even comes bundled in the standard library! However, a time.Time{} struct uses more than **24 bytes** of memory under most conditions, and I've run into situations where I need to store millions of them in memory, but all I really needed was a UTC date! [Go-TinyDate](https://github.com/lane-c-wagner/go-tinydate) solves this with just **4 bytes** of memory.

Star the Github! [https://github.com/lane-c-wagner/go-tinydate](https://github.com/lane-c-wagner/go-tinydate)

## How?

Let's look at the time.Time struct:

```go
type Time struct {
	wall uint64 // 8 bytes
	ext  int64 // b bytes
	loc *Location // 8 bytes if not nil, plus location memory
}

type Location struct {
	name string // unlimited
	zone []zone // unlimited
	tx   []zoneTrans // unlimited
	cacheStart int64 // 8 bytes
	cacheEnd   int64 // 8 bytes
	cacheZone  *zone // 8 bytes if not nil, plus zone
}

type zone struct {
	name   string // unlimited
	offset int    // 4-8 bytes depending on OS
	isDST  bool   // 1 bit
}

type zoneTrans struct {
	when         int64 // 8 bytes
	index        uint8 // 1 byte
	isstd, isutc bool  // 1 bit
}
```

[https://golang.org/src/time/time.go?s=6278:7279#L117](https://golang.org/src/time/time.go?s=6278:7279#L117)

As you can see, depending on how the TimeZone is set, there can be quite a bit of memory allocated just to store a `time.Time`. Even if there is no location set, the lower-bound is still **16 bytes**.

Contrast with a [tinydate.TinyDate{}](https://github.com/lane-c-wagner/go-tinydate/blob/ffa215d72dd383a4088f58ef34c43fd056b3051e/tinydate.go#L8):

```go
type TinyDate struct {
	year uint16 // 2 byte
	month uint8 // 1 byte
	day uint8 // 1 byte
}
```

Only **4 bytes!** We give up the ability to track anything more specific than the date, but often that is all we need.

## Quick Start

Create a date and add to it:

```go
package main

import (
    tinydate "github.com/lane-c-wagner/go-tinydate"
)

func main(){
    td, err := tinydate.New(2020, 04, 3)
	if err != nil {
		fmt.Println(err.Error())
    }
    
    td = td.Add(time.Hour * 48)
    fmt.Println(td)
    // prints 2020-04-05
}
```

Or Cast a time to a tinydate and back:

```go
newTinydate, err := FromTime(time.Now())
if err != nil{
    fmt.Println(err.Error())
}
convertedTime := newTinydate.ToTime()
```

## When Should I Use It?

As the TinyDate [Readme](https://github.com/lane-c-wagner/go-tinydate/blob/master/README.md) states, if you aren't constrained for resources, better to stick with the standard time.Time. But the following situations can be good reasons to switch to TinyDate:

- You are working in embedded systems and every byte counts
- You are working on a system that stores thousands of dates, and reducing memory costs by >75% is significant
- You are sure you will never need more than date precision

## Why No Timezones?

The main reason? Timezones are the most memory heavy part of a time.Time struct, yet the best practice is **usually** to store dates and times only in UTC. TinyDate stays tiny by always storing dates in UTC, but still gives the ability to calculate dates in other timezones via methods like [ParseInLocation](https://godoc.org/github.com/lane-c-wagner/go-tinydate#ParseInLocation) [FromTime](https://godoc.org/github.com/lane-c-wagner/go-tinydate#FromTime) and [ToTime](https://godoc.org/github.com/lane-c-wagner/go-tinydate#TinyDate.ToTime).

## API

The tinydate.Tinydate API largely mirrors that of time.Time. The only methods missing are the ones that make no sense without timezone or intra-day support. Check out the godoc for reference: [https://godoc.org/github.com/lane-c-wagner/go-tinydate](https://godoc.org/github.com/lane-c-wagner/go-tinydate)

If you like the package, give it a Star on [Github](https://github.com/wagslane/go-tinydate)
