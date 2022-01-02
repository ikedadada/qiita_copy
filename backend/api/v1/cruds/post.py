from sqlalchemy.orm import Session

from api.v1.models.post import Post
import api.v1.schemas.post as PostSchema

def get_posts(db:Session):
  posts = db.query(Post).all()
  return posts

def create_post(db:Session,post:PostSchema.PostCreateRequest):
  db_post = Post(
    title=post.title,
    context=post.context,
    user_id=post.user_id
  )
  db.add(db_post)
  db.commit()
  db.refresh(db_post)
  return db_post

def get_post(db:Session,id:int):
  post = db.query(Post).filter_by(id=id).first()
  return post
