from asgiref.sync import sync_to_async

from user.models import UserModel
from user.schemas.user import UserResponseSchema, CreateUserSchema
from user.serializers import CreateUserSerializer, UserSerializer
from fastapi import HTTPException


class UserAPI:

    @classmethod
    async def create(cls, schema: CreateUserSchema):
        serializer = CreateUserSerializer(data=schema.dict())

        is_valid = await sync_to_async(serializer.is_valid)()
        if is_valid:
            user = await sync_to_async(UserModel.objects.create_user)(**schema.dict())
            return UserResponseSchema.model_validate(UserSerializer(user).data)

        raise HTTPException(status_code=400, detail=serializer.errors)

    @classmethod
    def get(cls, current_user: UserModel) -> UserModel:
        return current_user

    @classmethod
    async def get_by_username(cls, username: str):
        return await sync_to_async(UserModel.objects.get)(username=username)
