from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class RoleCategory(Base):
    __tablename__ = "rolecategory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    parent = Column(String, unique=False, index=True)


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    rolecategory_id = Column(Integer, ForeignKey("rolecategory.id"))

    rolecategory = relationship(RoleCategory)

