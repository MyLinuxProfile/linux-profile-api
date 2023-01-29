from datetime import datetime
from pydantic import BaseModel


class SchemaSignup(BaseModel):
    username: str
    created_date: datetime


class SchemaLogin(BaseModel):
    access_token: str
    refresh_token: str


class SchemaRefreshToken(BaseModel):
    access_token: str
