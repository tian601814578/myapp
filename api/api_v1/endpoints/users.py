from fastapi import APIRouter


router = APIRouter()


# 顺序很重要，在创建路径操作时，你会发现有些路径时固定的
# 比如：可以使用 /user/me 来获取当前用户的信息
@router.get("/me")
async def read_user_me():
    return {"user_id": "the current user"}
