#!/bin/bash

# Entrypoint script to handle different configuration modes for UCL server

if [ "$CONFIG_MODE" = "extended" ]; then
    echo "Starting UCL server with extended configuration (tenant_id and auth_token)"
    exec uv run fastn-server.py \
        --api_key "$API_KEY" \
        --space_id "$SPACE_ID" \
        --tenant_id "$TENANT_ID" \
        --auth_token "$AUTH_TOKEN"
else
    echo "Starting UCL server with basic configuration (api_key and space_id)"
    exec uv run fastn-server.py \
        --api_key "$API_KEY" \
        --space_id "$SPACE_ID"
fi