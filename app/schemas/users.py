from typing import Optional
from pydantic import BaseModel, EmailStr, SecretStr


class SchemaBase(BaseModel):
    email: EmailStr
    username: Optional[str] = None
    password: SecretStr


class SchemaCreate(SchemaBase):
    pass


class SchemaUpdate(SchemaBase):
    email: EmailStr
    username: Optional[str] = None
    password: SecretStr


class Schema(SchemaBase):
    id: str

    class Config:
        orm_mode = True
