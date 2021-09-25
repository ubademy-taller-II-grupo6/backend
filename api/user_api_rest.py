import uvicorn
from fastapi import FastAPI
from schemas.schemas import UserRequestModel
from dao.user_dao import UserDao


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/userRegistration")
async def insert_user(user: UserRequestModel):
    UserDao().insert_user(user.name, user.lastname, user.email, user.password)

if __name__ == "__main__":
    uvicorn.run(app)