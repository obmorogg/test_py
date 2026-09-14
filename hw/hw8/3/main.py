"""_summary_
## Задание 3. Собственный пакет

Создайте пакет:

```text
text_tools/
    __init__.py
    names.py
    phones.py

main.py
```

В `names.py` реализуйте:

```python
format_name(name)
```

Функция должна убрать пробелы по краям и привести имя к нормальному виду:

```text
"   иВАН   " → "Иван"
```

В `phones.py` реализуйте:

```python
hide_phone(phone)
```

Пример:

```text
"+79991234567" → "+7999***4567"
```

Настройте `__init__.py` и `__all__`, чтобы функции можно было импортировать так:

```python
from text_tools import format_name, hide_phone
```

### Пример

```python
print(format_name("   аННА   "))
print(hide_phone("+79991234567"))
```

### Результат

```text
Анна
+7999***4567
```

---
"""

from text_tools import hide_phone, format_name

print(format_name('  sadasddsa   sd  '))

print (hide_phone('+7123123123123'))

print(format_name("   аННА   "))
print(hide_phone("+79991234567"))