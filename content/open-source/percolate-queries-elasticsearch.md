---
title: "Percolate Queries in ElasticSearch - How I Built an Alerts System"
author: Lane Wagner
date: "2019-11-14"
categories: 
  - "open-source"
images:
  - /img/800/How-We-Used-Percolate-Queries-in-Elasticsearch-To-Build-a-Fast-Alerts-System.jpeg
---

Once upon a time, a company I worked for had a problem, we had thousands of messages flowing through our data pipeline every second, and we wanted to be able to send real-time emails, SMS, and Slack alerts when messages matching specific criteria were found. A simple solution built using [ElasticSearch's percolate queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-percolate-query.html) ended up being our saving grace.

Our first failed attempt to build an alerting system utilized [PipelineDB](https://github.com/pipelinedb/pipelinedb). To make a long story short, not only was that architecture rigid and hard to make changes to, it didn't scale well and was constantly having performance issues. We would get called out by users for not sending alerts that should have triggered.

## Enter ElasticSearch

![elasticsearch](/img/800/elasticsearch-logo-300x139.png)

Elasticsearch is a NoSQL distributed database that is good for, well, **searching**. I would never recommend it as a transactional database for basic CRUD actions, but aggregations, metrics, and percolate queries are where it shines.

## What is a percolate query?

Percolate queries can be simply thought of as an inverse search. Instead of sending a _query_ to an index and getting the _matching documents_, you send a _document_ to an index and get the _matching queries_. This is exactly what most alerting systems need.

{{< cta1 >}}

## What does it look like?

From [elastic's documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-percolate-query.html#query-dsl-percolate-query), we will create an index with a mapping (which is basically a loosey-goosy SQL schema) for an index that holds percolating queries:

```
PUT /my-index
{
    "mappings": {
        "properties": {
             "threshold": {
                 "type": "long"
             },
             "count": {
                 "type": "long"
             },
             "query": {
                 "type": "percolator"
             }
        }
    }
}
```

- **my-index** is the name of the index
- **threshold** and **count** are fields that we plan on utilizing in either the queries or the documents. All fields should be defined in the mapping

Now that we have an index that can store percolating queries, we can register a new query:

```
PUT /my-index/my-doc/1?refresh
{
    "threshold": 100,
    "query" : {
        "bool" : {
            "must": {
                "query_string": {
                    "default_field": "query_string",
                    "query": "count:>100"
                }
            }
        }
    }
}
```

The query object contains all the logic for percolation. If a document's count field is greater than 100 then this query will be returned in the document's result set. The only purpose of the **threshold** field is for convenience, that is, when we are doing [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations on our queries, we can manage the threshold in its own field instead of parsing the query string every time.

Now, lets percolate a document and see if it matches:

```
GET /my-index/_search
{
    "query" : {
        "percolate" : {
            "field" : "query",
            "document" : {
                "count" : 101
            }
        }
    }
}
```

Response:

```json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1,
    "hits": [
      {
        "_index": "my-index",
        "_type": "my-doc",
        "_id": "1",
        "_score": 1,
        "_source": {
          "threshold": 100,
          "query": {
            "bool": {
              "must": {
                "query_string": {
                  "default_field": "query_string",
                  "query": "count:>100"
                }
              }
            }
          }
        }
      }
    ]
  }
}
```

Because the count was greater than the threshold, the percolate query was returned! As you can see, this works great for an alerting system because users can create "alerts" which we store as percolating queries. For example, a user can create a query that triggers when a twitter post mentions their name, or when a temperature in a city is above a certain threshold.

## Use it

Percolate queries are perfect for when you have an ever changing set of criteria (probably created by users) that many documents need to be checked against. I've used it for alerting and auto-tagging systems in the past. Let me know on twitter if you have questions or can think of another interesting use case for them!
