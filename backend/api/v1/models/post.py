from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from api.v1.db import Base
import api.v1.models.user
import api.v1.models.lgtm

class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  context = Column(LONGTEXT)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)#ForeignKeyのついたカラムのオプションはForeginKeyより後ろに書かなければならない

  user = relationship('api.v1.models.user.User',back_populates='posts')
  lgtms = relationship('api.v1.models.lgtm.Lgtm',back_populates="post")
