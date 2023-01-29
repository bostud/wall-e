# wall-e
A fast-fire repeater


# Setup env
1. Install docker, docker-compose
2. Install [protobuf](https://developers.google.com/protocol-buffers/docs/downloads)

# Run App
1. make clear that port **__8899__** is free
2. install Makefile command runner (if needed)

# Commands
- __make build__ - build application
- __make run__ - up initial application
- __make rebuild__ - up & build application with **force-recreate** flag
- __make migrate__ - create initial tables; run after launch application
- __make dev-test__ - run test on dev env


# Docs
Available after start - http://localhost:8899/api/docs
