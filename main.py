import pandas as pd
import msvcrt as m
import re
import os
import db_operate as db

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getuserresp():
    cls()
    print('<<<------------ start <<<------------', flush=True)
    for key, value in menu.items():
        print(f'{key}. {value}')
    print("Выберите действие: ")
    cse = m.getch()
    return str(int(cse)) if cse in (b'1', b'2', b'3', b'4', b'5', b'6', b'0') else '-1'

def printerr(err):
    print(f"\033[31m{err}\033[0m")
    m.getch()

def printinfo(err):
    print(f"\033[1;32m{err}\033[0m")
    m.getch()

def addcontact(name, phone):
    #rez = db.add(name=name, phone=phone)
    if db.dbadd(name=name, phone=phone) == 1:
        printinfo(f'Контакт "{name}: {tel}" добавлен.')
    else:
        printerr(f'error: {name}, {phone}')

def delcontact(name):
    try:
        rez= db.dbdel(name=name)
        if rez > 0:
            printinfo(f'Контакт "{name}" удален в колтчестве {rez}')
        elif rez == 0:
            printinfo(f'Контакт "{name}" не найден')
        else:
            printerr(f'Something wrong with deleting {name}')
    except:
        printerr(f'error: {name}')

def showcontacts(**kwargs):
    print(kwargs)
    name = kwargs.get('name', '')
    cls()
    if len(contacts) > 0:
        df = pd.DataFrame(contacts, columns=['name', 'phone'])
        df = df[df['name'].str.contains(name, case=False)]
        if df.empty == False:
            print(df)
        else:
            print('контактов не найдено')

def modifycontact(**kwargs):
    name = kwargs.get('name', '')
    phone = kwargs.get('phone', '')
    cursor.execute('''
    UPDATE contacts SET phone = ? WHERE name = ?
    ''', (phone, name))
    dbcommit()
    printinfo(f'Контакт "{name}: {phone}" изменен.')


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
###################################################################################
contacts = []

menu = {
    '1': 'Добавить контакт',
    '2': 'Показать все контакты',
    '3': 'Найти контакт',
    '4': 'Изменить контакт',
    '5': 'Удалить контакт',
    '6': 'Выход',
    '0': 'Почистить контакты'
}

cls()
db.dbinit()
contacts = db.dbget()

i = 0
#print('123')


# data = [['Apple', 2, 150], ['Banana', 3, 120]]
# df = pd.DataFrame(data, columns=['Fruit', 'Quantity', 'Price'])
# showcontacts(name = '')
# exit()
while True :
    i += 1
    exit('<<<<<<<<<<<<< megaloop check exit >>>>>>>>>>>>') if i == 100 else None # megaloop exit
    cse = getuserresp()
    if cse == '1': # добавить
        name = getname()
        tel = getphone()
        addcontact(name, tel)
        contacts = db.dbget()
    elif cse == '2': # показать
        #print(contacts)
        showcontacts()
        printinfo('Нажмите любую клавишу для продолжения')
    elif cse == '3': # 
        name = input("Введите имя(фильтр): ")
        #print(contacts)
        showcontacts(name = name)
        printinfo('Нажмите любую клавишу для продолжения')
    elif cse == '4': # изменить контакт
        name = getname()
        tel = getphone()
        modifycontact(name=name, phone=tel)
        contacts = db.dbget()
    elif cse == '5': # удалить контакт
        name = getname()
        delcontact(name)
        contacts = db.dbget()
    elif cse == '6':
        dbclose()
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