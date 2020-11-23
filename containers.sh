#!/bin/bash
echo "# Creating network"
docker network create zk_kfk_app --driver bridge &
echo ""

echo "# Remove dangling containers"
docker container rm -f zookeeper-server &
docker container rm -f kafka-server &

echo "# Starting zookeeper"
docker run -d --name zookeeper-server \
    --network zk_kfk_app \
    -e ALLOW_ANONYMOUS_LOGIN=yes \
    bitnami/zookeeper:latest &

echo "# Starting Kafka"
docker run --name kafka-server \
    --network zk_kfk_app \
    -e ALLOW_PLAINTEXT_LISTENER=yes \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
    -p 9092:9092 \
    -p 9093:9093\
    bitnami/kafka:latest &
echo ""

echo "# Creating topic"
docker exec -it kafka-server kafka-topics.sh --create --topic topicarq30 --bootstrap-server localhost:9092 &
echo ""

echo "# Listing existing topics"
docker exec -it kafka-server kafka-topics.sh --list --zookeeper zookeeper-server:2181 &
echo ""
