from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from rest_framework_simplejwt.tokens import AccessToken
from user.models import User
from asgiref.sync import sync_to_async

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Получает текущего пользователя из JWT"""
    print(token)
    try:
        payload = AccessToken(token)
        print(payload)
        user_id = payload["user_id"]
        user = await sync_to_async(User.objects.get)(id=user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
