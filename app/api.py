from app.user_dao import UserDao
from app.user_handler import UserHandler
from fastapi import APIRouter, status
from app.schemas import UserDataModel, MessageModel

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


# READ
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


# DELETE
@router.delete(
    '/users/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=MessageModel
)
async def delete_user(
        user_id: str
):
    return user_handler.delete_user(user_id)
