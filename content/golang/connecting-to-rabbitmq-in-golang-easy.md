---
title: "Using a High-Level RabbitMQ Client in Golang"
author: lane
date: "2021-03-10"
categories:
  - "golang"
  - "open-source"
images:
  - /img/800/ruinreborn_fantasy_art_simple_background_fantasy_rabbit_--ar__3debb245-0296-4bb5-8738-261f7d793f8d_1.png.webp
aliases:
  - /golang/connecting-to-rabbitmq-in-golang/
---

So you might already know that the [amqp package](https://github.com/streadway/amqp) is awesome and you can get up and running with just 40-50 lines of simple code. Unfortunately, the bare-bones amqp library doesn't handle a lot of the stuff you probably wish it did, things like reconnecting logic, the spawning of threads, queue and binding boilerplate, and flow control.

Fear not! I recently open-sourced my own package that neatly wraps Streadway's amqp library and provides those higher-level abstractions. Behold, [go-rabbitmq](https://github.com/wagslane/go-rabbitmq).

My main goals when building this new package were the following:

- Automatic reconnection handling. The amqp lib doesn't handle when a Node goes down.
- The spawning of concurrent goroutines to consume from a queue - there's no reason for everyone to have to write those same 20 lines of code in each app they build.
- Reasonable defaults, but total control. Using go-rabbitmq, you still get practically all of the control you had at the amqp level, but defaults are provided that will reduce the amount of boilerplate code you need in your application logic.
- Flow control. The AMQP library just provides a channel that tells you when publishers _should_ stop. The go-rabbitmq library actually returns an error when publishing to a server that has requested the client to stop publishing.

## Examples

The [go-rabbitmq](https://github.com/wagslane/go-rabbitmq) library provides two types that will hold all your configurations for publishing and consuming messages, a [Publisher](https://pkg.go.dev/github.com/wagslane/go-rabbitmq?utm_source=godoc#Publisher) and a [Consumer](https://pkg.go.dev/github.com/wagslane/go-rabbitmq?utm_source=godoc#Consumer).

### Consuming with the defaults

```go
consumer, err := rabbitmq.NewConsumer("amqp://user:pass@localhost")
if err != nil {
    log.Fatal(err)
}
err = consumer.StartConsuming(
    func(d rabbitmq.Delivery) bool {
        log.Printf("consumed: %v", string(d.Body))
        // true to ACK, false to NACK
        return true
    },
    "my_queue",
    []string{"routing_key1", "routing_key2"}
)
if err != nil {
    log.Fatal(err)
}
```

The code above does the following:

1. Creates a new Consumer connected to the provided cluster
2. Creates the `my_queue` queue if it doesn't exist and binds `routing_key1` and `routing_key2` to it.
3. Starts consuming messages on a single thread using the provided handler. We provided a handler that prints the message and ACKs it off the queue.
4. If the app loses connection to the cluster or a node goes down, the client will continuously try to reconnect with an exponential backoff strategy.

### Publishing with the defaults

```go
publisher, returns, err := rabbitmq.NewPublisher("amqp://user:pass@localhost")
if err != nil {
    log.Fatal(err)
}
err = publisher.Publish([]byte("hello, world"), []string{"routing_key"})
if err != nil {
    log.Fatal(err)
}
```

The code above does the following:

1. Creates a publisher connected to the provided cluster
2. Creates a `returns` channel that will send messages back when the server rejects a publish. Note that this happens when specific options (mandatory and immediate) are used. If the cluster goes down or a connection is lost, publishing will fail until the publisher reconnects, which it does automatically.
3. Publish the bytes of the text "hello, world" to the `routing_key` routing key.

## Consuming Options

The full suite of [consuming options](https://pkg.go.dev/github.com/wagslane/go-rabbitmq?utm_source=godoc#ConsumeOptions) is quite large, I didn't want to limit functionality:

```go
type ConsumeOptions struct {
    QueueDurable      bool
    QueueAutoDelete   bool
    QueueExclusive    bool
    QueueNoWait       bool
    QueueArgs         Table
    BindingExchange   string
    BindingNoWait     bool
    BindingArgs       Table
    Concurrency       int
    QOSPrefetch       int
    QOSGlobal         bool
    ConsumerName      string
    ConsumerAutoAck   bool
    ConsumerExclusive bool
    ConsumerNoWait    bool
    ConsumerNoLocal   bool
    ConsumerArgs      Table
}

type Table map[string]interface{}
```

Most of the options are fairly self-explanatory if you look into the feature set of RabbitMQ. For example, durable queues aren't lost on server restart, exclusive queues can't be used by more than one connection, auto-delete queues are deleted when they have no consumers, etc. Let's go over how to set some of the more advanced configurations.

```go
err = consumer.StartConsuming(
    func(d rabbitmq.Delivery) rabbitmq.Action {
        log.Printf("consumed: %v", string(d.Body))
        return rabbitmq.Ack
    },
    "my_queue",
    []string{"routing_key1", "routing_key2"},
    rabbitmq.WithConsumeOptionsQueueDurable,
    rabbitmq.WithConsumeOptionsConcurrency(10),
    rabbitmq.WithConsumeOptionsQOSPrefetch(100),
)
```

There are some out-of-the-box configuration function (using Go's variadic feature) that will mutate a pointer to the configuration struct the way we want. In the above code, we made our queue durable, we tell the consumer we want ten threads running their own handler, and we want the server to send us batches of 100 messages at a time (this just helps with throughput, each handler still only processes a single message at once).

You can also build your own custom function:

```go
err = consumer.StartConsuming(
     func(d rabbitmq.Delivery) bool {
        log.Printf("consumed: %v", string(d.Body))
        return true
     },
    "my_queue",
    []string{"routing_key1", "routing_key2"},
    func(opts *rabbitmq.ConsumeOptions) {
        opts.QueueDurable = true
        opts.Concurrency = 10
        opts.QOSPrefetch = 100
    },
)
```

## Publishing options

Frankly, I'm not a huge fan of the mandatory and immediate options. To me, it seems like it breaks a simple tenet of the pub/sub architecture, that is, publishers should be unaware of their consumers. It should be up to the consumers to make sure they're correctly connected and their queues are created. That said, you can still use those options:

```go
err = publisher.Publish(
    []byte("hello, world"),
    []string{"routing_key"},
    // leave blank for defaults
    rabbitmq.WithPublishOptionsContentType("application/json"),
    rabbitmq.WithPublishOptionsMandatory,
    rabbitmq.WithPublishOptionsPersistentDelivery,
)
```

If you have any questions about the library or suggestions for improvement please open an issue on the GitHub project and let's talk about it!

## A note on stability

I plan to keep the library in v0 until I'm super sure I'm happy with the API. So be aware there may be very small breaking changes before v1.
