from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from core.tools import get_db
from database import SessionLocal


router = APIRouter()


@router.post("/category", response_model=schemas.RoleCategory, summary="创建角色目录")
def create_role_category(
        role_category: schemas.CreateRoleCategory,
        db: Session=Depends(get_db)
):
    return crud.create_role_category(db=db, role_category=role_category)


@router.post("/", response_model=schemas.Role, summary="创建指定信息的角色")
def create_role(
        role: schemas.CreateRole,
        db: Session = Depends(get_db)
):
    return crud.create_role(db=db, role=role)

