#!/bin/bash

docker run --name gary --net=host -d anton31kah/gary
docker run -d --name service2 -p 8020:8020 --net=srad anton31kah/service2

