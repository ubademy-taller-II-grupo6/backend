import os

from fastapi import FastAPI
from app.exception_handlers import add_user_exception_handlers
import uvicorn
from app.api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
add_user_exception_handlers(app)
app.include_router(router)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)
    #uvicorn.run('main:app')
