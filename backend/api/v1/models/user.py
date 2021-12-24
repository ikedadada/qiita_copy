from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.v1.db import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  login_id = Column(String, unique=True)
  password_hash = Column(String)
  name = Column(String)
  description = Column(String)

  posts = relationship('Post', back_populates="user")
  lgtms = relationship('Lgtm', back_populates="user")
  