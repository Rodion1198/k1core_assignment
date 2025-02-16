"""ASGI fastapi for fastapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django_app = get_asgi_application()


from user.routes.user import router as user_router
from user.routes.auth import router as auth_router
from provider.routes.provider import router as provider_router
from block.routes.block import router as block_router

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

fastapi_app = FastAPI()

# routers
api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(user_router, prefix="/user", tags=["user"])
api_v1_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(provider_router, prefix="/provider", tags=["provider"])
api_v1_router.include_router(block_router, prefix="/block", tags=["block"])

fastapi_app.include_router(api_v1_router)

# to mount Django
fastapi_app.mount("/django", django_app)
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")


@fastapi_app.get("/health", tags=["health check"])
async def health_check():
    return {"message": "FastAPI + Django works fine!"}
