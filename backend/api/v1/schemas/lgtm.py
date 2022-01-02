from pydantic import BaseModel, Field

class PostLgtm(BaseModel):
  user_id: int = Field(None, description="ユーザーID")

  class Config:
    orm_mode: True

class UserLgtm(BaseModel):
  post_id: int

  class Config:
    orm_mode: True
