import os

from fastapi import FastAPI
from app.exception_handlers import add_user_exception_handlers
import uvicorn
from app.api import router

app = FastAPI()
add_user_exception_handlers(app)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app')
