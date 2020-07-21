from typing import List, Optional
from schemas.item import Item
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserCreate1002(BaseModel):
    loginName: str
    displayName: str
    password: str

    class Config:
        orm_mode = True


class User1002(UserCreate1002):
    id: int


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
