
#import phonebook.db as db
import phonebook.helpers as h
import re
import phonebook.exceptions as e
import json
from datetime import datetime


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ###
        if not re.match("^[A-Za-zА-Яа-я ]*$", name) or len(name) < 2:
            h.printErr(r'Err: неправильное имя: должны быть только буквы\пробелы(не менее 2 символов)')
            raise e.InvalidNameError(name)
        if not re.match(r"^(\+7|8)\d{10}$", phone):
            h.printErr(r'Err: неправильный номер: должны быть только цифры\пробелы(не менее 2 символов)')
            raise e.InvalidPhoneError(phone)


    def __str__(self):
        return f'{self.name} | {self.phone} | {self.created_at}'

    def show_info(self):
        print(f'Имя: {self.name}\nТелефон: {self.phone}')

    def additional_info(self):
        pass

    def update_contact(self,**kwargs):
        self.name = kwargs.get('name', '')
        self.phone = kwargs.get('phone', '')
    def to_json(self):
        return json.dumps(self, cls=CustomEncoder, ensure_ascii=False, indent=2)

    #def __post_init__(self):

class PersonalContact(Contact):
    def __init__(self, name, phone, relation):
        super().__init__(name, phone)
        self.relation = relation

    def __post_init__(self):
        super().__post_init__(self)
        if not re.match("^[A-Za-zА-Яа-я ]*$", self.relation) or len(self.relation) < 2:
            h.printErr(r'Err: неправильное отношение: должны быть только буквы\пробелы(не менее 2 символов)')
            raise e.InvalidRelationError(self.relation)
    def __str__(self):
        return f'{super().__str__()} | {self.relation}'
    def additional_info(self):
        #print(f'Relation: {self.realtion}')
        return f'Relation: {self.relation}'
    def update_contact(self,**kwargs):
        super().update_contact(**kwargs)
        asd = kwargs.get('relation', '')
        print(asd)
        self.relation = asd
        print(self.additional_info())
    def to_json(self):
        return json.dumps(self, cls=CustomEncoder, ensure_ascii=False, indent=2)

class WorkContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company
    def __post_init__(self):
        super().__post_init__(self)
        if not re.match("^[A-Za-zА-Яа-я ]*$", self.company) or len(self.company) < 2:
            h.printErr(r'Err: неправильное название компании: должны быть только буквы\пробелы(не менее 2 символов)')
            raise e.InvalidCompanyError(self.company)
    def __str__(self):
        return f'{super().__str__()} | {self.company}'
    def additional_info(self):
        #print(f'Company: {self.company}')
        return f'Company: {self.company}'
    def update_contact(self,**kwargs):
        self.company = kwargs.get('company', '')
        super().update_contact(**kwargs)

    def to_json(self):
        return json.dumps(self, cls=CustomEncoder, ensure_ascii=False, indent=2)

