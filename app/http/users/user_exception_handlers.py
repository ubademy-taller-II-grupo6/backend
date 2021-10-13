from fastapi import status, Request, FastAPI
from starlette.responses import JSONResponse

from app.exceptions.user_exceptions import (
    InvalidEmailException,
    InvalidNameException,
    InvalidLastnameException,
    InvalidPasswordFormatException,
    UserBlockedException,
    UserAlreadyExistException,
    IncorrectLoginDataException
)


async def invalid_email_exception_handler(request: Request, exc: InvalidEmailException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


async def invalid_name_exception_handler(request: Request, exc: InvalidNameException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


async def invalid_lastname_exception_handler(request: Request, exc: InvalidLastnameException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


async def invalid_password_format_exception_handler(request: Request, exc: InvalidPasswordFormatException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


async def user_blocked_exception_handler(request: Request, exc:  UserBlockedException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


async def user_already_exist_exception_handler(request: Request, exc:  UserAlreadyExistException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


async def user_incorrect_login_data_exception_handler(request: Request, exc:  IncorrectLoginDataException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.message)


def add_user_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidEmailException, invalid_email_exception_handler)
    app.add_exception_handler(InvalidNameException, invalid_name_exception_handler)
    app.add_exception_handler(InvalidLastnameException, invalid_lastname_exception_handler)
    app.add_exception_handler(InvalidPasswordFormatException, invalid_password_format_exception_handler)
    app.add_exception_handler(UserBlockedException, user_blocked_exception_handler)
    app.add_exception_handler(UserAlreadyExistException, user_already_exist_exception_handler)
    app.add_exception_handler(IncorrectLoginDataException, user_already_exist_exception_handler)

