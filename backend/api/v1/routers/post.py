from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

import api.v1.schemas.post as post_schema
import api.v1.cruds.post as post_crud
import api.v1.cruds.lgtm as lgtm_crud
import api.v1.cruds.auth as auth_crud
from api.v1.db import get_db

router = APIRouter()

@router.get('/posts',response_model=List[post_schema.Post])
def get_posts(db:Session = Depends(get_db)):
  posts = post_crud.get_posts(db=db)
  return posts

@router.post('/posts',response_model=post_schema.Post)
def create_post(post:post_schema.PostBase,token: str = Depends(auth_crud.oauth2_scheme),db:Session = Depends(get_db)):
  current_user = auth_crud.get_current_user(db=db,token=token)
  post = post_crud.create_post(db=db,post=post,user_id=current_user.id)
  return post

@router.get('/post/{id}',response_model=post_schema.Post)
def get_post(id:int,db:Session = Depends(get_db)):
  post = post_crud.get_post(db=db,id=id)
  if post is None:
    raise HTTPException(status_code = 400, detail = "Post not Found")
  return post

@router.post('/post/{id}/lgtm')
def add_lgtm(id:int,token: str = Depends(auth_crud.oauth2_scheme),db:Session = Depends(get_db)):
  current_user = auth_crud.get_current_user(db=db,token=token)
  lgtm_crud.add_lgtm(db=db,post_id=id,user_id=current_user.id)
  return None

@router.delete('/post/{id}/lgtm')
def delete_lgtm(id:int,token: str = Depends(auth_crud.oauth2_scheme),db:Session = Depends(get_db)):
  current_user = auth_crud.get_current_user(db=db,token=token)
  lgtm = lgtm_crud.get_lgtm(db=db,post_id=id,user_id=current_user.id)
  if lgtm is None:
    raise HTTPException(status_code = 400, detail = "Lgtm not Found")
  lgtm_crud.remove_lgtm(db=db,lgtm=lgtm)
  return None
