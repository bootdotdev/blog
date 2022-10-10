---
title: "Writing Good Unit Tests; Don't Mock Database Connections"
author: Lane Wagner
date: "2020-11-23"
lastmod: "2022-10-01"
categories: 
  - "clean-code"
images:
  - /img/800/Writing-Good-Unit-Tests-Dont-Use-Database-Mocking.webp
---

Unit tests are incredibly important because they allow us to *demonstrate* the correctness of the code we've written. More importantly, unit tests allow us to make updates to our code base with the confidence that we haven't broken anything. However, in our zeal to achieve 100% code coverage, we often write tests for logic that we may not even *want* to test. I'm here to convince you that creating mock database abstractions to write unit tests is usually a **bad idea**.

I work on a lot of RESTful Go API servers, and I do my best to write small testable functions so I don't *have* to write useless mocking logic. This kind of code pollutes the repository, adds unnecessary abstractions, makes the code harder to understand, and does not contribute to the robustness of the test suite. My "tl;dr" for you can be summed up as:

> Write better code so that you don't need to unit test your database queries. Test all your database queries in *integration* tests as needed.

If you like my approach to back-end architecture, you might enjoy my back-end development courses on [Boot.dev](https://boot.dev).

## What is a unit test?

> In computer programming, unit testing is a software testing method by which individual units of source code—sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures—are tested to determine whether they are fit for use.
> 
> [Wikipedia](https://en.wikipedia.org/wiki/Unit_testing)

In Go, unit tests can be executed using the `go test` command and some example source code looks something like this:

```go
func TestLogPow(t *testing.T) {
	expected := math.Round(math.Log2(math.Pow(7, 8)))
	actual := math.Round(logPow(7, 8, 2))
	if actual != expected {
		t.Errorf("Expected %v, got %v", expected, actual)
	}

	expected = math.Round(math.Log2(math.Pow(10, 11)))
	actual = math.Round(logPow(10, 11, 2))
	if actual != expected {
		t.Errorf("Expected %v, got %v", expected, actual)
	}
}
```

Where we are testing the `logPow` function that looks like this:

```go
// logPow calculates log_base(x^y)
// without leaving logspace for each multiplication step
// this makes it take less space in memory
func logPow(expBase float64, pow int, logBase float64) float64 {
	// logb (MN) = logb M + logb N
	total := 0.0
	for i := 0; i < pow; i++ {
		total += logX(logBase, expBase)
	}
	return total
}
```

The goal of unit tests is to test a "unit", or small portion, of code. If we can break our code into many small testable units, then we can automate much of our testing through these kinds of test suites.

## Good code is easier to test

`logPow` is a perfect candidate for a suite of unit tests. It's a mathematical function with predictable outputs for any given inputs. Not all functions we write will be *nearly* this straightforward to test. However, if we can write small and ideally [pure functions whereever possible](/golang/pure-functions-in-golang/), writing tests for them becomes much easier.

**Testing shouldn't be hard.** Good code is easy to test.

{{< cta1 >}}

## Unit tests shouldn't depend on infrastructure

In web development, it is commonly regarded as good practice (see [Clean Code](https://reflectoring.io/book-review-clean-code/)) to create architectural boundaries at every point of I/O. For example, your database functions with all their [SQL](https://boot.dev/learn/learn-sql) and driver libraries should be separate from the code that ensures [your user's passwords are secure.](https://github.com/lane-c-wagner/go-password-validator)

Take a look at the following function:

```go
func saveUser(db *sql.DB, user *User) error {
	if user.EmailAddress == "" {
		return errors.New("user requires an email")
	}
	if len(user.Password) < 8 {
		return errors.New("user password requires at least 8 characters")
	}
	hashedPassword, err = hash(user.Password)
	if err != nil {
		return err
	}
	_, err := db.Exec(`                                                                                                                          
		INSERT INTO users (password, email_address, created)                                                                
		VALUES ($1, $2, $3);`,
		hashedPassword, user.EmailAddress, time.Now(),
	)
	return err
}
```

There's no way to test this function without a database connection available at the time of testing. If a new developer clones the project they will need to set up a database before they can successfully run the unit tests. If you set up CI pipeline tests, they will *also* fail without a dummy database on the server. The point is, this isn't the best way to write tests.

Developers should be able to clone a repo and immediately run unit tests that pass.

The way to fix the code so that tests can be implemented would be to separate the testable logic. For example:

```go
func saveUser(db *sql.DB, user *User) error {
	err := validateUser(user)
	if err != nil{
		return err
	}
	user.Password, err = hash(user.Password)
	if err != nil {
		return err
	}
	return saveUserInDB(user)
}
```

Now our primary function for saving users has been broken into three different functions:

* Validate the user
* Hash the password
* Save the user in the database

We don't need to write a test that tests this function as a *whole*, we can test the parts we care about independently. Assuming the `saveUserInDB()` function is just making a SQL query, it probably doesn't need a unit test at all. If the password hashing algorithm contains any more logic than a simple call to a well-tested crypto library, then we can easily write a test for it. Otherwise, we can trust the tests in the crypto library. The only test we probably need here is to test *our own business logic*, the `validateUser()` function.

```go
func TestValidateUser(t *testing.T) {
	err := validateUser(&User{})
	if err == nil {
		t.Error("expected an error")
	}

	err := validateUser(&User{
		Email: "test@test.com",
		Password: "thisIsALongEnoughPassword"
	})
	if err != nil {
		t.Error("should have passed")
	}
}
```

The point is, we need to break our large functions into smaller encapsulated units if we want to have a good time writing effective unit tests.

## Don't mock your external dependencies either

While my last rule of thumb, "unit tests shouldn't depend on infrastructure" is fairly uncontroversial, this next one is more fiercely debated. I believe that the majority of database mocking is a result of bad code. It follows then that assuming your team has the time, the best solution is to [refactor the code](/clean-code/spend-time-refactoring/) into smaller functions or "units" as we did a moment ago.

However, some engineers would rather lazily create a mock database interface and test the whole damn thing.

```go
type sqlDB interface {
	Exec(query string, args ...interface{}) (sql.Result, error)
}

type mockDB struct {}

func (mdb *mockDB) Exec(query string, args ...interface{}) (sql.Result, error) {
	return nil, nil
}

func saveUser(db sqlDB, user *User) error {
	if user.EmailAddress == "" {
		return errors.New("user requires an email")
	}
	if len(user.Password) < 8 {
		return errors.New("user password requires at least 8 characters")
	}
	hashedPassword, err := hash(user.Password)
	if err != nil {
		return err
	}
	_, err := db.Exec(`                                                                                                                          
		INSERT INTO usr (password, email_address, created)                                                                                                                                                                                                                                                                                                                                                                                       
		VALUES ($1, $2, $3);`,
		hashedPassword, user.EmailAddress, time.Now(),
	)
	return err
}
```

With this code, we can now write a unit test that calls the entire `saveUser()` function by passing in a `mockDB` so that we don't need on a running database for the tests. As I hope is clear, there are several issues with this approach:

* The mock database code is unused in production. *We are testing code that literally doesn't matter.*
* We technically have better "test coverage" with this approach, but our tests aren't actually any more robust. We get a false sense of security.
* We have made the *real* code harder to find by abstracting it behind an interface.
* The fact that `saveUser()` was hard to test was a great signal to us as developers that it needed refactoring. We've silenced a good signal that our code needs to be cleaned up.

{{< cta2 >}}

## Don't test your dependencies, ensure they pass their own tests

Building on the example of the refactored `saveUser()` function from before, we sill have two functions that are likely dependent on third party libraries, namely the `hash()` function and the `saveUserToDB()` function. If we've written our code well, those functions shouldn't do much more than encapsulate a libraries API.

```go
func hash(password string) (string, error) {
	const cost = 10
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), cost)
	return string(bytes), err
}
```

There is no reason I can see to write a test for the `hash` function. Before importing the `bcrypt` library I should have done due diligence and made sure that the maintainers of that codebase have written good tests. Once I'm confident that they had done so, I don't need to redundantly test all that library's exported functions.

## So what do I do, just not test my database layer?

Nope, I think you absolutely *should* test your database layer, I just don't think you should be using *mocks*. Where possible, I think it makes a ton of sense to write automated integration tests for your database logic. The way that you implement the tests will probably depend quite a bit on your tech stack, but let me give you an example of something I'd be happy to see.

You could write a test script that spins up a *very real* instance of your database within a docker container, and executes *your exact queries that will be used in production* in a series of tests. Maybe it:

1. Creates the db schema
2. Inserts a bunch of records
3. Checks that the insertions worked
4. Updates some of the records
5. Makes sure the updates performed as expected
6. Deletes some stuff
7. Makes sure stuff got deleted
8. Tears down the database

When done this way, you're always testing code that actually gets deployed to production. Again, the biggest problem with mocking is that there are execution paths being tested that never are taken in production.

If you have any questions or comments about the article be sure to [contact me on Twitter](https://twitter.com/wagslane) and let me know.
