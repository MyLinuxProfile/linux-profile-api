from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from app.core.database.mongodb import get_mongodb
from app.core.database.mysql import get_mysql
from app.core.security import authorization
from app.core.controller import ControllerSyncs
from app.schemas.profiles import Schema, SchemaBase


router = APIRouter()


@router.post("/profiles", response_model=SchemaBase, status_code=201)
async def create(
    profile: Schema,
    mongodb = Depends(get_mongodb),
    mysql = Depends(get_mysql),
    user = Depends(authorization)):

    profile = jsonable_encoder(profile)
    user_id = user.id

    sync = ControllerSyncs(db=mysql).read(
        file=profile.get("file"),
        user_id=user_id)

    if sync:
        profile.pop("_id")
        await mongodb.update_one({"_id": sync.profile_id}, {"$set": profile})
    else:
        await mongodb.insert_one(profile)
        ControllerSyncs(db=mysql).create(
            data=dict(
                file=profile.get("file"),
                profile_id=profile.get("_id"),
                user_id=user_id))

    return profile
