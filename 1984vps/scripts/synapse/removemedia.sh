#!/bin/bash
docker exec -it synapse curl --header "Authorization: Bearer TOKEN" -X POST http://0.0.0.0:8008/_synapse/admin/v1/purge_media_cache?before_ts=TIME-IN-UNIX