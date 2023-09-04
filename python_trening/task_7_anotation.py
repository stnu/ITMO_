a: int = 5
b: str = "строка"
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent("123", 123))


def hw(s=""):
    return len(s)


print(hw())


def hw_2(list1, list2: list) -> int:
    return len(max(list1, list2))


print(hw_2((1, 2, 3), (1, 2, 3, 4)))
