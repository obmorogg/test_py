'''
# Домашнее задание по ООП

## Задание 1. Книга

Создайте класс:

```python
Book
```

При создании книги передавайте:

* название;
* автора;
* количество страниц.

Добавьте метод:

```python
show_info()
```

### Пример работы

```python
book = Book("1984", "Джордж Оруэлл", 328)
book.show_info()
```

### Результат

```text
Название: 1984
Автор: Джордж Оруэлл
Страниц: 328
```
'''
##################################################################################


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Страниц: {self.pages}")

book = Book("1984", "Джордж Оруэлл", 328)
book.show_info()


##################################################################################
'''

---

## Задание 2. Плейлист

Создайте класс:

```python
Playlist
```

У плейлиста должно быть название и список песен.

При создании объекта список песен пустой.

Добавьте методы:

```python
add_song(song)
show_songs()
songs_count()
```

`add_song()` добавляет песню в плейлист.

`show_songs()` выводит все песни.

`songs_count()` возвращает количество песен.

### Пример работы

```python
playlist = Playlist("Для работы")

playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

playlist.show_songs()
print("Количество песен:", playlist.songs_count())
```

### Результат

```text
Song 1
Song 2
Song 3
Количество песен: 3
```

---
'''
##################################################################################
class playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def show_songs(self):
        for song in self.songs:
            print(song)

    def songs_count(self):
        return len(self.songs)

a = playlist()

a.add_song('asd')
a.add_song('qwe')


a.show_songs()
print(a.songs_count())


##################################################################################
'''
## Задание 3. Трекер активности

Создайте класс:

```python
FitnessTracker
```

При создании объекта количество шагов должно быть равно `0`.

Добавьте методы:

```python
add_steps(count)
get_steps()
get_distance()
reset()
```

### Требования

`add_steps(count)` добавляет указанное количество шагов.

Нельзя добавить отрицательное количество шагов.

`get_steps()` возвращает текущее количество шагов.

`get_distance()` возвращает примерное пройденное расстояние в километрах.

Считайте, что один шаг равен:

```text
0.0008 км
```

`reset()` сбрасывает количество шагов до `0`.

### Пример работы

```python
tracker = FitnessTracker()

tracker.add_steps(3000)
tracker.add_steps(2000)

print("Шагов:", tracker.get_steps())
print("Расстояние:", tracker.get_distance(), "км")

tracker.reset()

print("Шагов:", tracker.get_steps())
```

### Результат

```text
Шагов: 5000
Расстояние: 4.0 км
Шагов: 0
```

Если попытаться добавить отрицательное количество:

```python
tracker.add_steps(-500)
```

выведите:

```text
Некорректное количество шагов
```

---

'''
##################################################################################
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        pass
    def add_steps(self,count):
        if count < 0:
            print("Некорректное количество шагов")
        else:
            self.steps += count 
        pass
    def get_steps(self):
        return self.steps
        pass
    def get_distance(self):
        return self.steps * 0.0008
        pass
    def reset(self):
        self.steps = 0
        pass

tracker = FitnessTracker()

tracker.add_steps(3000)
tracker.add_steps(2000)

print("Шагов:", tracker.get_steps())
print("Расстояние:", tracker.get_distance(), "км")

tracker.reset()

print("Шагов:", tracker.get_steps())

##################################################################################
'''
---

## Задание 4. Игровой инвентарь

Создайте класс:

```python
Inventory
```

Внутри объекта должен храниться список предметов:

```python
self.items = []
```

Добавьте методы:

```python
add_item(item)
remove_item(item)
has_item(item)
show_items()
```

`add_item()` добавляет предмет.

`remove_item()` удаляет предмет, если он существует.

`has_item()` возвращает `True` или `False`.

`show_items()` выводит все предметы.

### Пример работы

```python
inventory = Inventory()

inventory.add_item("меч")
inventory.add_item("щит")
inventory.add_item("зелье")

inventory.remove_item("щит")

inventory.show_items()

print(inventory.has_item("меч"))
print(inventory.has_item("лук"))
```

### Результат

```text
меч
зелье
True
False
```

---

'''
##################################################################################
class Inventory:
    def __init__(self):
        self.items = []
        pass

    def add_item(self,item):
        self.items.append(item)
        pass
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Такого предмета нет в инвентаре")
        pass
    def has_item(self,item):
        if item in self.items:
            return True
        else:
            return False
        pass
    def show_items(self):
        for item in self.items:
            print(item)
        pass

