from pydantic import BaseModel, Field

import api.v1.schemas.user as user_schema

class PostBase(BaseModel):
  title: str = Field(None, description="投稿タイトル")
  context: str = Field(None, description="投稿本文")

class Post(PostBase):
  id: int
  user: user_schema.User = Field(None, description="投稿ユーザー情報")
  lgtm＿count: int = Field(0, description="LGTM数")

class PostCreateRequest(PostBase):
  user_id: int = Field(None, description="ユーザーID")
  