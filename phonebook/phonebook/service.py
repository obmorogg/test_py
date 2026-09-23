"""

## `service.py`

Перенесите сюда класс:

```python
PhoneBook
```

Сохраните методы:

```python
add_contact()
find_contact()
update_contact()
delete_contact()
```

### `add_contact()`

Если контакт с таким именем уже существует:

```python
raise DuplicateContactError(...)
```

### `find_contact()`

Если контакт не найден:

```python
raise ContactNotFoundError(...)
```

### `update_contact()` и `delete_contact()`

Если контакта нет, должно возникать `ContactNotFoundError`.

---
"""

import phonebook.db as db
import phonebook.helpers as h
import phonebook.exceptions as e

class PhoneBook:
    def __init__(self):
        self.contacts = []
    """
    find_contact()

    """
    # def add_contact(self, object):
    #     self.contacts.append(object)

    def add_contact(self, object):
        try:
            rez = 0
            if self.find_contact(name=object.name):
                raise e.DuplicateContactError(object.name)
            self.contacts.append(object)
        except e.DuplicateContactError as err:
            h.printErr(f'{err}')

    def delete_contact(self,name):
        try:
            rez = 0
            for contact in self.contacts:
                if contact.name == name:
                    self.contacts.remove(contact)
                    rez = 1
                    break
            if rez == 1:
                h.printInfo(f'Контакт "{name}" удален')
            else:
                raise e.ContactNotFoundError(name)
        except e.ContactNotFoundError as err:
            h.printErr(f'{err}')

    def find_contact(self, **kwargs):
        for contact in self.contacts:
            if contact.name == kwargs.get('name', ''):
                return contact

    def show_contacts(self, **kwargs):
        data = []#contacts.copy()
        name = kwargs.get('name', '')
        for contact in self.contacts:
            data.append({'name': contact.name, 'phone': contact.phone, 'info': contact.additional_info()})
            #print({'name': contact.name, 'phone': contact.phone, 'info': contact.additional_info()})
        print(data)
        headers = {'name':"Имя",'phone':"Телефон",'info':"Дополнительно"}

        col_widths = [
            max([len(val['name']) for k, val in enumerate(data+[headers])]),
            max([len(str(val['phone'])) for k, val in enumerate(data+[headers])]),
            max([len(str(val['info'])) for k, val in enumerate(data+[headers])])
        ]

        separator = '+' + '+'.join('-' * (width + 2) for width in col_widths) + '+'

        print(separator)
        header_row = '|' + '|'.join(f' {h:{w}} ' for h, w in zip([headers['name'], headers['phone'], headers['info']], col_widths)) + '|'
        print(header_row)
        print(separator)
        for row in data:
            #print (row)
            data_row = '|' + '|'.join(f' {str(cell):{width}} ' for cell, width in zip([row['name'], row['phone'], row['info']], col_widths)) + '|'
            if row['name'].lower().find(name.lower()) == -1:
                continue
            print(data_row)
        print(separator)

    def update_contact(self,**kwargs):
        name = kwargs.get('name', '')
        # phone = kwargs.get('phone', '')
        upd = self.find_contact(name=name)
        if upd != None:
            upd.update_contact(**kwargs)

        # if db.dbmodify(name=name, phone=phone) > 0:
        #     for contact in self.contacts:
        #         if contact.name == name:
        #             contact.phone = phone
        #     printInfo(f'Контакт "{name}: {phone}" изменен.')
        # else:
        #     printErr(f'error: {name}, {phone}')

    def __len__(self):
        return len(self.contacts)

    def __str__(self):
        #self.show_contacts2()
        for contact in self.contacts:
            print(contact)
        return ''
