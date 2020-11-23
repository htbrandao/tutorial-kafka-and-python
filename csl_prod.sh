#!/bin/bash
echo "# Console PRODUCER"
docker exec -it kafka-server kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topicarq30
