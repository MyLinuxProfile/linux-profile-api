from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.auth import Auth
from app.schemas.users import SchemaCreate
from app.models import Users

from sqlalchemy.orm import Session
from app.core.database import get_db

auth = APIRouter()
security = HTTPBearer()
auth_handler = Auth()


@auth.post('/signup')
def signup(user_details: SchemaCreate, db: Session = Depends(get_db)):
    query_user = db.query(Users).filter(
        Users.username==user_details.username).first()

    if query_user != None:
        return 'Account already exists'
    try:
        hashed_password = auth_handler.encode_password(user_details.password)
        user = {'username': user_details.username, 'password': hashed_password}
        db_data = Users(**user)
        db.merge(db_data)
        db.commit()
        return db_data
    except Exception as error:
        print(error)
        error_msg = 'Failed to signup user'
        return error_msg


@auth.post('/login')
def login(user_details: SchemaCreate, db: Session = Depends(get_db)):

    query_user = db.query(Users).filter(
        Users.username==user_details.username).first()

    if (query_user is None):
        return HTTPException(status_code=401, detail='Invalid username')
    if (not auth_handler.verify_password(user_details.password, query_user.password)):
        return HTTPException(status_code=401, detail='Invalid password')
    
    access_token = auth_handler.encode_token(query_user.username)
    refresh_token = auth_handler.encode_refresh_token(query_user.username)
    return {'access_token': access_token, 'refresh_token': refresh_token}


@auth.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}
