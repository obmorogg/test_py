

########################################################################################################################
"""

## Задание 3. Работа с путями

Используя `pathlib`, создайте структуру:

```text
reports/
    2026/
        september/
```

В папке `september` создайте файл:

```text
result.txt
```

и запишите в него:

```text
Отчёт сформирован
```

После этого выведите:

* имя файла;
* родительскую папку;
* существует ли файл;
* является ли путь файлом;
* абсолютный путь.

### Пример результата

```text
Имя: result.txt
Родитель: reports/2026/september
Существует: True
Это файл: True
Абсолютный путь: ...
```

> Вид пути может немного отличаться в зависимости от операционной системы.

---
"""
########################################################################################################################

from pathlib import Path


def main():
    path = Path("./reports/2026/september/")
    path.mkdir(parents=True, exist_ok=True)
    with open(f'{path}result.txt', "w", encoding="utf-8") as f:
        f.write("Отчёт сформирован")
        f.close()
    print(f"Имя: {path.name}")
    print(f"Родитель: {path.parent}")
    print(f"Существует: {path.exists()}")
    print(f"Это файл: {path.is_file()}")
    print(f"Абсолютный путь: {path.absolute()}")
    with open(f'{path}result.txt', "r", encoding="utf-8") as f:
        print(f.read())
        f.close()


if __name__ == "__main__":
    main()

