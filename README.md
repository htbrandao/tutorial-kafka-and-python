$ docker network create zk_kfk_app --driver bridge

$ docker container rm -f zookeeper-server

$ docker run -d --name zookeeper-server \
    --network zk_kfk_app \
    -e ALLOW_ANONYMOUS_LOGIN=yes \
    bitnami/zookeeper:latest

$ docker container rm -f kafka-server

$ docker run --name kafka-server \
    --network zk_kfk_app \
    -e ALLOW_PLAINTEXT_LISTENER=yes \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
    -p 9092:9092 \
    -p 9093:9093\
    bitnami/kafka:latest

$ docker exec -it kafka-server kafka-topics.sh --create --topic topicarq30 --bootstrap-server localhost:9092

$ docker exec -it kafka-server kafka-topics.sh --list --zookeeper zookeeper-server:2181

$ docker exec -it kafka-server kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topicarq30

$ docker exec -it kafka-server kafka-console-consumer.sh --from-beginning --bootstrap-server localhost:9092 --topic topicarq30

