from sqlalchemy.orm import Session
from passlib.context import CryptContext

from api.v1.models.user import User
import api.v1.schemas.user as UserSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db:Session,user_id:int):
  return db.query(User).filter_by(User.id == user_id).first()

def create_user(db:Session,user:UserSchema.UserCreateRequest):
  password_hash = get_password_hash(user.password)
  db_user = User(
    login_id=user.login_id,
    name=user.name,
    description=user.description,
    password_hash=password_hash
  )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user
  