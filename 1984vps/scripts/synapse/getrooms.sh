#!/bin/bash
docker exec -it synapse curl --header "Authorization: Bearer TOKEN" -X GET http://0.0.0.0:8008/_synapse/admin/v1/rooms