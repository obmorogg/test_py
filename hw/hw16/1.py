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

# Задание 1. Первые книги каталога

Получите главную страницу сайта.

Соберите данные о первых `10` книгах:

- полное название;
- цена;
- наличие.

Выведите результат в консоль.

### Пример начала результата

```text
1. A Light in the Attic | £51.77 | In stock
2. Tipping the Velvet | £53.74 | In stock
3. Soumission | £50.10 | In stock
4. Sharp Objects | £47.82 | In stock
5. Sapiens: A Brief History of Humankind | £54.23 | In stock
```

Всего должно быть:

```text
10 книг
```

---
"""

import requests
import tabulate as tab
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
headers = ["No", "Название", "Цена", "Наличие"]

for book in books[:10]:
    title = book.find_all("a")[1].get_attribute_list("title")[0]
    price = book.find("p", class_="price_color").get_text(" ", strip=True)
    availability = book.find("p", class_="instock availability").get_text(" ", strip=True)

    # print(f"{i}. {title} | {price} | {availability}")
    data.append([i, title, price, availability])

    i += 1

print(tab.tabulate(data, headers=headers))
