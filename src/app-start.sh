#/bin/bash

./docker-start-consul.sh

sleep 2

./aladdin/docker-start.sh

./gary/docker-start.sh
