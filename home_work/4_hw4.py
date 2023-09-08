class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def add_year(self):
        self.year = "1985"

    def add_type(self):
        self.type = "пикап"

    def add_color(self):
        self.color = "синий"



