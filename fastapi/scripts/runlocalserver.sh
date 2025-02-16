#!/bin/bash

cleanup() {
    echo "Stopping FastAPI and Django..."
    kill -SIGTERM "$FASTAPI_PID" "$DJANGO_PID"
    wait "$FASTAPI_PID" "$DJANGO_PID"
    echo "Servers stopped."
    exit 0
}

trap cleanup SIGINT SIGTERM

uvicorn config.asgi:fastapi_app --reload --host 0.0.0.0 --port 8000 --log-level debug &
FASTAPI_PID=$!

uvicorn config.asgi:django_app --reload --host 0.0.0.0 --port 8001 --log-level debug &
DJANGO_PID=$!

wait "$FASTAPI_PID" "$DJANGO_PID"
