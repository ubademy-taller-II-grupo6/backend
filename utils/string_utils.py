import re
import constants.regular_expresions as regular_expressions


def contains_lower_case(string):
    if not re.search(regular_expressions.LOWER_CASE, string):
        return False
    return True


def contains_upper_case(string):
    if not re.search(regular_expressions.UPPER_CASE, string):
        return False
    return True


def contains_number(string):
    if not re.search(regular_expressions.NUMBER, string):
        return False
    return True


def is_email(string):
    if not re.search(regular_expressions.EMAIL, string):
        return False
    return True


def is_text(string):
    if not re.search(regular_expressions.TEXT, string):
        return False
    return True
