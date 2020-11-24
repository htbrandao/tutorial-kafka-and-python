#!/bin/bash
echo "# Creating network"
docker network create arq30net --driver bridge
echo ""

# echo "# Starting zookeeper"
# docker run -d --name zk \
#     --hostname zk
#     --network arq30net \
#     -e ALLOW_ANONYMOUS_LOGIN=yes \
#     bitnami/zookeeper:latest

echo "# Starting zookeeper"
docker run --name zk \
    --hostname zk
    -e ALLOW_ANONYMOUS_LOGIN=yes \
    bitnami/zookeeper:latest
