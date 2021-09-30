from app.handlers.user_handler import UserHandler


class Api:
    def __init__(self):
        self.user_handler = UserHandler()

    def create_new_user(self, user_name, user_lastname, user_email, user_password):
        self.user_handler.create_new_user(user_name, user_lastname, user_email, user_password)
