
import phonebook.db as db
import phonebook.helpers as h

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name} | {self.phone}'

    def show_info(self):
        print(f'Имя: {self.name}\nТелефон: {self.phone}')

class PersonalContact(Contact):
    def __init__(self, name, phone, relation):
        super().__init__(name, phone)
        self.realtion = relation
    def __str__(self):
        return f'{self.name} | {self.phone} | {self.realtion}'

class WorkContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company
    def __str__(self):
        return f'{self.name} | {self.phone} | {self.company}'

