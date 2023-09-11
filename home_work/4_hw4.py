class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def add_year(self, y_new):
        self.year = y_new

    def add_type(self, t_new):
        self.type = t_new

    def add_color(self, t_color):
        self.color = t_color


# в задании нет выведения в консоль
