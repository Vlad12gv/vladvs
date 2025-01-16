import math


def f(x):
    k = 2 if math.sin(x) else 1
    return k * x if x < 0 else x * k


x = float(input("Введите значение x: "))
result = f(x)
print(f"Значение функции f(x) при x={x} равно {result}")
