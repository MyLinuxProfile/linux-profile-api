from fastapi import status, Depends, Security, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.auth import Auth
from app.core.controller import ControllerUsers
from app.core.database.mysql import get_mysql


security = HTTPBearer()
auth_handler = Auth()


async def authorization(
        mysql: Session = Depends(get_mysql),
        credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if not auth_handler.decode_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return ControllerUsers(db=mysql).read(id=auth_handler.decode_token(token))
