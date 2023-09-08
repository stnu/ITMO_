class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rec_1 = Rectangle(2, 4)
rec_2 = Rectangle(2, 3)
rec_3 = Rectangle(3, 4)

print(rec_1.square(), rec_1.perimeter())
print(rec_2.square(), rec_2.perimeter())
print(rec_3.square(), rec_3.perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


m = Math(10, 2)
print(m.addition(), m.multiplication(), m.division(), m.subtraction())


class Demoqa:
    type_ = "кнопка"  # тип одинаковый для всех, поэтому выносим

    def __init__(self, text, locator):
        self.text = text
        self.locator = locator

    def clik_(self):  # метод для нажатия на кнопку
        print("Клик по кнопке {}".format(self.text))


# создаем обьекты
text_box = Demoqa("Text Box", " ")
check_box = Demoqa("Check Box", " ")
radio_botton = Demoqa("Radio Button", " ")
web_tables = Demoqa("Web Tables", " ")
buttons = Demoqa("Buttons", " ")
links = Demoqa("Links", " ")
broken_links = Demoqa("Broken Kinks - Images", " ")
upload_download = Demoqa("Upload and Download", " ")
dynamic_properties = Demoqa("Dynamic Properties", " ")

# выводим тект для каждой кнопки
print(text_box.text, check_box.text, radio_botton.text, web_tables.text, buttons.text, links.text,
      broken_links.text, upload_download.text, dynamic_properties.text, sep=', ')

# вызываем "Клик"
text_box.clik_()
check_box.clik_()
radio_botton.clik_()
web_tables.clik_()
buttons.clik_()
links.clik_()
broken_links.clik_()
upload_download.clik_()
dynamic_properties.clik_()
