"""
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
"""

def calculate_order(price, quantity):
    """_summary_

    Args:
        price (str): _description_
        quantity (str): _description_
    """
    try:
        if float(price) and int(quantity):
            return float(price) * int(quantity)
    except TypeError:
        print('Некорректное числовое значение')

    except ValueError:
        print('Некорректное числовое значение')

    finally:
        print('Расчёт завершён')

print(calculate_order("125.5", "4"))
print(calculate_order("сто", "4"))