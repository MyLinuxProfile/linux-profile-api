from fastapi import APIRouter
from app.api.v1.endpoints import profiles


v1 = APIRouter()
v1.include_router(profiles.router, tags=["Profiles"])
