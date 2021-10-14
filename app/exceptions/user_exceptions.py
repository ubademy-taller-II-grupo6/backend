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


class InvalidPasswordFormatException(Exception):
    def __init__(self):
        self.message = f'La contraseña debe contener al menos 8 caracteres incluyendo al menos una letra minuscula, ' \
                       f'una letra mayuscula y un número '

    def __str__(self):
        return self.message


class UserBlockedException(Exception):
    message = "El usuario se encuentra bloqueado"

    def __str__(self):
        return self.message


class UserAlreadyExistException(Exception):
    def __init__(self, user_email: str):
        self.message = f'Ya existe un usuario registrado con el email  {user_email}'

    def __str__(self):
        return self.message


class IncorrectLoginDataException(Exception):
    def __init__(self):
        self.message = f'El usuario o la contraseña son incorrectos'

    def __str__(self):
        return self.message
