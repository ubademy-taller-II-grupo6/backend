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
    def __init__(self, user_email: str):
        self.message = f'Ya existe un usuario registrado con el email  {user_email}'

    def __str__(self):
        return self.message


class InvalidUserIdException(Exception):
    def __init__(self, user_id):
        self.message = f'No existe el ususario con el id {user_id}'

    def __str__(self):
        return self.message


class InvalidProfileIdException(Exception):
    def __init__(self, profile_id):
        self.message = f'No existe un perfil con el id {profile_id}'

    def __str__(self):
        return self.message


class ProfileAlreadyAssociatedException(Exception):
    def __init__(self):
        self.message = f'El peril ya se encuentra asociado al usuario'

    def __str__(self):
        return self.message


class InvalidUserEmail(Exception):
    def __init__(self, user_email):
        self.message = f'No hay ningún usuario asociado al correo electrónico {user_email}'

    def __str__(self):
        return self.message


class UserBlockedException(Exception):
    def __init__(self):
        self.message = f'El usuario se encuentra bloqueado'

    def __str__(self):
        return self.message







