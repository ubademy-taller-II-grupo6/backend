from app.dataAccess.user_dao import UserDao
from app.utils.string_utils import is_email, is_text, contains_upper_case, contains_lower_case, contains_number
from app.exceptions.user_exceptions import InvalidEmailException, InvalidNameException, \
    InvalidPasswordFormatException


class UserHandler:
    userDao = UserDao()

    def create_new_user(self, user_name, user_lastname, user_email, user_password):
        self.validate_new_user_data(user_name, user_lastname, user_email, user_password)
        self.userDao.insert_user(user_name, user_lastname, user_email, user_password)

    @staticmethod
    def validate_user_name(user_name):
        if not is_text(user_name):
            raise InvalidNameException(user_name)

    @staticmethod
    def validate_user_lastname(user_lastname):
        if not is_text(user_lastname):
            raise InvalidNameException(user_lastname)

    @staticmethod
    def validate_user_email(user_email):
        if not is_email(user_email):
            raise InvalidEmailException(user_email)

    @staticmethod
    def validate_user_password(user_password):
        if (
            len(user_password) < 8
            or not contains_lower_case(user_password)
            or not contains_upper_case(user_password)
            or not contains_number(user_password)
        ):
            raise InvalidPasswordFormatException()

    def validate_new_user_data(self, user_name, user_lastname, user_email, user_password):
        self.validate_user_name(user_name)
        self.validate_user_lastname(user_lastname)
        self.validate_user_email(user_email)
        self.validate_user_password(user_password)
