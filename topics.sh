#!/bin/bash
echo "# Creating topic"
docker exec -it guilda_kafka_python_kafka_1 kafka-topics.sh --create --topic topicarq30 --bootstrap-server guilda_kafka_python_kafka_1:9092
echo ""

echo "# Listing existing topics"
docker exec -it guilda_kafka_python_kafka_1 kafka-topics.sh --list --zookeeper guilda_kafka_python_zookeeper_1:2181
echo ""
