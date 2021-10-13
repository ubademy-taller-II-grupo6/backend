from pydantic import BaseModel


class UserRegistrationModel(BaseModel):
    name: str
    lastname: str
    email: str
    password: str


class UserLoginModel(BaseModel):
    email: str
    password: str
