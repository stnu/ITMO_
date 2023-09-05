# permit_print = True
# num = 3
# if num > 0 and permit_print:
#   print("num - положительное число")
# elif not permit_print:
#   print("Печать запрещена")

a = 5

if 1 <= a <= 4:
    print("бакалавр")
elif a < 7:
    print("магистр")
elif 7 <= a <= 9:
    print("аспирант")
else:
    print("некорректная вводная")

if a in range(5, 7):
    print()

x = 5

if x > 100 or x < -100:
    print("-")
else:
    print("+")




if x not in range(-100, 100):
    print("-")
else:
    print("+")
