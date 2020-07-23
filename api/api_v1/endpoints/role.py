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


@router.get("/", response_model=List[schemas.Role], summary="分页查询角色")
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles


@router.get("/{role_id}", response_model=schemas.Role, summary="根据角色信息查询相关角色")
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

