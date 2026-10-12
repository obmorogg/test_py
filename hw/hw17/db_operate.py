import sqlite3
import warehause as wh

def dbinit():
    try:
        #cursor.execute('drop TABLE contacts')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            category TEXT,
            price INTEGER,
            currency TEXT,
            count INTEGER
        )
        ''')
    except Exception as e:
        print(e)

def dbclose():
    connection.close()

def dbcommit():
    connection.commit()

def dbclear():
    cursor.execute('delete from items')
    dbcommit()

def dbget():
    cursor.execute('SELECT * FROM items')
    result = cursor.fetchall()
    #return result
    #global contacts
    items = []
    for col in result:
        items.append(wh.item(name=col[1], category=col[2], price=col[3], currency=col[4], count=col[5], id=col[0]) )
    return items

def dbdel(id):
    try:

        cursor.execute('''
        DELETE FROM items WHERE id = ?
        ''', (id,))
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
      category = kwargs.get('category', '')
      price = kwargs.get('price', '')
      currency = kwargs.get('currency', '')
      count = kwargs.get('count', '')
      cursor.execute('''
      INSERT INTO items (name, category, price, currency, count) VALUES (?, ?, ?, ?, ?) RETURNING id
      ''', (name, category, price, currency, count))
      id = cursor.fetchone()[0]
      dbcommit()
      print(f'%%%%%%%%%%%% добавлено %%%%%%%%%%%%%%%%%% id={id}')
      #printInfo(f'Контакт "{name}: {tel}" добавлен.')
      return id
    except Exception as e:
      print(f'error: {e}')
      return -1


connection = sqlite3.connect('items.db')
cursor = connection.cursor()
