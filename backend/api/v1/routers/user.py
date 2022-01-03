from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import api.v1.schemas.user as user_schema
import api.v1.cruds.user as user_crud

from api.v1.db import get_db

router = APIRouter()

@router.post('/users',response_model=user_schema.User)
def create_user(user:user_schema.UserCreateRequest,db:Session = Depends(get_db)):
  db_user = user_crud.get_user_by_login_id(db,user.login_id)
  if db_user:
    raise HTTPException(status_code = 400,detail = "LoginId already exists")
  return user_crud.create_user(db,user)

@router.get('/user/{login_id}',response_model=user_schema.User)
def get_user(login_id:str, db:Session = Depends(get_db)):
  db_user = user_crud.get_user_by_login_id(db,login_id)
  if db_user is None:
    raise HTTPException(status_code = 400,detail = "User not found")
  return db_user
