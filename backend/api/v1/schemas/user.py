from pydantic import BaseModel, Field

class UserBase(BaseModel):
  login_id: str = Field(None, description="ログインID")
  name: str = Field(None, description="表示名")
  description: str = Field(None, description="プロフィール文")

class User(UserBase):
  id: int

  class Config:
    orm_mode = True

class UserCreateRequest(UserBase):
  password: str = Field(None, description="パスワード")
  