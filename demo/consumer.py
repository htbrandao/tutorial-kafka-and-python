#!/usr/bin/env python3

from math import sqrt

from confluent_kafka import Consumer

# from demo.config import bootstrap_servers, topic
bootstrap_servers = "localhost:9092"
topic = 'topicarq30'


conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'little brands'
}

consumer = Consumer(conf)


if __name__ == '__main__':
    print(f'Conectando: {bootstrap_servers}/{topic}')
    consumer.subscribe([topic])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        elif msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        else:
            r = msg.value().decode('utf-8')
            r = sqrt(int(r.replace(r'NUMERO ', '')))
            print(f'A RAIZ É {r}')
