from fastapi import FastAPI

app = FastAPI()

from api.v1.routers import user,post,auth

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
  return {"Hello":"World"}