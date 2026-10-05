"""

# Проект: Телефонный справочник. Часть 9

Продолжите работу с телефонным справочником.

Основную функциональность приложения менять не нужно.

Добавьте статистику с использованием NumPy.

Если проект работает через Poetry, NumPy должен быть добавлен как основная зависимость проекта.

## Метод statistics()

Добавьте в `PhoneBook` метод:

```python
statistics()
```

Исходные данные справочника хранятся в виде объектов Python, поэтому **разрешается один раз преобразовать данные контактов в NumPy-массивы**.

После этого все статистические вычисления должны выполняться средствами NumPy.

Создайте массив длин имён контактов.

На его основе определите:

* количество контактов;
* минимальную длину имени;
* максимальную длину имени;
* общее количество символов;
* среднюю длину имени.

Также создайте NumPy-массивы для определения количества:

* личных контактов;
* рабочих контактов.

После формирования массивов не используйте обычные Python-функции:

```python
sum()
min()
max()
```

для статистических вычислений.

### Пример

В справочнике находятся:

```text
Анна
Александр
Мария
Константин
```

Анна и Мария — личные контакты.

Александр и Константин — рабочие.

### Результат

```text
Всего контактов: 4
Личных: 2
Рабочих: 2

Минимальная длина имени: 4
Максимальная длина имени: 10
Всего символов: 28
Средняя длина имени: 7.0
```

Добавьте пункт:

```text
9. Статистика
```


"""

import json
import tabulate as tab
import numpy as np

from phonebook import (
    PhoneBook,
    PersonalContact,
    WorkContact,
    Contact,
    cls,
    printInfo,
    printErr,
    getUserResp,
    getCompany,
    getName,
    getPhone,
    getRelation
)



def load(obj):
    """
    Он должен загружать данные из:

    ```text
    data/contacts.json
    ```

    Если файла ещё нет, справочник остаётся пустым.

    Если JSON повреждён, обработайте:

    ```python
    json.JSONDecodeError
    ```

    и выведите:

    ```text
    Не удалось загрузить контакты
    ```"""
    try:
        with open('./data/contacts.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Не удалось загрузить контакты")
        return
    obj.contacts = []
    for asd in data:
        contact = json.loads(asd)
        if contact.get('relation') != None:
            obj.contacts.append(PersonalContact(name=contact.get('name'), phone=contact.get('phone'), relation=contact.get('relation')))
        elif contact.get('company') != None:
            obj.contacts.append(WorkContact(name=contact.get('name'), phone=contact.get('phone'), company=contact.get('company')))

def statistics():
    headers = ["Имя", "Телефон",'relation','company']
    data = []
    for contact in phone_book.contacts:
        data.append([contact.name, contact.phone, contact.additional_info() if isinstance(contact, PersonalContact) else None, contact.additional_info() if isinstance(contact, WorkContact) else None])
    print(tab.tabulate(data, headers=headers))


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
        b'7': 'Случайный контакт',
        b'8': r'Выход(ctrl+c\esc)'
        # b'0': 'Почистить контакты'
    }


    # exit()



    phone_book = PhoneBook()
    load(phone_book)

    # data = [
    #     ["Alice", 30, "Engineer"],
    #     ["Bob", 25, "Designer"],
    #     ["Charlie", 35, "Manager"]
    # ]

    headers = ["Имя", "Телефон",'Дополнительно']

    # print(tab.tabulate(data, headers=headers))



    # print(phone_book.get_tab())
    # print(tab.tabulate(phone_book.get_tab(), headers=headers))
    # exit()

    # phone_book.add_contact(PersonalContact("Анна", "+71234567890", "друг"))
    # # exit()
    # #phone_book.add_contact(Contact("Анна", "+71234567890"))
    # # phone_book1.add_contact(PersonalContact("Анна", "12345", "друг"))
    # phone_book.add_contact(WorkContact("Иванa", "+71234567891", "SkyPro"))
    # phone_book.add_contact(WorkContact("Иванs", "+71234567392", "SkyPro"))
    # phone_book.add_contact(WorkContact("Иванd", "81234567893", "SkyPro"))
    # phone_book.update_contact(name="Анна", phone="81234567894", relation="sdfs")
    # print(phone_book.find_contact(name = "Анна").to_json())
    # asd = WorkContact("Иванa", "+71234567891", "SkyPro")
    # print(asd.to_json())
    # print(phone_book)
    # exit()
    """
    printInfo('Нажмите любую клавишу для продолжения')
    # phone_book1.delete_contact("Анна1")
    print(phone_book)
    # print("Всего контактов:", len(phone_book1))
    exit()
    """

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
            # print(phone_book.show_contacts(name = ''))
            # print(tab.tabulate(phone_book.show_contacts2(name = ''), headers='keys', tablefmt='psql'))
            print(tab.tabulate(phone_book.get_tab(), headers=headers))
            # name = input("Введите имя(фильтр): ")
            # #print(contacts)
            # phone_book.show_contacts2(name = name)
            printInfo('Нажмите любую клавишу для продолжения')
        elif cse == '4': # Найти контакт
            name = getName()
            print(phone_book.find_contact(name=name))
            printInfo('Нажмите любую клавишу для продолжения')
            # #print(contacts)
            # name = getname()
            # if name == None:
            #     continue
            # tel = getphone()
            # if tel == None:
            #     continue
            # phone_book.modify_contact(name=name, phone=tel)
            # contacts = db.dbget()
        elif cse == '5': # Изменить контакт
            name = getName()
            if name == None:
                continue
            upd = phone_book.find_contact(name=name)

            if upd != None:
                print(upd)
                phone = getPhone()

                if upd.__class__.__name__ == 'PersonalContact':
                    print('>>Личный контакт')
                    rel = getRelation()
                    phone_book.update_contact(name=name, phone=phone, relation=rel)
                elif upd.__class__.__name__ == 'WorkContact':
                    print('>>Рабочий контакт')
                    comp = getCompany()
                    phone_book.update_contact(name=name, phone=phone, company=comp)
            else:
                printErr('Контакт не найден')
            printInfo('Нажмите любую клавишу для продолжения')

            # tel = getPhone()
            # if tel == None:
            #     continue
            # rel = getRelation()
            # phone_book.modify_contact(name=name, phone=tel, relation=rel)
            # contacts = db.dbget()
        elif cse == '6': # Удалить контакт
            name = getТame()
            phone_book.del_contact(name)
            contacts = db.dbget()
        elif cse == '7': # Случайный контакт
            print(phone_book.random_contact())
            printInfo('Нажмите любую клавишу для продолжения')
        elif cse == '8':
            cls()
            print(f'Количество контактов: {len(phone_book)}')
            printInfo('Нажмите любую клавишу для продолжения')
        elif cse == '0':
            db.dbclear()
            contacts = []
            cls()
            printInfo('Контакты очищены')
