#!/bin/bash
echo "# Remove previous content"
docker network rm arq30net
docker container rm -f kfk
docker container rm -f zk
