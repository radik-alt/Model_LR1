class Message:

    def __init__(self):
        self.type = 0
        self.address = 0
        self.len = 0
        self.time = 0

    def __repr__(self):
        return f"Тип: {self.type}, адресс: {self.address}, длинна: {self.len}, время: {self.time}"

    def __str__(self):
        return f"Тип: {self.type}, адресс: {self.address}, длинна: {self.len}, время: {self.time:5}"
