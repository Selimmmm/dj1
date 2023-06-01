import re


def validate_data(first_name, last_name, tel, email, message):
    return {
        "first_name": validate_is_not_empty(first_name),
        "last_name": validate_is_not_empty(last_name),
        "tel": validate_tel(tel),
        "email": validate_email(email),
        "message": True,
    }


def validate_tel(tel):
    return tel.isnumeric()


def validate_email(email):
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def validate_is_not_empty(text):
    if text is None:
        return False
    return len(text) > 1
