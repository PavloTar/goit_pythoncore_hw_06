# === Вимоги технічого завдання ===
# AddressBook: Клас для зберігання та управління записами.
# Функціональність:
#     Додавання записів.
#     Пошук записів за іменем.
#     Видалення записів за іменем.

from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]