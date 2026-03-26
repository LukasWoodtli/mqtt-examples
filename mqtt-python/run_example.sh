#!/usr/bin/sh

docker compose build
docker compose up -d
docker compose logs -f

trap "docker compose down" EXIT KILL INT

