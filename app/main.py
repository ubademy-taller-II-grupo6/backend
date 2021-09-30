from fastapi import FastAPI
from app.http.users.user_exception_handlers import add_user_exception_handlers
import uvicorn
from app.http.users.users_controller import router

app = FastAPI()
add_user_exception_handlers(app)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app)
