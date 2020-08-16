#!/bin/bash
echo "1. To build enter 'build'. \n2. To run enter 'run' "
read choice
case "$choice" in
    "build")
        docker build -f Dockerfile-Server -t sudipta26889/socket-server .
        ;;
    "run")
        docker run -d -p 1234:1234 --rm --name server --net socket-net sudipta26889/socket-server
        ;;
    "logs")
        docker logs -f server
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