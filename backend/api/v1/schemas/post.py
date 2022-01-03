from typing import List, Optional
from pydantic import BaseModel, Field

import api.v1.schemas.user as user_schema
import api.v1.schemas.lgtm as lgtm_schema

class PostBase(BaseModel):
  title: str = Field(None, description="投稿タイトル")
  context: str = Field(None, description="投稿本文")

class Post(PostBase):
  id: int
  user: user_schema.User = Field(None, description="投稿者")
  lgtm_count: int = Field(0,description="LGTM数")

  class Config:
    orm_mode = True #リクエストを返す時にこの項目だけレスポンスするようになる
  
class PostLgtmCreateRequest(BaseModel):
  id: int
  user_id: int = Field(None, description="ユーザーID")

class PostLgtmDeleteRequest(BaseModel):
  id: int
  user_id: int = Field(None, description="ユーザーID")
  