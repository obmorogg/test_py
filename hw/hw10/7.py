

########################################################################################################################
"""

# Задания со звёздочкой ⭐

## Задание 7 ⭐. Конвертация CSV в JSON

Дан файл:

```text
students.csv
```

```text
Анна,5,4,5
Иван,4,3,4
Мария,5,5,5
Олег,3,4,3
```

Каждая строка содержит:

```text
имя, оценка1, оценка2, оценка3
```

Считайте, что у каждого студента указаны ровно три оценки.

Прочитайте CSV-файл и сформируйте список словарей:

```python
[
    {
        "name": "Анна",
        "grades": [5, 4, 5],
        "average": 4.67
    },
    ...
]
```

Среднюю оценку округлите до двух знаков.

Сохраните результат в:

```text
students.json
```

Дополнительно найдите студента с самой высокой средней оценкой.

### Пример результата

```text
Лучший студент: Мария
Средняя оценка: 5.0
```

### Пример структуры одного элемента `students.json`

```json
{
    "name": "Анна",
    "grades": [
        5,
        4,
        5
    ],
    "average": 4.67
}
```

В итоговом `students.json` должны находиться данные всех студентов.

---
"""
########################################################################################################################
import csv
import statistics
import json

with open('students.csv','w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'grade1', 'grade2', 'grade3'])
    writer.writerow(['Анна', 5, 4, 5])
    writer.writerow(['Иван', 4, 3, 4])
    writer.writerow(['Мария', 5, 5, 5])
    writer.writerow(['Олег', 3, 4, 3])


with open('students.csv', 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
    #print(data)
    f.close

for d in data:
    d['grades'] = [int(d['grade1']), int(d['grade2']), int(d['grade3'])]
    d['average'] = statistics.mean(d['grades']).__round__(2)
    d.pop('grade1')
    d.pop('grade2')
    d.pop('grade3')

print (data)

with open('students.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    f.close