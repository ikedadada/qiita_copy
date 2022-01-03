from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

import api.v1.schemas.auth as auth_schema
import api.v1.schemas.user as user_schema
import api.v1.cruds.auth as auth_crud

from api.v1.db import get_db

router = APIRouter()

@router.post("/token", response_model=auth_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
  user = auth_crud.authenticate_user(db, form_data.username, form_data.password)
  if user is None:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect login_id or password",
      headers={"WWW-Authenticate":"Bearer"}
    )
  access_token = auth_crud.create_access_token(data={"sub": user.login_id})
  return {"access_token":access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=user_schema.User)
async def read_users_me(token: str = Depends(auth_crud.oauth2_scheme),db:Session = Depends(get_db)):
  current_user = auth_crud.get_current_user(db=db,token=token)
  print(current_user)
  return current_user