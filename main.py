from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def get_info(self):
        phones_info = ""
        for phone in self.phones:
            phones_info += f"{phone.value}"
        return f"{self.name.value}:{phones_info[:]}"


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False


    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)



class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return name in self.data

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)
        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        return ValueError(f" Запис  {value} не існує.")
