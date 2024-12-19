#!/usr/bin/env bash
sh stop.sh
docker compose -p assist-hub pull
docker compose -p assist-hub up -d
