from pydantic import BaseModel


class UserRequestModel(BaseModel):
    name: str
    lastname: str
    email: str
    password: str
