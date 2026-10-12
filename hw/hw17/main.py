"""
# Домашнее задание. Первый API-сервис на FastAPI

## Проект: API склада товаров

Создайте FastAPI-приложение для управления небольшим складом.

Для каждого товара должны храниться:

- название;
- категория;
- цена в рублях;
- количество на складе.

Самостоятельно создайте начальные данные: список минимум из **5 объектов товаров** не менее чем из **3 разных категорий**.

⭐ Задание 2 — **необязательное**.

---

# Задание 1. API управления складом

Реализуйте полный CRUD для товаров.

API должно позволять:

- получить список товаров;
- получить один товар;
- добавить новый товар;
- полностью изменить существующий товар;
- удалить товар.

Для списка товаров добавьте необязательную фильтрацию:

- по категории;
- по максимальной цене;
- по наличию на складе.

Фильтры должны передаваться через query-параметры и работать как отдельно, так и одновременно.

Номер конкретного товара передавайте через path-параметр.

Для фильтра наличия:

```text
available=true  - только товары, количество которых больше 0
available=false - только товары с нулевым остатком
```

### Требования

При успешном создании товара возвращайте:

```text
201 Created
```

Не разрешайте добавлять два товара с одинаковым названием.

При попытке создать дубликат:

```text
409 Conflict
```

При получении, изменении или удалении несуществующего товара:

```text
404 Not Found
```

Сообщение:

```text
Товар не найден
```

После изменения или удаления данные в списке должны действительно измениться.

---

# Задание 2 ⭐. Цены в другой валюте

Доработайте API из задания 1.

Для получения курса валют используйте бесплатный сервис Frankfurter:

https://frankfurter.dev/

Регистрация и API-ключ не нужны.

Пример получения курса RUB → USD:

https://api.frankfurter.dev/v2/rate/rub/usd

Курс находится в поле:

```text
rate
```

Добавьте две новые возможности.

## Цена одного товара в выбранной валюте

Получите товар по его номеру и пересчитайте его цену из рублей в выбранную валюту.

Валюта передаётся обязательным query-параметром:

```text
currency
```

Поддерживайте:

```text
USD
EUR
```

Верните:

- название товара;
- цену в рублях;
- выбранную валюту;
- текущий курс;
- пересчитанную цену.

### Пример формата ответа

```json
{
    "name": "Ноутбук",
    "price_rub": 75000,
    "currency": "USD",
    "rate": 0.012,
    "price": 900.0
}
```

Курс и итоговая цена будут зависеть от даты выполнения задания.

---

## Стоимость всего склада

Добавьте отдельный маршрут, который возвращает:

- количество разных товаров;
- общее количество единиц товаров;
- стоимость всего склада в рублях;
- стоимость всего склада в выбранной валюте.

Стоимость склада рассчитывайте с учётом количества каждого товара.

Например:

```text
цена товара × количество товара
```

и затем суммируйте стоимость всех товаров.

Если передана валюта, отличная от:

```text
USD
EUR
```

верните:

```text
400 Bad Request
```

Если внешний сервис курсов валют недоступен или вернул ошибку:

```text
502 Bad Gateway
```

---
"""



import uvicorn
from fastapi import FastAPI
from fastapi.params import Query
from fastapi.exceptions import HTTPException
import pandas as pd
import warehause as wh
import db_operate as db

#wh = pd.read_csv('warehouse.csv', sep=';')


db.dbinit()

warehause = db.dbget()

# for i in range(len(wh)):
#   warehause.append(wh.item(name=wh['Name'].values[i], category=wh['Category'].values[i], price=wh['Price'].values[i], currency=wh['Currency'].values[i], count=wh['Count'].values[i]))

app = FastAPI()

@app.get("/")
async def index():
    """Добро пожаловать."""
    return {"message": "Welcome to the warehouse API"}


@app.get("/items/", response_model=list[wh.item])
async def items(
   id: int = Query(None, description="ID товара."),
   name: str = Query(None, description="Название товара."),
   category: str = Query(None, description="Категория товара."),
   price: int = Query(None, description="Цена товара."),
   currency: str = Query(None, description="Валюта товара."),
   count: int = Query(None, description="Количество товара.")
):
    """Получить список товаров."""
    result = warehause
    if name is not None:
        result = [item for item in result if name in item.name]
    if category is not None:
        result = [item for item in result if category in item.category]
    if price is not None:
        result = [item for item in result if item.price == price]
    if currency is not None:
        result = [item for item in result if item.currency == currency]
    if count is not None:
        result = [item for item in result if item.count == count]

    return result

@app.get("/items/add/", response_model=str)
async def add_item(
   name: str = Query(None, description="Название товара."),
   category: str = Query(None, description="Категория товара."),
   price: int = Query(None, description="Цена товара."),
   currency: str = Query(None, description="Валюта товара."),
   count: int = Query(None, description="Количество товара.")
):
    """Добавить товар."""
    id = db.dbadd(name=name, category=category, price=price, currency=currency, count=count)
    if id == -1:
        raise HTTPException(status_code=400, detail="Bad Request")
    new_item = wh.item(name=name, category=category, price=price, currency=currency, count=count, id=id)
    warehause.append(new_item)

    return f'Добавлен товар с id={id}' #

@app.get("/items/del/", response_model=str)
async def del_item(
   id: int = Query(None, description="ID товара.")
):
    """Удалить товар."""
    #new_item = wh.item(name=name, category=category, price=price, currency=currency, count=count)
    #warehause.remove(warehause)
    db.dbdel(id=id)
    warehause = db.dbget()
    return f'Удален товар с id={id}'

@app.get("/items/modify/", response_model=list[wh.item])
async def modify_item(
   id: int = Query(None, description="ID товара."),
   name: str = Query(None, description="Название товара."),
   category: str = Query(None, description="Категория товара."),
   price: int = Query(None, description="Цена товара."),
   currency: str = Query(None, description="Валюта товара."),
   count: int = Query(None, description="Количество товара.")
):
    """Изменить товар."""
    #new_item = wh.item(name=name, category=category, price=price, currency=currency, count=count)
    #warehause.append(new_item)
    db.dbmodify(id=id, name=name, category=category, price=price, currency=currency, count=count)
    #! поправить
    warehause = db.dbget()

    return warehause

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)