from app.api.api import Api
from fastapi import APIRouter, status
from app.http.users.user_schemas import UserRegistrationModel, UserLoginModel
from app.utils.string_utils import get_dictionary_from_message

router = APIRouter(tags=["users"])
api = Api()


@router.post('/users/registration', status_code=status.HTTP_201_CREATED)
async def create_new_user(user: UserRegistrationModel):
    message = api.create_new_user(user.name, user.lastname, user.email, user.password, user.profile)
    return get_dictionary_from_message(message)


@router.post('/users/login', status_code=status.HTTP_200_OK)
async def user_login(user: UserLoginModel):
    return api.user_login(user.email, user.password)


@router.get('/users/profiles', status_code=status.HTTP_200_OK)
async def user_profiles():
    return api.get_user_profiles()