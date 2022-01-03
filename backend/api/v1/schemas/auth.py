from pydantic import BaseModel

from api.v1.schemas.user import UserBase

class Token(BaseModel):
  access_token:str
  token_type:str

class CurrentUser(UserBase):
  id:int
  password_hash: str
