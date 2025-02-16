from fastapi import APIRouter, Query, Path, Depends

from block.api.block import BlockAPI
from block.schemas import BlockSchema

from user.dependencies.auth import get_current_user

router = APIRouter()


@router.get("/blocks", response_model=list[BlockSchema])
async def get_blocks(
        currency: str | None = Query(None, description="Filter by currency (BTC, ETH)"),
        provider: str | None = Query(None, description="Filter by provider"),
        page: int = Query(1, description="Page number"),
        page_size: int = Query(10, description="Page size"),
        user=Depends(get_current_user),
):
    return await BlockAPI.get_blocks(currency, provider, page, page_size)


@router.get("/{currency}/{number}", response_model=BlockSchema)
async def get_block_by_currency_and_number(
        currency: str = Path(..., description="Currency name (BTC, ETH)"),
        number: int = Path(..., description="Block number"),
        # user=Depends(get_current_user),
):
    return await BlockAPI.get_block_by_currency_and_number(currency, number)


@router.get("/{block_id}", response_model=BlockSchema)
async def get_block_by_id(
        block_id: int = Path(..., description="Block ID"),
        # user=Depends(get_current_user),
):
    return await BlockAPI.get_block_by_id(block_id)
