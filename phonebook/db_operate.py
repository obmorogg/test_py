import sqlite3
def dbinit():
    try:
        #cursor.execute('drop TABLE contacts')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            phone TEXT
        )
        ''')
    except Exception as e:
        print(e)

def dbclose():
    connection.close()

def dbcommit():
    connection.commit()

def dbclear():
    cursor.execute('delete from contacts')
    dbcommit()

def dbget():
    cursor.execute('SELECT * FROM contacts')
    result = cursor.fetchall()
    #return result
    #global contacts
    contacts = []
    for col in result:
        contacts.append({"phone": col[2], "name": col[1]} )
    return contacts

def dbdel(name):
    try:

        cursor.execute('''
        DELETE FROM contacts WHERE name = ?
        ''', (name,))
        dbcommit()
        if cursor.rowcount == 0:
            return 0
        return cursor.rowcount
    except Exception as e:
        print(f'error: {e}')
        return -1

def dbadd(**kwargs):
    try:
        name = kwargs.get('name', '')
        phone = kwargs.get('phone', '')
        cursor.execute('''
        INSERT INTO contacts (name, phone) VALUES (?, ?)
        ''', (name, phone))
        dbcommit()
        #printInfo(f'Контакт "{name}: {tel}" добавлен.')
        return cursor.rowcount
    except Exception as e:
        print(f'error: {e}')
        return 0

def dbmodify(**kwargs):
    try:
        name = kwargs.get('name', '')
        phone = kwargs.get('phone', '')
        cursor.execute('''
        UPDATE contacts SET phone = ? WHERE name = ?
        ''', (phone, name))
        dbcommit()
        return cursor.rowcount
    except Exception as e:
        print(f'error: {e}')
        return 0

connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()
