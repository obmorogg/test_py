

########################################################################################################################
"""

## Задание 8 ⭐. Формирование отчёта из нескольких файлов

Есть два файла.

### `products.json`

```json
{
    "Ноутбук": 80000,
    "Мышь": 2000,
    "Монитор": 30000,
    "Клавиатура": 5000
}
```

### `orders.csv`

```text
Ноутбук,2
Мышь,10
Монитор,3
Клавиатура,4
```

Создайте программу, которая:

1. с помощью `pathlib` проверяет наличие обоих файлов;
2. загружает цены из JSON;
3. загружает количество проданных товаров из CSV;
4. вычисляет выручку по каждому товару;
5. создаёт папку `reports`, если её ещё нет;
6. сохраняет результат в:

```text
reports/report.txt
```

### Содержимое отчёта

```text
Ноутбук: 160000
Мышь: 20000
Монитор: 90000
Клавиатура: 20000

Общая выручка: 290000
Самая большая выручка: Ноутбук
```

Если `products.json` содержит некорректный JSON, обработайте:

```python
json.JSONDecodeError
```

и выведите:

```text
Не удалось прочитать файл products.json
```
"""

import pathlib
import json
import csv

with open("products.json", "w", encoding="utf-8") as f:
    f.write(
        """
{
    "Ноутбук": 80000,
    "Мышь": 2000,
    "Монитор": 30000,
    "Клавиатура": 5000
}
"""
    )
    f.close()

with open("orders.csv", "w", encoding="utf-8") as f:
    csv.writer(f).writerow(["name", "quantity"])
    csv.writer(f).writerow(["Ноутбук", "2"])
    csv.writer(f).writerow(["Мышь", "10"])
    csv.writer(f).writerow(["Монитор", "3"])
    csv.writer(f).writerow(["Клавиатура", "4"])
    f.close()


def main():
    path = pathlib.Path.cwd() / "reports"
    path.mkdir(parents=True, exist_ok=True)

    try:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)
            f.close()
    except json.JSONDecodeError:
        print("Не удалось прочитать файл products.json")
        return

    with open("orders.csv", "r", encoding="utf-8") as f:
        orders = csv.DictReader(f)
        orders = [row for row in orders]
        f.close()

    print(orders)

    report = ""
    total_revenue = 0
    most_profit_product = None
    most_profit_product_revenue = 0

    for order in orders:
        product = order["name"]
        quantity = int(order["quantity"])
        revenue = products[product] * quantity
        report += f"{product}: {revenue}\n"
        total_revenue += revenue

    for product, revenue in products.items():
        if revenue > most_profit_product_revenue:
            most_profit_product = product
            most_profit_product_revenue = revenue

    report += f"Общая выручка: {total_revenue}\n"
    report += f"Самая большая выручка: {most_profit_product}"

    with open(path / "report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()