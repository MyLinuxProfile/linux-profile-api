from fastapi import FastAPI, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from mangum import Mangum

from app import __version__
from app.api.auth import auth
from app.api.v1.routers import v1
from app.core.auth import Auth


app = FastAPI(
    title="LinuxProfile API",
    description="Linux Profile Project API",
    version=__version__,
    docs_url=None,
    redoc_url=None)


app.include_router(auth, prefix="/auth", tags=["Auth"])
app.include_router(v1, prefix="/v1")

security = HTTPBearer()
auth_handler = Auth()


@app.get("/status", include_in_schema=False)
def get_status(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Get status of messaging server."""
    token = credentials.credentials
    if(auth_handler.decode_token(token)):
        return ({"status":  "it's alive"})


@app.get("/error", include_in_schema=False)
def get_status(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Get error of messaging server."""
    token = credentials.credentials
    if(auth_handler.decode_token(token)):
        raise


handler = Mangum(app)
