from app.user_dao import UserDao
from app.user_handler import UserHandler
from fastapi import APIRouter, status
from typing import Optional
from app.schemas import MessageModel, CreateUserModel, GetUserModel, UpdateUserModel
from typing import List

from app.utils import to_bool

router = APIRouter(tags=["users"])
user_handler = UserHandler(UserDao())


# CREATE
@router.post(
    '/users',
    status_code=status.HTTP_201_CREATED,
    response_model=MessageModel
)
async def create_user(
        user: CreateUserModel
):
    return user_handler.create_user(
        user.name,
        user.lastname,
        user.email
    )


# READ
@router.get(
    '/users',
    status_code=status.HTTP_200_OK,
    response_model=List[GetUserModel],
)
async def get_user(
        user_id: Optional[str] = None,
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
        user: UpdateUserModel
):
    return user_handler.update_user(
        user_id,
        user.name,
        user.lastname,
        user.email,
        to_bool(user.blocked)
    )

