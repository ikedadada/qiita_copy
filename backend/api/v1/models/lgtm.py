from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.v1.db import Base

import api.v1.models.post

class Lgtm(Base):
  __tablename__ = "lgtms"

  id = Column(Integer, primary_key=True)
  post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

  post = relationship('api.v1.models.post.Post',back_populates='lgtms')
