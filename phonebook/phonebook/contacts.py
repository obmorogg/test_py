
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

    def additional_info(self):
        pass

    def update_contact(self,**kwargs):
        self.name = kwargs.get('name', '')
        self.phone = kwargs.get('phone', '')

class PersonalContact(Contact):
    def __init__(self, name, phone, relation):
        super().__init__(name, phone)
        self.realtion = relation
    def __str__(self):
        return f'{self.name} | {self.phone} | {self.realtion}'
    def additional_info(self):
        #print(f'Relation: {self.realtion}')
        return f'Relation: {self.realtion}'
    def update_contact(self,**kwargs):
        self.relation = kwargs.get('relation', '')
        super().update_contact(**kwargs)

class WorkContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company
    def __str__(self):
        return f'{self.name} | {self.phone} | {self.company}'
    def additional_info(self):
        #print(f'Company: {self.company}')
        return f'Company: {self.company}'
    def update_contact(self,**kwargs):
        self.company = kwargs.get('company', '')
        super().update_contact(**kwargs)

