# Домашнее задание. Модули, пакеты и исключения

## Задание 1. Модуль конвертации времени

Создайте модуль:

```text
time_tools.py
```

Добавьте функции:

```python
minutes_to_hours(minutes)
hours_to_minutes(hours)
```

Первая переводит минуты в часы, вторая — часы в минуты.

В файле `main.py` импортируйте обе функции и вызовите их.

### Пример

```python
print(minutes_to_hours(150))
print(hours_to_minutes(3))
```

### Результат

```text
2.5
180
```

---

## Задание 2. Модуль с тестовым запуском

Создайте модуль:

```text
price_tools.py
```

Реализуйте функцию:

```python
apply_discount(price, percent)
```

Она возвращает цену после применения скидки.

Добавьте в `price_tools.py` несколько тестовых вызовов функции, но сделайте так, чтобы они выполнялись только при непосредственном запуске файла.

Используйте:

```python
if __name__ == "__main__":
```

В отдельном `main.py` импортируйте функцию.

### Пример

```python
print(apply_discount(2000, 15))
```

### Результат

```text
1700.0
```

При импорте `price_tools` тестовые вызовы выполняться не должны.

---

## Задание 3. Собственный пакет

Создайте пакет:

```text
text_tools/
    __init__.py
    names.py
    phones.py

main.py
```

В `names.py` реализуйте:

```python
format_name(name)
```

Функция должна убрать пробелы по краям и привести имя к нормальному виду:

```text
"   иВАН   " → "Иван"
```

В `phones.py` реализуйте:

```python
hide_phone(phone)
```

Пример:

```text
"+79991234567" → "+7999***4567"
```

Настройте `__init__.py` и `__all__`, чтобы функции можно было импортировать так:

```python
from text_tools import format_name, hide_phone
```

### Пример

```python
print(format_name("   аННА   "))
print(hide_phone("+79991234567"))
```

### Результат

```text
Анна
+7999***4567
```

---

## Задание 4. Безопасный ввод числа

Напишите функцию:

```python
get_positive_number()
```

Она должна запрашивать положительное целое число.

Если пользователь вводит значение, которое нельзя преобразовать в `int`, обработайте `ValueError` и попросите повторить ввод.

Если число равно `0` или меньше `0`, также запросите значение ещё раз.

### Пример

```text
Введите количество: abc
Необходимо ввести целое число

Введите количество: -5
Число должно быть больше нуля

Введите количество: 7
```

Функция возвращает:

```text
7
```

---

## Задание 5. Расчёт стоимости заказа

Напишите функцию:

```python
calculate_order(price, quantity)
```

Значения могут передаваться строками:

```python
calculate_order("125.5", "4")
```

Внутри функции преобразуйте:

* `price` в `float`;
* `quantity` в `int`.

Обработайте:

* `ValueError` — значение невозможно преобразовать в число;
* `TypeError` — передан неподходящий тип данных.

Если ошибок нет, в блоке `else` верните стоимость заказа.

В `finally` всегда выводите:

```text
Расчёт завершён
```

### Пример 1

```python
print(calculate_order("125.5", "4"))
```

### Результат

```text
Расчёт завершён
502.0
```

### Пример 2

```python
print(calculate_order("сто", "4"))
```

### Результат

```text
Некорректное числовое значение
Расчёт завершён
None
```

---

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

---

# Задания со звёздочкой ⭐

## Задание 7 ⭐. Бронирование места

Создайте собственную иерархию исключений:

```python
BookingError
InvalidSeatError
SeatOccupiedError
```

`BookingError` наследуется от `Exception`.

Остальные исключения наследуются от `BookingError`.

Напишите функцию:

```python
book_seat(seats, seat_number)
```

`seats` — список занятых мест:

```python
seats = [2, 5, 8]
```

В зале есть места от `1` до `10`.

Функция должна:

* вызвать `InvalidSeatError`, если такого места не существует;
* вызвать `SeatOccupiedError`, если место уже занято;
* добавить место в список, если бронирование возможно.

