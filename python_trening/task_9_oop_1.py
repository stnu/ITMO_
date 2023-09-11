from task_9_checks import Check


class Input(Check):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


search = Input("input", "locator")

print(search.loc)


class Button(Check):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


home = Button("Home ", "locator.button")


class Title(Check):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


object_title = Title("Title ", "locator.title")


class Link(Check):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text


object_link = Link("Link ", "locator.link")

print(search.text, search.loc)
print(home.text, home.loc)
print(object_title.text, object_title.loc)
print(object_link.text, object_link.loc)

print(search.check_text())
print(home.check_text())
print(object_title.check_text())
print(object_link.check_text())
