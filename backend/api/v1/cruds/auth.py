from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

from api.v1.models.user import User

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
  return pwd_context.hash(password)

def authenticate_user(db:Session,login_id:str, password:str):
  user = db.query(User).filter_by(login_id=login_id).first()
  if user is None:
    return None
  if not verify_password(password, user.password_hash):
    return None
  return user

def create_access_token(data:dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})
  encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encode_jwt

def get_current_user(db:Session,token: str):
  try:
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    login_id:str = payload.get("sub")
    if login_id is None:
      return None
  except JWTError:
    return None
  current_user = db.query(User).filter_by(login_id=login_id).first()
  if current_user is None:
    return None
  return current_user
