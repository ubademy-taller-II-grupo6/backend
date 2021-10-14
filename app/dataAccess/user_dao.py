import psycopg2
from psycopg2.extras import RealDictCursor
from app.utils.json_utils import read_json_file


class UserDao:

    def __init__(self, connection=None):
        self.connection = connection

        if not self.connection:
            self.set_default_connection()

    def set_default_connection(self):
        db_data = read_json_file("app/config/remote_db.json")

        connection = psycopg2.connect(
            host=db_data["host"],
            database=db_data["database"],
            user=db_data["user"],
            password=db_data["password"],
            cursor_factory=RealDictCursor
        )

        self.connection = connection

    def insert_user(self, user_name, user_lastname, user_email, user_password, user_profile):
        cur = self.connection.cursor()
        query = "INSERT INTO users(user_name,user_lastname,user_email,user_password,user_wallet,user_blocked," \
                "user_profile) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, (user_name, user_lastname, user_email, user_password, 0.0, False, user_profile))
        self.connection.commit()

    def find_user_by_email (self, user_email):
        cur = self.connection.cursor()
        query = "SELECT *  FROM users join user_profiles on users.user_profile = user_profiles.profile_id where user_email = %s "
        cur.execute(query, (user_email,))
        result = cur.fetchone()
        return result

    def exists_user(self, user_email):
        if not self.find_user_by_email(user_email):
            return False
        return True

    def get_user_profiles(self):
        cur = self.connection.cursor()
        query = "SELECT *  FROM user_profiles"
        cur.execute(query)
        result = cur.fetchall()
        return result
