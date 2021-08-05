from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
