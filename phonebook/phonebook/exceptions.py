
class PhoneBookError(Exception):
    pass

class ContactNotFoundError(PhoneBookError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Контакт {self.value} не найден"

class DuplicateContactError(PhoneBookError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Контакт {self.value} уже существует"

class InvalidPhoneError(PhoneBookError):
    def __init__(self, value):
        self.value = value
        print('asd')
    def __str__(self):
        return f"Номер {self.value} некорректен"

class InvalidNameError(PhoneBookError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Имя {self.value} некорректно"

class InvalidCompanyError(PhoneBookError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Компания {self.value} некорректна"

class InvalidRelationError(PhoneBookError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Отношение {self.value} некорректно"