### Пример

```python
seats = [2, 5, 8]

try:
    print(book_seat(seats, 7))
    print(book_seat(seats, 5))
except BookingError as error:
    print(error)
```

### Результат

```text
Место 7 забронировано
Место 5 уже занято
```

---

## Задание 8 ⭐. Пакет обработки заказов

Создайте пакет:

```text
order_system/
    __init__.py
    exceptions.py
    validators.py
    calculator.py

main.py
```

### `exceptions.py`

Создайте:

```python
OrderError
InvalidPriceError
InvalidQuantityError
InvalidDiscountError
```

`OrderError` — базовое исключение.

Остальные наследуются от него.

### `validators.py`

Реализуйте:

```python
validate_price(price)
validate_quantity(quantity)
validate_discount(discount)
```

Правила:

* цена должна быть больше `0`;
* количество должно быть целым числом и больше `0`;
* скидка должна быть от `0` до `50`.

При ошибках вызывайте соответствующие собственные исключения.

### `calculator.py`

Реализуйте:

```python
calculate_total(price, quantity, discount=0)
```

Алгоритм:

1. Посчитать стоимость:

```text
price * quantity
```

2. Вычесть указанный процент скидки.

Например:

```text
1000 * 3 = 3000
скидка 10% = 300
итого = 2700
```

Перед расчётом используйте функции из `validators.py`.

### `__init__.py`

Настройте пакет так, чтобы работал импорт:

```python
from order_system import calculate_total, OrderError
```

### `main.py`

Запросите:

* цену;
* количество;
* скидку.

Обработайте:

* `ValueError` при преобразовании введённых значений;
* `OrderError` и его дочерние исключения.

Если ошибок нет, выведите результат в `else`.

В `finally` всегда выводите:

```text
Обработка заказа завершена
```

### Пример

```text
Цена: 1000
Количество: 3
Скидка: 10

Итого: 2700.0
Обработка заказа завершена
```

---

# Проект: Телефонный справочник. Часть 5

Продолжите работу с телефонным справочником.

Существующую функциональность сохраняем, но теперь программу необходимо разделить на пакет и добавить собственные исключения.

## Структура

```text
phonebook/
    __init__.py
    contacts.py
    service.py
    exceptions.py

main.py
```

## `contacts.py`

Перенесите классы:

```python
Contact
PersonalContact
WorkContact
```

---

## `exceptions.py`

Создайте:

```python
PhoneBookError
ContactNotFoundError
DuplicateContactError
```

`PhoneBookError` наследуется от `Exception`.

Остальные исключения наследуются от `PhoneBookError`.

---

## `service.py`

Перенесите сюда класс:

```python
PhoneBook
```

Сохраните методы:

```python
add_contact()
find_contact()
update_contact()
delete_contact()
```

### `add_contact()`

Если контакт с таким именем уже существует:

```python
raise DuplicateContactError(...)
```

### `find_contact()`

Если контакт не найден:

```python
raise ContactNotFoundError(...)
```

### `update_contact()` и `delete_contact()`

Если контакта нет, должно возникать `ContactNotFoundError`.

---

## `__init__.py`

Настройте пакет так, чтобы можно было написать:

```python
from phonebook import (
    PhoneBook,
    PersonalContact,
    WorkContact,
    PhoneBookError
)
```

---

## `main.py`

Меню:

```text
1. Добавить личный контакт
2. Добавить рабочий контакт
3. Показать все контакты
4. Найти контакт
5. Изменить контакт
6. Удалить контакт
7. Выйти
```

Ошибки справочника обрабатывайте через:

```python
try:
    ...
except PhoneBookError as error:
    print(error)
```

### Пример

```text
Введите имя: Анна
Введите телефон: 12345
Контакт добавлен

Введите имя: Анна
Введите телефон: 99999
Контакт с именем Анна уже существует
```

При поиске отсутствующего контакта:

```text
Контакт Иван не найден
```

---

