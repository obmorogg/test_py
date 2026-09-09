'''
# Домашнее задание по ООП

## Задание 1. Фильм

Создайте класс:

```python
Movie
```

При создании фильма передавайте:

* название;
* год выпуска;
* рейтинг.

Реализуйте методы:

```python
__str__()
__repr__()
```

`__str__()` должен возвращать удобное представление фильма для пользователя.

`__repr__()` должен показывать основные данные объекта.

### Пример работы

```python
movie = Movie("Интерстеллар", 2014, 8.7)

print(movie)
print([movie])
```

### Пример результата

```text
Интерстеллар (2014), рейтинг: 8.7
[Movie("Интерстеллар", 2014, 8.7)]
```

########################################################################################################################
'''
class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def __str__(self):
        return f'{self.title} ({self.year}), рейтинг: {self.rating}'

    def __repr__(self):
        return f'Movie("{self.title}", {self.year}, {self.rating})'

movie = Movie("Интерстеллар", 2014, 8.7)

print(movie)
print([movie])


'''
########################################################################################################################


---

## Задание 2. Очередь задач

Создайте класс:

```python
TaskQueue
```

Внутри должен храниться список задач.

Добавьте методы:

```python
add_task(task)
complete_task()
__len__()
```

`add_task()` добавляет задачу в конец очереди.

`complete_task()` удаляет и возвращает первую задачу.

Если очередь пуста, `complete_task()` должен вернуть `None`.

`len(queue)` должен возвращать количество оставшихся задач.

### Пример работы

```python
queue = TaskQueue()

queue.add_task("Ответить на письмо")
queue.add_task("Проверить отчёт")
queue.add_task("Позвонить клиенту")

print(queue.complete_task())
print(len(queue))
```

### Результат

```text
Ответить на письмо
2
```

########################################################################################################################
'''
class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)

    def complete_task(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def __len__(self):
        return len(self.queue)

queue = TaskQueue()

queue.add_task("Ответить на письмо")
queue.add_task("Проверить отчёт")
queue.add_task("Позвонить клиенту")

print(queue.complete_task())
print(len(queue))


'''
########################################################################################################################


---

## Задание 3. Кошелёк

Создайте класс:

```python
Wallet
```

При создании передавайте количество денег.

Реализуйте:

```python
__str__()
__add__()
```

При сложении двух кошельков должен создаваться новый объект `Wallet`, содержащий общую сумму.

Исходные объекты изменяться не должны.

### Пример

```python
wallet1 = Wallet(1500)
wallet2 = Wallet(2300)

wallet3 = wallet1 + wallet2

print(wallet1)
print(wallet2)
print(wallet3)
```

### Результат

```text
Баланс: 1500 руб.
Баланс: 2300 руб.
Баланс: 3800 руб.
```

---

########################################################################################################################
'''
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Баланс: {self.amount} руб.'

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

wallet1 = Wallet(1500)
wallet2 = Wallet(2300)

wallet3 = wallet1 + wallet2

print(wallet1)
print(wallet2)
print(wallet3)
'''
########################################################################################################################


## Задание 4. Сравнение посылок

Создайте класс:

```python
Parcel
```

При создании передавайте:

* название;
* вес.

Две посылки считаются равными, если их вес одинаковый.

Также должна поддерживаться возможность сравнения:

```python
parcel1 < parcel2
parcel1 > parcel2
parcel1 <= parcel2
parcel1 >= parcel2
```

Реализуйте:

```python
__eq__()
__lt__()
```

и используйте:

```python
from functools import total_ordering
```

Для упрощения считаем, что сравниваются только объекты `Parcel`.

### Пример

```python
parcel1 = Parcel("Книги", 4)
parcel2 = Parcel("Техника", 7)
parcel3 = Parcel("Одежда", 4)

print(parcel1 < parcel2)
print(parcel1 == parcel3)
print(parcel2 > parcel1)
```

### Результат

```text
True
True
True
```

---
########################################################################################################################
'''
from functools import total_ordering

@total_ordering
class Parcel:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

parcel1 = Parcel("Книги", 4)
parcel2 = Parcel("Техника", 7)
parcel3 = Parcel("Одежда", 4)

print(parcel1 < parcel2)
print(parcel1 == parcel3)
print(parcel2 < parcel1)

'''
########################################################################################################################



## Задание 5. Тарифы доставки

Создайте родительский класс:

```python
Delivery
```

Он принимает вес посылки и содержит метод:

```python
calculate()
```

Создайте дочерние классы:

```python
StandardDelivery
CourierDelivery
ExpressDelivery
```

Правила расчёта:

```text
StandardDelivery: 100 + вес * 20
CourierDelivery: 300 + вес * 40
ExpressDelivery: 500 + вес * 70
```

Переопределите метод `calculate()`.

После этого создайте список разных доставок и вызовите `calculate()` у каждой через один цикл.

Тип объекта через `if` проверять не нужно.

### Пример

```python
deliveries = [
    StandardDelivery(5),
    CourierDelivery(5),
    ExpressDelivery(5)
]

for delivery in deliveries:
    print(delivery.calculate())
```

### Результат

```text
200
500
850
```

---

########################################################################################################################
'''

class Delivery:
    def __init__(self, weight):
        self.weight = weight

    def calculate(self):
        return -1
        pass

class StandardDelivery(Delivery):
    def calculate(self):
        return 100 + self.weight * 20
        pass

class CourierDelivery(Delivery):
    def calculate(self):
        return 300 + self.weight * 40
        pass

class ExpressDelivery(Delivery):
    def calculate(self):
        return 500 + self.weight * 70
        pass

deliveries = [
    StandardDelivery(5),
    CourierDelivery(5),
    ExpressDelivery(5)
]

for delivery in deliveries:
    print(delivery.calculate())

'''
########################################################################################################################


## Задание 6. Туристический дрон

Создайте два независимых класса:

```python
CameraModule
NavigationModule
```

`CameraModule` содержит:

```python
take_photo()
```

`NavigationModule` содержит:

```python
build_route(city)
```

Создайте класс:

```python
TravelDrone
```

который наследуется одновременно от `CameraModule` и `NavigationModule`.

Сам дрон должен иметь название и метод:

```python
fly()
```

### Пример

```python
drone = TravelDrone("Explorer")

print(drone.fly())
print(drone.take_photo())
print(drone.build_route("Сочи"))
```

### Результат

```text
Explorer начал полёт
Фотография сделана
Маршрут построен до: Сочи
```

---

########################################################################################################################
'''
class CameraModule:
    def take_photo(self):
        return "Фотография сделана"

class NavigationModule:
    def build_route(self, city):
        return f"Маршрут построен до:{city}"

class TravelDrone(CameraModule, NavigationModule):
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name}, начал полёт"

