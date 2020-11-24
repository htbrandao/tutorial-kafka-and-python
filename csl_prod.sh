#!/bin/bash
echo "# Console PRODUCER"
docker exec -it guilda_kafka_python_kafka_1 kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topicarq30
