from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
