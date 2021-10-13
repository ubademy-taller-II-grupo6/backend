from app.dataAccess.user_dao import UserDao
from app.utils.string_utils import is_email, is_text, contains_upper_case, contains_lower_case, contains_number
from app.exceptions.user_exceptions import InvalidEmailException, InvalidNameException, \
    InvalidPasswordFormatException, UserAlreadyExistException, IncorrectLoginDataException, UserBlockedException


class UserHandler:
    userDao = UserDao()

    def create_new_user(self, user_name, user_lastname, user_email, user_password, user_profile):
        self.validate_new_user_data(user_name, user_lastname, user_email, user_password)
        self.userDao.insert_user(user_name, user_lastname, user_email, user_password, user_profile)
        return "Usuario creado con éxito"

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
    def validate_user_password_match(real_user_password, given_user_password):
        return real_user_password == given_user_password

    @staticmethod
    def validate_user_password_format(user_password):
        if (
                len(user_password) < 8
                or not contains_lower_case(user_password)
                or not contains_upper_case(user_password)
                or not contains_number(user_password)
                or not contains_number(user_password)
        ):
            raise InvalidPasswordFormatException()

    @staticmethod
    def validate_user_blocked(blocked):
        if blocked:
            raise UserBlockedException()

    def validate_user_existence(self, user_email):
        if self.userDao.exists_user(user_email):
            raise UserAlreadyExistException(user_email)

    def validate_new_user_data(self, user_name, user_lastname, user_email, user_password):
        self.validate_user_name(user_name)
        self.validate_user_lastname(user_lastname)
        self.validate_user_email(user_email)
        self.validate_user_password_format(user_password)
        self.validate_user_existence(user_email)

    def get_user_profiles(self):
        return self.userDao.get_user_profiles()

    def user_login(self, user_email, user_password):
        user_data = self.userDao.find_user_by_email(user_email)
        if not user_data or not self.validate_user_password_match(user_data['user_password'], user_password):
            raise IncorrectLoginDataException
        self.validate_user_blocked(user_data['user_blocked'])
        result = {
            "user_name": user_data['user_name'],
            "user_lastname": user_data['user_lastname'],
            "user_email": user_data['user_email'],
            "user_profile": user_data['profile_name']
        }
        return result