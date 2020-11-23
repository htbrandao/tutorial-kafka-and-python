#!/usr/bin/env python3

from time import sleep
from random import randint
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
TOPICO = 'topicarq30'


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


if __name__ == '__main__':
    i = 0
    while True:
        producer.poll(0)
        producer.produce(topic=TOPICO,
                         value=f'olha o numero {randint(1, 100)}',
                         callback=delivery_report)
        print('#')
        p.flush()
        i += 1
        sleep(2)
