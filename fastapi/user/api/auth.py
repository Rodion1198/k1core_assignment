from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from django.contrib.auth import authenticate
from asgiref.sync import sync_to_async
from rest_framework_simplejwt.tokens import RefreshToken

from user.exceptions import UserNotFoundOrInactiveException, InValidCredentialsException
from user.models import UserModel


def create_jwt_tokens(
        user: UserModel
) -> dict:
    refresh = RefreshToken.for_user(user)
    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
        "token_type": "Bearer"
    }


class AuthAPI:

    async def _authenticate_user(self, username: str, password: str) -> dict | None:
        user = await sync_to_async(authenticate)(username=username, password=password)
        if not user:
            return None
        return create_jwt_tokens(user)

    @classmethod
    async def login(
            cls,
            form_data: OAuth2PasswordRequestForm = Depends()
    ):
        token = await cls()._authenticate_user(form_data.username, form_data.password)
        if not token:
            raise InValidCredentialsException()
        return token

    @classmethod
    async def refresh_token(
            cls,
            refresh_token: str
    ):
        try:
            refresh = RefreshToken(refresh_token)
            user = await sync_to_async(UserModel.objects.filter(id=refresh["user_id"]).first)()

            if not user or not user.is_active:
                raise UserNotFoundOrInactiveException()

            new_access = refresh.access_token
            return {"access_token": str(new_access)}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
