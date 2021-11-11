import re
import app.regular_expresions as regular_expressions


def is_email(string):
    if not re.search(regular_expressions.EMAIL, string):
        return False
    return True


def is_text(string):
    if not re.search(regular_expressions.TEXT, string):
        return False
    return True


def create_message_response(message):
    return {
        "message": message
    }


def to_bool(string):
    string = str(string).upper()
    if string == "TRUE":
        return True
    if string == "FALSE":
        return False
    return None
