from fastapi import APIRouter
from typing import List

import api.v1.schemas.post as post_schema

router = APIRouter()

@router.get('/posts',response_model=List[post_schema.Post])
def get_posts():
  pass

@router.post('/posts',response_model=post_schema.Post)
def create_post(post:post_schema.PostCreateRequest):
  pass

@router.get('/post/{post_id}',response_model=post_schema.Post)
def get_post():
  pass

@router.post('/post/{post_id}/lgtm',response_model=post_schema.Post)
def add_lgtm():
  pass

@router.delete('/post/{post_id}/lgtm',response_model=post_schema.Post)
def delete_lgtm():
  pass