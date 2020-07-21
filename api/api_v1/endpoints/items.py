from fastapi import APIRouter


router = APIRouter()


# 路径参数 参数如果被声明类型，传入其他类型的值会报错
# 所有数据校验都是有  Pydantic 完成的
@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}