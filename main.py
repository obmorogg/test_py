import pandas as pd
import re
import os
import db_operate as db
#import visual as v
import msvcrt as m

def printerr(err):
    print(f"\033[31m{err}\033[0m")
    m.getch()

def printinfo(err):
    print(f"\033[1;32m{err}\033[0m")
    m.getch()



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getuserresp():
    cls()
    print('<<<------------ start <<<------------', flush=True)
    for key, value in menu.items():
        print(f'{key}. {value}')
    print("Выберите действие: ")
    cse = m.getch()
    #print(cse)
    if cse in [b'\x03', b'\x1b']:
        exit()
    return str(int(cse)) if cse in (b'1', b'2', b'3', b'4', b'5', b'6', b'0') else '-1'


def getname():
    name = input("Введите имя: ")
    name = name.strip()
    if not re.match("^[A-Za-zА-Яа-я ]*$", name) or len(name) < 2:
        printerr(r'Err: неправильное имя: должны быть только буквы\пробелы(не менее 2 символов)')
        return
    return name

def getphone():
    tel = input("Введите номер: ")
    tel = tel.strip()
    if not re.match("^[0-9]*$", tel) or len(tel) < 2:
        printerr(r'Err: неправильное имя должны быть только буквы\пробелы(не менее 2 символов)')
        return
    return tel

'''

# Проект: Телефонный справочник. Часть 3

Перенесите действия справочника в методы:

```python

```

Меню остаётся прежним:

```text
1. Добавить контакт
2. Показать все контакты
3. Найти контакт
4. Изменить контакт
5. Удалить контакт
6. Выйти
```

### Пример

```python
phone_book = PhoneBook()

phone_book.add_contact("Анна", "12345")
phone_book.add_contact("Иван", "67890")

phone_book.show_contacts()
```

### Результат

```text
Имя       | Телефон
-----------+----------
Анна      | 12345
Иван      | 67890
```

Поиск контакта должен работать независимо от регистра.

---

'''

class contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        print(f'Имя: {self.name}\nТелефон: {self.phone}')


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        if db.dbadd(name=name, phone=phone) == 1:
            self.contacts.append(contact(name, phone))
            printinfo(f'Контакт "{name}: {tel}" добавлен.')
        else:
            printerr(f'error: {name}, {phone}')


    # def show_contacts(self):
    #     for contact in self.contacts:
    #         contact.show_info()

    def del_contact(self,name):
        try:
            rez = db.dbdel(name=name)
            if rez > 0:
                for contact in self.contacts:
                    if contact.name == name:
                        self.contacts.remove(contact)
                printinfo(f'Контакт "{name}" удален в колтчестве {rez}')
            elif rez == 0:
                printinfo(f'Контакт "{name}" не найден')
            else:
                printerr(f'Something wrong with deleting {name}')
        except:
            printerr(f'error: {name}')


    def show_contacts2(self, **kwargs):
        cls()
        data = []#contacts.copy()
        name = kwargs.get('name', '')
        for contact in self.contacts:
            data.append({'name': contact.name, 'phone': contact.phone})
        headers = {'name':"Имя",'phone':"Телефон"}

        col_widths = [
        max([len(val['name']) for k, val in enumerate(data+[headers])]),
        max([len(str(val['phone'])) for k, val in enumerate(data+[headers])])
        ]

        separator = '+' + '+'.join('-' * (width + 2) for width in col_widths) + '+'

        print(separator)
        header_row = '|' + '|'.join(f' {h:{w}} ' for h, w in zip([headers['name'], headers['phone']], col_widths)) + '|'
        print(header_row)
        print(separator)
        for row in data:
            # print (row)
            data_row = '|' + '|'.join(f' {str(cell):{width}} ' for cell, width in zip([row['name'], row['phone']], col_widths)) + '|'
            if row['name'].lower().find(name.lower()) == -1:
                continue
            print(data_row)
        print(separator)
    '''

    def showcontacts(**kwargs):
        print(kwargs)
        name = kwargs.get('name', '')
        cnts = []
        for contact in self.contacts:
            cnts.append(contact={'name':contact.name, 'phone':contact.phone})
        cls()
        if len(cnts) > 0:
            df = pd.DataFrame(cnts, columns=['name', 'phone'])
            df = df[df['name'].str.contains(name, case=False)]
            if df.empty == False:
                print(df)
                return
            print('контактов не найдено')
    '''
    def modify_contact(self,**kwargs):
        name = kwargs.get('name', '')
        phone = kwargs.get('phone', '')
        if db.dbmodify(name=name, phone=phone) > 0:
            for contact in self.contacts:
                if contact.name == name:
                    contact.phone = phone
            printinfo(f'Контакт "{name}: {phone}" изменен.')
        else:
            printerr(f'error: {name}, {phone}')




###################################################################################


phone_book = PhoneBook()

menu = {
    '1': 'Добавить контакт',
    '2': 'Показать все контакты(странное самописное)',
    '3': 'Найти контакт(pandas)',
    '4': 'Изменить контакт',
    '5': 'Удалить контакт',
    '6': r'Выход(ctrl+c\esc)',
    '0': 'Почистить контакты'
}

cls()
db.dbinit()
#phone_book.contacts = db.dbget()
asd = db.dbget()
print(asd)

for k in asd:
     phone_book.contacts.append(contact(k["name"], k["phone"]))

i = 0
#print(phone_book.contacts)


# data = [['Apple', 2, 150], ['Banana', 3, 120]]
# df = pd.DataFrame(data, columns=['Fruit', 'Quantity', 'Price'])
# showcontacts(name = '')
#exit()
while True :
    i += 1
    exit('<<<<<<<<<<<<< megaloop check exit >>>>>>>>>>>>') if i == 100 else None # megaloop exit
    cse = getuserresp()
    if cse == '1': # добавить
        name = getname()
        tel = getphone()
        phone_book.add_contact(name, tel)
        contacts = db.dbget()
    elif cse == '2': # показать
        #print(contacts)
        phone_book.show_contacts2()
        printinfo('Нажмите любую клавишу для продолжения')
    elif cse == '3': #
        name = input("Введите имя(фильтр): ")
        #print(contacts)
        phone_book.show_contacts2(name = name)
        printinfo('Нажмите любую клавишу для продолжения')
    elif cse == '4': # изменить контакт
        name = getname()
        if name == None:
            continue
        tel = getphone()
        if tel == None:
            continue
        phone_book.modify_contact(name=name, phone=tel)
        contacts = db.dbget()
    elif cse == '5': # удалить контакт
        name = getname()
        phone_book.del_contact(name)
        contacts = db.dbget()
    elif cse == '6':
        db.dbclose()
        print('Программа завершает работу.')
        exit()
        printerr('Err: неправильная команда')
    elif cse == '0':
        db.dbclear()
        contacts = []
        cls()
        printinfo('Контакты очищены')
    # else:
    #     print('неправильная команда')
#"""