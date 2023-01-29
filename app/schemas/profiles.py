from bson import ObjectId
from typing import Optional
from pydantic import BaseModel, Field
from app.core.database.mongodb import PyObjectId


class SchemaBase(BaseModel):
    file: Optional[str] = {}
    profile: Optional[dict] = {}


class SchemaCreate(SchemaBase):
    pass


class SchemaUpdate(SchemaBase):
    file: Optional[str] = {}
    profile: Optional[dict] = {}

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Schema(SchemaBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        aloow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
