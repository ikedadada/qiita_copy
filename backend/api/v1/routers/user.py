from fastapi import APIRouter

import api.v1.schemas.user as user_schema

router = APIRouter()

@router.post('/users',response_model=user_schema.User)
def create_user(user:user_schema.UserCreateRequest):
  pass

@router.get('/user/{user_id}',response_model=user_schema.User)
def get_user():
  pass