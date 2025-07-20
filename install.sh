#!/bin/bash
set -e

# Create virtual environment if not exists
test -d venv || python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "[INFO] Building Docker image..."
docker build -t fastapi-notification-app .
echo "[INFO] Docker image built. Bringing up the container..."
docker rm -f fastapi_notification_container 2>/dev/null || true
docker run -d --name fastapi_notification_container -p 8000:8000 fastapi-notification-app

echo "[INFO] The FastAPI container is running on http://localhost:8000/"
