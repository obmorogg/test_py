

########################################################################################################################
"""
## Задание 5. Настройки программы в JSON

Дан словарь:

```python
settings = {
    "theme": "dark",
    "language": "ru",
    "notifications": True
}
```

Сохраните его в файл:

```text
settings.json
```

После этого:

1. прочитайте данные из файла;
2. измените `"theme"` на `"light"`;
3. добавьте `"font_size": 16`;
4. снова сохраните данные в файл.

### Итоговое содержимое

```json
{
    "theme": "light",
    "language": "ru",
    "notifications": true,
    "font_size": 16
}
```

---
"""
########################################################################################################################
import json

settings = {
    "theme": "dark",
    "language": "ru",
    "notifications": True
}

with open("settings.json", "w") as f:
    json.dump(settings, f)

with open("settings.json", "r") as f:
    settings1 = json.load(f)

settings1["theme"] = "light"
settings1["font_size"] = 16

with open("settings.json", "w") as f:
    json.dump(settings1, f)

with open("settings.json", "r") as f:
    settings2 = json.load(f)

print(settings2)