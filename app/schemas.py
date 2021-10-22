from pydantic import BaseModel


class UserDataModel(BaseModel):
    name: str
    lastname: str
    email: str


class MessageModel(BaseModel):
    message: str
