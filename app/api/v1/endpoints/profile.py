from fastapi import APIRouter


router = APIRouter()


@router.get("/profiles")
async def read_profiles():
    """Read Profiles"""
    return ({"status":  True})
