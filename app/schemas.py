from pydantic import BaseModel
from typing import Optional


class CreateUserModel(BaseModel):
    name: str
    lastname: str
    email: str


class GetUserModel(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    blocked: bool


class UpdateUserModel(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    blocked: Optional[bool] = None


class MessageModel(BaseModel):
    message: str