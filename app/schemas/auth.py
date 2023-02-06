from pydantic import BaseModel, EmailStr, SecretStr


class SchemaSignup(BaseModel):
    email: EmailStr
    password: SecretStr


class SchemaLogin(BaseModel):
    access_token: str
    refresh_token: str


class SchemaRefreshToken(BaseModel):
    access_token: str
