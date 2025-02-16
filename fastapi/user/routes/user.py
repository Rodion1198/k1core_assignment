from fastapi import APIRouter, Depends

from user.api.user import UserAPI
from user.dependencies.auth import get_current_user
from user.models import UserModel
from user.schemas.user import CreateUserSchema, UserResponseSchema

router = APIRouter()


@router.post("/create", response_model=UserResponseSchema)
async def create_user(
        schema: CreateUserSchema
):
    return await UserAPI.create(schema=schema)


@router.get("/", response_model=UserResponseSchema)
async def get_user(
        current_user: UserModel = Depends(get_current_user)
):
    return UserAPI.get(current_user=current_user)
