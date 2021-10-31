from app.user_dao import UserDao
from app.user_handler import UserHandler
from fastapi import APIRouter, status
from app.schemas import UserDataModel, MessageModel, ProfileModel, AddProfileModel, UsersListDataModel
from typing import List

router = APIRouter(tags=["users"])
user_handler = UserHandler(UserDao())


# CREATE
@router.post(
    '/users',
    status_code=status.HTTP_201_CREATED,
    response_model=MessageModel
)
async def create_user(
        user: UserDataModel
):
    return user_handler.create_user(user.name, user.lastname, user.email)


@router.post(
    '/users/profiles',
    status_code=status.HTTP_201_CREATED,
    response_model=MessageModel
)
async def add_user_profile(
        data: AddProfileModel
):
    return user_handler.add_profile_to_user(data.user_id, data.profile_id)


# READ

@router.get(
    '/users/profiles',
    status_code=status.HTTP_200_OK,
    response_model=List[ProfileModel]
)
async def get_profiles():
    return user_handler.get_profiles()


@router.get(
    '/users/',
    status_code=status.HTTP_200_OK,
    response_model=List[UsersListDataModel]
)
async def get_users_list():
    return user_handler.get_users_list()


@router.get(
    '/users/profiles/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=List[ProfileModel]
)
async def get_user_profiles(
        user_id: str
):
    return user_handler.get_user_profiles(user_id)


@router.get(
    '/users/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=UserDataModel,
)
async def get_user(
        user_id: str
):
    return user_handler.get_user(user_id)


# UPDATE
@router.put(
    '/users/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=MessageModel
)
async def update_user(
        user_id: str,
        user_data: UserDataModel
):
    return user_handler.update_user(user_id, user_data.name, user_data.lastname, user_data.email)


@router.put(
    '/users/block/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=MessageModel
)
async def block_user(
        user_id: str,
):
    return user_handler.block_user(user_id)


@router.put(
    '/users/unblock/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=MessageModel
)
async def unblock_user(
        user_id: str,
):
    return user_handler.unblock_user(user_id)

