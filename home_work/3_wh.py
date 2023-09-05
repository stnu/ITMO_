def task_1():
    x = 2
    y = 3
    return max(x, y)


print(task_1())


def task_2():
    a = 4
    b = 5

    if a - b == 135 or b - a == 135:
        print("yes")
    else:
        print("no")


task_2()


def task_3():
    m = 13
    if m in range(3, 5):
        print("Spring")
    elif m in range(6, 8):
        print("Summer")
    elif m in range(9, 11):
        print("Autumn")
    elif m not in range(1, 13):
        print("it's not a month")
    else:
        print("Winter")


task_3()


def task_4():  # если хотя бы одно число меньше 9, то автоматом "no"
    num1 = 10
    num2 = 11
    num3 = 13
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")


task_4()


def task_5():
    a = 1
    b = -1
    c = 2
    d = 3
    e = -5
    summ = 0
    if a > 0:
        summ = summ + 1
    if b > 0:
        summ = summ + 1
    if c > 0:
        summ = summ + 1
    if d > 0:
        summ = summ + 1
    if e > 0:
        summ = summ + 1
    print("количество положительных чисел", summ)


task_5()
