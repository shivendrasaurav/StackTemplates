from sqlalchemy import Column, Integer, String
from db import Base, SessionLocal  # Import from db.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

def create_user(name: str, email: str):
    db = SessionLocal()  # Open a new session
    try:
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()  # Ensure the session is closed

def get_user(user_id: int):
    db = SessionLocal()  # Open a new session
    try:
        return db.query(User).filter(User.id == user_id).first()
    finally:
        db.close()  # Ensure the session is closed
