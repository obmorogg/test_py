"""#
## Задание 1. Модуль конвертации времени

Создайте модуль:

```text
time_tools.py
```

Добавьте функции:

```python
minutes_to_hours(minutes)
hours_to_minutes(hours)
```

Первая переводит минуты в часы, вторая — часы в минуты.

В файле `main.py` импортируйте обе функции и вызовите их.

### Пример

```python
print(minutes_to_hours(150))
print(hours_to_minutes(3))
```

### Результат

```text
2.5
180
```

---
"""

from time_tools import minutes_to_hours,hours_to_minutes

print(minutes_to_hours(150))
print(hours_to_minutes(3))