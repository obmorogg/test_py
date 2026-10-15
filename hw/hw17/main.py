"""
# Домашнее задание. Первый API-сервис на FastAPI

⭐ Задание 2 — **необязательное**.

---

# Задание 1. API управления складом




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

Получите товар по его номеру и пересчитайте его цену из рублей в выбранную
валюту.

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
# import pandas as pd
import warehause as wh
import db_operate as db

import requests

# https://api.frankfurter.dev/v2/currencies

currencies = requests.get('https://api.frankfurter.dev/v2/currencies').json()
# print(currencies)
# for currency in currencies:
#     print(currency['iso_code'])


#exit()


# wh = pd.read_csv('warehouse.csv', sep=';')





db.dbinit()

warehause = db.dbget()

app = FastAPI()


@app.get("/")
async def index():
    """Добро пожаловать."""
    return {"message": "Welcome to the warehouse API"}

@app.get("/items/", response_model=list[wh.item])
async def items(
    item_id: int = Query(None, description="ID товара."),
    name: str = Query(None, description="Название товара."),
    category: str = Query(None, description="Категория товара."),
    available: bool = Query(False, description="Проверить наличие товара."),
    is_max_price: bool = Query(False, description="Получить товар с максимальной ценой."),
):
    """Получить список товаров."""
    result = warehause
    if name is not None:
        result = [item for item in result if name in item.name]
    if item_id is not None:
        result = [item for item in result if  item.id == item_id]
    if category is not None:
        result = [item for item in result if category in item.category]
    if available:
        result = [item for item in result if item.count > 0]
    if is_max_price:
        price = 0
        for i in range(len(result)):
            if result[i].price > price:
                price = result[i].price
                rez = result[i]
        result = [rez]

    return result

@app.get("/items/{item_id}/{to_currency}/", response_model=wh.item)
async def get_item(
    item_id: int,
    to_currency: str
):
    """Получить товар."""
    item = [item for item in warehause if item.id == item_id][0]
    response = requests.get(f'https://api.frankfurter.dev/v2/rate/{item.currency}/{to_currency}')
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"{item.currency}/{to_currency} not found")

    rate = response.json()['rate']
    item.price = item.price * rate
    item.currency = to_currency
    return item



@app.post("/items/add/", response_model=wh.item)
async def add_item(
   name: str = Query(None, description="Название товара."),
   category: str = Query(None, description="Категория товара."),
   price: int = Query(None, description="Цена товара."),
   currency: str = Query(None, description="Валюта товара."),
   count: int = Query(None, description="Количество товара.")
):
    """Добавить товар."""
    try:
        idd = db.dbadd(
            name=name,
            category=category,
            price=price,
            currency=currency,
            count=count
        )
    except Exception as e: # ! fix
        print(e)
        # if e == 'UNIQUE constraint failed':
        raise HTTPException(status_code=409, detail="Conflict")

    new_item = wh.item(
        name=name,
        category=category,
        price=price,
        currency=currency,
        count=count,
        id=idd
    )
    warehause.append(new_item)

    return new_item


@app.delete("/items/delete/{item_id}/", response_model=str)
async def del_item(item_id: int):
    """Удалить товар."""
    print(item_id)
    db.dbdel(item_id)
    try:
        warehause.remove([item for item in warehause if item.id == item_id])
    except:
        raise HTTPException(status_code=400, detail="Bad Request")
    return f'Удален товар с id={item_id}'


@app.put("/items/update/{item_id}/", response_model=wh.item)
async def update_item(
    item_id: int,
    name: str = Query(None, description="Название товара."),
    category: str = Query(None, description="Категория товара."),
    price: int = Query(None, description="Цена товара."),
    currency: str = Query(None, description="Валюта товара."),
    count: int = Query(None, description="Количество товара.")
):
    """Изменить товар."""
    try:
        db.dbupdate(
            item_id = item_id,
            name = name,
            category = category,
            price = price,
            currency = currency,
            count = count
        )
        warehause = db.dbget()
    except Exception as e:
        print (e)
        raise HTTPException(status_code=409, detail="Conflict")
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    rezult = [item for item in warehause if item.id == item_id]
    return rezult[0]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



#   {
#     "id": 9,
#     "name": "www33",
#     "category": "a",
#     "price": 12,
#     "currency": "ru",
#     "count": 1
#   },