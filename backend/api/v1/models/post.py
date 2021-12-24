from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.v1.db import Base

class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True)
  title = Column(String)
  context = Column(String)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates="posts")
  lgtms = relationship('Lgtm', back_populates="post")
