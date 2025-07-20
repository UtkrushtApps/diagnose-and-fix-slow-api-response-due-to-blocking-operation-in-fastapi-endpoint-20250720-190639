#!/bin/bash
set -e

bash install.sh

echo "[INFO] Checking FastAPI container logs:"
docker logs fastapi_notification_container --tail 10

echo "[INFO] FastAPI server is READY at http://localhost:8000/"
