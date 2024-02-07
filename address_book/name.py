# === Вимоги технічого завдання ===
# Name: Клас для зберігання імені контакту. Обов'язкове поле.


from .field import Field

class Name(Field):
    def __init__(self, value):
        # Перевірка, чи значення не порожнє
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)
