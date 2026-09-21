


########################################################################################################################
"""
## Задание 9 ⭐. Планировщик работы

Создайте программу:

```text
planner.py
```

Пример запуска:

```text
python planner.py 10.09.2026 30.09.2026 --tasks 47 --per-day 6
```

Аргументы:

* первая дата — начало работы;
* вторая дата — дедлайн;
* `--tasks` — количество задач, по умолчанию `30`;
* `--per-day` — количество задач в день, по умолчанию `5`.

Необходимо:

1. с помощью регулярного выражения проверить формат дат `дд.мм.гггг`;
2. преобразовать даты через `datetime.strptime()`;
3. определить количество доступных дней;
4. через `math.ceil()` вычислить количество дней, необходимое для выполнения задач;
5. определить, получится ли выполнить всё до дедлайна.

Количество доступных дней считайте как разницу:

```text
дедлайн - дата начала
```

Дополнительно прибавлять день начала или день дедлайна не нужно.

### Для примера выше

```text
Доступно дней: 20
Необходимо дней: 8
Успеете выполнить задачи
Запас: 12 дней
```

Если необходимых дней больше:

```text
Не успеете выполнить задачи
Не хватает дней: 3
```
"""

import argparse
import datetime
import math


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("start_date")
  parser.add_argument("end_date")
  parser.add_argument("--tasks", default=30, type=int)
  parser.add_argument("--per-day", default=5, type=int)
  args = parser.parse_args()

  start_date = datetime.datetime.strptime(args.start_date, "%d.%m.%Y")
  end_date = datetime.datetime.strptime(args.end_date, "%d.%m.%Y")
  available_days = (end_date - start_date).days
  needed_days = math.ceil(args.tasks / args.per_day)
  print(f"Доступно дней: {available_days}")
  print(f"Необходимо дней: {needed_days}")
  if available_days >= needed_days:
    print("Успеете выполнить задачи")
    print(f"Запас: {available_days - needed_days} дней")
  else:
    print("Не успеете выполнить задачи")
    print(f"Не хватает дней: {needed_days - available_days}")


if __name__ == "__main__":
  main()