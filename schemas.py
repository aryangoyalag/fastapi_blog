from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class User(UserBase):
    password: str

    class Config:
        orm_mode = True

class ShowUser(UserBase):
    blogs: List[Blog] = []

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser] = None  # Make sure to initialize Optional fields

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
