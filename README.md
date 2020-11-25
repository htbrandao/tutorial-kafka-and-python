# Apache Kafka and Python

![](.img/kafka.png)
# Kafka

### 1 - Intro

Kafka is a distributed system consisting of servers and clients that communicate via a high-performance TCP network protocol.

Technically speaking, event streaming is the practice of capturing data in real-time from event sources like databases, sensors, mobile devices, cloud services, and software applications in the form of streams of events; storing these event streams durably for later retrieval; manipulating, processing, and reacting to the event streams in real-time as well as retrospectively; and routing the event streams to different destination technologies as needed. Event streaming thus ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time. 

 Kafka combines three key capabilities so you can implement your use cases for event streaming end-to-end with a single battle-tested solution:

    - To publish (write) and subscribe to (read) streams of events, including continuous import/export of your data from other systems.

    - To store streams of events durably and reliably for as long as you want.

    - To process streams of events as they occur or retrospectively.

Servers: Kafka is run as a cluster of one or more server.

Clients: They allow you to write distributed applications and microservices that read, write, and process streams of events in parallel.

Event records the fact that "something happened" in the world or in your business. It is also called record or message in the documentation. When you read or write data to Kafka, you do this in the form of events. Conceptually, an event has a **key**, **value**, **timestamp**, and optional metadata headers. 

**Producers** are those client applications that publish (write) events to Kafka, and **consumers** are those that subscribe to (read and process) these events. In Kafka, producers and consumers are fully decoupled and agnostic of each other. **Events** are organized and durably stored in topics.

Topics have partitions and can be replicated across servers.

# Python lib: confluent-kafka

Confluent develops and maintains confluent-kafka-python, a Python Client for Apache Kafka® that provides a high-level Producer, Consumer and AdminClient compatible with all Kafka brokers >= v0.8, Confluent Cloud and Confluent Platform.

# Putting it all together

Prepare the environment:

`$ docker-compose up`

Create the topics:

`$ ./topics.sh`

Create a console consumer and producer to interact with the topic:

`$ csl_prod.sh`

`$ csl_csm.sh`

Launch the applications

`$ cd demo/`

`$ ./producer.py`

`$ ./consumer.py`

# Referências

- [Apache Kafka](https://kafka.apache.org/documentation/)
- [Kafka Python Client](https://docs.confluent.io/clients-confluent-kafka-python/current/index.html)
