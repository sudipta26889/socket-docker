#!/bin/bash
echo "1. To build enter 'build'. \n2. To run enter 'run' "
read up_or_down
case "$up_or_down" in
    "build")
        docker build -f Dockerfile-Client -t sudipta26889/socket-client .
        ;;
    "run")
        docker run --rm --name client --net socket-net sudipta26889/socket-client
        ;;
    "logs")
        docker logs -f client
        ;;
    "up")
        docker-compose up -d --remove-orphans
        ;;
    "down")
        docker-compose down
        ;;
    *)
        echo "incorrect selection"
esac