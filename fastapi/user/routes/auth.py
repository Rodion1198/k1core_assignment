from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from user.api.auth import AuthAPI
from user.schemas.auth import TokenSchema, AccessTokenSchema, RefreshTokenSchema

router = APIRouter()


@router.post("/login", response_model=TokenSchema)
async def login_user(
        form_data: OAuth2PasswordRequestForm = Depends()
):
    return await AuthAPI.login(form_data)


@router.post("/token/refresh", response_model=AccessTokenSchema)
async def refresh_access_token(
        refresh_data: RefreshTokenSchema
):
    return await AuthAPI.refresh_token(refresh_data.refresh_token)
