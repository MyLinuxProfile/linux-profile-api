from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.auth import Auth
from app.core.controller import ControllerUsers
from app.schemas.users import SchemaCreate

from sqlalchemy.orm import Session
from app.core.database import get_db


auth = APIRouter()
security = HTTPBearer()
auth_handler = Auth()


@auth.post('/signup')
def signup(user: SchemaCreate, db: Session = Depends(get_db)):
    query_user = ControllerUsers(db=db).read(username=user.username)

    if query_user:
        return 'Account already exists'
    else:
        hashed_password = auth_handler.encode_password(user.password)
        return ControllerUsers(db=db).create(
            data={
                "username": user.username,
                "password": hashed_password})


@auth.post('/login')
def login(user: SchemaCreate, db: Session = Depends(get_db)):
    query_user = ControllerUsers(db=db).read(username=user.username)

    if (query_user is None):
        return HTTPException(status_code=401, detail='Invalid username')
    if (not auth_handler.verify_password(user.password, query_user.password)):
        return HTTPException(status_code=401, detail='Invalid password')
    
    access_token = auth_handler.encode_token(query_user.username)
    refresh_token = auth_handler.encode_refresh_token(query_user.username)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token}


@auth.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)

    return {"access_token": new_token}
