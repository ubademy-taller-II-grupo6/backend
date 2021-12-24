from pydantic import BaseModel
from typing import Optional


class CreateUserModel(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    latitude: str
    longitude: str


class GetUserModel(BaseModel):
    name: str
    lastname: str
    email: str
    latitude: str
    longitude: str
    blocked: bool
    subscription: str


class UpdateUserModel(BaseModel):
    name: str = None
    lastname: str = None
    email: str = None
    latitude: str = None
    longitude: str = None
    blocked: bool = None
    subscription: str = None


class MessageModel(BaseModel):
    message: str


class SubscriptionModel(BaseModel):
    subscription_id: str
    conditions: str