drone = TravelDrone("Explorer")

print(drone.fly())
print(drone.take_photo())
print(drone.build_route("Сочи"))

'''
########################################################################################################################


## Задание 7. Абстрактный медиаплеер

Создайте абстрактный класс:

```python
MediaFile
```

Используйте:

```python
from abc import ABC, abstractmethod
```

При создании объекта передавайте название файла.

Добавьте абстрактный метод:

```python
play()
```

Создайте дочерние классы:

```python
AudioFile
VideoFile
Podcast
```

Каждый класс должен реализовать `play()` по-своему.

### Пример

```python
files = [
    AudioFile("music.mp3"),
    VideoFile("lesson.mp4"),
    Podcast("python.mp3")
]

for file in files:
    print(file.play())
```

### Результат

```text
Воспроизводим аудио: music.mp3
Воспроизводим видео: lesson.mp4
Запускаем подкаст: python.mp3
```

Создать напрямую:

```python
MediaFile("file")
```

быть не должно возможно.

---

########################################################################################################################
'''
from abc import ABC, abstractmethod
class MediaFile:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self):
        return f"Воспроизводим {self.name}"

class AudioFile(MediaFile):
    def play(self):
        return f"Воспроизводим аудио: {self.name}"

class VideoFile(MediaFile):
    def play(self):
        return f"Воспроизводим видео: {self.name}"

class Podcast(MediaFile):
    def play(self):
        return f"Запускаем подкаст: {self.name}"

files = [
    AudioFile("music.mp3"),
    VideoFile("lesson.mp4"),
    Podcast("python.mp3")
]

for file in files:
    print(file.play())
'''
########################################################################################################################


# Задания со звёздочкой ⭐

## Задание 8 ⭐. Книжная полка

Создайте класс:

```python
BookShelf
```

Внутри хранится список названий книг.

Реализуйте:

```python
__len__()
__str__()
__add__()
```

`len(shelf)` возвращает количество книг.

`print(shelf)` выводит книги по одной строке.

При сложении двух полок должна создаваться новая полка с книгами обеих исходных полок.

### Пример

```python
shelf1 = BookShelf(["1984", "Дюна"])
shelf2 = BookShelf(["Солярис", "Марсианин"])

shelf3 = shelf1 + shelf2

print(shelf3)
print("Книг:", len(shelf3))
```

### Результат

```text
1984
Дюна
Солярис
Марсианин
Книг: 4
```

---

########################################################################################################################
'''
class BookShelf:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return "\n".join(self.books)

    def __add__(self, other):
        return BookShelf(self.books + other.books)

