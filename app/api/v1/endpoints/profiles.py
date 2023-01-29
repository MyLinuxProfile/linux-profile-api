from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.core.database.mongodb import get_mongodb
from app.core.database.mysql import get_mysql
from app.core.security import authorization
from app.core.controller import ControllerSyncs
from app.schemas.profiles import Schema


router = APIRouter()


@router.post("/profiles")
async def create(
    profile: Schema,
    mongodb = Depends(get_mongodb),
    mysql = Depends(get_mysql),
    user = Depends(authorization)):
    profile = jsonable_encoder(profile)

    sync = ControllerSyncs(
        db=mysql).read(
            user_id=user.id,
            file=profile.get("file"))

    if sync:
        profile.pop("_id")
        await mongodb["profiles"].update_one({"_id": sync.profile_id}, {"$set": profile})
    else:
        new_profile = await mongodb["profiles"].insert_one(profile)
        ControllerSyncs(db=mysql).create(
            data={
                "file": profile.get("file"),
                "user_id": user.id,
                "profile_id": new_profile.inserted_id})

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=profile)
