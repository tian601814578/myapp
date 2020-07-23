from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from core.tools import get_db
from database import SessionLocal


router = APIRouter()


@router.post("/", response_model=schemas.Role, summary="创建指定信息的角色")
def create_user(role: schemas.CreateRole, db: Session = Depends(get_db)):
    return crud.create_role(db=db, role=role)
