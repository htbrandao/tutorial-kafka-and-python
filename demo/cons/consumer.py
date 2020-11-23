#!/usr/bin/env python3

from confluent_kafka import Consumer

from demo import bootstrap_servers, topic

conf = {
    'bootstrap.servers': bootstrap_servers,
    'auto.offset.reset': 'smallest',
    'group.id': 'little brands'
}

consumer = Consumer(conf)


if __name__ == '__main__':
    consumer.subscribe([topic])
    while True:
        msg = consumer.poll(timeout=1.0)
        print(f'>>> {msg}')
