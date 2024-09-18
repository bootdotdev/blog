---
title: "Build a Blog Aggregator"
author: Lane Wagner
date: "2024-09-17"
categories:
  - "tutorials"
  - "golang"
images:
  - /img/800/blog_aggregator_art.png.webp
toc: true
---

We're going to build an [RSS](https://en.wikipedia.org/wiki/RSS) feed aggregator in Go! It's a web server that allows clients to:

- Add RSS feeds to be collected
- Follow and unfollow RSS feeds that other users have added
- Fetch all of the latest posts from the RSS feeds they follow

RSS feeds are a way for websites to publish updates to their content. You can use this project to keep up with your favorite blogs, news sites, podcasts, and more!

**Pre-requisites**:

This project assumes that you've already taken our "Learn Web Servers" course. If you haven't, go take it! It will give you a solid foundation for this project.

**Learning goals**:

- Learn how to integrate a Go server with PostgreSQL
- Learn about the basics of database migrations
- Learn about long-running service workers

**Setup**:

Before we dive into the project, let's make sure you have everything you'll need on your machine.

1. An editor. I use [VS code](https://code.visualstudio.com/), you can use whatever you like.
2. A command line. I work on Mac OS/Linux, so instructions will be in Bash. I recommend [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install) if you're on Windows so you can still use Linux commands.
3. The latest [Go toolchain](https://golang.org/doc/install).
4. If you're in VS Code, I recommend the official [Go extension](https://marketplace.visualstudio.com/items?itemName=golang.Go).
5. An HTTP client. I use [Thunder Client](https://www.thunderclient.com/), but you can use whatever you like.

If you're ready, move on to the next step!

**Optional video walkthrough**:

_Try to build this project on your own!_ Use this video if you get stuck, or to compare your architecture and coding patterns to mine.

@[youtube](https://www.youtube.com/watch?v=dpXhDzgUSe4)

**Caveat**: There is a more updated version of this course that's more interactive over on [Boot.dev here](https://www.boot.dev/courses/build-blog-aggregator). If you're looking for a more interactive experience, I recommend checking it out!

## Boilerplate

Before we get to the app-specific stuff, let's scaffold a simple CRUD server, hopefully, you're already familiar with how to do this from the "Learn Web Servers" course! That said, I'll provide a quick refresher.

_It might be a good idea to use your "Learn Web Servers" code as a reference while building this project!_

### Assignment

1. [ ] Create a new project. You should know how to do this by now! My process is:
   - [ ] Create a repo on [GitHub](https://github.com) (initialized with a README).
   - [ ] Clone it onto your machine.
   - [ ] Create a new Go module with `go mod init`.
   - [ ] Create a `main.go` file in the root of your project, and add a `func main()` to it.
2. [ ] Install the [godotenv](https://github.com/joho/godotenv) package using `go get github.com/joho/godotenv`.
3. [ ] Create a [gitignore](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/)'d `.env` file in the root of your project and add the following:

```bash
PORT="8080"
```

The `.env` file is a convenient way to store environment (configuration) variables.

- [ ] Use [godotenv.Load()](https://pkg.go.dev/github.com/joho/godotenv#Load) to load the variables from the file into your environment at the top of `main()`.
- [ ] Use [os.Getenv()](https://pkg.go.dev/os#Getenv) to get the value of `PORT`.

4. [ ] Create a router and server

   - [ ] Create a [ServeMux](https://pkg.go.dev/net/http#ServeMux) using [http.NewServeMux](https://pkg.go.dev/net/http#NewServeMux)
   - [ ] Create a new [http.Server](https://pkg.go.dev/net/http#Server) and add the port and your multiplexer to it.
   - [ ] Start the server

5. [ ] Create some JSON helper functions:
   - [ ] `respondWithJSON(w http.ResponseWriter, code int, payload interface{})`
   - [ ] `respondWithError(w http.ResponseWriter, code int, msg string)` (which calls `respondWithJSON` with error-specific values)

You used these in the "Learn Web Servers" course, so you should be able to figure out how to implement them again. They're simply helper functions that write an HTTP response with:

- A status code
- An `application/json` content type
- A JSON body

6. [ ] Add a readiness handler. It should handle `GET /v1/healthz` requests. It should return a 200 status code and a JSON body:

```json
{
  "status": "ok"
}
```

_The purpose of this endpoint is for you to test your `respondWithJSON` function._

7. [ ] Add an error handler.

Add a handler for `GET /v1/err` requests. It should return a 500 status code and a JSON body:

```json
{
  "error": "Internal Server Error"
}
```

_The purpose of this endpoint is for you to test your `respondWithError` function._

8. [ ] Run and test your server.

```bash
go build -o out && ./out
```

Once it's running, use an HTTP client to test your endpoints.

## PostgreSQL

PostgreSQL is a production-ready, open-source database. It's a great choice database for many web applications, and as a back-end engineer, it might be the single most important database to be familiar with.

### How does PostgreSQL work?

Postgres, like most other database technologies, is itself a server. It listens for requests on a port (Postgres' default is `:5432`), and responds to those requests. To interact with Postgres, first you will install the server and start it. Then, you can connect to it using a client like [psql](https://www.postgresql.org/docs/current/app-psql.html#:~:text=psql%20is%20a%20terminal%2Dbased,or%20from%20command%20line%20arguments.) or [PGAdmin](https://www.pgadmin.org/).

1. [ ] Install Postgres.

**Mac OS with [brew](https://brew.sh/)**

```bash
brew install postgresql@15
```

**Linux / WSL (Debian). Here are the [docs from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-postgresql), but simply:**

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

2. [ ] Ensure the installation worked. The `psql` command-line utility is the default client for Postgres. Use it to make sure you're on version 14+ of Postgres:

```bash
psql --version
```

3. [ ] (Linux only) Update postgres password:

```bash
sudo passwd postgres
```

Enter a password, and be sure you won't forget it. You can just use something easy like `postgres`.

4. [ ] Start the Postgres server in the background

- Mac: `brew services start postgresql`
- Linux: `sudo service postgresql start`

5. [ ] Connect to the server. I recommend simply using the `psql` client. It's the "default" client for Postgres, and it's a great way to interact with the database. While it's not as user-friendly as a GUI like [PGAdmin](https://www.pgadmin.org/), it's a great tool to be able to do at least basic operations with.

Enter the `psql` shell:

- Mac: `psql postgres`
- Linux: `sudo -u postgres psql`

You should see a new prompt that looks like this:

```bash
postgres=#
```

6. [ ] Create a new database. I called mine `blogator`:

```sql
CREATE DATABASE blogator;
```

7. [ ] Connect to the new database:

```sql
\c blogator
```

You should see a new prompt that looks like this:

```bash
blogator=#
```

8. [ ] Set the user password (Linux only)

```sql
ALTER USER postgres PASSWORD 'postgres';
```

For simplicity, I used `postgres` as the password. Before, we altered the _system_ user's password, now we're altering the _database_ user's password.

9. [ ] Query the database

From here you can run SQL queries against the `blogator` database. For example, to see the version of Postgres you're running, you can run:

```sql
SELECT version();
```

If everything is working, you can move on. _You can type `exit` to leave the `psql` shell._

## Create Users

In this step, we'll be adding an endpoint to create new users on the server. We'll be using a couple of tools to help us out:

- [database/sql](https://pkg.go.dev/database/sql): This is part of Go's standard library. It provides a way to connect to a SQL database, execute queries, and scan the results into Go types.
- [sqlc](https://sqlc.dev/): SQLC is an _amazing_ Go program that generates Go code from SQL queries. It's not exactly an [ORM](https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/), but rather a tool that makes working with raw SQL almost as easy as using an ORM.
- [Goose](https://github.com/pressly/goose): Goose is a database migration tool written in Go. It runs migrations from the same SQL files that SQLC uses, making the pair of tools a perfect fit.

1. [ ] Install SQLC

SQLC is just a command line tool, it's not a package that we need to import. I recommend [installing](https://docs.sqlc.dev/en/latest/overview/install.html) it using `go install`. Installing Go CLI tools with `go install` is easy and ensures compatibility with your Go environment.

```bash
go install github.com/sqlc-dev/sqlc/cmd/sqlc@latest
```

Then run `sqlc version` to make sure it's installed correctly.

2. [ ] Install Goose

Like SQLC, Goose is just a command line tool. I also recommend [installing](https://github.com/pressly/goose#install) it using `go install`:

```bash
go install github.com/pressly/goose/v3/cmd/goose@latest
```

Run `goose -version` to make sure it's installed correctly.

3. [ ] Create the `users` migration

I recommend creating an `sql` directory in the root of your project, and in there creating a `schema` directory.

A "migration" is a SQL file that describes a change to your database schema. For now, we need our first migration to create a `users` table. The simplest format for these files is:

```
number_name.sql
```

For example, I created a file in `sql/schema` called `001_users.sql` with the following contents:

```sql
-- +goose Up
CREATE TABLE ...

-- +goose Down
DROP TABLE users;
```

Write out the `CREATE TABLE` statement in full, I left it blank for you to fill in. A `user` should have 4 fields:

- id: a `UUID` that will serve as the primary key
- created_at: a `TIMESTAMP` that can not be null
- updated_at: a `TIMESTAMP` that can not be null
- name: a string that can not be null

The `-- +goose Up` and `-- +goose Down` comments are required. They tell Goose how to run the migration. An "up" migration moves your database from its old state to a new state. A "down" migration moves your database from its new state back to its old state.

By running all of the "up" migrations on a blank database, you should end up with a database in a ready-to-use state. "Down" migrations are only used when you need to roll back a migration, or if you need to reset a local testing database to a known state.

4. [ ] Get your connection string

A connection string is just a URL with all of the information needed to connect to a database. The format is:

```
protocol://username:password@host:port/database
```

Here are examples:

- Mac OS (no password, your username): `postgres://wagslane:@localhost:5432/blogator`
- Linux (password from last lesson, postgres user): `postgres://postgres:postgres@localhost:5432/blogator`

Test your connection string by running `psql`, for example:

```bash
psql "postgres://wagslane:@localhost:5432/blogator"
```

It should connect you to the `blogator` database directly. If it's working, great. `exit` out of `psql` and save the connection string.

5. [ ] Run the migration.

`cd` into the `sql/schema` directory and run:

```bash
goose postgres CONN up
```

Where `CONN` is the connection string for your database.

Run your migration! Make sure it works by using `psql` to find your newly created `users` table:

```bash
psql blogator
\dt
```

6. [ ] Add your connection string to your `.env` file. When using it with `goose`, you'll use it in the format we just used. However, here in the `.env` file it needs an additional `sslmode=disable` query string:

```
protocol://username:password@host:port/database?sslmode=disable
```

Your application code needs to know to not try to use SSL locally.

7. [ ] Configure [SQLC](https://docs.sqlc.dev/en/latest/tutorials/getting-started-postgresql.html). You'll always run the `sqlc` command from the root of your project. Create a file called `sqlc.yaml` in the root of your project. Here is mine:

```yaml
version: "2"
sql:
  - schema: "sql/schema"
    queries: "sql/queries"
    engine: "postgresql"
    gen:
      go:
        out: "internal/database"
```

We're telling SQLC to look in the `sql/schema` directory for our schema structure (which is the same set of files that Goose uses, but `sqlc` automatically ignores "down" migrations), and in the `sql/queries` directory for queries. We're also telling it to generate Go code in the `internal/database` directory.

8. [ ] Write a query to create a user. Inside the `sql/queries` directory, create a file called `users.sql`. Here is mine:

```sql
-- name: CreateUser :one
INSERT INTO users (id, created_at, updated_at, name)
VALUES ($1, $2, $3, $4)
RETURNING *;
```

`$1`, `$2`, `$3`, and `$4` are parameters that we'll be able to pass into the query in our Go code. The `:one` at the end of the query name tells SQLC that we expect to get back a single row (the created user).

Keep the [SQLC docs](https://docs.sqlc.dev/en/latest/tutorials/getting-started-postgresql.html) handy, you'll probably need to refer to them again later.

9. [ ] Generate the Go code. Run `sqlc generate` from the root of your project. It should create a new package of go code in `internal/database`.
10. [ ] Import a PostgreSQL driver

We need to add and import a [Postgres driver](https://github.com/lib/pq) to use it in our code. Install it in your module:

```bash
go get github.com/lib/pq
```

Add this import to the top of your `main.go` file:

```go
import _ "github.com/lib/pq"
```

_This is one of my least favorite things working with SQL in Go currently. You have to import the driver, but you don't use it directly anywhere in your code. The underscore tells Go that you're importing it for its side effects, not because you need to use it._

11. [ ] Open a connection to the database, and store it in a config struct

If you recall from the web servers project, it's common to use a "config" struct to store shared data that HTTP handlers need access to. We'll do the same thing here. Mine looks like this:

```go
type apiConfig struct {
	DB *database.Queries
}
```

At the top of `main()` load in your database URL from your `.env` file, and then [.Open()](https://pkg.go.dev/database/sql#Open) a connection to your database:

```go
db, err := sql.Open("postgres", dbURL)
```

Use your generated `database` package to create a new `*database.Queries`, and store it in your config struct:

```go
dbQueries := database.New(db)
```

12. [ ] Create an HTTP handler to create a user

Endpoint: `POST /v1/users`

Example body:

```json
{
  "name": "Lane"
}
```

Example response:

```json
{
  "id": "3f8805e3-634c-49dd-a347-ab36479f3f83",
  "created_at": "2021-09-01T00:00:00Z",
  "updated_at": "2021-09-01T00:00:00Z",
  "name": "Lane"
}
```

Use Google's [UUID](https://pkg.go.dev/github.com/google/uuid) package to generate a new [UUID](https://blog.boot.dev/clean-code/what-are-uuids-and-should-you-use-them/) for the user's ID. Both `created_at` and `updated_at` should be set to the current time. If we ever need to update a user, we'll update the `updated_at` field.

I'm a fan of a convention where _every table_ in my database has:

- An `id` field that is a UUID (if you're curious why, [read this](https://blog.boot.dev/clean-code/what-are-uuids-and-should-you-use-them/))
- A `created_at` field that indicates when the row was created
- An `updated_at` field that indicates when the row was last updated

13. [ ] Test your handler with an HTTP client!

C'mon, you know what to do.

## API Key

1. [ ] Add an "api key" column to the users table

Use a new migration file in the `sql/schema` directory to add a new column to the `users` table. I named my file `002_users_apikey.sql`.

The "up" migration adds the column, and the "down" migration removes it.

Use a `VARCHAR(64)` that must be unique and not null. Using a string of a specific length does two things:

- [ ] It ensures we don't accidentally store a key that's too long (type safety)
- [ ] It's more performant than using a variable length `TEXT` column

Because we're enforcing the `NOT NULL` constraint, and we already have some users in the database, we need to set a default value for the column. A blank default would be a bit silly: that's no better than null! Instead, we'll generate valid API keys (256-bit hex values) using SQL. Here's the function I used:

```sql
encode(sha256(random()::text::bytea), 'hex')
```

When you're done, use `goose postgres CONN up` to perform the migration.

2. [ ] Create an API key for new users. Update your "create user" SQL query to use the same SQL function to generate API keys for new users.
3. [ ] Add a new SQL query to get a user by their API key. This query can live in the same file as the "create user" query, or you can make a new one - it's up to you.
4. [ ] Generate new Go code. Run `sqlc generate` to generate new Go code for your queries.
5. [ ] New endpoint: Add a new endpoint that allows users to get their own user information. You'll need to parse the header and use your new query to get the user data.

Endpoint: `GET /v1/users`

Request headers: `Authorization: ApiKey <key>`

Example response body:

```json
{
  "id": "3f8805e3-634c-49dd-a347-ab36479f3f83",
  "created_at": "2021-09-01T00:00:00Z",
  "updated_at": "2021-09-01T00:00:00Z",
  "name": "Lane",
  "api_key": "cca9688383ceaa25bd605575ac9700da94422aa397ef87e765c8df4438bc9942"
}
```

_Test your endpoints with an HTTP client before moving on!_

Don't forget that each time you update your queries or schema you'll need to regenerate your Go code with `sqlc generate`. If you update the schema you'll also need to migrate your database up (and maybe down).

## Create a Feed

An RSS feed is just a URL that points to some XML. Users will be able to add feeds to our database so that our server (in a future step) can go download all of the posts in the feed (like blog posts or podcast episodes).

1. [ ] Create a feeds table

Like any table in our DB, we'll need the standard `id`, `created_at`, and `updated_at` fields. We'll also need a few more:

- `name`: The name of the feed (like "The Changelog, or "The Boot.dev Blog")
- `url`: The URL of the feed
- `user_id`: The ID of the user who added this feed

I'd recommend making the `url` field unique so that in the future we aren't downloading duplicate posts. I'd also recommend using [ON DELETE CASCADE](https://stackoverflow.com/a/14141354) on the `user_id` foreign key so that if a user is deleted, all of their feeds are automatically deleted as well.

Write the appropriate migrations and run them.

2. [ ] Add a new query to create a feed, then use `sqlc generate` to generate the Go code.

3. [ ] Create some authentication middleware. Most of the endpoints going forward will require a user to be logged in. Let's DRY up our code by creating some middleware that will check for a valid API key.

Now, I'm not a fan of how some frameworks handle stateful middleware using [context](https://pkg.go.dev/context) (middleware that passes data down to the next handler). I prefer to create custom handlers that accept extra values. You can add middleware however you like, but here are some examples from my code.

#### A custom type for handlers that require authentication

```go
type authedHandler func(http.ResponseWriter, *http.Request, database.User)
```

#### Middleware that authenticates a request, gets the user and calls the next authed handler

```go
func (cfg *apiConfig) middlewareAuth(handler authedHandler) http.HandlerFunc {
    ///
}
```

#### Using the middleware

```go
v1Router.Get("/users", apiCfg.middlewareAuth(apiCfg.handlerUsersGet))
```

4. [ ] Create a handler to create a feed

Create a handler that creates a feed. This handler _and_ the "get user" handler should use the authentication middleware.

Endpoint: `POST /v1/feeds`

Example request body:

```json
{
  "name": "The Boot.dev Blog",
  "url": "https://blog.boot.dev/index.xml"
}
```

Example response body:

```json
{
  "id": "4a82b372-b0e2-45e3-956a-b9b83358f86b",
  "created_at": "2021-05-01T00:00:00Z",
  "updated_at": "2021-05-01T00:00:00Z",
  "name": "The Boot.dev Blog",
  "url": "https://blog.boot.dev/index.xml",
  "user_id": "d6962597-f316-4306-a929-fe8c8651671e"
}
```

5. [ ] Test your handler using an HTTP client, then use your database client to make sure the data was saved correctly.

## Get all feeds

Create a new endpoint to retrieve _all_ of the feeds in the database. This endpoint should _not_ require authentication.

You should be familiar with all of the steps to make this happen by now, use your other endpoints as a reference.

## Feed Follows

Aside from just adding new feeds to the database, users can specify _which_ feeds they want to follow. This will be important later when we want to show users a list of posts from the feeds they follow.

Add support for the following endpoints, and update the "create feed" endpoint as specified below.

### What is a "feed follow"?

A feed follow is just a link between a user and a feed. It's a [many-to-many](<https://en.wikipedia.org/wiki/Many-to-many_(data_model)>) relationship, so a user can follow many feeds, and a feed can be followed by many users.

Creating a feed follow indicates that a user is now following a feed. Deleting it is the same as "unfollowing" a feed.

It's important to understand that the `ID` of a feed follow is not the same as the `ID` of the feed itself. Each user/feed pair will have a unique feed follow id.

1. [ ] Create a feed follow

Endpoint: `POST /v1/feed_follows`

_Requires authentication_

Example request body:

```json
{
  "feed_id": "4a82b372-b0e2-45e3-956a-b9b83358f86b"
}
```

Example response body:

```json
{
  "id": "c834c69e-ee26-4c63-a677-a977432f9cfa",
  "feed_id": "4a82b372-b0e2-45e3-956a-b9b83358f86b",
  "user_id": "0e4fecc6-1354-47b8-8336-2077b307b20e",
  "created_at": "2017-01-01T00:00:00Z",
  "updated_at": "2017-01-01T00:00:00Z"
}
```

2. [ ] Delete a feed follow

Endpoint: `DELETE /v1/feed_follows/{feedFollowID}`

3. [ ] Get all feed follows for a user

Endpoint: `GET /v1/feed_follows`

_Requires authentication_

Example response:

```json
[
  {
    "id": "c834c69e-ee26-4c63-a677-a977432f9cfa",
    "feed_id": "4a82b372-b0e2-45e3-956a-b9b83358f86b",
    "user_id": "0e4fecc6-1354-47b8-8336-2077b307b20e",
    "created_at": "2017-01-01T00:00:00Z",
    "updated_at": "2017-01-01T00:00:00Z"
  },
  {
    "id": "ad752167-f509-4ff3-8425-7781090b5c8f",
    "feed_id": "f71b842d-9fd1-4bc0-9913-dd96ba33bb15",
    "user_id": "0e4fecc6-1354-47b8-8336-2077b307b20e",
    "created_at": "2017-01-01T00:00:00Z",
    "updated_at": "2017-01-01T00:00:00Z"
  }
]
```

4. [ ] Automatically create a feed follow when creating a feed

When a user creates a new feed, they should automatically be following that feed. They can of course choose to unfollow it later, but it should be there by default.

The response of this endpoint should now contain both entities:

```json
{
  "feed": { the feed object },
  "feed_follow": { the feed follow object }
}
```

5. [ ] Test. As always, test all of your endpoints and make sure they work. Additionally, make sure that they return the proper error codes when they receive invalid inputs.

## Scraper

This is going to be a fairly large step. I recommend breaking it down into smaller pieces and functions, and testing each piece as you go.

Here are some different strategies I use depending on the situation:

- Write a unit test for a function that has simple inputs and outputs
- Edit `main.go` to call a function so I can quickly test it by running the whole program. Remove the call after testing and plug it into its proper place
- Put the code in a package, then write a separate `main` package (just a little `main()` script) that I can use to independently test the code in the package

_Commit your code each time you get a new piece working._

1. [ ] Add a `last_fetched_at` column to the `feeds` table.

We need to keep track of when we last fetched the posts from a feed. This should be a nullable timestamp.

The `sql.NullTime` type is useful for nullable timestamps on the database side, but it's not great for marshaling into JSON. It results in a weird nested object. I'd recommend converting it to a `*time.Time` before returning it across the HTTP response.

I map all of my database structs to a different struct that has the intended JSON structure. This is a good way to keep your database and HTTP APIs separate.

For example: `func databaseFeedToFeed(feed database.Feed) Feed`

2. [ ] Add `GetNextFeedsToFetch()` query to the database.

It should return the next `n` feeds that need to be fetched, ordered by `last_fetched_at`, but with `NULL` values first. We obviously want to fetch the feeds that have never been fetched before or the ones that were fetched the longest time ago.

3. [ ] Add a `MarkFeedFetched()` query to the database.

It should update a feed and set its `last_fetched_at` to the current time. Don't forget to also update the `updated_at` field because we've updated the record.

4. [ ] Write a function that can fetch data from a feed.

This function should accept the URL of a live RSS feed, and return the parsed data in a Go struct.

You can test with these ones:

- `https://blog.boot.dev/index.xml`
- `https://wagslane.dev/index.xml`

And any other blogs you enjoy that have RSS feeds.

_Please be careful not to [DDOS](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) any of the sites you're fetching from. Don't send too many requests!_

You can parse the returned XML with the [encoding/xml](https://pkg.go.dev/encoding/xml) package, it works _very_ similarly to `encoding/json`. Define the structure of an RSS feed as a Go struct, then unmarshal the XML into that struct.

5. [ ] Write a worker that fetches feeds continuously.

This function should, on an interval (say every 60 seconds or so):

- Get the next `n` feeds to fetch from the database (you can configure `n`, I used `10`)
- Fetch and process all the feeds _at the same time_ (you can use [sync.WaitGroup](https://pkg.go.dev/sync#WaitGroup) for this)

For now, "process" the feed by simply printing out the titles of each post

I recommend adding a lot of logging messages to this worker so that as it runs you can see what it's doing!

6. [ ] Call your worker from `main.go`. Be sure to start the worker in its own goroutine, so that it runs in the background and processes feeds even as it simultaneously handles new HTTP requests.

## Posts

1. [ ] Add a `posts` table to the database.

A post is a single entry from a feed. It should have:

- `id` - a unique identifier for the post
- `created_at` - the time the record was created
- `updated_at` - the time the record was last updated
- `title` - the title of the post
- `url` - the URL of the post _this should be unique_
- `description` - the description of the post
- `published_at` - the time the post was published
- `feed_id` - the ID of the feed that the post came from

Some of these fields can probably be null, others you might want to be more strict about - it's up to you.

2. [ ] Add a "create post" SQL query to the database. This should insert a new post into the database.
3. [ ] Add a "get posts by user" SQL query to the database. Order the results so that the most recent posts are first. Make the number of posts returned configurable.

4. [ ] Update your scraper to save posts. Instead of just printing out the titles of the posts, save them to the database! If you encounter an error where the post with that URL already exists, just ignore it. That will happen a lot. If it's a different error, you should probably log it. Make sure that you're parsing the "published at" time properly from the feeds. Sometimes they might be in a different format than you expect, so you might need to handle that.
5. [ ] Add a "get posts by user" HTTP endpoint.

Endpoint: `GET /v1/posts`

_This is an authenticated endpoint_

This endpoint should return a list of posts for the authenticated user. It should accept a `limit` query parameter that limits the number of posts returned. The default if the parameter is not provided can be whatever you think is reasonable.

6. [ ] Start scraping some feeds! Test your scraper to make sure it's working! Go find some of your favorite websites and add their RSS feeds to your database. Then start your scraper and watch it go to work.

## Submit your Git repo

Your link should look something like `https://github.com/github-username/repo-name`.

### Ideas for extending the project

You don't _have_ to extend this project, but here are just a few ideas if you're interested:

- Support [pagination](https://nordicapis.com/everything-you-need-to-know-about-api-pagination/) of the endpoints that can return many items
- Support different options for sorting and filtering posts using query parameters
- Classify different types of feeds and posts (e.g. blog, podcast, video, etc.)
- Add a CLI client that uses the API to fetch and display posts, maybe it even allows you to read them in your terminal
- Scrape lists of feeds themselves from a third-party site that aggregates feed URLs
- Add support for other types of feeds (e.g. Atom, JSON, etc.)
- Add integration tests that use the API to create, read, update, and delete feeds and posts
- Add bookmarking or "liking" to posts
- Create a simple web UI that uses your backend API

## Solution

If you get lost at any point, I've uploaded my solution repo to [GitHub here](https://github.com/bootdotdev/blog-agg-solution-snapshot-v0).
