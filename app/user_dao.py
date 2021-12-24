import sys

import psycopg2

from psycopg2.extras import RealDictCursor

from app.exceptions import InvalidUserIdException, UserAlreadyExistException, InvalidSubscriptionIDException, \
    InvalidOperationException


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
    def create_user(self, id, name, lastname, email, latitude, longitude):
        cur = self.connection.cursor()
        query = "INSERT INTO users(id,name,lastname,email,latitude,longitude,blocked, subscription) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cur.execute(query, (id, name, lastname, email, latitude, longitude, False, 'FREE'))
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.rollback()
            raise UserAlreadyExistException()
        return True

    def get_user(self, user_id):
        cur = self.connection.cursor()
        query = "SELECT *" \
                " FROM users " \
                "where id = %s"
        cur.execute(query, (user_id,))
        data = cur.fetchone()
        if not data:
            raise InvalidUserIdException(user_id)
        return [self.parse_user(data)]

    def get_users_list(self):
        cur = self.connection.cursor()
        query = "SELECT *" \
                " FROM users"
        cur.execute(query)
        data = cur.fetchall()
        users = []
        for row in data:
            users.append(self.parse_user(row))
        return users

    def update_user(self, id, name, lastname, email, latitude, longitude, blocked, subscription):
        cur = self.connection.cursor()
        query = f"""UPDATE users 
                    SET name = %s, lastname = %s, email = %s, latitude= %s,  longitude= %s, blocked = %s, 
                    subscription = %s\
                    WHERE id = %s"""
        try:
            cur.execute(query, (name, lastname, email, latitude, longitude, blocked, subscription, id))
        except:
            self.connection.rollback()
            raise InvalidOperationException("Los datos ingresados no son válidos")
        self.connection.commit()

    def get_subscription_conditions(self, subscription_id):
        cur = self.connection.cursor()
        query = f"""SELECT conditions FROM subscriptions WHERE id = %s"""
        cur.execute(query, (subscription_id,))
        data = cur.fetchone()
        if not data:
            raise InvalidSubscriptionIDException(subscription_id)
        return data

    def get_subscriptions(self):
        cur = self.connection.cursor()
        query = f"""SELECT * FROM subscriptions"""
        cur.execute(query)
        data = cur.fetchall()
        response = []
        for subscription in data:
            response.append(self.parse_subscription(subscription))
        return response

    @staticmethod
    def parse_user(data):
        user = {
            "id": data["id"],
            "name": data['name'],
            "lastname": data['lastname'],
            "email": data['email'],
            "latitude": data['latitude'],
            "longitude": data['longitude'],
            "blocked": data["blocked"],
            "subscription":  data["subscription"]
        }
        return user

    @staticmethod
    def parse_subscription(data):
        subscription = {
            "subscription_id" : data["id"],
            "conditions" : data["conditions"]
        }
        return subscription



