#!/bin/bash

docker run -d --name=dev-consul -e CONSUL_BIND_INTERFACE=eth0 -p 8500:8500 consul
docker run -d --name=consul -e CONSUL_BIND_INTERFACE=eth0 --net=srad -p 8500:8500 consul
