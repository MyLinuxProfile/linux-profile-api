from fastapi import APIRouter
from app.api.v1.routers import v1

api = APIRouter()
api.include_router(v1, prefix="/v1")
