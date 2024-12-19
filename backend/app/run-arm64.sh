#!/usr/bin/env bash
docker network create assist-hub
sh stop.sh
docker compose -p assist-hub -f docker-compose-arm64.yml pull
docker compose -p assist-hub -f docker-compose-arm64.yml up -d
