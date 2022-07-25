---
title: "Comprehensive Guide to Dates and Times in Go"
author: Lane Wagner
date: "2021-05-17"
categories: 
  - "golang"
images:
  - /img/800/clock.webp
---

Keeping track of time in code has long been every developer's nightmare. While no language or package manages time perfectly, I think Golang does a pretty good job out-of-the-box. This full tutorial should answer ~90% of the questions you'll have about time management in Go.

## Overview - How dates and times are stored in Go

The first thing to know is that you probably don't need any third-party packages to manage times and dates in Go. The Go standard library's [time](https://golang.org/pkg/time/) package is very robust and can do almost anything you're going to want to do.

The default `[time.Time](https://golang.org/pkg/time/#Time)` type represents an instant in time with nanosecond precision. It's a struct that has no exported fields, which means you'll never need to use a dot operator to access different fields. Instead, various methods are available to get the data you need. For example, [`time.Year()`](https://golang.org/pkg/time/#Time.Year) returns the year (as an integer) of the time object in question.

The two most common ways to create a new time object are to use the current time, or to provide a date as input.

### Get the current time with time.Now()

The `[time.Now()](https://golang.org/pkg/time/#Now)` function returns the current local time. If you work on the backend, it's likely you'll also want to immediately convert it to UTC.

```go
currentTime := time.Now()

currentTimeUTC := time.Now().UTC()
```

### Create a time object for a specific date

If instead, you want a time object for a specific date, you can use the `time.Date()` function.

```go
// takes a year, month, day, hour, minute, second, nanosecond, and location
someonesBirthday := time.Date(1990, time.May, 10, 23, 12, 5, 3, time.UTC)
```

{{< cta1 >}}

## Printing, parsing, and formatting times in Go

While dates and times are typically stored as `time.Time` objects _within_ Go programs, we frequently need to save them to databases, [marshal them to JSON](/golang/json-golang/), or just print them to the console. It's nice that Go provides functions to format and parse dates easily. That said, the way it's handled is unique compared to most coding languages.

Let's say we have a time object and we want to be able to print in a specific format. The Go formatting engine takes a layout of specific constants and uses that as an example for how to format the time.

The reference time is defined [in the docs](https://golang.org/pkg/time/#Time.Format) as:

```
Mon Jan 2 15:04:05 -0700 MST 2006
```

So if we want to format our time object a specific way, we can just use the constants from the reference time but rearrange them how we want.

```go
t := time.Now().UTC()
fmt.Println(t.Format("2006 01 02 MST"))

// prints 2021 05 16 UTC (assuming that's the current time)
```

The [time.Parse()](https://golang.org/pkg/time/#Parse) function works the same way, but takes a time string and a layout as an input, and attempts to create a new time object.

```go
t, err := time.Parse("2006 01 02 MST", "2021 05 16 UTC")
if err != nil{
    log.Fatal(err)
}
fmt.Println(t)

// Prints "2021-05-16 00:00:00 +0000 UTC" assuming that's the current time
// The above is the default printing format for a time object (rfc3339)
```

As I mentioned above in the comment, the default parsing and formatting layout for Go is [rfc3339](https://datatracker.ietf.org/doc/html/rfc3339). Where possible, if your team works primarily in Go, I'd recommend using the default formatting,, it's the default for a reason.

## Time durations

My bane in programming is when developers [don't include units](/clean-code/naming-variables/) in their calculations. Inevitably one developer assumes the variable `timeElapsed` (an int) represents seconds, it really represents milliseconds. In Go, this isn't a problem as long as everyone adheres to the standard of the `[time.Duration](https://golang.org/pkg/time/#Duration)` type.

Durations are just a specific kind of `int64`. They represent the elapsed time between two instants as a nanosecond count. the only drawback is that the largest representable duration is ~290 years, which hasn't been a problem for me yet. There are several constants defined by the time package to represent some common durations.

```go
fiveSeconds := time.Second * 5
sixMinutes := time.Minute * 6
oneDay := time.Hour * 24
```

{{< cta2 >}}

## Convert between separate timezones and locations

Every `time.Time` object is associated with a location, which is basically a timezone. 5 o'clock is meaningless if you don't know which timezone it's in. Locations are defined by the `[time.Location](https://golang.org/pkg/time/#Location)` type, which, like the `time.Time` type, is a struct with no exported fields.

### Get the timezone from an existing time object

```go
myTime := time.Now()
myTimezone := myTime.Location()
```

### Create a new `time.Location` object

```go
mstLocation, err := time.LoadLocation("MST")
```

### Convert a time from one location to another

```go
loc, err = time.LoadLocation("MST")
if err != nil{
    log.Fatal(err)
}
mstTime := t.In(loc)
```

### Custom timezone name

A timezone is basically just a name and a duration offset from UTC. If you want a specific timezone but want to change its name you can do that.

```go
tzName := "CUSTOM-TZ"
tzOffset := 60*60*5 // seconds east of UTC
loc := time.FixedZone(tzName, tzOffset)
```

## Add, subtract and compare times

Times and durations naturally work well together, and several helper functions are available to do basic time arithmetic and comparisons.

### Add time and duration

There are two primary functions for adding time to an existing time. Keep in mind, these functions also work for subtracting time, you just add a negative duration.

[time.Add()](https://golang.org/pkg/time/#Time.Add)

```go
myTime := time.Now().UTC()
inTenMinutes := myTime.Add(time.Minute * 10)
// inTenMinutes is 10 minutes in the future

myTime = time.Now().UTC()
tenMinutesAgo := myTime.Add(-time.Minute * 10)
// tenMinutesAgo is 10 minutes in the past
```

[time.AddDate()](https://golang.org/pkg/time/#Time.AddDate)

```go
myTime := time.Now().UTC()

// adds years, months, and days
inOneMonth := myTime.AddDate(0, 1, 0)
// inOneMonth is 1 month in the future

myTime = time.Now().UTC()
twoDaysAgo := myTime.AddDate(0, 0, -2)
// twoDaysAgo is 2 days in the past
```

### Get difference between two times

The [sub()](https://golang.org/pkg/time/#Time.Sub) function gets the difference between two times. Keep in mind, the `sub()` function does not subtract a duration from a time. You, perhaps counterintuitively, need to use the `add()` function for that.

```go
start := time.Date(2020, 2, 1, 3, 0, 0, 0, time.UTC)
end := time.Date(2021, 2, 1, 12, 0, 0, 0, time.UTC)

difference := end.Sub(start) fmt.Printf("difference = %v\n", difference)
```

### Compare two times to see which comes after the other

  
There are two functions that should take care of most of your time comparison needs.

[time.After()](https://golang.org/pkg/time/#Time.After)

```go
first := time.Date(2020, 2, 1, 3, 0, 0, 0, time.UTC)
second := time.Date(2021, 2, 1, 12, 0, 0, 0, time.UTC)

isFirstAfter := first.After(second)
```

[time.Equal()](https://golang.org/pkg/time/#Time.Equal)

```go
first := time.Date(2020, 2, 1, 3, 0, 0, 0, time.UTC)
second := time.Date(2021, 2, 1, 12, 0, 0, 0, time.UTC)

equal := first.Equal(second)
// equal is true if the both times refer to the same instant
// two times are equal even if they are in different locations
```

## Intervals, sleeping, and tickers

If you need your program to synchronously sleep, there's an easy way to do that, [time.Sleep()](https://golang.org/pkg/time/#Sleep). Keep in mind, this is synchronous, it will block the current goroutine.

### Force the current goroutine to sleep

```go
fmt.Println("hello")
time.Sleep(time.Second * 2)
fmt.Println("world 2 seconds in the future")
```

### Execute code on an interval using tickers

If you need to do something on a fixed interval, the [time.Ticker](https://golang.org/pkg/time/#Ticker) type makes it easy to do so.

```go
func doSomethingWithRateLimit() {
    ticker := time.NewTicker(time.Second)
    for range ticker.C {
        // doSomething() is executed every second forever
        doSomething()
    }
}
```

The first tick to come through the ticker channel is after the first duration. If you want an immediate first tick you can [read about that here](/golang/range-over-ticker-in-go-with-immediate-first-tick/).

## Saving memory with TinyDate and TinyTime

A typical time.Time value takes ~24 bytes in memory. Sometimes, you can't afford to use that much. If you're in that situation then check out my TinyTime and TinyDate libraries on GitHub. They only use 4 bytes each!

- [TinyDate Github](https://github.com/wagslane/go-tinydate)
- [TinyTime Github](https://github.com/wagslane/go-tinytime)