shelf1 = BookShelf(["1984", "Дюна"])
shelf2 = BookShelf(["Солярис", "Марсианин"])

shelf3 = shelf1 + shelf2

print(shelf3)
print(f"Книг:{len(shelf3)}")
'''
########################################################################################################################


## Задание 9 ⭐. Версии программы

Создайте класс:

```python
Version
```

Версия передаётся строкой:

```text
"2.5.10"
```

Она состоит из:

```text
major.minor.patch
```

Необходимо поддержать:

```python
==
!=
<
>
<=
>=
```

Сравнение выполняется последовательно:

1. `major`;
2. `minor`;
3. `patch`.

Используйте:

```python
__eq__()
__lt__()
```

и:

```python
from functools import total_ordering
```

Также реализуйте `__str__()`.

Для упрощения считаем, что строка версии всегда корректная и содержит ровно три числа.

### Пример

```python
v1 = Version("1.10.0")
v2 = Version("1.2.9")
v3 = Version("2.0.0")

print(v1 > v2)
print(v1 < v3)
print(v1)
```

### Результат

```text
True
True
1.10.0
```

---

########################################################################################################################
'''
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self.version = version

    def __str__(self):
        return self.version
    def __eq__(self, other):
        return self.version == other.version
    def __lt__(self, other): # для простоты рассчетов считаем что разрядность версии 3 знака
        return self.version.split(".")[0] * 1000000 + self.version.split(".")[1] * 10000 + self.version.split(".")[2] * 100 < other.version.split(".")[0] * 1000000 + other.version.split(".")[1] * 10000 + other.version.split(".")[2] * 100

v1 = Version("1.10.0")
v2 = Version("1.2.9")
v3 = Version("2.0.0")

print(v1 > v2)
print(v1 < v3)
print(v1)

'''
########################################################################################################################


## Задание 10 ⭐. Двумерный вектор

Создайте класс:

```python
Vector2D
```

Он хранит:

```python
x
y
```

Реализуйте:

```python
__str__()
__add__()
__sub__()
__eq__()
__call__()
```

### Сложение

```text
(x1, y1) + (x2, y2)
=
(x1 + x2, y1 + y2)
```

### Вычитание

```text
(x1, y1) - (x2, y2)
=
(x1 - x2, y1 - y2)
```

Два вектора равны, если совпадают обе координаты.

При вызове объекта:

```python
vector(3)
```

должен возвращаться новый вектор, координаты которого умножены на `3`.

### Пример

```python
v1 = Vector2D(2, 3)
v2 = Vector2D(4, 1)

print(v1 + v2)
print(v1 - v2)
print(v1 == Vector2D(2, 3))
print(v1(3))
```

### Результат

```text
(6, 4)
(-2, 2)
True
(6, 9)
```

Исходные векторы изменяться не должны.

---

########################################################################################################################
'''

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return f'({self.x + other.x}, {self.y + other.y})'

    def __sub__(self, other):
        return f'({self.x - other.x}, {self.y - other.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __call__(self, num):
        return f'({self.x * num}, {self.y * num})'

v1 = Vector2D(2, 3)
v2 = Vector2D(4, 1)
print(v1 + v2)
print(v1 - v2)
print(v1 == Vector2D(2, 3))
print(v1(3))

'''
########################################################################################################################


## Задание 11 ⭐. Цепочка обработки данных

Создайте классы:

```python
BaseProcessor
ValidationProcessor
LoggingProcessor
```

`BaseProcessor` содержит метод:

```python
process(data)
```

который возвращает:

```text
Обработано: <данные>
```

`ValidationProcessor` реализует `process()`:

* если строка пустая, возвращает `"Нет данных"`;
* иначе передаёт выполнение следующему классу через `super()`.

`LoggingProcessor`:

* выводит `"LOG: <данные>"`;
* затем передаёт выполнение дальше через `super()`.

Создайте класс:

```python
DataService
```

с множественным наследованием:

```python
LoggingProcessor
ValidationProcessor
BaseProcessor
```

### Пример

```python
service = DataService()

print(service.process("Python"))
print(service.process(""))
```

### Результат

```text
LOG: Python
Обработано: Python
LOG:
Нет данных
```

Дополнительно выведите:

```python
DataService.mro()
```

и посмотрите порядок поиска методов.

> Подсказка: каждый промежуточный `process()` должен передавать работу следующему классу с помощью `super()`.

---

########################################################################################################################
'''

class BaseProcessor:
    def process(self, data):
        return f'Обработано: {data}'

