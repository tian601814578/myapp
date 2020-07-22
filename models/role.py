from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    loginName = Column(String, unique=True, index=True)
    displayName = Column(String, unique=True, index=True)
    password = Column(String)