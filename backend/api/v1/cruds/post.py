from sqlalchemy.orm import Session

from api.v1.models.post import Post
from api.v1.models.lgtm import Lgtm
import api.v1.schemas.post as post_schema

def get_posts(db:Session):
  posts = db.query(Post).all()
  for n in posts:
    n.lgtm_count =  db.query(Lgtm).filter_by(post_id=n.id).count()
  return posts

def create_post(db:Session,post:post_schema.PostCreateRequest):
  new_post = Post(
    title=post.title,
    context=post.context,
    user_id=post.user_id
  )
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def get_post(db:Session,id:int):
  post = db.query(Post).filter_by(id=id).first()
  post.lgtm_count = db.query(Lgtm).filter_by(post_id=id).count()
  return post
