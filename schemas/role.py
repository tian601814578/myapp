from typing import List, Optional
from pydantic import BaseModel


class CreateRoleCategory(BaseModel):
    name: str
    parent: Optional[str] = None

    class Config:
        orm_mode = True


class RoleCategory(CreateRoleCategory):
    id: int


class CreateRole(BaseModel):
    name: str
    rolecategory_id: int

    class Config:
        orm_mode = True


class Role(CreateRole):
    id: int