inventory = Inventory()

inventory.add_item("меч")
inventory.add_item("щит")
inventory.add_item("зелье")

inventory.remove_item("щит")

inventory.show_items()

print(inventory.has_item("меч"))
print(inventory.has_item("лук"))

##################################################################################
'''
## Задание 5. Громкость аудиоплеера

Создайте класс:

```python
AudioPlayer
```

Уровень громкости должен храниться в приватном атрибуте:

```python
__volume
```

Добавьте методы:

```python
get_volume()
set_volume(volume)
volume_up()
volume_down()
```

Громкость может принимать значения только от `0` до `100`.

`volume_up()` увеличивает громкость на `10`.

`volume_down()` уменьшает громкость на `10`.

Значение не должно выходить за допустимые границы.

### Пример работы

```python
player = AudioPlayer(50)

player.volume_up()
player.volume_up()
player.volume_down()

print(player.get_volume())
```

### Результат

```text
60
```

При попытке установить некорректную громкость:

```python
player.set_volume(150)
```

должно появиться сообщение:

```text
Некорректная громкость
```

Старое значение при этом сохраняется.

---

'''
##################################################################################
class AudioPlayer:
    def __init__(self, volume):
        if volume < 0 or volume > 100:
            print("Некорректная громкость")
            self.__volume = 0
        else:
            self.__volume = volume
        pass
    def get_volume(self):
        return self.__volume
        pass
    def set_volume(self,volume):
        if volume < 0 or volume > 100:
            print("Некорректная громкость")
        else:
            self.__volume = volume
        pass
    def volume_up(self):
        if self.__volume + 10 > 100:
            self.__volume = 100
        else:
            self.__volume += 10
        pass
    def volume_down(self):
        if self.__volume - 10 < 0:
            self.__volume = 0
        else:
            self.__volume -= 10
        pass

player = AudioPlayer(50)

player.volume_up()
player.volume_up()
player.volume_down()

print(player.get_volume())

##################################################################################
'''
## Задание 6. Доставка посылок

Создайте родительский класс:

```python
Delivery
```

При создании передавайте:

* город;
* вес посылки.

Добавьте метод:

```python
calculate_price()
```

Создайте два дочерних класса:

```python
CourierDelivery
PostDelivery
```

Переопределите метод `calculate_price()`.

### Правила

Курьерская доставка:

```text
500 + 50 * вес
```

Почтовая доставка:

```text
200 + 30 * вес
```

### Пример работы

```python
courier = CourierDelivery("Москва", 3)
post = PostDelivery("Казань", 3)

print(courier.calculate_price())
print(post.calculate_price())
```

### Результат

```text
650
290
```

После этого создайте список разных доставок и одним циклом выведите стоимость каждой.

##################################################################################
'''
class Delivery:
    def __init__(self,town,weight):
        self.town = town
        self.weight = weight

    def calculate_price(self):
        return -1
        pass

class CourierDelivery(Delivery):
    def calculate_price(self):
        return 500 + 50 * self.weight

class PostDelivery(Delivery):
    def calculate_price(self):
        return 200 + 30 * self.weight

nop = Delivery("НН", 3)
courier = CourierDelivery("Москва", 3)
post = PostDelivery("Казань", 3)

print(nop.calculate_price())
print(courier.calculate_price())
print(post.calculate_price())



