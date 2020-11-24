#!/bin/bash
echo "# Console CONSUMER"
docker exec -it guilda_kafka_python_kafka_1 kafka-console-consumer.sh --from-beginning --bootstrap-server localhost:9092 --topic topicarq30
