#!/usr/bin/env python3

from confluent_kafka import Consumer


conf = {
    'bootstrap.servers': 'localhost:9092',
    'auto.offset.reset': 'smallest',
    'group.id': 'little brands'
}

consumer = Consumer(conf)

TOPICS = ['topicarq30']

if __name__ == '__main__':
    consumer.subscribe(TOPICS)
    while True:
        msg = consumer.poll(timeout=1.0)
        print(f'>>> {msg}')
