from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    email: Optional[str] = None
    username: str
    password: str


class SchemaCreate(SchemaBase):
    pass


class SchemaUpdate(SchemaBase):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class Schema(SchemaBase):
    id: str

    class Config:
        orm_mode = True
