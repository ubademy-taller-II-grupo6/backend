class InvalidEmailException(Exception):
    def __init__(self, user_email: str):
        self.message = f'El email {user_email} no es válido'

    def __str__(self):
        return self.message


class InvalidNameException(Exception):
    def __init__(self, user_name: str):
        self.message = f'El nombre {user_name}  no es válido'

    def __str__(self):
        return self.message


class InvalidLastnameException(Exception):
    def __init__(self, user_lastname: str):
        self.message = f'El apellido {user_lastname}  no es válido'

    def __str__(self):
        return self.message


class UserAlreadyExistException(Exception):
    def __init__(self):
        self.message = f'El ususario ya existe'

    def __str__(self):
        return self.message


class InvalidUserIdException(Exception):
    def __init__(self, user_id):
        self.message = f'No existe el ususario con el id {user_id}'

    def __str__(self):
        return self.message


class UserBlockedException(Exception):
    def __init__(self):
        self.message = f'El usuario se encuentra bloqueado'

    def __str__(self):
        return self.message


class InvalidSubscriptionIDException(Exception):
    def __init__(self, subscription_id):
        self.message = f'No existe ninguna suscripción con el id {subscription_id}'

    def __str__(self):
        return self.message


class InvalidOperationException(Exception):
    def __init__(self, message):
        self.message = f'{message}'

    def __str__(self):
        return self.message
