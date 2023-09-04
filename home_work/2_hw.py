def task_1() -> None:
    a: int = 1  # int
    b: float = 5.5  # float
    c: str = "строка"  # str
    d: list = [1, 2, 3]  # list
    e: bool = True  # bool
    print(" Тип переменной а: ", type(a), "\n", "Тип переменной b: ", type(b), "\n", "Тип переменной c: ", type(c),
          "\n", "Тип переменной d: ", type(d), "\n", "Тип переменной e: ", type(e))

    return


task_1()


def task_2() -> None:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
    return


task_2()

print("последовательность называется 'последовательность Фибоначчи'")


def task_3(a: float) -> float:
    return a ** 2

print(task_3(5))
