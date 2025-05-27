from fastapi import FastAPI
from backend.api.UserApi import api as user_router


app = FastAPI()

app.include_router(user_router, prefix="/user")

@app.get("/")
def root():
    return {"message": "Hello, This Is My APP!"}