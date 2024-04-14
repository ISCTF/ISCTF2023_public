#!/bin/sh
docker-compose build
docker run -p 80:80 ezphp:latest