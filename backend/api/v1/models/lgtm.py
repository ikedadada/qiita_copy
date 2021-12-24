from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.v1.db import Base

class Lgtm(Base):
  __tablename__ = "lgtms"

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  post_id = Column(Integer, ForeignKey("posts.id"))

  user = relationship('User', back_populates="lgtms")
  post = relationship('Post', back_populates="lgtms")
