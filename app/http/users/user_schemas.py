from pydantic import BaseModel


class UserRegistrationModel(BaseModel):
    name: str
    lastname: str
    email: str
    password: str
    profile: int


class UserLoginModel(BaseModel):
    email: str
    password: str
