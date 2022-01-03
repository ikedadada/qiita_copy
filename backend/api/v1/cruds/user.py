from sqlalchemy.orm import Session
from passlib.context import CryptContext

from api.v1.models.user import User
import api.v1.schemas.user as user_schema
from api.v1.cruds.auth import get_password_hash

def get_user(db:Session,id:int):
  return db.query(User).filter_by(id=id).first()

def get_user_by_login_id(db:Session,login_id:str):
  return db.query(User).filter_by(login_id=login_id).first()

def create_user(db:Session,user:user_schema.UserCreateRequest):
  password_hash = get_password_hash(user.password)
  new_user = User(
    login_id=user.login_id,
    name=user.name,
    description=user.description,
    password_hash=password_hash
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user
