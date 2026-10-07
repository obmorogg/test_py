"""
# Домашнее задание. Извлечение данных из веб-страниц

Для выполнения заданий используйте учебный сайт:

https://books.toscrape.com/

Сайт специально предназначен для практики веб-парсинга. Регистрация и авторизация не нужны.

## Общие требования

Используйте:

- `requests`;
- `BeautifulSoup`;
- `find()` и `find_all()`;
- `get_text()`;
- получение значений HTML-атрибутов;
- `urljoin()`, когда необходимо получить полный адрес страницы;
- `User-Agent`;
- `timeout`;
- `raise_for_status()`.

Все данные должны извлекаться из HTML сайта. Не записывайте полученные результаты вручную.

⭐ Задание со звёздочкой — необязательное.

---

# Задание 2. Недорогие книги

Работайте только с первой страницей каталога.

Найдите все книги дешевле:

```text
£20
```

Для каждой выведите:

```text
Название | Цена
```

В конце выведите количество найденных книг.

### Ожидаемый результат

```text
The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull | £17.93
Starving Hearts (Triangular Trade Trilogy, #1) | £13.99
Set Me Free | £17.46

Количество: 3
```


---
"""

import requests
import tabulate as tab
import re
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "MovieParserBot/1.0 (contact: user@mail.com)"
}

response = requests.get(
    url,
    headers=HEADERS,
    timeout=10
)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
i = 1

data = []
headers = ["No", "Название", "Цена","Валюта", "Наличие"]

for book in books:
    title = book.find_all("a")[1].get_attribute_list("title")[0]
    price = book.find("p", class_="price_color").get_text(" ", strip=True)
    currency = re.sub(r"[0-9.]", "", price)
    price = re.sub(r"[^0-9.]", "", price)
    availability = book.find("p", class_="instock availability").get_text(" ", strip=True)

    if float(price) > 20:
        continue
    data.append([i, title, price, currency, availability])

    i += 1

print(tab.tabulate(data, headers=headers))
