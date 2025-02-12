#!/bin/bash

# Функция для остановки обоих процессов
cleanup() {
    echo "Stopping FastAPI and Django..."
    kill -SIGTERM "$FASTAPI_PID" "$DJANGO_PID"
    wait "$FASTAPI_PID" "$DJANGO_PID"
    echo "Servers stopped."
    exit 0
}

# Перехватываем SIGINT (Ctrl+C) и SIGTERM (docker stop)
trap cleanup SIGINT SIGTERM

# Запускаем FastAPI на 8000
uvicorn config.asgi:fastapi_app --reload --host 0.0.0.0 --port 8000 --log-level debug &
FASTAPI_PID=$!

# Запускаем Django на 8001
uvicorn config.asgi:django_app --reload --host 0.0.0.0 --port 8001 --log-level debug &
DJANGO_PID=$!

# Ждём завершения процессов
wait "$FASTAPI_PID" "$DJANGO_PID"
