---
title: "Writing Good Unit Tests; Don't Mock Database Connections"
author: Lane Wagner
date: "2020-11-23"
categories: 
  - "clean-code"
tags: 
  - "sharing"
images:
  - /img/Writing-Good-Unit-Tests-Dont-Use-Database-Mocking.webp
---

Unit tests are incredibly important to us as developers because they allow us to demonstrate the correctness of the code we've written. More importantly, unit tests allow us to make updates to our code base with confidence that we haven't broken anything. However, in our zeal to achieve 100% code coverage, we often write tests for logic that we may not even want to test. I'm here to assert that creating mock database abstractions to write unit tests is almost always a bad idea.

I work on a lot of RESTful Go API servers, and I do my best to write small testable functions so I don't _have_ to write useless mocking logic. This kind of code pollutes the repository, adds unnecessary abstractions that make the code harder to understand, and does not contribute to the robustness of the test suite.

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

`logPow` is a perfect candidate for a suite of unit tests. It's a mathematical function with predictable outputs for any given inputs. Not all functions we write will be nearly this straightforward to test. However, if we can write small and ideally [pure functions where possible](https://qvault.io/2020/09/07/purity-in-my-programming-please/), writing tests for them becomes much easier.

**Testing shouldn't be hard.** Simple code is easy to test.

## Unit tests shouldn't depend on infrastructure

In web development, it is commonly regarded as good practice (see [Clean Code](https://reflectoring.io/book-review-clean-code/)) to create architectural boundaries at every point of I/O. For example, your database functions with all their `SQL` and driver libraries should be separate from the code that ensures [your user's passwords are secure.](https://github.com/lane-c-wagner/go-password-validator)

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
		INSERT INTO usr (password, email_address, created)                                                                                                                                                                                                                                                                                                                                                                                       
		VALUES ($1, $2, $3);`,
		hashedPassword, user.EmailAddress, time.Now(),
	)
	return err
}
```

There's no way to test this function without having a database connection available at the time of testing. If a new developer clones the project they will need to set up a database or else tests will fail. If you set up continuous integration testing pipelines they will also fail without a dummy database on the server. The point is, this is _bad_.

Developers should be able to clone a repo and immediately run tests that pass.

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

- Validate the user
- Hash the password
- Save the user in the database

We don't need to write a test that tests this function as a whole, we can test the parts we care about independently. Assuming the `saveUserInDB` function is just making a SQL query, it probably doesn't need a unit test at all. If the password hashing algorithm contains any more logic than a simple call to a well-tested crypto library then we can easily write a test for it, otherwise, we can trust the tests in the crypto library. The only test we probably need here is to test our own business logic, the `validateUser` function.

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

The point is, we need to break our large functions into smaller encapsulated units if we want to have an easy time of writing good tests.

## Don't mock your external dependencies either

While the last rule of thumb, "unit tests shouldn't depend on infrastructure" is fairly uncontroversial, this next one is a more fiercely debated topic. I believe that the majority of database and API mocking is a result of bad code, and that to fix the problem, the best course of action is to refactor into smaller functions or "units" as we did a moment ago.

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

With this code, we could now write a unit test that calls the entire `saveUser` function by passing in a `mockDB` so that we don't depend on a running database for tests. As I hope is clear, there are several issues with this approach:

- The mock database code is unused in production. _We are testing code that literally doesn't matter._
- We technically have better "test coverage" with this approach, but our tests aren't actually any more robust. We get a false sense of security.
- We have made the _real_ code harder to find by abstracting it behind an interface.
- The fact that `saveUser` was hard to test was a great signal to us as developers that it needed refactoring. We've silenced a good signal that our code needs to be cleaned up.

## Don't test your dependencies, ensure they pass their own tests

Building on the example of the refactored `saveUser` function before, we sill have two functions that are likely dependent on third party libraries, namely the `hash` function and the `saveUserToDB` function. If we've written our code well, those functions shouldn't do much more than encapsulate a libraries API.

```go
func hash(password string) (string, error) {
	const cost = 10
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), cost)
	return string(bytes), err
}
```

There is no reason I can see to write a test for the `hash` function. Before importing the `bcrypt` library I should have done due diligence and made sure that the maintainers of that codebase have written good tests. Once I'm confident that they had done so, I don't need to redundantly test all the exported functions.

If you have any questions or comments about the article be sure to contact me on social and let me know.
