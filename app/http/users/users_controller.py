from app.api.api import Api
from fastapi import APIRouter, status
from app.http.users.user_schemas import UserRegistrationModel, UserLoginModel


router = APIRouter(tags=["users"])
api = Api()


@router.post('/users', status_code=status.HTTP_201_CREATED)
async def create_new_user(user: UserRegistrationModel):
    return api.create_new_user(user.name, user.lastname, user.email, user.password)


@router.post('/users/login', status_code=status.HTTP_200_OK)
async def user_login(user: UserLoginModel):
    return api.user_login(user.email, user.password)







