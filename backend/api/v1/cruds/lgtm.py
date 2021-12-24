from sqlalchemy.orm import Session

from api.v1.models.lgtm import Lgtm

def get_lgtm(db:Session,post_id:int,user_id:int):
  db_lgtm = db.query(Lgtm).filter_by(post_id==post_id,user_id==user_id).first()
  return db_lgtm

def add_lgtm(db:Session,post_id:int,user_id:int):
  db_lgtm = Lgtm(user_id=user_id,post_id=post_id)
  db.add(db_lgtm)
  db.commit()
  db.refresh(db_lgtm)

def remove_lgtm(db:Session,lgtm:Lgtm):
  db.delete(lgtm)
  db.commit()
