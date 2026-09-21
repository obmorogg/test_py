"""

## Задание 2. Дата доставки

Дана дата отправки заказа:

```python
order_date = "05.09.2026"
```

И срок доставки:

```python
delivery_days = 14
```

Используя `datetime`:

1. преобразуйте строку в дату;
2. прибавьте количество дней;
3. выведите дату доставки в формате `дд.мм.гггг`.

### Результат

```text
19.09.2026
```

---
"""
########################################################################################################################

import datetime

order_date = "05.09.2026"
delivery_days = 14

order_date = datetime.datetime.strptime(order_date, "%d.%m.%Y")
delivery_date = order_date + datetime.timedelta(days=delivery_days)

print(delivery_date.strftime("%d.%m.%Y"))

