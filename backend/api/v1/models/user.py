from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.v1.db import Base
import api.v1.models.post

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  login_id = Column(String(255), unique=True, nullable=False)
  password_hash = Column(String(255), nullable=False)
  name = Column(String(255), nullable=False)
  description = Column(String(255))

  posts = relationship('api.v1.models.post.Post',back_populates='user')
