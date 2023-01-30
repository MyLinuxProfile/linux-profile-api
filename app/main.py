import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from fastapi import FastAPI, Depends
from mangum import Mangum

from app import __version__
from app.api.auth import auth
from app.api.v1.routers import v1

from app.core.settings import set_up
from app.core.security import authorization


config = set_up()
sentry_sdk.init(
    dsn=config.get("SENTRY_DSN"),
    integrations=[
        AwsLambdaIntegration(timeout_warning=True),
    ],
    traces_sample_rate=1.0,
)


app = FastAPI(
    title="LinuxProfile API",
    description="Linux Profile Project API",
    version=__version__,
    docs_url=None,
    redoc_url=None)


app.include_router(auth, prefix="/auth")
app.include_router(v1, prefix="/v1")


@app.get("/status", include_in_schema=False)
def get_status(user=Depends(authorization)):
    """Get status of messaging server."""
    return ({"status": "it's alive"})


@app.get("/error", include_in_schema=False)
def get_error(user=Depends(authorization)):
    """Get error of messaging server."""
    raise


handler = Mangum(app)
