# Dockerfile for docker-logs

# BUILD-USING:        docker build -t docker-logs .
# RUN-USING:          docker run -d -v /updatedns-logs --name updatedns-logs docker-logs
# INSPECT-USING:      docker run -t -i  --volumes-from updatedns-logs ubuntu:latest /bin/bash

FROM stackbrew/busybox:latest

# Create logs volume
VOLUME /var/log

CMD  ["true"]