'''
##################################################################################
---

## Задание 7. Обработка уведомлений

Создайте родительский класс:

```python
Notification
```

Он принимает текст сообщения и содержит метод:

```python
send()
```

Создайте два дочерних класса:

```python
EmailNotification
SmsNotification
```

Переопределите метод `send()`.

После этого создайте список:

```python
notifications = [
    EmailNotification("Первое сообщение"),
    SmsNotification("Второе сообщение"),
    EmailNotification("Третье сообщение")
]
```

С помощью одного цикла:

1. вызовите `send()` у каждого объекта;
2. с помощью `isinstance()` посчитайте количество Email- и SMS-уведомлений.

### Пример результата

```text
Email: Первое сообщение
SMS: Второе сообщение
Email: Третье сообщение

Email: 2
SMS: 1
```

---

'''
##################################################################################
class Notification:
    def __init__(self):
        self.text = ""
        pass
    def send(self):
        print(self.text)
        pass

class EmailNotification(Notification):
    def __init__(self,text):
        self.text = text

class SmsNotification(Notification):
    def __init__(self,text):
        self.text = text


notifications = [
    EmailNotification("Первое сообщение"),
    SmsNotification("Второе сообщение"),
    EmailNotification("Третье сообщение")
]

sms_cnt = 0
email_cnt = 0

for i in notifications:
    if isinstance(i, EmailNotification):
        email_cnt += 1
    else:
        sms_cnt += 1
    i.send()

print(f"Email: {email_cnt}")
print(f"SMS: {sms_cnt}")
'''
##################################################################################
# Задания со звёздочкой ⭐

## Задание 8 ⭐. Система бронирования мест

Создайте класс:

```python
CinemaHall
```

При создании передавайте количество мест.

Количество свободных мест храните в приватном атрибуте:

```python
__free_seats
```

Добавьте методы:

```python
book(count)
cancel(count)
get_free_seats()
```

### Правила

`book(count)`:

* уменьшает количество свободных мест;
* нельзя забронировать больше мест, чем доступно;
* нельзя передавать отрицательное количество.

`cancel(count)`:

* возвращает места;
* количество свободных мест не должно становиться больше первоначального количества мест.

### Пример работы

```python
hall = CinemaHall(100)

hall.book(20)
hall.book(30)

print(hall.get_free_seats())

hall.cancel(10)

print(hall.get_free_seats())
```

### Результат

```text
50
60
```
'''
##################################################################################

class CinemaHall:
    def __init__(self, free_seats):
        if free_seats <= 0:
            print(f'Cinema closed(no seats)')
            exit()
        self.__free_seats = free_seats
        self.__all_seats = free_seats
        print(f'Cinema open for: {free_seats} seats')

    def book(self, count):
        if count > self.__free_seats or count <= 0:
            return False
        self.__free_seats -= count
        return count

    def cancel(self, count):
        if count > self.__all_seats - self.__free_seats or count <= 0:
            return False
        self.__free_seats += count
        return count

    @property
    def get_free_seats(self):
        return self.__free_seats

    @property
    def get_all_seats(self):
        return self.__all_seats

    @property
    def get_book_seats(self):
        return self.__all_seats - self.__free_seats


hall = CinemaHall(9)
print(f"Booking: {hall.book(6) or 'Nothing'}, Free seats: {hall.get_free_seats}")
print(f"Cancel booking: {hall.cancel(5) or 'Nothing'} goes to free, Free seats: {hall.get_free_seats}") 
print(f"Free seats: {hall.get_free_seats}")
print(f"All seats: {hall.get_all_seats}")
print(f"Booked seats: {hall.get_book_seats}")
'''
##################################################################################
---

## Задание 9 ⭐. Игровые персонажи

Создайте родительский класс:

```python
Character
```

Он принимает:

* имя;
* силу.

Добавьте метод:

```python
attack()
```

Создайте дочерние классы:

```python
Warrior
Mage
Archer
```

Каждый класс должен по-своему рассчитывать силу атаки.

### Правила

Воин:

```text
сила * 2
```

Маг:

```text
сила * 3
```

Лучник:

```text
сила + 10
```

### Пример

```python
characters = [
    Warrior("Рагнар", 20),
    Mage("Мерлин", 20),
    Archer("Робин", 20)
]

for character in characters:
    print(character.attack())
```

### Результат

```text
Рагнар наносит 40 урона
Мерлин наносит 60 урона
Робин наносит 30 урона
```
'''
##################################################################################

