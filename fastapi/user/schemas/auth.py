from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


class AccessTokenSchema(BaseModel):
    access_token: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str
