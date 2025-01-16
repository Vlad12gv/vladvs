import math


def k(x):
    if math.sin(x) != 0:
        return 2
    else:
        return 1


def f(x):
    if x < 0:
        return k(x) * x
    else:
        return k(x) + x


x = float(input("Введите значение x: "))
result = f(x)
print(f"Значение функции f(x) при x={x} равно {result}")
