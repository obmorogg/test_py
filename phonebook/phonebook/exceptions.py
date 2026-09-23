"""
## `exceptions.py`

Создайте:

```python
PhoneBookError
ContactNotFoundError
DuplicateContactError
```

`PhoneBookError` наследуется от `Exception`.

Остальные исключения наследуются от `PhoneBookError`.

"""

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

