import sys

import psycopg2

from psycopg2.extras import RealDictCursor

from app.exceptions import InvalidUserIdException, InvalidProfileIdException, ProfileAlreadyAssociatedException, \
    UserAlreadyExistException, InvalidUserEmail


class UserDao:

    def __init__(self):
        connection = psycopg2.connect(
            host="ec2-18-209-143-227.compute-1.amazonaws.com",
            database="d6i6l2t43ot65q",
            user="xtiqdxqijpalyg",
            password="29ce786ec9eb67436b1392b438b03cbe8a779f00869cd1ccf763c399e940acb2",
            cursor_factory=RealDictCursor
        )

        self.connection = connection

    # USER DATA
    def create_user(self, user_name, user_lastname, user_email):
        cur = self.connection.cursor()
        query = "INSERT INTO users(user_name,user_lastname,user_email) VALUES (%s,%s,%s)"
        try:
            cur.execute(query, (user_name, user_lastname, user_email))
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.rollback()
            raise UserAlreadyExistException(user_email)
        user_id = self.get_user_id_by_email(user_email)
        query = "INSERT INTO userstatus (user_id,blocked) VALUES (%s,false)"
        cur.execute(query, (user_id,))
        self.connection.commit()
        return True

    def get_user(self, user_id):
        cur = self.connection.cursor()
        query = "SELECT user_name,user_lastname, user_email" \
                " FROM users " \
                "where user_id = %s"
        cur.execute(query, (user_id,))
        data = cur.fetchone()
        if not data:
            raise InvalidUserIdException(user_id)
        return data

    def update_user(self, user_id, user_name, user_lastname, user_email):
        cur = self.connection.cursor()
        query = "UPDATE users " \
                "SET user_name = %s, user_lastname = %s, user_email = %s" \
                " WHERE user_id = %s"
        cur.execute(query, (user_name, user_lastname, user_email, user_id))
        self.connection.commit()

    def get_users_list(self):
        cur = self.connection.cursor()
        query = "SELECT user_id, user_name, user_lastname, user_email" \
                " FROM users"
        cur.execute(query)
        data = cur.fetchall()
        users = []
        for row in data:
            user = {
                'id': row['user_id'],
                'name': row['user_name'],
                'lastname': row['user_lastname'],
                'email': row['user_email']
            }
            users.append(user)
        return users

    def get_user_id_by_email(self, user_email):
        cur = self.connection.cursor()
        query = "SELECT * FROM users WHERE user_email=%s"
        cur.execute(query, (user_email,))
        data = cur.fetchone()
        if not data:
            raise InvalidUserEmail(user_email)
        return data['user_id']

    # USER PROFILES

    def get_profiles(self):
        cur = self.connection.cursor()
        query = "SELECT *  FROM user_profiles"
        cur.execute(query)
        result = cur.fetchall()
        return result

    def add_profile_to_user(self, user_id, profile_id):
        cur = self.connection.cursor()
        query = "INSERT INTO userprofiles (user_id,profile_id) VALUES (%s,%s)"
        try:
            cur.execute(query, (user_id, profile_id))
        except psycopg2.errors.ForeignKeyViolation as e:
            if 'user_id' in e.pgerror:
                raise InvalidUserIdException(user_id)
            elif 'profile_id' in e.pgerror:
                self.connection.rollback()
                raise InvalidProfileIdException(profile_id)
        except psycopg2.errors.UniqueViolation:
            self.connection.rollback()
            raise ProfileAlreadyAssociatedException()
        self.connection.commit()
        return True

    def get_user_profiles(self, user_id):
        cur = self.connection.cursor()
        query = "SELECT p.profile_id, p.profile_name from userprofiles up " \
                "LEFT JOIN profiles p on up.profile_id = p.profile_id " \
                "WHERE user_id = %s  "
        cur.execute(query, (user_id,))
        data = cur.fetchall()
        return data

    # USER STATUS
    def block_user(self, user_id):
        cur = self.connection.cursor()
        query = "UPDATE userstatus SET blocked= true WHERE user_id = %s"
        cur.execute(query, (user_id,))
        self.connection.commit()
        return True

    def unblock_user(self, user_id):
        cur = self.connection.cursor()
        query = "UPDATE userstatus SET blocked= false WHERE user_id = %s"
        cur.execute(query, (user_id,))
        self.connection.commit()
        return True
