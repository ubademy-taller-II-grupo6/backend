from pydantic import BaseModel


class UserDataModel(BaseModel):
    name: str
    lastname: str
    email: str


class MessageModel(BaseModel):
    message: str


class ProfileModel(BaseModel):
    profile_id: int
    profile_name: str
