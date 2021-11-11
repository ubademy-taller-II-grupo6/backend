import sys

import psycopg2

from psycopg2.extras import RealDictCursor

from app.exceptions import InvalidUserIdException, UserAlreadyExistException


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
        query = "INSERT INTO users(user_name,user_lastname,user_email,user_blocked) VALUES (%s,%s,%s,%s)"
        try:
            cur.execute(query, (user_name, user_lastname, user_email, False))
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.rollback()
            raise UserAlreadyExistException(user_email)
        return True

    def get_user(self, user_id):
        cur = self.connection.cursor()
        query = "SELECT user_id,user_name,user_lastname, user_email, user_blocked" \
                " FROM users " \
                "where user_id = %s"
        cur.execute(query, (user_id,))
        data = cur.fetchone()
        if not data:
            raise InvalidUserIdException(user_id)
        return [self.parse_user(data)]

    def get_users_list(self):
        cur = self.connection.cursor()
        query = "SELECT user_id, user_name, user_lastname, user_email, user_blocked" \
                " FROM users"
        cur.execute(query)
        data = cur.fetchall()
        users = []
        for row in data:
            users.append(self.parse_user(row))
        return users

    def update_user(self, user_id, user_name, user_lastname, user_email, user_blocked):
        cur = self.connection.cursor()
        query = "UPDATE users " \
                "SET user_name = %s, user_lastname = %s, user_email = %s, user_blocked= %s " \
                "WHERE user_id = %s"
        cur.execute(query, (user_name, user_lastname, user_email, user_blocked, user_id))
        self.connection.commit()

    @staticmethod
    def parse_user(data):
        user = {
            "id": data["user_id"],
            "name": data['user_name'],
            "lastname": data['user_lastname'],
            "email": data['user_email'],
            "blocked": data["user_blocked"]
        }
        return user
