
'''

# Проект: Телефонный справочник. Часть 5


---

## `main.py`

Меню:

```text
1. Добавить личный контакт
2. Добавить рабочий контакт
3. Показать все контакты
4. Найти контакт
5. Изменить контакт
6. Удалить контакт
7. Выйти
```

Ошибки справочника обрабатывайте через:

```python
try:
    ...
except PhoneBookError as error:
    print(error)
```

### Пример

```text
Введите имя: Анна
Введите телефон: 12345
Контакт добавлен

Введите имя: Анна
Введите телефон: 99999
Контакт с именем Анна уже существует
```

При поиске отсутствующего контакта:

```text
Контакт Иван не найден
```

---
'''




#import pandas as pd
# import re
# import os
# import db_operate as db
# import phonebook.helpers as h
# import phonebook.contacts as c
# import phonebook.service as s

from phonebook import (
    PhoneBook,
    PersonalContact,
    WorkContact,
    cls,
    printInfo,
    printErr,
    getUserResp,
    getCompany,
    getName,
    getPhone,
    getRelation
)



###################################################################################

if __name__ == "__main__":
    """
    1. Добавить личный контакт
    2. Добавить рабочий контакт
    3. Показать все контакты
    4. Найти контакт
    5. Изменить контакт
    6. Удалить контакт
    7. Выйти
    """

    #phone_book = c.PhoneBook()
    #b'1', b'2', b'3', b'4', b'5', b'6', b'0'
    menu = {
        b'1': 'Добавить личный контакт',
        b'2': 'Добавить рабочий контакт',
        b'3': 'Показать все контакты',
        b'4': 'Найти контакт',
        b'5': 'Изменить контакт',
        b'6': 'Удалить контакт',
        b'7': r'Выход(ctrl+c\esc)'
        # b'0': 'Почистить контакты'
    }

    cls()

    phone_book = PhoneBook()
    phone_book.add_contact(PersonalContact("Анна", "12345", "друг"))
    # phone_book1.add_contact(PersonalContact("Анна", "12345", "друг"))
    phone_book.add_contact(WorkContact("Иван", "67890", "SkyPro"))
    # phone_book1.delete_contact("Анна1")
    # print(phone_book1)
    # print("Всего контактов:", len(phone_book1))
    # exit()


    ########################################################################################################################
    # до лучших времен
    ########################################################################################################################

    # db.dbinit()
    # asd = db.dbget()

    # for k in asd:
        # phone_book.contacts.append(Contact(k["name"], k["phone"]))

    #print(phone_book.contacts)
    # data = [['Apple', 2, 150], ['Banana', 3, 120]]
    # df = pd.DataFrame(data, columns=['Fruit', 'Quantity', 'Price'])
    # showcontacts(name = '')



    i = 0
    while True :
        i += 1
        exit('<<<<<<<<<<<<< megaloop check exit >>>>>>>>>>>>') if i == 100 else None # megaloop exit
        cse = getUserResp(menu)
        if cse == '1': # Добавить личный контакт
            name = getName()
            tel = getPhone()
            rel = getRelation()
            phone_book.add_contact(PersonalContact(name, tel, rel)) #phone_book.add_contact(name, tel)
            #contacts = db.dbget()
        elif cse == '2': # Добавить рабочий контакт
            name = getName()
            tel = getPhone()
            comp = getCompany()
            phone_book.add_contact(WorkContact(name, tel, comp))
            # #print(contacts)
            # print(phone_book)
            # printInfo('Нажмите любую клавишу для продолжения')
        elif cse == '3': # Показать все контакты
            cls()
            print(phone_book)
            # name = input("Введите имя(фильтр): ")
            # #print(contacts)
            # phone_book.show_contacts2(name = name)
            printInfo('Нажмите любую клавишу для продолжения')
        elif cse == '4': # Найти контакт
            name = getName()
            print(phone_book.find_contact(name))
            # printInfo('Нажмите любую клавишу для продолжения')
            # #print(contacts)
            # name = getname()
            # if name == None:
            #     continue
            # tel = getphone()
            # if tel == None:
            #     continue
            # phone_book.modify_contact(name=name, phone=tel)
            # contacts = db.dbget()
        elif cse == '5': # удалить контакт
            name = getname()
            phone_book.del_contact(name)
            contacts = db.dbget()
        elif cse == '6':
            db.dbclose()
            print('Программа завершает работу.')
            exit()
            printErr('Err: неправильная команда')
        elif cse == '7':
            cls()
            print(f'Количество контактов: {len(phone_book)}')
            printInfo('Нажмите любую клавишу для продолжения')
        elif cse == '0':
            db.dbclear()
            contacts = []
            cls()
            printInfo('Контакты очищены')
