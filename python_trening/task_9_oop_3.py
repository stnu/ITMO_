class Soda:
    def __init__(self, dob=None):
        self.dob = dob

    def show_my_drink(self):
        if self.dob:
            print("Газировка и" - {self.dob})# тут чето не так
        else:
            print("Обычная газировка")


gas_1 = Soda()
gas_2 = Soda("малинка")

gas_1.show_my_drink()
gas_2.show_my_drink()