class ValidationProcessor(BaseProcessor):
    def process(self, data):
        return super().process(data) if data else 'Нет данных'

class LoggingProcessor(BaseProcessor):
    def process(self, data):
        print(f'LOG: {data}')
        return super().process(data)

class DataService(LoggingProcessor, ValidationProcessor, BaseProcessor):
    pass


service = DataService()

print(service.process("Python"))
print(service.process(""))

print(DataService.mro())

'''
########################################################################################################################


## Задание 12 ⭐. Многочлен

Создайте класс:

```python
Polynomial
```

Коэффициенты передаются списком.

Например:

```python
Polynomial([2, 3, 1])
```

означает:

```text
2x² + 3x + 1
```

Для упрощения считаем, что складываемые многочлены имеют одинаковое количество коэффициентов.

Реализуйте:

```python
__str__()
__add__()
__call__()
```

### `__str__()`

Должен возвращать многочлен в читаемом виде:

```text
2x^2 + 3x + 1
```

Для упрощения можно:

* не убирать коэффициенты, равные `0`;
* не делать отдельное красивое форматирование отрицательных коэффициентов.

Например допустимо:

```text
2x^2 + 0x + 1
2x^2 + -3x + 1
```

### `__add__()`

Позволяет складывать многочлены.

```python
p1 = Polynomial([2, 3, 1])
p2 = Polynomial([1, 0, 4])

p3 = p1 + p2
```

Получаем:

```text
3x^2 + 3x + 5
```

### `__call__()`

Объект должен работать как функция.

```python
p1(2)
```

для:

```text
2x² + 3x + 1
```

означает:

```text
2 * 2² + 3 * 2 + 1
```

### Пример

```python
p1 = Polynomial([2, 3, 1])
p2 = Polynomial([1, 0, 4])

p3 = p1 + p2

print(p1)
print(p3)
print(p1(2))
```

### Результат

```text
2x^2 + 3x + 1
3x^2 + 3x + 5
15
```
########################################################################################################################
'''
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        return f'{self.coeffs[0]}x^2 {'+' if self.coeffs[1] > 0 else '-'} {abs(self.coeffs[1])} x {'+' if self.coeffs[2] > 0 else '-'} {abs(self.coeffs[2])}'

    def __add__(self, other):
        return Polynomial([x + y for x, y in zip(self.coeffs, other.coeffs)])

    def __call__(self, num):
        return sum(coeff * num ** (len(self.coeffs) - 1 - i) for i, coeff in enumerate(self.coeffs))


p1 = Polynomial([2, 3, 1])
p2 = Polynomial([1, 0, 4])

p3 = p1 + p2

print(p1)
print(p3)
print(p1(2))


'''
########################################################################################################################
---

# Проект: Телефонный справочник. Часть 4

Продолжите дорабатывать телефонный справочник.

Сильно усложнять программу не нужно.

Теперь добавьте наследование, полиморфизм и dunder-методы.

## Базовый класс Contact

Создайте:

```python
Contact
```

Он хранит:

```python
name
phone
```

Реализуйте:

```python
__str__()
```

### Пример

```python
contact = Contact("Анна", "12345")

print(contact)
```

### Результат

```text
Анна | 12345
```

---

## Личный контакт

Создайте класс:

```python
PersonalContact
```

Он наследуется от `Contact`.

Дополнительно храните:

```python
relation
```

Например:

```text
друг
родственник
знакомый
```

Переопределите `__str__()`.

### Пример результата

```text
Анна | 12345 | друг
```

---

## Рабочий контакт

Создайте класс:

```python
WorkContact
```

Он также наследуется от `Contact`.

Дополнительно храните:

```python
company
```

### Пример результата

```text
Иван | 67890 | SkyPro
```

---

## Класс PhoneBook

Внутри по-прежнему хранится список контактов:

```python
self.contacts = []
```

Сохраните методы:

```python
add_contact()
find_contact()
update_contact()
delete_contact()
```

Добавьте:

```python
__len__()
__str__()
```

Теперь:

```python
len(phone_book)
```

должен возвращать количество контактов.

А:

```python
print(phone_book)
```

должен выводить все контакты.

### Пример

```python
phone_book = PhoneBook()

phone_book.add_contact(
    PersonalContact("Анна", "12345", "друг")
)

phone_book.add_contact(
    WorkContact("Иван", "67890", "SkyPro")
)

print(phone_book)
print("Всего контактов:", len(phone_book))
```

### Результат

```text
Анна | 12345 | друг
Иван | 67890 | SkyPro

Всего контактов: 2
```

Объекты `PersonalContact` и `WorkContact` должны храниться вместе в одном списке и корректно выводиться через общий код.

---

'''