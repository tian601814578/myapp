from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
import schemas
from core.tools import get_db

router = APIRouter()


# 路径参数 参数如果被声明类型，传入其他类型的值会报错
# 所有数据校验都是有  Pydantic 完成的
@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
