#!/usr/bin/env python3

from confluent_kafka import Consumer

from demo.config import bootstrap_servers, topic


conf = {
    'bootstrap.servers': bootstrap_servers,
    'auto.offset.reset': 'smallest',
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
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print('Received message: {}'.format(msg.value().decode('utf-8')))
