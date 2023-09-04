def add(x, y):
    return x + y


add(1, 2)


def add(x, y):
    return x + y


print(add(1, 2))

print(add("I a", "m tester"))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))


# print(arg(2, 2))  # ошибка

# print(arg(2, 2, '1', 1))  # ошибка


def range_arg(a, b, c, d):
    return a + " " + b + " " + c + " " + d


print(range_arg('1', '2', '3', "4"))
print(range_arg('1', '2', d='3', c="4"))


def work_1(a=(1, 2, 3, 4)):
    return a[1]


print(work_1())


def work_2(r, pi=3.14159):
    S = pi * r ** 2
    return S


print(work_2(2))
