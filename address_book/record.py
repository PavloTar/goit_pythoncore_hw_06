# === Вимоги технічого завдання ===
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
# Функціональність:
#     Додавання телефонів.
#     Видалення телефонів.
#     Редагування телефонів.
#     Пошук телефону

from .name import Name
from .phone import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"