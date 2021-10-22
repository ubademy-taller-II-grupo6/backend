from app.exceptions import InvalidNameException, InvalidUserIdException, InvalidEmailException, \
    UserAlreadyExistException, InvalidLastnameException
from app.utils import is_text, is_email, create_message_response


class UserHandler:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, user_name, user_lastname, user_email):
        self.validate_user_name(user_name)
        self.validate_user_lastname(user_lastname)
        self.validate_user_email(user_email)
        inserted = self.user_dao.create_user(user_name, user_lastname, user_email)
        if not inserted:
            raise UserAlreadyExistException(user_email)
        response = create_message_response("El ususario se creó con éxito")
        return response

    def get_user(self, user_id):
        user = self.user_dao.get_user(user_id)
        if not user:
            raise InvalidUserIdException(user_id)
        response = {
            "name": user['user_name'],
            "lastname": user['user_lastname'],
            "email": user['user_email']
        }
        return response

    def update_user(self, user_id, user_name, user_lastname, user_email):
        user = self.get_user(user_id)
        if not user:
            raise InvalidUserIdException(user_id)
        self.validate_user_name(user_name)
        self.validate_user_lastname(user_lastname)
        self.validate_user_email(user_email)
        self.user_dao.update_user(user_id, user_name, user_lastname, user_email)
        response = create_message_response("El usuario fue actualizado con éxito")
        return response

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            raise InvalidUserIdException(user_id)
        self.user_dao.delete_user(user_id)
        response = create_message_response("Usuario eliminado con éxito")
        return response

    @staticmethod
    def validate_user_name(user_name):
        if not is_text(user_name):
            raise InvalidNameException(user_name)

    @staticmethod
    def validate_user_lastname(user_lastname):
        if not is_text(user_lastname):
            raise InvalidLastnameException(user_lastname)

    @staticmethod
    def validate_user_email(user_email):
        if not is_email(user_email):
            raise InvalidEmailException(user_email)
