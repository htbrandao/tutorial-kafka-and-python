#!/bin/bash
echo "# Console CONSUMER"
docker exec -it kafka-server kafka-console-consumer.sh --from-beginning --bootstrap-server localhost:9092 --topic topicarq30
