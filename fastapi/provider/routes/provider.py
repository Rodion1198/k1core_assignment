from fastapi import APIRouter, Depends

from provider.api.provider import ProviderAPI
from provider.schemas import ProviderSchema
from user.dependencies.auth import get_current_user
from user.models import UserModel

router = APIRouter()


@router.get("/providers", response_model=list[ProviderSchema])
async def get_providers(
        current_user: UserModel = Depends(get_current_user)
):
    return await ProviderAPI.get_all()
