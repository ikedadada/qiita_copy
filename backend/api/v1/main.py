from fastapi import FastAPI

app = FastAPI()

from api.v1.routers import user,post

app.include_router(user.router)
app.include_router(post.router)

@app.get("/")
def read_root():
  return {"Hello":"World"}