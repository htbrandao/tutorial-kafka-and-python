#!/bin/bash
echo "# Creating topic"
docker exec -it kfk kafka-topics.sh --create --topic topicarq30 --bootstrap-server localhost:9092
echo ""

echo "# Listing existing topics"
docker exec -it kfk kafka-topics.sh --list --zookeeper zk:2181
echo ""
