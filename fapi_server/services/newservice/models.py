# services/newservice/models.py

# ========== Pydantic Base Models ========== #

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass  # Inherits from UserBase with no additional fields

class UserResponse(UserBase):
    id: int

# ========== Pydantic Base Models ========== #
# ========================================== #
# ========= SQL Alchemy ORM Models ========= #


"""
Enable If You Want To Use ORM Based Database Operations

from .db_orm import Base

class UserORM(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

"""


# ========= SQL Alchemy ORM Models ========= #

