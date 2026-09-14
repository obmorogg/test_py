"""
## Задание 6. Проверка данных через `raise`

Напишите функцию:

```python
create_user(name, age)
```

Правила для имени:

* значение должно быть строкой;
* строка не должна быть пустой;
* имя должно содержать только буквы.

Правила для возраста:

* значение должно быть целым числом;
* возраст должен быть от `1` до `119`.

Используйте:

* `TypeError` — если передан неправильный тип;
* `ValueError` — если тип правильный, но значение некорректно.

Исключения нужно создавать самостоятельно через `raise`.

Если данные корректны, функция возвращает:

```python
{
    "name": "Анна",
    "age": 25
}
```

### Пример

```python
try:
    user = create_user("Анна", 25)
    print(user)
except (ValueError, TypeError) as error:
    print(error)
```

### Результат

```text
{'name': 'Анна', 'age': 25}
```

"""
class UserBaseException(Exception):
    pass

class EmptyString(UserBaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"строка не должна быть пустой"

class NonAlphaString(UserBaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"имя должно содержать только буквы ({self.value})"

class WrongAge(UserBaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"возраст должен бытьцелым числом от `1` до `119` ({self.value})"

def create_user(name:str, age):
    """create_user
    Args:
        name (str): 
        * строка не должна быть пустой;
        * имя должно содержать только буквы.
        age (str): 
        * значение должно быть целым числом;
        * возраст должен быть от `1` до `119`.
    """
    if name == '':
        raise EmptyString("EmptyString")
    elif not name.isalpha():
        raise NonAlphaString(name)
    elif not (int(age) >= 1 and int(age) <= 119):
        raise WrongAge(age)
    # print(name)
    return {'name':name,'age':age}

try:
    print(create_user('asd',1111))
except (EmptyString, NonAlphaString, WrongAge) as error:
    print(error)
