#!/bin/bash
# echo "# Starting Kafka"
# docker run -d --name kfk \
#     --hostname kfk
#     --network arq30net \
#     -e ALLOW_PLAINTEXT_LISTENER=yes \
#     -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
#     -p 9092:9092 \
#     -p 9093:9093 \
#     bitnami/kafka:latest
# echo ""

echo "# Starting Kafka"
docker run --name kfk \
    --hostname kfk
    -e ALLOW_PLAINTEXT_LISTENER=yes \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
    -p 9092:9092 \
    -p 9093:9093 \
    bitnami/kafka:latest
echo ""
