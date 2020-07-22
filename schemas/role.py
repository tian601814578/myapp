from typing import List, Optional
from schemas.item import Item
from pydantic import BaseModel


class Role(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

