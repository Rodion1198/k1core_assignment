"""ASGI fastapi for fastapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# from app.routers import auth_router, health_router, user_router

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

"""
Settings
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

"""
Django settings
"""
django_app = get_asgi_application()

"""
FastAPI settings
"""

fastapi_app = FastAPI()

# routers
# fastapi_app.include_router(user_router, tags=["users"], prefix="/user")
# fastapi_app.include_router(auth_router, tags=["auth"], prefix="/auth")
# fastapi_app.include_router(health_router, tags=["health"], prefix="/health")

# to mount Django
fastapi_app.mount("/django", django_app)
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
fastapi_app.mount("/media", StaticFiles(directory="media"), name="media")
