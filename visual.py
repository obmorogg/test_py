import msvcrt as m

def printerr(err):
    print(f"\033[31m{err}\033[0m")
    m.getch()

def printinfo(err):
    print(f"\033[1;32m{err}\033[0m")
    m.getch()
