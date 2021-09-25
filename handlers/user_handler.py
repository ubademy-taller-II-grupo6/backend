from dao.user_dao import UserDao


class UserHandler:
    userDao = UserDao()

    def insert_user(self, user_name, user_lastname, user_email, user_password):
        """ VALIDAR CAMPOS VACIOS
            EL FORMATO DE LOS CAMPOS
        """
        self.userDao.insert_user((user_name, user_lastname, user_email, user_password))