class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f"{self.name} наносит {self.power * 2} урона"

class Warrior(Character):
    def attack(self):
        return f"{self.name} наносит {self.power * 2} урона"

class Mage(Character):
    def attack(self):
        return f"{self.name} наносит {self.power * 3} урона"

class Archer(Character):
    def attack(self):
        return f"{self.name} наносит {self.power + 10} урона"

characters = [
    Warrior("Рагнар", 20),
    Mage("Мерлин", 20),
    Archer("Робин", 20)
]

for character in characters:
    print(character.attack())


'''
##################################################################################

---

## Задание 10 ⭐. Способы оплаты

Создайте родительский класс:

```python
Payment
```

Он принимает сумму покупки.

Создайте дочерние классы:

```python
CashPayment
CardPayment
BonusPayment
```

Во всех классах переопределите метод:

```python
get_final_amount()
```

### Правила

При оплате наличными сумма не изменяется.

При оплате картой добавляется комиссия `2%`.

При оплате бонусами действует скидка `10%`.

### Пример

```python
payments = [
    CashPayment(1000),
    CardPayment(1000),
    BonusPayment(1000)
]

for payment in payments:
    print(payment.get_final_amount())
```

### Результат

```text
1000
1020.0
900.0
```

'''
##################################################################################

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def get_final_amount(self):
        return self.amount

class CashPayment(Payment): 
    def get_final_amount(self):
        return self.amount

class CardPayment(Payment):
    def get_final_amount(self):
        return self.amount * 1.02

class BonusPayment(Payment):
    def get_final_amount(self):
        return self.amount * 0.9

payments = [
    CashPayment(1000),
    CardPayment(1000),
    BonusPayment(1000)
]

for payment in payments:
    print(payment.get_final_amount())

'''
##################################################################################

---

## Задание 11 ⭐. Склад

Создайте класс:

```python
Product
```

У товара есть:

* название;
* цена;
* количество.

Также создайте класс:

```python
Warehouse
```

Внутри него должен храниться список объектов `Product`.

Добавьте методы:

```python
add_product(product)
show_products()
get_total_price()
find_product(name)
```

`get_total_price()` должен возвращать общую стоимость всех товаров:

```text
цена * количество
```

### Пример

```python
warehouse = Warehouse()

warehouse.add_product(Product("Ноутбук", 80000, 3))
warehouse.add_product(Product("Мышь", 2000, 10))
warehouse.add_product(Product("Монитор", 30000, 5))
```

### Пример результата

```text
Ноутбук: 3 шт.
Мышь: 10 шт.
Монитор: 5 шт.

Общая стоимость: 410000
```

'''
##################################################################################

class Product:
    def __init__(self, name, price, quantity, currency):
        if price <= 0:
            print("Цена товара должна быть больше 0")
            self.bad_product = True
            return
        elif name == '':
            print("Название товара не может быть пустым")
            self.bad_product = True
            return
        elif quantity <= 0:
            print("Количество товара должно быть больше 0")
            self.bad_product = True
            return
        elif currency == '':
            print("Валюта товара не может быть пустой")
            self.bad_product = True
            return
        self.bad_product = False
        self.name = name
        self.price = price
        self.quantity = quantity
        self.currency = currency

class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.bad_product:
            return
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(f"{product.name}: {product.quantity} шт.")

    def get_total_price(self):
        total_price = {}
        for product in self.products:
            if total_price.get(product.currency) == None:
                total_price[product.currency] = 0
            total_price[product.currency] += product.price * product.quantity
        return total_price

warehouse = Warehouse()

