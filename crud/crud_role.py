from sqlalchemy.orm import Session

import models
import schemas


def create_role(db: Session, role: schemas.Role):
    """
    创建模型--》创建 schemas 架构--》crud 构建逻辑
    """
    db_role = models.Role(
        name=role.name,
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
