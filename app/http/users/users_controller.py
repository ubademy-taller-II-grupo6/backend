from app.api.api import Api
from fastapi import APIRouter, status
from app.http.users.user_schemas import UserRequestModel


router = APIRouter(tags=["users"])
api = Api()


@router.post('/users/create_new_user', status_code=status.HTTP_201_CREATED)
async def create_new_user(user: UserRequestModel):
    api.create_new_user(user.name, user.lastname, user.email, user.password)
    return "ok"


