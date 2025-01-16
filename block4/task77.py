import math


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


if math.sqrt(b) < b:
    b = b*5
print(a)
print(b)
