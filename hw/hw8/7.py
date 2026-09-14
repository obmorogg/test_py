
"""## Задание 7 ⭐. Бронирование места

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
"""

class UserBaseException(Exception):
    pass

class BookingError(UserBaseException):
    def __str__(self):
        return f"BookingError"

class InvalidSeatError(BookingError):
    def __str__(self):
        return f"InvalidSeatError"

class SeatOccupiedError(BookingError):
    def __str__(self):
        return f"SeatOccupiedError"

def book_seat(seats, seat_number):
    if seat_number not in range(1,11):
        print(f'Места {seat_number} не существует')
        raise InvalidSeatError()
    elif seat_number in  range(1,11) and seat_number in seats:
        print(f'Место {seat_number} уже занято')
        raise SeatOccupiedError()
    print(f'Место {seat_number} забронировано')
    seats.append(seat_number)
    return



seats = [2, 5, 8]



try:
    print(book_seat(seats, 7))
    print(book_seat(seats, 5))
except BookingError as error:
    print(error)