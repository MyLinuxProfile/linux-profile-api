from fastapi import FastAPI
from mangum import Mangum
from app.api.routers import v1


app = FastAPI(
        title="LinuxProfile API",
        description="Linux Profile Project API",
        version="0.0.1"
    )

app.include_router(v1, prefix="/v1")


@app.get("/status", include_in_schema=False)
async def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's alive"})


handler = Mangum(app)
