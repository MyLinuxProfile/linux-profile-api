from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    username: str
    password: str


class SchemaCreate(SchemaBase):
    pass


class SchemaPut(SchemaBase):
    username: Optional[str] = None
    password: Optional[str] = None


class Schema(SchemaBase):
    id: str

    class Config:
        orm_mode = True
