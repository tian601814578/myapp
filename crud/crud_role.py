from sqlalchemy.orm import Session

import models
import schemas


def create_role_category(db: Session, role_category: schemas.CreateRoleCategory):
    if role_category.parent:
        db_role_category = models.RoleCategory(
            name = role_category.name,
            parent = role_category.parent
        )
    else:
        db_role_category = models.RoleCategory(
            name=role_category.name,
        )
    db.add(db_role_category)
    db.commit()
    db.refresh(db_role_category)
    return db_role_category


def create_role(db: Session, role: schemas.CreateRole):
    """
    创建模型--》创建 schemas 架构--》crud 构建逻辑
    """
    db_role = models.Role(
        name=role.name,
        rolecategory_id=role.rolecategory_id
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

