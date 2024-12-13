---
title: "Using GitHub Issues to Hack Together A Feedback System"
author: lane
date: "2022-07-31"
categories:
  - "misc"
images:
  - /img/800/github-cat-and-groot.avif.webp
---

Boot.dev has been my side-project for the last couple of years now. Being a [learning path for backend developers](https://www.boot.dev) focused on quality over quantity, I knew early on that it needed to have a _really tight_ feedback loop from students. We had (and still have) a [Discord server](https://discord.gg/EEkFwbv) where myself and the students hang out, and that worked okay at first. Unfortunately, Discord channels have a couple problems when it comes to issue tracking:

- Long conversations make it hard to keep track of individual reports
- There's not way to "resolve" a "ticket"
- Not all students are in the Discord
- There is more friction to report issues in a different application

The solution that has been working splendidly for me so far was to add a feedback box directly within each coding assignment! Now students can easily report issues with near-zero hassle. Unfortunately, running SQL queries to get at those submitted issues is a giant pain... _The GitHub API has entered the chat_.

## Using GitHub issues to track user feedback

I have a private GitHub repo where I store all the content for the [back-end CS courses](https://www.boot.dev/tracks/backend) on Boot.dev in markdown files. It would be _really convenient_ if user reported issues automatically manifested as GitHub issues on that repository! After just a few minutes of digging, I realized it was quite easy to do with the GitHub API. Given that my backend is a REST-ish API written in Go, I decided to use [Google's GitHub API client package](https://github.com/google/go-github/) and the official [Golang oauth2 package](https://pkg.go.dev/golang.org/x/oauth2).

I you're interested in following along, first you need is a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with "repo" permissions.

Next, I created a `githubclient` package in my project to manage interactions with the GitHub API. It exposes a `Client` struct:

```go
// Client -
type Client struct {
	githubClient *github.Client
}

// NewClient -
func NewClient(personalAccessToken string) (Client, error) {
	ctx := context.Background()
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: personalAccessToken},
	)
	tc := oauth2.NewClient(ctx, ts)

	client := github.NewClient(tc)

	_, ghResp, err := client.Issues.List(ctx, false, nil)
	if err != nil {
		return Client{}, err
	}
	if ghResp.StatusCode > 299 {
		dat, err := io.ReadAll(ghResp.Body)
		if err != nil {
			return Client{}, err
		}
		return Client{}, fmt.Errorf("status code: %v, message: %v", ghResp.StatusCode, string(dat))
	}

	return Client{
		githubClient: client,
	}, nil
}
```

You'll notice that I added some logic to list the issues. We don't actually do anything with those issues, and you can remove that code if you want. For me, it was useful to test that the token is working on application startup.

Next, I wrote a simple `CreateIssue()` method on the client:

```go
// CreateIssue creates an issue in the example-org/example-repo repository
func (c Client) CreateIssue(exercisePath, fromUsername, userComment string) error {
	ctx := context.Background()
  const repoName = "example-repo"
  const orgName = "example-org"

	summary := userComment
	const summaryLength = 20
	if len(summary) > summaryLength {
		summary = summary[:summaryLength]
	}

	title := fmt.Sprintf("exercise: %v, Summary: %v", exercisePath, summary)
	body := fmt.Sprintf(`
Comment: %v

From: %v
`, userComment, fromUsername)

	_, ghResp, err := c.githubClient.Issues.Create(ctx, orgName, repoName, &github.IssueRequest{
		Title:  &title,
		Body:   &body,
		Labels: &[]string{"course-feedback"},
	})
	if err != nil {
		return err
	}

	if ghResp.StatusCode > 299 {
		dat, err := io.ReadAll(ghResp.Body)
		if err != nil {
			return err
		}
		return fmt.Errorf("status code: %v, message: %v", ghResp.StatusCode, string(dat))
	}
	return nil
}
```

As you can see, given an...

- exercise path (which is just the filepath to the exercise receiving feedback)
- username of the reporter
- comment from the reporter

...the `CreateIssue` method simply creates a new issue in the repo with a static label. I've split the inputs into a GitHub issue "title" and "body" that's formatted to my needs so that I can resolve the issues as quickly as possible.

## Why not use an out of the box solution?

I know there are a billion and a half issue tracking tools you can buy on the market, but I really liked this solution for a few reasons:

- It took about an hour to code from start to finish
- It's free
- It's integrated with the tooling I already use daily (GitHub)

If you need a simple issue tracker for your app I'd recommend looking into using GitHub issues via the API, at least until it stops working for you!
