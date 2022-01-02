import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'root'
PASSWORD = os.environ["MYSQL_ROOT_PASSWORD"]
HOST     = 'db'
PORT     = 3306
DATABASE = 'qiita_copy'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
  USER,PASSWORD,HOST,PORT,DATABASE
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
