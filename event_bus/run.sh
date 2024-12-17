#!/usr/bin/env bash
sh stop.sh

docker compose -p assist-hub -f docker-compose.yml up -d
