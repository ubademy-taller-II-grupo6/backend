from app.exceptions import InvalidNameException, InvalidEmailException, \
    InvalidLastnameException, UserBlockedException
from app.utils import is_text, is_email, create_message_response


class UserHandler:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, id, name, lastname, email, latitude, longitude):
        self.validate_user_name(name)
        self.validate_user_lastname(lastname)
        self.validate_user_email(email)
        self.user_dao.create_user(id, name, lastname, email, latitude, longitude)
        response = create_message_response("El usuario se creó con éxito")
        return response

    @staticmethod
    def validate_user_name(name):
        if not is_text(name):
            raise InvalidNameException(name)

    @staticmethod
    def validate_user_lastname(lastname):
        if not is_text(lastname):
            raise InvalidLastnameException(lastname)

    @staticmethod
    def validate_user_email(email):
        if not is_email(email):
            raise InvalidEmailException(email)

    def get_user(self, id, check_blocked):
        if id:
            response = self.user_dao.get_user(id)
            if check_blocked and response[0]['blocked']:
                raise UserBlockedException()
        else:
            response = self.user_dao.get_users_list()
        return response

    def update_user(self, id, name, lastname, email, latitude, longitude, blocked, subscription):
        user = self.get_user(id, False)[0]

        if blocked is None:
            blocked = user["blocked"]

        if name:
            self.validate_user_name(name)
        else:
            name = user["name"]

        if lastname:
            self.validate_user_lastname(lastname)
        else:
            lastname = user["lastname"]

        if email:
            self.validate_user_email(email)
        else:
            email = user["email"]

        if not subscription:
            subscription = user["subscription"]

        if not latitude:
            latitude = user['latitude']

        if not longitude:
            longitude = user['longitude']

        self.user_dao.update_user(id, name, lastname, email, latitude, longitude, blocked, subscription)

        response = create_message_response("El usuario fue actualizado con éxito")
        return response

    def get_subscription_conditions(self, subscription_id):
        return self.user_dao.get_subscription_conditions(subscription_id)

    def get_subscriptions(self):
        return self.user_dao.get_subscriptions()
