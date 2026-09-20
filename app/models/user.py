from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer,primary_key=True,index=True,)
    username = Column(String,unique=True,nullable=False,index=True,)
    hashed_password = Column(String,nullable=False,)
    is_active = Column(Boolean,nullable=False,default=True,)
    role = Column(String,nullable=False,default="user",)