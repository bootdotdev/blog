---
title: "Using a Low-Level RabbitMQ Client in Golang"
date: "2020-04-29"
categories: 
  - "golang"
  - "open-source"
---

[RabbitMQ](https://www.rabbitmq.com/features.html) is a great message broker with awesome Golang support. It's a great pub-sub system, and pub-sub has become a staple communication architecture in micro-services. At my current day job, we use RabbitMQ to push hundreds of millions of social media posts through our Go services daily.

In this post, we're going to go over how to implement the low-level open-source [amqp](https://godoc.org/github.com/streadway/amqp) package. If instead, you want a higher-level abstraction that provides reasonable defaults, queue boilerplate, and automatic reconnections, check out my new post, [Using a High-Level RabbitMQ Client in Golang](https://qvault.io/2021/03/10/connecting-to-rabbitmq-in-golang-easy/).

## Brief Overview On Rabbit

The two main entities to be aware of with Rabbit are `routing keys` and `queues`. A service publishes a message (JSON in our case) to a routing key. RabbitMQ then _copies_ that message into each queue that's subscribed to that routing key.

![](images/exchanges-bidings-routing-keys.png)

The subscribing service (the consumer) can pull messages off of a queue one at a time. It's worthwhile to note that a queue can also receive messages from multiple routing keys, but we won't be diving into that here.

## Connecting With Go

First things first, there's no reason to reinvent the wheel. We'll use the [amqp](https://godoc.org/github.com/streadway/amqp) package provided by streadway to handle the nitty-gritty of the connection details.

In most of my projects, I build a small rabbit package in the [internal folder of the project](https://qvault.io/2020/03/29/how-to-separate-library-packages-in-go/). It exposes only the rabbit functionality that our project cares about.

```
// Conn -
type Conn struct {
	Channel *amqp.Channel
}

// GetConn -
func GetConn(rabbitURL string) (Conn, error) {
	conn, err := amqp.Dial(rabbitURL)
	if err != nil {
		return Conn{}, err
	}

	ch, err := conn.Channel()
	return Conn{
		Channel: ch,
	}, err
}
```

The `Conn` struct just holds a connection to the RabbitMQ server. We'll also expose a method to get a new connection using just a [connection URI](https://www.rabbitmq.com/uri-spec.html). For example, `amqp://username:password@localhost`.

## Publishing

Publishing is easy and is thread-safe out-of-the-box. We just need to expose one more function that publishes using the connection. The calling code provides a routing key and a payload.

```
// Publish -
func (conn Conn) Publish(routingKey string, data []byte) error {
	return conn.Channel.Publish(
		// exchange - yours may be different
		"events",
		routingKey,
		// mandatory - we don't care if there I no queue
		false,
		// immediate - we don't care if there is no consumer on the queue
		false,
		amqp.Publishing{
			ContentType:  "application/json",
			Body:         data,
			DeliveryMode: amqp.Persistent,
		})
}
```

The purpose of this small internal package is to set some defaults for the more powerful AMQP package and control which functionality is exposed to our app. For example, if we know that our app will always use the `events` exchange and we want the `mandatory` or `immediate` flags set we can just do so here.

## Consuming

Consuming is a bit trickier than publishing. We'll use a simple pattern here where we have the app supply a handler function, a queue, the routing key that the queue binds to, and the maximum number of goroutines we should spin up to handle messaegs.

```
// StartConsumer -
func (conn Conn) StartConsumer(
	queueName,
	routingKey string,
	handler func(d amqp.Delivery) bool,
	concurrency int) error {

	// create the queue if it doesn't already exist
	_, err := conn.Channel.QueueDeclare(queueName, true, false, false, false, nil)
	if err != nil {
		return err
	}

	// bind the queue to the routing key
	err = conn.Channel.QueueBind(queueName, routingKey, "events", false, nil)
	if err != nil {
		return err
	}

	// prefetch 4x as many messages as we can handle at once
	prefetchCount := concurrency * 4
	err = conn.Channel.Qos(prefetchCount, 0, false)
	if err != nil {
		return err
	}

	msgs, err := conn.Channel.Consume(
		queueName, // queue
		"",        // consumer
		false,     // auto-ack
		false,     // exclusive
		false,     // no-local
		false,     // no-wait
		nil,       // args
	)
	if err != nil {
		return err
	}

	// create a goroutine for the number of concurrent threads requested
	for i := 0; i < concurrency; i++ {
		fmt.Printf("Processing messages on thread %v...\n", i)
		go func() {
			for msg := range msgs {
				// if tha handler returns true then ACK, else NACK
				// the message back into the rabbit queue for
				// another round of processing
				if handler(msg) {
					msg.Ack(false)
				} else {
					msg.Nack(false, true)
				}
			}
			fmt.Println("Rabbit consumer closed - critical Error")
			os.Exit(1)
		}()
	}
	return nil
}
```

If you're concerned with speed then don't be afraid to run with a concurrency of at least 100, depending on how computationally and memory intensive your handler is. Assuming your handler is written in a thread-safe way, this is a good way to ensure that your app uses all of its available CPU without being bottlenecked by I/O.

If your app's handler is very fast (perhaps no network or disk involved) you may need to change the `prefetch` multiplier from 4 to something higher. The prefetch count tells the Rabbit connection how many messages to retrieve from the server per request. The higher the number, the less time waiting on network calls for each message.

Most of the programs I work on are ephemeral - I don't mind if they just restart from time to time when bad things happen. For this reason, if the rabbit consumer fails for any reason I just call the `os.Exit(1)` command. My logs pick it up and we just restart the program. If this doesn't work for your use case you may want to handle that more elegantly.

## Testing The Package

```
func main() {
	conn, err := rabbit.GetConn("amqp://guest:guest@localhost")
	if err != nil {
		panic(err)
	}

	go func() {
		for {
			time.Sleep(time.Second)
			conn.Publish("test-key", []byte(`{"message":"test"}`))
		}
	}()

	err = conn.StartConsumer("test-queue", "test-key", handler, 2)

	if err != nil {
		panic(err)
	}

	forever := make(chan bool)
	<-forever
}

func handler(d amqp.Delivery) bool {
	if d.Body == nil {
		fmt.Println("Error, no message body!")
		return false
	}
	fmt.Println(string(d.Body))
	return true
}
```

## Related Reading

- [The Proper Use of Pointers in Go (golang)](https://qvault.io/2019/09/25/the-proper-use-of-pointers-in-go-golang/)
- [How to: Global Constant Maps and Slices in Go](https://qvault.io/2019/10/21/how-to-global-constant-maps-and-slices-in-go/)
- [Top 10 Golang Technical Interview Questions](https://qvault.io/2020/08/31/top-10-technical-go-interview-questions/)
