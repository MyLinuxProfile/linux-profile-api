from fastapi import FastAPI
from mangum import Mangum

from app import __version__
from app.api.auth import auth
from app.api.v1.routers import v1


app = FastAPI(
    title="LinuxProfile API",
    description="Linux Profile Project API",
    version=__version__,
    docs_url=None,
    redoc_url=None)


app.include_router(auth, prefix="/auth", tags=["Auth"])
app.include_router(v1, prefix="/v1")


@app.get("/status", include_in_schema=False)
def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's alive"})


@app.get("/error", include_in_schema=False)
def get_status():
    """Get error of messaging server."""
    raise


handler = Mangum(app)
