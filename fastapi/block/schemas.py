from pydantic import BaseModel

from provider.schemas import ProviderSchema
from datetime import datetime


class CurrencySchema(BaseModel):
    id: int
    name: str


class BlockSchema(BaseModel):
    id: int
    currency: CurrencySchema
    provider: ProviderSchema
    number: int
    created_at: datetime | None
    stored_at: datetime


class ServiceResult(BaseModel):
    block_number: int
    created_at: datetime | None = None
