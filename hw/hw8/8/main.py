"""_summary_

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

"""



############# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! не доделано, в отпуске , не всегда успеваю



from order_system import calculate_total, OrderError

price = '10'
quantity = '10'
discount = '10'

while True:
    try:
        print('Введите цену')
        price = input()
        print('Введите количество')
        quantity = input()
        print('Введите скидку')
        discount = input()
        break
    except OrderError(error):
        print(error)
    

calculate_total(int(price),int(quantity),int(discount))