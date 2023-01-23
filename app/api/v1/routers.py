from fastapi import APIRouter
from app.api.v1.endpoints import profile


v1 = APIRouter()
v1.include_router(profile.router, tags=["Profiles"])
