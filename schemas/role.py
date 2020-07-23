from typing import List, Optional
from schemas.item import Item
from pydantic import BaseModel


class CreateRole(BaseModel):
    name: str

    class Config:
        orm_mode = True



class Role(CreateRole):
    id: int
