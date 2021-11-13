from app.exceptions import InvalidNameException, InvalidEmailException, \
    InvalidLastnameException, UserBlockedException
from app.utils import is_text, is_email, create_message_response


class UserHandler:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, user_name, user_lastname, user_email):
        self.validate_user_name(user_name)
        self.validate_user_lastname(user_lastname)
        self.validate_user_email(user_email)
        self.user_dao.create_user(user_name, user_lastname, user_email)
        response = create_message_response("El usuario se creó con éxito")
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

    def get_user(self, user_id, check_blocked):
        if user_id:
            response = self.user_dao.get_user(user_id)
            if check_blocked and response[0]['blocked']:
                raise UserBlockedException()
        else:
            response = self.user_dao.get_users_list()
        return response

    def update_user(self, user_id, user_name, user_lastname, user_email, user_blocked):
        user = self.get_user(user_id, False)[0]

        if user_blocked is None:
            user_blocked = user["blocked"]

        if user_name:
            self.validate_user_name(user_name)
        else:
            user_name = user["name"]

        if user_lastname:
            self.validate_user_lastname(user_lastname)
        else:
            user_lastname = user["lastname"]

        if user_email:
            self.validate_user_email(user_email)
        else:
            user_email = user["email"]

        self.user_dao.update_user(user_id,
                                  user_name,
                                  user_lastname,
                                  user_email,
                                  user_blocked
                                  )

        response = create_message_response("El usuario fue actualizado con éxito")
        return response