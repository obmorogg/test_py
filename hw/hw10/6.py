

########################################################################################################################
"""

## Задание 6. Анализ продаж из CSV

Создайте файл:

```text
sales.csv
```

Содержимое:

```text
Ноутбук,2,80000
Мышь,5,2000
Монитор,3,30000
Клавиатура,4,5000
```

Каждая строка содержит:

```text
товар, количество, цена
```

Прочитайте файл с помощью `csv.reader()`.

Определите:

1. общую сумму продаж;
2. товар, проданный в наибольшем количестве.

### Пример результата

```text
Общая сумма продаж: 280000
Больше всего продано: Мышь
Количество: 5
```

---
"""
########################################################################################################################
import csv

with open('sales.csv', 'w', newline='', encoding="utf-8") as file:
  writer = csv.writer(file, delimiter=',')
  writer.writerow(['Ноутбук', '2', '80000'])
  writer.writerow(['Мышь', '5', '2000'])
  writer.writerow(['Монитор', '3', '30000'])
  writer.writerow(['Клавиатура', '4', '5000'])


with open('sales.csv', 'r', newline='', encoding="utf-8") as file:
  reader = csv.reader(file, delimiter=',')

  total_sum = 0
  most_sold_item = None
  most_sold_quantity = 0

  for row in reader:
    product, quantity, price = row
    total_sum += int(quantity) * int(price)

    if int(quantity) > most_sold_quantity:
      most_sold_item = product
      most_sold_quantity = int(quantity)

  print(f"Общая сумма продаж: {total_sum}")
  print(f"Больше всего продано: {most_sold_item}")
  print(f"Количество: {most_sold_quantity}")