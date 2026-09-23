import msvcrt as m
import re
import os

def printErr(err):
    print(f"\033[31m{err}\033[0m")
    m.getch()

def printInfo(err):
    print(f"\033[1;32m{err}\033[0m")
    m.getch()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getUserResp(menu):

    cls()
    print('<<<------------ start <<<------------', flush=True)

    # цикл по сортированным ключам items
    for key in sorted(menu):
        print(f'{int(key)}. {menu[key]}')
    print("Выберите действие: ")
    cse = m.getch()
    #print(cse)
    if cse in [b'\x03', b'\x1b']:
        exit()
    return str(int(cse)) if cse in (menu.keys()) else '-1'


def getName():
    name = input("Введите имя: ")
    name = name.strip()
    if not re.match("^[A-Za-zА-Яа-я ]*$", name) or len(name) < 2:
        printErr(r'Err: неправильное имя: должны быть только буквы\пробелы(не менее 2 символов)')
        return
    return name

def getCompany():
    name = input("Введите имя компании: ")
    name = name.strip()
    if not re.match("^[A-Za-zА-Яа-я ]*$", name) or len(name) < 2:
        printErr(r'Err: неправильное имя: должны быть только буквы\пробелы(не менее 2 символов)')
        return
    return name

def getRelation():
    name = input("Введите статус  отношений: ")
    name = name.strip()
    if not re.match("^[A-Za-zА-Яа-я ]*$", name) or len(name) < 2:
        printErr(r'Err: неправильное имя: должны быть только буквы\пробелы(не менее 2 символов)')
        return
    return name

def getPhone():
    tel = input("Введите номер: ")
    tel = tel.strip()
    if not re.match("^[0-9]*$", tel) or len(tel) < 2:
        printErr(r'Err: неправильное имя должны быть только буквы\пробелы(не менее 2 символов)')
        return
    return tel
