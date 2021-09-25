import psycopg2
from utils.json_utils import read_json_file



class UserDao:

    def __init__(self, connection=None):
        self.connection = connection

        if not self.connection:
            self.set_default_connection()

    def set_default_connection(self):
        db_data = read_json_file("../config/db.json")

        connection = psycopg2.connect(
            host=db_data["host"],
            database=db_data["database"],
            user=db_data["user"],
            password=db_data["password"]
        )

        self.connection = connection

    def insert_user(self, user_name, user_lastname, user_email, user_password):
        cur = self.connection.cursor()
        query = "INSERT INTO users(user_name,user_lastname,user_email,user_password) VALUES (%s,%s,%s,%s)"
        cur.execute(query, (user_name, user_lastname, user_email, user_password))
        self.connection.commit()
