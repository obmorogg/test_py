import re

def hide_phone(phone):
    """"+79991234567" → "+7999***4567"

    Args:
        phone (str): без валидации
    """
    return re.sub("^(\+\d{4}).*?(\d{4})$", r"\1***\2", phone)