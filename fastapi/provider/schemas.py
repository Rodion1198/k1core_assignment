from pydantic import BaseModel


class ProviderSchema(BaseModel):
    id: int
    name: str
