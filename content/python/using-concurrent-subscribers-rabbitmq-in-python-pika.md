---
title: "Using Concurrent Subscribers With RabbitMQ in Python (pika)"
author: Lane Wagner
date: "2020-05-26"
categories: 
  - "open-source"
  - "python"
images:
  - /img/800/2E2B1BD900000578-0-image-a-19_1446807445687.webp
---

It's a fairly common scenario to subscribe to a Rabbit queue and process messages before acknowledging receipt. The [pika package](https://pypi.org/project/pika/) for dealing with RabbitMQ in Python however is only single-threaded out of the box. If we want to make a network or database call before each acknowledgment our subscribers can get _really_ slow.

Waiting on i/o for each message means **we likely can't process more than a message or two per second.** That's often not good enough. Read further to find out how to easily process each RabbitMQ message using different threads with the Python pika library.

## Let's Get To It

We will be using Python 3 for the following examples. You will also need to install pika via Pip.

```
pip3 install pika
```

Let's start by specifying some configurations we will need:

```bash
# some configuration variables
RABBIT_URL = 'amqp://username:password@localhost'
ROUTING_KEY = 'routing_key'
QUEUE_NAME = 'my_queue.' + ROUTING_KEY
EXCHANGE = 'exchange_name'
THREADS = 5
```

RABBIT\_URL is the connection string to the rabbit cluster. ROUTING\_KEY is the name of the [routing key](https://www.rabbitmq.com/tutorials/tutorial-four-python.html) we want our queue to receive messages from. QUEUE\_NAME is the name of the **queue** we want to create and bind to. EXCHANGE is the name of the [exchange](https://www.rabbitmq.com/tutorials/amqp-concepts.html) we are using. THREADS is the number of threads we want to spawn to process messages.

Next let's import all the packages we will be using:

```py
import json
import pika
import time
import threading
```

The messages we consume will be in JSON format so we need a parser. Pika is the package to interact with RabbitMQ. We will use _time.sleep()_ to simulate i/o operations to ensure our concurrency is performing as expected. Lastly, the [threading](https://docs.python.org/3/library/threading.html) package allows us to spawn threads.

  
To make use of the threading package, let's subclass the Thread class:

```py
class ThreadedConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        parameters = pika.URLParameters(RABBIT_URL)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()
        self.channel.queue_declare(queue=QUEUE_NAME, auto_delete=False)
        self.channel.queue_bind(queue=QUEUE_NAME, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS*10)
        self.channel.basic_consume(QUEUE_NAME, on_message_callback=self.callback)
        threading.Thread(target=self.channel.basic_consume(QUEUE_NAME, on_message_callback=self.callback))

    def callback(self, channel, method, properties, body):
        message = json.loads(body)
        time.sleep(5)
        print(message)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        
    def run(self):
        print ('starting thread to consume from rabbit...')
        self.channel.start_consuming()
```

The constructor will create an entirely new connection to Rabbit because pika is **not** thread safe. Each message will be handled by _callback()_ where we will sleep for 5 seconds and print the message.

## Putting It All Together

```py
#!/usr/bin/env python3

import json
import pika
import time
import threading

RABBIT_URL = 'amqp://username:pass@hostname'
ROUTING_KEY = 'throttle.compact_social_activity.throttled'
QUEUE_NAME = 'test.' + ROUTING_KEY
EXCHANGE = 'events'
THREADS = 5

class ThreadedConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        parameters = pika.URLParameters(RABBIT_URL)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()
        self.channel.queue_declare(queue=QUEUE_NAME, auto_delete=False)
        self.channel.queue_bind(queue=QUEUE_NAME, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS*10)
        self.channel.basic_consume(QUEUE_NAME, on_message_callback=self.callback)
        threading.Thread(target=self.channel.basic_consume(QUEUE_NAME, on_message_callback=self.callback))
        
    def callback(self, channel, method, properties, body):
        message = json.loads(body)
        time.sleep(5)
        print(message)
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        print ('starting thread to consume from rabbit...')
        self.channel.start_consuming()

def main():
    for i in range(THREADS):
        print ('launch thread', i)
        td = ThreadedConsumer()
        td.start()

main()
```

Assuming that all of our configuration variables are correct (we are connected to the right cluster and there are messages being published to the routing key), we should see each thread start and messages consumed and printed to the console.

We can know that the concurrency is helping with performance because (again, assuming that messages are coming into the routing key fast enough) we should see messages printed more often than once every 5 seconds.
