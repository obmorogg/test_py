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

# Задание 3 ⭐. Парсер всего каталога

Соберите книги со всех страниц каталога.

Программа должна самостоятельно переходить на следующую страницу, пока она существует.

Для каждой книги соберите:

```text
title
price
url
```

После этого:

1. найдите `5` самых дешёвых книг;
2. перейдите на отдельную страницу каждой из них;
3. дополнительно получите:
   - UPC;
   - наличие;
   - количество отзывов;
4. сохраните результат в файл:

```text
cheapest_books.csv
```

### Контроль

Всего в каталоге:

```text
1000 книг
```

В итоговом CSV:

```text
5 книг
```

Структура файла:

```text
title,price,upc,availability,reviews,url
```

---
"""

import requests
import tabulate as tab
import re
import pandas as pd
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
ii = 1
data = []
headers = ["No", "Название", "Цена","Валюта", "Наличие",'Ссылка']

next = 'url'


# next = soup.find_all("li", class_="next")
# next = next[0].find("a").get_attribute_list("href")[0]
# print(next)
# exit()

def get_book_data(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )

    soup = BeautifulSoup(response.text, "html.parser")
    book = soup.find("table", class_="table table-striped")
    print()
    return {
        "upc": book.find_all("tr")[0].get_text(" ", strip=True),
        "availability": book.find_all("tr")[5].get_text(" ", strip=True),
        "reviews": book.find_all("tr")[6].get_text(" ", strip=True)
    }


while next:
  ii += 1
  for book in books:
      title = book.find_all("a")[1].get_attribute_list("title")[0]
      price = book.find("p", class_="price_color").get_text(" ", strip=True)
      href = book.find_all("a")[1].get_attribute_list("href")[0]
      if href.find('catalogue') == -1:
          href = 'catalogue/' + href
      currency = re.sub(r"[0-9.]", "", price)
      price = re.sub(r"[^0-9.]", "", price)
      availability = book.find("p", class_="instock availability").get_text(" ", strip=True)

      # if float(price) > 20:
      #     continue
      data.append([i, title, price, currency, availability,href])

      i += 1

  next = soup.find_all("li", class_="next")

  try:
    next1 = next[0].find("a").get_attribute_list("href")[0]
  except:
    break

  if next1.find('catalogue') == -1:
      next1 = 'catalogue/' + next1


  response = requests.get(
      f'{url}{next1}',
      headers=HEADERS,
      timeout=10
  )

  soup = BeautifulSoup(response.text, "html.parser")
  books = soup.find_all("article", class_="product_pod")
  if ii > 2:
      break

df = pd.DataFrame(data, columns=headers)
#df.to_csv("cheapest_books.csv", index=False, sep=";")

df1 = df.sort_values(by=("Цена"), ascending=True).head(5)

for index, row in df1.iterrows():
    url1 = row["Ссылка"]
    print(f'{url}{url1}')
    book_data = get_book_data(f'{url}{url1}')
    print(book_data)
    df1.loc[index, "upc"] = book_data["upc"]
    df1.loc[index, "availability"] = book_data["availability"]
    df1.loc[index, "reviews"] = book_data["reviews"]

print(df1)

df1.to_csv("cheapest_books.csv", index=False, sep=";")

# import csv
# with open("cheapest_books.csv", "w", encoding="utf-8") as f:
#     csv.writer(f).writerows(data)

#print(tab.tabulate(data, headers=headers))
