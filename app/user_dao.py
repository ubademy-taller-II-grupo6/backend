import psycopg2

from psycopg2.extras import RealDictCursor


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

    def create_user(self, user_name, user_lastname, user_email):
        cur = self.connection.cursor()
        query = "INSERT INTO users(user_name,user_lastname,user_email) VALUES (%s,%s,%s)"
        try:
            cur.execute(query, (user_name, user_lastname, user_email))
            self.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.connection.rollback()
            return False
        return True

    def get_user(self, user_id):
        cur = self.connection.cursor()
        query = "SELECT user_name,user_lastname, user_email" \
                " FROM users " \
                "where user_id = %s"
        cur.execute(query, (user_id,))
        result = cur.fetchone()
        return result

    def update_user(self, user_id, user_name, user_lastname, user_email):
        cur = self.connection.cursor()
        query = "UPDATE users " \
                "SET user_name = %s, user_lastname = %s, user_email = %s" \
                " WHERE user_id = %s"
        cur.execute(query, (user_name, user_lastname, user_email, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        cur = self.connection.cursor()
        query = "DELETE FROM users WHERE user_id = %s"
        cur.execute(query, (user_id,))
        self.connection.commit()

    def get_profiles(self):
        cur = self.connection.cursor()
        query = "SELECT *  FROM user_profiles"
        cur.execute(query)
        result = cur.fetchall()
        return result