warehouse.add_product(Product("Ноутбук", 80000, 3,'USD'))
warehouse.add_product(Product("Мышь", 2000, 10,'RUR'))
warehouse.add_product(Product("Мышь", -1, 10,'RUR'))
warehouse.add_product(Product("Монитор", 30000, 5,'USD'))

warehouse.show_products()
print(f"Общая стоимость товаров: {'; '.join([f'{value},{key}' for key, value in warehouse.get_total_price().items()])}.")

'''
##################################################################################

---

## Задание 12 ⭐. Система заказов

Создайте родительский класс:

```python
Order
```

При создании передавайте:

* номер заказа;
* стоимость товаров.

Стоимость храните в приватном атрибуте:

```python
__price
```

Добавьте методы:

```python
get_price()
set_price(price)
get_total()
show_info()
```

Цена не может быть отрицательной.

Создайте три дочерних класса:

```python
PickupOrder
CourierOrder
ExpressOrder
```

Переопределите метод:

```python
get_total()
```

### Правила расчёта

Самовывоз:

```text
стоимость товаров
```

Курьерская доставка:

```text
стоимость товаров + 500
```

Экспресс-доставка:

```text
стоимость товаров + 1000
```

Создайте список разных заказов:

```python
orders = [
    PickupOrder(101, 5000),
    CourierOrder(102, 3000),
    ExpressOrder(103, 10000),
    CourierOrder(104, 7000)
]
```

С помощью одного цикла:

1. выведите номер каждого заказа;
2. выведите итоговую стоимость;
3. с помощью `isinstance()` определите способ получения заказа;
4. посчитайте общую стоимость всех заказов.

### Пример результата

```text
Заказ №101
Самовывоз
Итого: 5000

Заказ №102
Курьер
Итого: 3500

Заказ №103
Экспресс-доставка
Итого: 11000

Заказ №104
Курьер
Итого: 7500

Общая сумма: 27000
```
'''
##################################################################################

class Order:
    def __init__(self, number, price):
        self.number = number
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_total(self):
        return self.__price

    def show_info(self):
        print(f"Заказ №{self.number}")
        print(f"Итого: {self.__price}")

class PickupOrder(Order):
    def __init__(self, number, price):
        super().__init__(number, price)
    def get_total(self):
        return self.get_price()

class CourierOrder(Order):
    def __init__(self, number, price):
        super().__init__(number, price)
    def get_total(self):
        return self.get_price() + 500

class ExpressOrder(Order):
    def __init__(self, number, price):
        super().__init__(number, price)
    def get_total(self):
        return self.get_price() + 1000

orders = [
    PickupOrder(101, 5000),
    CourierOrder(102, 3000),
    ExpressOrder(103, 10000),
    CourierOrder(104, 7000)
]

total = 0
for order in orders:
    order.show_info()
    print(f"Итого: {order.get_total()}")
    total += order.get_total()

print(f"Общая сумма: {total}")



'''
##################################################################################

---

# Проект: Телефонный справочник. Часть 3

Перепишите телефонный справочник из прошлого домашнего задания с использованием ООП.

Сильно усложнять программу не нужно.

## Класс Contact

Создайте класс:

```python
Contact
```

Он хранит:

```python
name
phone
```

Добавьте метод:

```python
show_info()
```

---

## Класс PhoneBook

Создайте класс:

```python
PhoneBook
```

Внутри него хранится список объектов `Contact`:

```python
self.contacts = []
```

Перенесите действия справочника в методы:

```python
add_contact()
show_contacts()
find_contact()
update_contact()
delete_contact()
```

Меню остаётся прежним:

```text
1. Добавить контакт
2. Показать все контакты
3. Найти контакт
4. Изменить контакт
5. Удалить контакт
6. Выйти
```

### Пример

```python
phone_book = PhoneBook()

phone_book.add_contact("Анна", "12345")
phone_book.add_contact("Иван", "67890")

phone_book.show_contacts()
```

### Результат

```text
Имя       | Телефон
-----------+----------
Анна      | 12345
Иван      | 67890
```

Поиск контакта должен работать независимо от регистра.

---
'''