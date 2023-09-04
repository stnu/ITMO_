a = 2
print(a, "относится к типу", type(a))

b = 15.0001
print(b, "относится к типу", type(b))

c = 1 + 2j
print(c, "комплексное число?", isinstance(c, complex))

print(6 + 2)
print(6 - 2)
print(6 * 2)
print(6 / 2)

print(7 / 2)
print(7 // 2)

print(7 % 2)  # остаток от деления

print(6 ** 2)  # во 2 степень

s = "Это строка"
print(s + '\n')
g = """Многострочная 
строка"""
print(g + '\n')
print('Строки ' + "можно " + "складывать")

print("Auto" * 3)
print(len("test"))

a = "Auto"
print(a[0])
print(a[-2])
