#!/usr/bin/env python3

from time import sleep
from random import randint

from confluent_kafka import Producer

# from demo.config import bootstrap_servers, topic
bootstrap_servers = "localhost:9092"
topic = 'topicarq30'

producer = Producer({'bootstrap.servers': bootstrap_servers})


if __name__ == '__main__':
    i = 0
    print(f'# Conectando: {bootstrap_servers}/{topic}')
    while True:
        try:
            producer.produce(topic, f'NUMERO {randint(1, 100)**2}')
            i += 1
            sleep(0.5)
        except KeyboardInterrupt:
            break
