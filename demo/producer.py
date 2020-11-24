#!/usr/bin/env python3

from time import sleep
from random import randint
from confluent_kafka import Producer

from demo.config import bootstrap_servers, topic

producer = Producer({'bootstrap.servers': bootstrap_servers})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


if __name__ == '__main__':
    i = 0
    print(f'Conectando: {bootstrap_servers}/{topic}')
    while True:
        producer.produce(topic, f'olha o numero {randint(1, 100)}'.encode('utf-8'), callback=delivery_report)
        i += 1
        sleep(2)
