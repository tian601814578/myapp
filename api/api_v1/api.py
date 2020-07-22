from fastapi import APIRouter
from api.api_v1.endpoints import items, users, role


api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(role.router, prefix="/role", tags=["role"])
