from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))
    register_date = Column(DateTime, default=func.now(), nullable=False)
