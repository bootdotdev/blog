package main

import (
	"fmt"
	"net/http"
	"net/url"
	"os"
	"strings"
	"sync"
	"time"

	"golang.org/x/net/html"
)

type result struct {
	url  string
	err  error
	code int
}

var (
	visited       = make(map[string]bool)
	mux           sync.Mutex
	baseURL       = "http://localhost:1313" // Change to your local server address
	concurrency   = 3                       // Set the desired concurrency level
	requestDelay  = 2000 * time.Millisecond // Set the desired delay between requests
	semaphoreChan = make(chan struct{}, concurrency)
)

func main() {
	var wg sync.WaitGroup
	results := make(chan result)

	go func() {
		for r := range results {
			if r.err != nil || r.code >= 400 {
				fmt.Printf("BROKEN: %s (status: %d, error: %v)\n", r.url, r.code, r.err)
			}
		}
	}()

	// Start crawling from the base URL
	wg.Add(1)
	go crawl(baseURL, &wg, results)

	// Wait for all crawling to finish, then close the results channel
	wg.Wait()
	close(results)
}

func crawl(link string, wg *sync.WaitGroup, results chan<- result) {
	defer wg.Done()

	mux.Lock()
	if visited[link] {
		// Skip the request and sleep if already visited
		mux.Unlock()
		return
	}
	visited[link] = true
	mux.Unlock()

	// Limit concurrency by acquiring a semaphore
	semaphoreChan <- struct{}{}
	defer func() { <-semaphoreChan }()

	// Throttle each request only for the first time
	time.Sleep(requestDelay)

	fmt.Println("FETCH:", link)
	resp, err := http.Get(link)
	if err != nil {
		results <- result{url: link, err: err, code: 0}
		return
	}
	defer resp.Body.Close()

	results <- result{url: link, code: resp.StatusCode}

	// Only continue if the page is OK (status 200)
	if resp.StatusCode == 200 {
		links := extractLinks(resp, link)
		for _, l := range links {
			if strings.HasPrefix(l, baseURL) {
				// Internal link: crawl recursively
				wg.Add(1)
				go crawl(l, wg, results)
			} else {
				// External link: check once
				wg.Add(1)
				go func(link string) {
					defer wg.Done()
					mux.Lock()
					if visited[link] {
						mux.Unlock()
						return
					}
					visited[link] = true
					mux.Unlock()

					semaphoreChan <- struct{}{}
					defer func() { <-semaphoreChan }()
					time.Sleep(requestDelay) // Throttle external link requests

					fmt.Println("FETCH:", link)
					resp, err := http.Get(link)
					code := 0
					if err == nil {
						code = resp.StatusCode
						resp.Body.Close()
					}
					results <- result{url: link, err: err, code: code}
				}(l)
			}
		}
	}
}

func extractLinks(resp *http.Response, base string) []string {
	links := []string{}
	baseURL, err := url.Parse(base)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error parsing base URL %s: %v\n", base, err)
		return links
	}

	doc := html.NewTokenizer(resp.Body)
	for {
		tt := doc.Next()
		switch tt {
		case html.ErrorToken:
			return links
		case html.StartTagToken, html.SelfClosingTagToken:
			t := doc.Token()
			if t.Data == "a" {
				for _, a := range t.Attr {
					if a.Key == "href" {
						href, err := baseURL.Parse(a.Val)
						if err == nil && (href.Scheme == "http" || href.Scheme == "https") {
							links = append(links, href.String())
						}
					}
				}
			}
		}
	}
}
