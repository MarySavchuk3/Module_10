from collections import UserDict


class AddressBook(UserDict):

        def add_record(self, record):
            self.data[record.name.value] = record


class Field:
    pass


class Name(Field):

    def __init__(self, value):
        self.value = value


class Phone(Field):

    def __init__(self, phone):
        self.value = phone


class Record(Field):

    def __init__(self, name, phone=None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        for el in self.phones:
            if el.value == old_phone:
                el.value = new_phone

    def del_phone(self, phone):
        for elem in self.phones:
            if elem.value == phone:
                self.phones.remove(elem)


contacts = AddressBook()


def input_error(func):
     def wrapper(*args):
        try:
            return func(*args)
        except KeyError as error:
            return f' Name is not available. Error: {error}'
        except IndexError as error:
            return f'Please try again. Error: {error}'
        except ValueError as error:
            return f'Give me name and phone, please. Error: {error}'
        except TypeError as error:
            return f'Not enough arguments. Error: {error}'
     return wrapper


def hello() -> str:
    return f'How can I help you?'


def goodbye():
    print(f'Good bye!')
    quit()


@input_error
def add(*args) -> str:

      name, number, *_ = args
      if not name in contacts:
        new_number = Record(name, number)
        contacts.add_record(new_number)
        return f'The contact was added successfully'
      else:
          contacts[name].add_phone(number)
          return f'New phone number was added to {name}'


@input_error
def change(*args) -> str:

    name, old_number,new_number, *_ = args
    if name in contacts:
        contacts[name].change_phone(old_number, new_number)
    else:
        return f' No contact with this name "{name}"'
    return f' The contact was changed successfully'


@input_error
def del_phone(name, phone) -> str:

    if name in contacts:
        contacts[name].del_phone(phone)
    else:
        return f'There is no contact with name "{name}"'
    return f'Phone number was deleted successfully'


@input_error
def phone_func(*args) -> str:
    name = args[0]
    if name in contacts:
        for name, numbers in contacts.items():
            return f'Name: {name} | Numbers: {", ".join(phone.value for phone in numbers.phones)}'
    else:
        return f'No contact "{name}"'


@input_error
def show_all() -> str:

    result = []
    for name, numbers in contacts.items():
        result.append(f'Name: {name} | Numbers: {", ".join(phone.value for phone in numbers.phones)}')
    if len(result) < 1:
        return f'Contact list is empty'
    return '\n'.join(result)


def hlp(*args) -> str:
    return f'Commands: hello, help, add, change, phone, show all, delete, good bye, close, exit.'


def parser(msg: str):
    command = None
    parametrs = []

    operations = {
        'hello': hello,
        'h': hlp,
        'help': hlp,
        'add': add,
        'change': change,
        'phone': phone_func,
        'show all': show_all,
        'good bye': goodbye,
        'close': goodbye,
        'exit': goodbye,
        'delete': del_phone,
    }

    for key in operations:
        if msg.lower().startswith(key):
            command = operations[key]
            msg = msg.lstrip(key)
            for item in filter(lambda x: x != '', msg.split(' ')):
                parametrs.append(item)
            return command, parametrs
    return command, parametrs


def main():
    print(hello())
    while True:
        msg = input("Please enter command: ")
        command, parametrs = parser(msg)
        if command:
            print(command(*parametrs))
        else:
            print(f' This command is not available, please try again. Please type "h" for help.')


if __name__ == '__main__':
    main()