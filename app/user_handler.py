from app.exceptions import InvalidNameException, InvalidUserIdException, InvalidEmailException, InvalidLastnameException
from app.utils import is_text, is_email, create_message_response


class UserHandler:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, user_name, user_lastname, user_email):
        self.validate_user_name(user_name)
        self.validate_user_lastname(user_lastname)
        self.validate_user_email(user_email)
        self.user_dao.create_user(user_name, user_lastname, user_email)
        response = create_message_response("El ususario se creó con éxito")
        return response

    def get_user(self, user_id):
        user = self.user_dao.get_user(user_id)
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

    def get_profiles(self):
        return self.user_dao.get_profiles()

    def add_profile_to_user(self, user_id, profile_id):
        self.user_dao.add_profile_to_user(user_id, profile_id)
        response = create_message_response("Perfil agregado con éxito")
        return response

    def get_user_profiles(self, user_id):
        return self.user_dao.get_user_profiles(user_id)

    def block_user(self, user_id):
        self.user_dao.block_user(user_id)
        response = create_message_response("El usuario ha sido bloqueado")
        return response

    def unblock_user(self, user_id):
        self.user_dao.unblock_user(user_id)
        response = create_message_response("El usuario ha sido desbloqueado")
        return response

    def get_users_list(self):
        return self.user_dao.get_users_list()

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








