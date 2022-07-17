from datetime import datetime
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    # Request Validation
    pass


class PostResponse(PostBase):
    # Response Validation
    id: int
    created_at: datetime

    class Config:
        # tells pydantic to convert sqlalchemy model for response
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        # tells pydantic to convert sqlalchemy model for response
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # Data embedded in to access token
    id: str | None = None
