
# === Вимоги технічого завдання ===
# Field: Базовий клас для полів запису.

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)